from __future__ import annotations

import argparse
import csv
from pathlib import Path

from PIL import Image, ImageDraw, ImageOps


def blank_runs(active_rows: list[bool], offset: int) -> list[tuple[int, int, int]]:
    runs: list[tuple[int, int, int]] = []
    start: int | None = None
    for idx, active in enumerate(active_rows):
        if not active and start is None:
            start = idx
        elif active and start is not None:
            runs.append((offset + start, offset + idx - 1, idx - start))
            start = None
    if start is not None:
        runs.append((offset + start, offset + len(active_rows) - 1, len(active_rows) - start))
    return runs


def analyze_page(path: Path) -> dict[str, int | float | str]:
    image = Image.open(path).convert("L")
    width, height = image.size
    # 仅分析正文版心附近，排除页码与物理页边距。
    x0, x1 = int(width * 0.075), int(width * 0.925)
    y0, y1 = int(height * 0.085), int(height * 0.91)
    crop = image.crop((x0, y0, x1, y1))
    # 抗锯齿后的浅灰像素也算内容；每行至少有 4 个深色像素才视为有效行。
    pixels = crop.load()
    row_counts = [
        sum(1 for x in range(crop.width) if pixels[x, y] < 242)
        for y in range(crop.height)
    ]
    active = [count >= 4 for count in row_counts]
    active_indices = [idx for idx, value in enumerate(active) if value]
    if active_indices:
        first, last = active_indices[0], active_indices[-1]
        internal = blank_runs(active[first : last + 1], y0 + first)
        longest = max(internal, key=lambda item: item[2], default=(0, 0, 0))
        bottom_blank = len(active) - 1 - last
        top_blank = first
        occupied_span = last - first + 1
    else:
        longest = (0, 0, len(active))
        bottom_blank = len(active)
        top_blank = len(active)
        occupied_span = 0
    dark_pixels = sum(row_counts)
    return {
        "page": int(path.stem.split("-")[-1]),
        "width": width,
        "height": height,
        "top_blank_px": top_blank,
        "bottom_blank_px": bottom_blank,
        "longest_internal_blank_px": longest[2],
        "longest_internal_blank_y0": longest[0],
        "longest_internal_blank_y1": longest[1],
        "occupied_span_ratio": round(occupied_span / len(active), 4),
        "dark_pixel_ratio": round(dark_pixels / (crop.width * crop.height), 5),
        "file": str(path),
    }


def make_contact_sheet(paths: list[Path], output: Path) -> None:
    thumb_width = 230
    label_height = 28
    columns = 4
    thumbs: list[Image.Image] = []
    for path in paths:
        image = Image.open(path).convert("RGB")
        ratio = thumb_width / image.width
        thumb = image.resize((thumb_width, int(image.height * ratio)))
        canvas = Image.new("RGB", (thumb_width, thumb.height + label_height), "white")
        canvas.paste(thumb, (0, label_height))
        draw = ImageDraw.Draw(canvas)
        draw.text((7, 6), f"Page {int(path.stem.split('-')[-1])}", fill="black")
        thumbs.append(ImageOps.expand(canvas, border=1, fill="#888888"))
    rows = (len(thumbs) + columns - 1) // columns
    cell_w = max(thumb.width for thumb in thumbs)
    cell_h = max(thumb.height for thumb in thumbs)
    sheet = Image.new("RGB", (columns * cell_w, rows * cell_h), "#dddddd")
    for idx, thumb in enumerate(thumbs):
        sheet.paste(thumb, ((idx % columns) * cell_w, (idx // columns) * cell_h))
    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output, quality=92)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("image_dir", type=Path)
    parser.add_argument("output_dir", type=Path)
    args = parser.parse_args()
    paths = sorted(args.image_dir.glob("page-*.png"), key=lambda path: int(path.stem.split("-")[-1]))
    if not paths:
        raise SystemExit(f"No rendered pages found in {args.image_dir}")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    rows = [analyze_page(path) for path in paths]
    with (args.output_dir / "page_metrics.csv").open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    make_contact_sheet(paths, args.output_dir / "contact_all.jpg")
    suspicious = [
        path
        for path, row in zip(paths, rows)
        if int(row["bottom_blank_px"]) >= 145
        or int(row["longest_internal_blank_px"]) >= 95
        or float(row["occupied_span_ratio"]) <= 0.7
    ]
    make_contact_sheet(suspicious, args.output_dir / "contact_suspicious.jpg")
    for row in sorted(
        rows,
        key=lambda item: max(
            int(item["bottom_blank_px"]), int(item["longest_internal_blank_px"])
        ),
        reverse=True,
    ):
        print(
            "page={page:02d} bottom={bottom_blank_px:3d} internal={longest_internal_blank_px:3d} "
            "span={occupied_span_ratio:.3f} dark={dark_pixel_ratio:.5f}".format(**row)
        )


if __name__ == "__main__":
    main()
