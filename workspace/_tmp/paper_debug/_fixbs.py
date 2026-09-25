import re, io
path = 'main.tex'
lines = open(path, encoding='utf-8').read().split('\n')
bad = []
for i, l in enumerate(lines, 1):
    s = l.rstrip()
    # count trailing backslashes
    c = 0
    j = len(s)
    while j > 0 and s[j-1] == '\\':
        c += 1
        j -= 1
    if c % 2 == 1:
        bad.append((i, s[-12:]))
for i, tail in bad:
    print(i, repr(tail))
print('TOTAL_ODD', len(bad))
