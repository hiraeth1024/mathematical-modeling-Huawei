---
pretty_name: Evaluation run of EleutherAI/pythia-410m
dataset_summary: "Dataset automatically created during the evaluation run of model\
  \ [EleutherAI/pythia-410m](https://huggingface.co/EleutherAI/pythia-410m)\nThe dataset\
  \ is composed of 44 configuration(s), each one corresponding to one of the evaluated\
  \ task.\n\nThe dataset has been created from 2 run(s). Each run can be found as\
  \ a specific split in each configuration, the split being named using the timestamp\
  \ of the run.The \"train\" split is always pointing to the latest results.\n\nAn\
  \ additional configuration \"results\" store all the aggregated results of the run.\n\
  \nTo load the details from a run, you can for instance do the following:\n```python\n\
  from datasets import load_dataset\ndata = load_dataset(\n\t\"HuggingFaceEvalInternal/EleutherAI__pythia-410m-details-private\"\
  ,\n\tname=\"EleutherAI__pythia-410m__leaderboard_arc_challenge\",\n\tsplit=\"latest\"\
  \n)\n```\n\n## Latest results\n\nThese are the [latest results from run 2024-06-16T22-11-25.600579](https://huggingface.co/datasets/HuggingFaceEvalInternal/EleutherAI__pythia-410m-details-private/blob/main/EleutherAI__pythia-410m/results_2024-06-16T22-11-25.600579.json)\
  \ (note that there might be results for other tasks in the repos if successive evals\
  \ didn't cover the same tasks. You find each in the results and the \"latest\" split\
  \ for each eval):\n\n```python\n{\n    \"all\": {\n        \"leaderboard\": {\n\
  \            \"inst_level_loose_acc,none\": 0.2841726618705036,\n            \"\
  inst_level_loose_acc_stderr,none\": \"N/A\",\n            \"prompt_level_strict_acc,none\"\
  : 0.1645101663585952,\n            \"prompt_level_strict_acc_stderr,none\": 0.015954017926718047,\n\
  \            \"acc_norm,none\": 0.294448823330706,\n            \"acc_norm_stderr,none\"\
  : 0.004632767730932793,\n            \"inst_level_strict_acc,none\": 0.2745803357314149,\n\
  \            \"inst_level_strict_acc_stderr,none\": \"N/A\",\n            \"exact_match,none\"\
  : 0.0030211480362537764,\n            \"exact_match_stderr,none\": 0.0015094760120804693,\n\
  \            \"acc,none\": 0.12269009391093608,\n            \"acc_stderr,none\"\
  : 0.0028419658401793793,\n            \"prompt_level_loose_acc,none\": 0.17005545286506468,\n\
  \            \"prompt_level_loose_acc_stderr,none\": 0.016166758064800224,\n   \
  \         \"alias\": \"leaderboard\"\n        },\n        \"leaderboard_arc_challenge\"\
  : {\n            \"acc,none\": 0.22440273037542663,\n            \"acc_stderr,none\"\
  : 0.012191404938603836,\n            \"acc_norm,none\": 0.26535836177474403,\n \
  \           \"acc_norm_stderr,none\": 0.012902554762313962,\n            \"alias\"\
  : \" - leaderboard_arc_challenge\"\n        },\n        \"leaderboard_bbh\": {\n\
  \            \"acc_norm,none\": 0.29942718278076724,\n            \"acc_norm_stderr,none\"\
  : 0.005670206683862552,\n            \"alias\": \" - leaderboard_bbh\"\n       \
  \ },\n        \"leaderboard_bbh_boolean_expressions\": {\n            \"acc_norm,none\"\
  : 0.5,\n            \"acc_norm_stderr,none\": 0.031686212526223896,\n          \
  \  \"alias\": \"  - leaderboard_bbh_boolean_expressions\"\n        },\n        \"\
  leaderboard_bbh_causal_judgement\": {\n            \"acc_norm,none\": 0.45454545454545453,\n\
  \            \"acc_norm_stderr,none\": 0.036509969495568145,\n            \"alias\"\
  : \"  - leaderboard_bbh_causal_judgement\"\n        },\n        \"leaderboard_bbh_date_understanding\"\
  : {\n            \"acc_norm,none\": 0.196,\n            \"acc_norm_stderr,none\"\
  : 0.025156857313255936,\n            \"alias\": \"  - leaderboard_bbh_date_understanding\"\
  \n        },\n        \"leaderboard_bbh_disambiguation_qa\": {\n            \"acc_norm,none\"\
  : 0.312,\n            \"acc_norm_stderr,none\": 0.029361067575219817,\n        \
  \    \"alias\": \"  - leaderboard_bbh_disambiguation_qa\"\n        },\n        \"\
  leaderboard_bbh_formal_fallacies\": {\n            \"acc_norm,none\": 0.5,\n   \
  \         \"acc_norm_stderr,none\": 0.031686212526223896,\n            \"alias\"\
  : \"  - leaderboard_bbh_formal_fallacies\"\n        },\n        \"leaderboard_bbh_geometric_shapes\"\
  : {\n            \"acc_norm,none\": 0.1,\n            \"acc_norm_stderr,none\":\
  \ 0.01901172751573438,\n            \"alias\": \"  - leaderboard_bbh_geometric_shapes\"\
  \n        },\n        \"leaderboard_bbh_hyperbaton\": {\n            \"acc_norm,none\"\
  : 0.472,\n            \"acc_norm_stderr,none\": 0.031636489531544396,\n        \
  \    \"alias\": \"  - leaderboard_bbh_hyperbaton\"\n        },\n        \"leaderboard_bbh_logical_deduction_five_objects\"\
  : {\n            \"acc_norm,none\": 0.22,\n            \"acc_norm_stderr,none\"\
  : 0.02625179282460584,\n            \"alias\": \"  - leaderboard_bbh_logical_deduction_five_objects\"\
  \n        },\n        \"leaderboard_bbh_logical_deduction_seven_objects\": {\n \
  \           \"acc_norm,none\": 0.152,\n            \"acc_norm_stderr,none\": 0.022752024491765468,\n\
  \            \"alias\": \"  - leaderboard_bbh_logical_deduction_seven_objects\"\n\
  \        },\n        \"leaderboard_bbh_logical_deduction_three_objects\": {\n  \
  \          \"acc_norm,none\": 0.344,\n            \"acc_norm_stderr,none\": 0.030104503392316392,\n\
  \            \"alias\": \"  - leaderboard_bbh_logical_deduction_three_objects\"\n\
  \        },\n        \"leaderboard_bbh_movie_recommendation\": {\n            \"\
  acc_norm,none\": 0.28,\n            \"acc_norm_stderr,none\": 0.028454148277832308,\n\
  \            \"alias\": \"  - leaderboard_bbh_movie_recommendation\"\n        },\n\
  \        \"leaderboard_bbh_navigate\": {\n            \"acc_norm,none\": 0.58,\n\
  \            \"acc_norm_stderr,none\": 0.03127799950463661,\n            \"alias\"\
  : \"  - leaderboard_bbh_navigate\"\n        },\n        \"leaderboard_bbh_object_counting\"\
  : {\n            \"acc_norm,none\": 0.072,\n            \"acc_norm_stderr,none\"\
  : 0.016381005750490105,\n            \"alias\": \"  - leaderboard_bbh_object_counting\"\
  \n        },\n        \"leaderboard_bbh_penguins_in_a_table\": {\n            \"\
  acc_norm,none\": 0.2191780821917808,\n            \"acc_norm_stderr,none\": 0.03435504786264927,\n\
  \            \"alias\": \"  - leaderboard_bbh_penguins_in_a_table\"\n        },\n\
  \        \"leaderboard_bbh_reasoning_about_colored_objects\": {\n            \"\
  acc_norm,none\": 0.096,\n            \"acc_norm_stderr,none\": 0.018668961419477156,\n\
  \            \"alias\": \"  - leaderboard_bbh_reasoning_about_colored_objects\"\n\
  \        },\n        \"leaderboard_bbh_ruin_names\": {\n            \"acc_norm,none\"\
  : 0.16,\n            \"acc_norm_stderr,none\": 0.02323271478206065,\n          \
  \  \"alias\": \"  - leaderboard_bbh_ruin_names\"\n        },\n        \"leaderboard_bbh_salient_translation_error_detection\"\
  : {\n            \"acc_norm,none\": 0.152,\n            \"acc_norm_stderr,none\"\
  : 0.02275202449176547,\n            \"alias\": \"  - leaderboard_bbh_salient_translation_error_detection\"\
  \n        },\n        \"leaderboard_bbh_snarks\": {\n            \"acc_norm,none\"\
  : 0.5617977528089888,\n            \"acc_norm_stderr,none\": 0.03729414592947276,\n\
  \            \"alias\": \"  - leaderboard_bbh_snarks\"\n        },\n        \"leaderboard_bbh_sports_understanding\"\
  : {\n            \"acc_norm,none\": 0.46,\n            \"acc_norm_stderr,none\"\
  : 0.031584653891499,\n            \"alias\": \"  - leaderboard_bbh_sports_understanding\"\
  \n        },\n        \"leaderboard_bbh_temporal_sequences\": {\n            \"\
  acc_norm,none\": 0.26,\n            \"acc_norm_stderr,none\": 0.027797315752644308,\n\
  \            \"alias\": \"  - leaderboard_bbh_temporal_sequences\"\n        },\n\
  \        \"leaderboard_bbh_tracking_shuffled_objects_five_objects\": {\n       \
  \     \"acc_norm,none\": 0.184,\n            \"acc_norm_stderr,none\": 0.02455581299422256,\n\
  \            \"alias\": \"  - leaderboard_bbh_tracking_shuffled_objects_five_objects\"\
  \n        },\n        \"leaderboard_bbh_tracking_shuffled_objects_seven_objects\"\
  : {\n            \"acc_norm,none\": 0.152,\n            \"acc_norm_stderr,none\"\
  : 0.022752024491765464,\n            \"alias\": \"  - leaderboard_bbh_tracking_shuffled_objects_seven_objects\"\
  \n        },\n        \"leaderboard_bbh_tracking_shuffled_objects_three_objects\"\
  : {\n            \"acc_norm,none\": 0.328,\n            \"acc_norm_stderr,none\"\
  : 0.02975239182447538,\n            \"alias\": \"  - leaderboard_bbh_tracking_shuffled_objects_three_objects\"\
  \n        },\n        \"leaderboard_bbh_web_of_lies\": {\n            \"acc_norm,none\"\
  : 0.512,\n            \"acc_norm_stderr,none\": 0.03167708558254709,\n         \
  \   \"alias\": \"  - leaderboard_bbh_web_of_lies\"\n        },\n        \"leaderboard_gpqa\"\
  : {\n            \"acc_norm,none\": 0.25922818791946306,\n            \"acc_norm_stderr,none\"\
  : 0.012707335192522795,\n            \"alias\": \" - leaderboard_gpqa\"\n      \
  \  },\n        \"leaderboard_gpqa_diamond\": {\n            \"acc_norm,none\": 0.2676767676767677,\n\
  \            \"acc_norm_stderr,none\": 0.03154449888270285,\n            \"alias\"\
  : \"  - leaderboard_gpqa_diamond\"\n        },\n        \"leaderboard_gpqa_extended\"\
  : {\n            \"acc_norm,none\": 0.2619047619047619,\n            \"acc_norm_stderr,none\"\
  : 0.01883343978951451,\n            \"alias\": \"  - leaderboard_gpqa_extended\"\
  \n        },\n        \"leaderboard_gpqa_main\": {\n            \"acc_norm,none\"\
  : 0.25223214285714285,\n            \"acc_norm_stderr,none\": 0.02054139101648797,\n\
  \            \"alias\": \"  - leaderboard_gpqa_main\"\n        },\n        \"leaderboard_ifeval\"\
  : {\n            \"prompt_level_strict_acc,none\": 0.1645101663585952,\n       \
  \     \"prompt_level_strict_acc_stderr,none\": 0.015954017926718047,\n         \
  \   \"inst_level_strict_acc,none\": 0.2745803357314149,\n            \"inst_level_strict_acc_stderr,none\"\
  : \"N/A\",\n            \"prompt_level_loose_acc,none\": 0.17005545286506468,\n\
  \            \"prompt_level_loose_acc_stderr,none\": 0.016166758064800228,\n   \
  \         \"inst_level_loose_acc,none\": 0.2841726618705036,\n            \"inst_level_loose_acc_stderr,none\"\
  : \"N/A\",\n            \"alias\": \" - leaderboard_ifeval\"\n        },\n     \
  \   \"leaderboard_math_hard\": {\n            \"exact_match,none\": 0.0030211480362537764,\n\
  \            \"exact_match_stderr,none\": 0.0015094760120804693,\n            \"\
  alias\": \" - leaderboard_math_hard\"\n        },\n        \"leaderboard_math_algebra_hard\"\
  : {\n            \"exact_match,none\": 0.006514657980456026,\n            \"exact_match_stderr,none\"\
  : 0.004599025618546266,\n            \"alias\": \"  - leaderboard_math_algebra_hard\"\
  \n        },\n        \"leaderboard_math_counting_and_prob_hard\": {\n         \
  \   \"exact_match,none\": 0.0,\n            \"exact_match_stderr,none\": 0.0,\n\
  \            \"alias\": \"  - leaderboard_math_counting_and_prob_hard\"\n      \
  \  },\n        \"leaderboard_math_geometry_hard\": {\n            \"exact_match,none\"\
  : 0.0,\n            \"exact_match_stderr,none\": 0.0,\n            \"alias\": \"\
  \  - leaderboard_math_geometry_hard\"\n        },\n        \"leaderboard_math_intermediate_algebra_hard\"\
  : {\n            \"exact_match,none\": 0.0,\n            \"exact_match_stderr,none\"\
  : 0.0,\n            \"alias\": \"  - leaderboard_math_intermediate_algebra_hard\"\
  \n        },\n        \"leaderboard_math_num_theory_hard\": {\n            \"exact_match,none\"\
  : 0.006493506493506494,\n            \"exact_match_stderr,none\": 0.006493506493506496,\n\
  \            \"alias\": \"  - leaderboard_math_num_theory_hard\"\n        },\n \
  \       \"leaderboard_math_prealgebra_hard\": {\n            \"exact_match,none\"\
  : 0.0,\n            \"exact_match_stderr,none\": 0.0,\n            \"alias\": \"\
  \  - leaderboard_math_prealgebra_hard\"\n        },\n        \"leaderboard_math_precalculus_hard\"\
  : {\n            \"exact_match,none\": 0.007407407407407408,\n            \"exact_match_stderr,none\"\
  : 0.007407407407407407,\n            \"alias\": \"  - leaderboard_math_precalculus_hard\"\
  \n        },\n        \"leaderboard_mmlu_pro\": {\n            \"acc,none\": 0.11278257978723404,\n\
  \            \"acc_stderr,none\": 0.002883933082801988,\n            \"alias\":\
  \ \" - leaderboard_mmlu_pro\"\n        },\n        \"leaderboard_musr\": {\n   \
  \         \"acc_norm,none\": 0.35714285714285715,\n            \"acc_norm_stderr,none\"\
  : 0.017127084208879092,\n            \"alias\": \" - leaderboard_musr\"\n      \
  \  },\n        \"leaderboard_musr_murder_mysteries\": {\n            \"acc_norm,none\"\
  : 0.488,\n            \"acc_norm_stderr,none\": 0.03167708558254709,\n         \
  \   \"alias\": \"  - leaderboard_musr_murder_mysteries\"\n        },\n        \"\
  leaderboard_musr_object_placements\": {\n            \"acc_norm,none\": 0.2734375,\n\
  \            \"acc_norm_stderr,none\": 0.027912287939448926,\n            \"alias\"\
  : \"  - leaderboard_musr_object_placements\"\n        },\n        \"leaderboard_musr_team_allocation\"\
  : {\n            \"acc_norm,none\": 0.312,\n            \"acc_norm_stderr,none\"\
  : 0.029361067575219817,\n            \"alias\": \"  - leaderboard_musr_team_allocation\"\
  \n        }\n    },\n    \"leaderboard\": {\n        \"inst_level_loose_acc,none\"\
  : 0.2841726618705036,\n        \"inst_level_loose_acc_stderr,none\": \"N/A\",\n\
  \        \"prompt_level_strict_acc,none\": 0.1645101663585952,\n        \"prompt_level_strict_acc_stderr,none\"\
  : 0.015954017926718047,\n        \"acc_norm,none\": 0.294448823330706,\n       \
  \ \"acc_norm_stderr,none\": 0.004632767730932793,\n        \"inst_level_strict_acc,none\"\
  : 0.2745803357314149,\n        \"inst_level_strict_acc_stderr,none\": \"N/A\",\n\
  \        \"exact_match,none\": 0.0030211480362537764,\n        \"exact_match_stderr,none\"\
  : 0.0015094760120804693,\n        \"acc,none\": 0.12269009391093608,\n        \"\
  acc_stderr,none\": 0.0028419658401793793,\n        \"prompt_level_loose_acc,none\"\
  : 0.17005545286506468,\n        \"prompt_level_loose_acc_stderr,none\": 0.016166758064800224,\n\
  \        \"alias\": \"leaderboard\"\n    },\n    \"leaderboard_arc_challenge\":\
  \ {\n        \"acc,none\": 0.22440273037542663,\n        \"acc_stderr,none\": 0.012191404938603836,\n\
  \        \"acc_norm,none\": 0.26535836177474403,\n        \"acc_norm_stderr,none\"\
  : 0.012902554762313962,\n        \"alias\": \" - leaderboard_arc_challenge\"\n \
  \   },\n    \"leaderboard_bbh\": {\n        \"acc_norm,none\": 0.29942718278076724,\n\
  \        \"acc_norm_stderr,none\": 0.005670206683862552,\n        \"alias\": \"\
  \ - leaderboard_bbh\"\n    },\n    \"leaderboard_bbh_boolean_expressions\": {\n\
  \        \"acc_norm,none\": 0.5,\n        \"acc_norm_stderr,none\": 0.031686212526223896,\n\
  \        \"alias\": \"  - leaderboard_bbh_boolean_expressions\"\n    },\n    \"\
  leaderboard_bbh_causal_judgement\": {\n        \"acc_norm,none\": 0.45454545454545453,\n\
  \        \"acc_norm_stderr,none\": 0.036509969495568145,\n        \"alias\": \"\
  \  - leaderboard_bbh_causal_judgement\"\n    },\n    \"leaderboard_bbh_date_understanding\"\
  : {\n        \"acc_norm,none\": 0.196,\n        \"acc_norm_stderr,none\": 0.025156857313255936,\n\
  \        \"alias\": \"  - leaderboard_bbh_date_understanding\"\n    },\n    \"leaderboard_bbh_disambiguation_qa\"\
  : {\n        \"acc_norm,none\": 0.312,\n        \"acc_norm_stderr,none\": 0.029361067575219817,\n\
  \        \"alias\": \"  - leaderboard_bbh_disambiguation_qa\"\n    },\n    \"leaderboard_bbh_formal_fallacies\"\
  : {\n        \"acc_norm,none\": 0.5,\n        \"acc_norm_stderr,none\": 0.031686212526223896,\n\
  \        \"alias\": \"  - leaderboard_bbh_formal_fallacies\"\n    },\n    \"leaderboard_bbh_geometric_shapes\"\
  : {\n        \"acc_norm,none\": 0.1,\n        \"acc_norm_stderr,none\": 0.01901172751573438,\n\
  \        \"alias\": \"  - leaderboard_bbh_geometric_shapes\"\n    },\n    \"leaderboard_bbh_hyperbaton\"\
  : {\n        \"acc_norm,none\": 0.472,\n        \"acc_norm_stderr,none\": 0.031636489531544396,\n\
  \        \"alias\": \"  - leaderboard_bbh_hyperbaton\"\n    },\n    \"leaderboard_bbh_logical_deduction_five_objects\"\
  : {\n        \"acc_norm,none\": 0.22,\n        \"acc_norm_stderr,none\": 0.02625179282460584,\n\
  \        \"alias\": \"  - leaderboard_bbh_logical_deduction_five_objects\"\n   \
  \ },\n    \"leaderboard_bbh_logical_deduction_seven_objects\": {\n        \"acc_norm,none\"\
  : 0.152,\n        \"acc_norm_stderr,none\": 0.022752024491765468,\n        \"alias\"\
  : \"  - leaderboard_bbh_logical_deduction_seven_objects\"\n    },\n    \"leaderboard_bbh_logical_deduction_three_objects\"\
  : {\n        \"acc_norm,none\": 0.344,\n        \"acc_norm_stderr,none\": 0.030104503392316392,\n\
  \        \"alias\": \"  - leaderboard_bbh_logical_deduction_three_objects\"\n  \
  \  },\n    \"leaderboard_bbh_movie_recommendation\": {\n        \"acc_norm,none\"\
  : 0.28,\n        \"acc_norm_stderr,none\": 0.028454148277832308,\n        \"alias\"\
  : \"  - leaderboard_bbh_movie_recommendation\"\n    },\n    \"leaderboard_bbh_navigate\"\
  : {\n        \"acc_norm,none\": 0.58,\n        \"acc_norm_stderr,none\": 0.03127799950463661,\n\
  \        \"alias\": \"  - leaderboard_bbh_navigate\"\n    },\n    \"leaderboard_bbh_object_counting\"\
  : {\n        \"acc_norm,none\": 0.072,\n        \"acc_norm_stderr,none\": 0.016381005750490105,\n\
  \        \"alias\": \"  - leaderboard_bbh_object_counting\"\n    },\n    \"leaderboard_bbh_penguins_in_a_table\"\
  : {\n        \"acc_norm,none\": 0.2191780821917808,\n        \"acc_norm_stderr,none\"\
  : 0.03435504786264927,\n        \"alias\": \"  - leaderboard_bbh_penguins_in_a_table\"\
  \n    },\n    \"leaderboard_bbh_reasoning_about_colored_objects\": {\n        \"\
  acc_norm,none\": 0.096,\n        \"acc_norm_stderr,none\": 0.018668961419477156,\n\
  \        \"alias\": \"  - leaderboard_bbh_reasoning_about_colored_objects\"\n  \
  \  },\n    \"leaderboard_bbh_ruin_names\": {\n        \"acc_norm,none\": 0.16,\n\
  \        \"acc_norm_stderr,none\": 0.02323271478206065,\n        \"alias\": \" \
  \ - leaderboard_bbh_ruin_names\"\n    },\n    \"leaderboard_bbh_salient_translation_error_detection\"\
  : {\n        \"acc_norm,none\": 0.152,\n        \"acc_norm_stderr,none\": 0.02275202449176547,\n\
  \        \"alias\": \"  - leaderboard_bbh_salient_translation_error_detection\"\n\
  \    },\n    \"leaderboard_bbh_snarks\": {\n        \"acc_norm,none\": 0.5617977528089888,\n\
  \        \"acc_norm_stderr,none\": 0.03729414592947276,\n        \"alias\": \" \
  \ - leaderboard_bbh_snarks\"\n    },\n    \"leaderboard_bbh_sports_understanding\"\
  : {\n        \"acc_norm,none\": 0.46,\n        \"acc_norm_stderr,none\": 0.031584653891499,\n\
  \        \"alias\": \"  - leaderboard_bbh_sports_understanding\"\n    },\n    \"\
  leaderboard_bbh_temporal_sequences\": {\n        \"acc_norm,none\": 0.26,\n    \
  \    \"acc_norm_stderr,none\": 0.027797315752644308,\n        \"alias\": \"  - leaderboard_bbh_temporal_sequences\"\
  \n    },\n    \"leaderboard_bbh_tracking_shuffled_objects_five_objects\": {\n  \
  \      \"acc_norm,none\": 0.184,\n        \"acc_norm_stderr,none\": 0.02455581299422256,\n\
  \        \"alias\": \"  - leaderboard_bbh_tracking_shuffled_objects_five_objects\"\
  \n    },\n    \"leaderboard_bbh_tracking_shuffled_objects_seven_objects\": {\n \
  \       \"acc_norm,none\": 0.152,\n        \"acc_norm_stderr,none\": 0.022752024491765464,\n\
  \        \"alias\": \"  - leaderboard_bbh_tracking_shuffled_objects_seven_objects\"\
  \n    },\n    \"leaderboard_bbh_tracking_shuffled_objects_three_objects\": {\n \
  \       \"acc_norm,none\": 0.328,\n        \"acc_norm_stderr,none\": 0.02975239182447538,\n\
  \        \"alias\": \"  - leaderboard_bbh_tracking_shuffled_objects_three_objects\"\
  \n    },\n    \"leaderboard_bbh_web_of_lies\": {\n        \"acc_norm,none\": 0.512,\n\
  \        \"acc_norm_stderr,none\": 0.03167708558254709,\n        \"alias\": \" \
  \ - leaderboard_bbh_web_of_lies\"\n    },\n    \"leaderboard_gpqa\": {\n       \
  \ \"acc_norm,none\": 0.25922818791946306,\n        \"acc_norm_stderr,none\": 0.012707335192522795,\n\
  \        \"alias\": \" - leaderboard_gpqa\"\n    },\n    \"leaderboard_gpqa_diamond\"\
  : {\n        \"acc_norm,none\": 0.2676767676767677,\n        \"acc_norm_stderr,none\"\
  : 0.03154449888270285,\n        \"alias\": \"  - leaderboard_gpqa_diamond\"\n  \
  \  },\n    \"leaderboard_gpqa_extended\": {\n        \"acc_norm,none\": 0.2619047619047619,\n\
  \        \"acc_norm_stderr,none\": 0.01883343978951451,\n        \"alias\": \" \
  \ - leaderboard_gpqa_extended\"\n    },\n    \"leaderboard_gpqa_main\": {\n    \
  \    \"acc_norm,none\": 0.25223214285714285,\n        \"acc_norm_stderr,none\":\
  \ 0.02054139101648797,\n        \"alias\": \"  - leaderboard_gpqa_main\"\n    },\n\
  \    \"leaderboard_ifeval\": {\n        \"prompt_level_strict_acc,none\": 0.1645101663585952,\n\
  \        \"prompt_level_strict_acc_stderr,none\": 0.015954017926718047,\n      \
  \  \"inst_level_strict_acc,none\": 0.2745803357314149,\n        \"inst_level_strict_acc_stderr,none\"\
  : \"N/A\",\n        \"prompt_level_loose_acc,none\": 0.17005545286506468,\n    \
  \    \"prompt_level_loose_acc_stderr,none\": 0.016166758064800228,\n        \"inst_level_loose_acc,none\"\
  : 0.2841726618705036,\n        \"inst_level_loose_acc_stderr,none\": \"N/A\",\n\
  \        \"alias\": \" - leaderboard_ifeval\"\n    },\n    \"leaderboard_math_hard\"\
  : {\n        \"exact_match,none\": 0.0030211480362537764,\n        \"exact_match_stderr,none\"\
  : 0.0015094760120804693,\n        \"alias\": \" - leaderboard_math_hard\"\n    },\n\
  \    \"leaderboard_math_algebra_hard\": {\n        \"exact_match,none\": 0.006514657980456026,\n\
  \        \"exact_match_stderr,none\": 0.004599025618546266,\n        \"alias\":\
  \ \"  - leaderboard_math_algebra_hard\"\n    },\n    \"leaderboard_math_counting_and_prob_hard\"\
  : {\n        \"exact_match,none\": 0.0,\n        \"exact_match_stderr,none\": 0.0,\n\
  \        \"alias\": \"  - leaderboard_math_counting_and_prob_hard\"\n    },\n  \
  \  \"leaderboard_math_geometry_hard\": {\n        \"exact_match,none\": 0.0,\n \
  \       \"exact_match_stderr,none\": 0.0,\n        \"alias\": \"  - leaderboard_math_geometry_hard\"\
  \n    },\n    \"leaderboard_math_intermediate_algebra_hard\": {\n        \"exact_match,none\"\
  : 0.0,\n        \"exact_match_stderr,none\": 0.0,\n        \"alias\": \"  - leaderboard_math_intermediate_algebra_hard\"\
  \n    },\n    \"leaderboard_math_num_theory_hard\": {\n        \"exact_match,none\"\
  : 0.006493506493506494,\n        \"exact_match_stderr,none\": 0.006493506493506496,\n\
  \        \"alias\": \"  - leaderboard_math_num_theory_hard\"\n    },\n    \"leaderboard_math_prealgebra_hard\"\
  : {\n        \"exact_match,none\": 0.0,\n        \"exact_match_stderr,none\": 0.0,\n\
  \        \"alias\": \"  - leaderboard_math_prealgebra_hard\"\n    },\n    \"leaderboard_math_precalculus_hard\"\
  : {\n        \"exact_match,none\": 0.007407407407407408,\n        \"exact_match_stderr,none\"\
  : 0.007407407407407407,\n        \"alias\": \"  - leaderboard_math_precalculus_hard\"\
  \n    },\n    \"leaderboard_mmlu_pro\": {\n        \"acc,none\": 0.11278257978723404,\n\
  \        \"acc_stderr,none\": 0.002883933082801988,\n        \"alias\": \" - leaderboard_mmlu_pro\"\
  \n    },\n    \"leaderboard_musr\": {\n        \"acc_norm,none\": 0.35714285714285715,\n\
  \        \"acc_norm_stderr,none\": 0.017127084208879092,\n        \"alias\": \"\
  \ - leaderboard_musr\"\n    },\n    \"leaderboard_musr_murder_mysteries\": {\n \
  \       \"acc_norm,none\": 0.488,\n        \"acc_norm_stderr,none\": 0.03167708558254709,\n\
  \        \"alias\": \"  - leaderboard_musr_murder_mysteries\"\n    },\n    \"leaderboard_musr_object_placements\"\
  : {\n        \"acc_norm,none\": 0.2734375,\n        \"acc_norm_stderr,none\": 0.027912287939448926,\n\
  \        \"alias\": \"  - leaderboard_musr_object_placements\"\n    },\n    \"leaderboard_musr_team_allocation\"\
  : {\n        \"acc_norm,none\": 0.312,\n        \"acc_norm_stderr,none\": 0.029361067575219817,\n\
  \        \"alias\": \"  - leaderboard_musr_team_allocation\"\n    }\n}\n```"
repo_url: https://huggingface.co/EleutherAI/pythia-410m
leaderboard_url: ''
point_of_contact: ''
configs:
- config_name: EleutherAI__pythia-410m__leaderboard_arc_challenge
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_arc_challenge_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_arc_challenge_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_bbh
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_bbh_boolean_expressions_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_causal_judgement_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_date_understanding_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_disambiguation_qa_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_formal_fallacies_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_geometric_shapes_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_hyperbaton_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_logical_deduction_five_objects_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_logical_deduction_seven_objects_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_logical_deduction_three_objects_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_movie_recommendation_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_navigate_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_object_counting_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_penguins_in_a_table_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_reasoning_about_colored_objects_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_ruin_names_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_salient_translation_error_detection_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_snarks_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_sports_understanding_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_temporal_sequences_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_five_objects_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_seven_objects_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_three_objects_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_web_of_lies_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_boolean_expressions_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_causal_judgement_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_date_understanding_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_disambiguation_qa_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_formal_fallacies_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_geometric_shapes_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_hyperbaton_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_logical_deduction_five_objects_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_logical_deduction_seven_objects_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_logical_deduction_three_objects_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_movie_recommendation_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_navigate_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_object_counting_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_penguins_in_a_table_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_reasoning_about_colored_objects_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_ruin_names_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_salient_translation_error_detection_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_snarks_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_sports_understanding_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_temporal_sequences_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_five_objects_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_seven_objects_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_three_objects_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_bbh_web_of_lies_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_bbh_boolean_expressions
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_bbh_boolean_expressions_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_boolean_expressions_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_bbh_causal_judgement
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_bbh_causal_judgement_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_causal_judgement_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_bbh_date_understanding
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_bbh_date_understanding_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_date_understanding_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_bbh_disambiguation_qa
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_bbh_disambiguation_qa_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_disambiguation_qa_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_bbh_formal_fallacies
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_bbh_formal_fallacies_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_formal_fallacies_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_bbh_geometric_shapes
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_bbh_geometric_shapes_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_geometric_shapes_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_bbh_hyperbaton
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_bbh_hyperbaton_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_hyperbaton_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_bbh_logical_deduction_five_objects
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_bbh_logical_deduction_five_objects_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_logical_deduction_five_objects_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_bbh_logical_deduction_seven_objects
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_bbh_logical_deduction_seven_objects_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_logical_deduction_seven_objects_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_bbh_logical_deduction_three_objects
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_bbh_logical_deduction_three_objects_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_logical_deduction_three_objects_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_bbh_movie_recommendation
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_bbh_movie_recommendation_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_movie_recommendation_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_bbh_navigate
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_bbh_navigate_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_navigate_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_bbh_object_counting
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_bbh_object_counting_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_object_counting_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_bbh_penguins_in_a_table
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_bbh_penguins_in_a_table_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_penguins_in_a_table_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_bbh_reasoning_about_colored_objects
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_bbh_reasoning_about_colored_objects_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_reasoning_about_colored_objects_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_bbh_ruin_names
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_bbh_ruin_names_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_ruin_names_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_bbh_salient_translation_error_detection
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_bbh_salient_translation_error_detection_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_salient_translation_error_detection_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_bbh_snarks
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_bbh_snarks_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_snarks_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_bbh_sports_understanding
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_bbh_sports_understanding_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_sports_understanding_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_bbh_temporal_sequences
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_bbh_temporal_sequences_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_temporal_sequences_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_bbh_tracking_shuffled_objects_five_objects
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_five_objects_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_five_objects_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_bbh_tracking_shuffled_objects_seven_objects
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_seven_objects_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_seven_objects_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_bbh_tracking_shuffled_objects_three_objects
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_three_objects_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_three_objects_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_bbh_web_of_lies
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_bbh_web_of_lies_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_web_of_lies_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_gpqa
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_gpqa_diamond_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_gpqa_extended_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_gpqa_main_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_gpqa_diamond_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_gpqa_extended_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_gpqa_main_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_gpqa_diamond
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_gpqa_diamond_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_gpqa_diamond_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_gpqa_extended
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_gpqa_extended_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_gpqa_extended_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_gpqa_main
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_gpqa_main_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_gpqa_main_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_ifeval
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_ifeval_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_ifeval_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_math
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_math_algebra_hard_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_math_counting_and_prob_hard_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_math_geometry_hard_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_math_intermediate_algebra_hard_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_math_num_theory_hard_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_math_prealgebra_hard_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_math_precalculus_hard_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_math_algebra_hard_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_math_counting_and_prob_hard_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_math_geometry_hard_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_math_intermediate_algebra_hard_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_math_num_theory_hard_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_math_prealgebra_hard_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_math_precalculus_hard_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_math_algebra_hard
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_math_algebra_hard_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_math_algebra_hard_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_math_counting_and_prob_hard
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_math_counting_and_prob_hard_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_math_counting_and_prob_hard_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_math_geometry_hard
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_math_geometry_hard_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_math_geometry_hard_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_math_intermediate_algebra_hard
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_math_intermediate_algebra_hard_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_math_intermediate_algebra_hard_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_math_num_theory_hard
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_math_num_theory_hard_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_math_num_theory_hard_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_math_prealgebra_hard
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_math_prealgebra_hard_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_math_prealgebra_hard_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_math_precalculus_hard
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_math_precalculus_hard_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_math_precalculus_hard_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_mmlu_pro
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_mmlu_pro_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_mmlu_pro_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_musr
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_musr_murder_mysteries_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_musr_object_placements_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_musr_team_allocation_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_musr_murder_mysteries_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_musr_object_placements_2024-06-16T22-11-25.600579.json'
    - '**/samples_leaderboard_musr_team_allocation_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_musr_murder_mysteries
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_musr_murder_mysteries_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_musr_murder_mysteries_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_musr_object_placements
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_musr_object_placements_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_musr_object_placements_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__leaderboard_musr_team_allocation
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/samples_leaderboard_musr_team_allocation_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/samples_leaderboard_musr_team_allocation_2024-06-16T22-11-25.600579.json'
- config_name: EleutherAI__pythia-410m__results
  data_files:
  - split: 2024_06_16T22_11_25.600579
    path:
    - '**/results_2024-06-16T22-11-25.600579.json'
  - split: latest
    path:
    - '**/results_2024-06-16T22-11-25.600579.json'
---

# Dataset Card for Evaluation run of EleutherAI/pythia-410m

<!-- Provide a quick summary of the dataset. -->

Dataset automatically created during the evaluation run of model [EleutherAI/pythia-410m](https://huggingface.co/EleutherAI/pythia-410m)
The dataset is composed of 44 configuration(s), each one corresponding to one of the evaluated task.

The dataset has been created from 2 run(s). Each run can be found as a specific split in each configuration, the split being named using the timestamp of the run.The "train" split is always pointing to the latest results.

An additional configuration "results" store all the aggregated results of the run.

To load the details from a run, you can for instance do the following:
```python
from datasets import load_dataset
data = load_dataset(
	"HuggingFaceEvalInternal/EleutherAI__pythia-410m-details-private",
	name="EleutherAI__pythia-410m__leaderboard_arc_challenge",
	split="latest"
)
```

## Latest results

These are the [latest results from run 2024-06-16T22-11-25.600579](https://huggingface.co/datasets/HuggingFaceEvalInternal/EleutherAI__pythia-410m-details-private/blob/main/EleutherAI__pythia-410m/results_2024-06-16T22-11-25.600579.json) (note that there might be results for other tasks in the repos if successive evals didn't cover the same tasks. You find each in the results and the "latest" split for each eval):

```python
{
    "all": {
        "leaderboard": {
            "inst_level_loose_acc,none": 0.2841726618705036,
            "inst_level_loose_acc_stderr,none": "N/A",
            "prompt_level_strict_acc,none": 0.1645101663585952,
            "prompt_level_strict_acc_stderr,none": 0.015954017926718047,
            "acc_norm,none": 0.294448823330706,
            "acc_norm_stderr,none": 0.004632767730932793,
            "inst_level_strict_acc,none": 0.2745803357314149,
            "inst_level_strict_acc_stderr,none": "N/A",
            "exact_match,none": 0.0030211480362537764,
            "exact_match_stderr,none": 0.0015094760120804693,
            "acc,none": 0.12269009391093608,
            "acc_stderr,none": 0.0028419658401793793,
            "prompt_level_loose_acc,none": 0.17005545286506468,
            "prompt_level_loose_acc_stderr,none": 0.016166758064800224,
            "alias": "leaderboard"
        },
        "leaderboard_arc_challenge": {
            "acc,none": 0.22440273037542663,
            "acc_stderr,none": 0.012191404938603836,
            "acc_norm,none": 0.26535836177474403,
            "acc_norm_stderr,none": 0.012902554762313962,
            "alias": " - leaderboard_arc_challenge"
        },
        "leaderboard_bbh": {
            "acc_norm,none": 0.29942718278076724,
            "acc_norm_stderr,none": 0.005670206683862552,
            "alias": " - leaderboard_bbh"
        },
        "leaderboard_bbh_boolean_expressions": {
            "acc_norm,none": 0.5,
            "acc_norm_stderr,none": 0.031686212526223896,
            "alias": "  - leaderboard_bbh_boolean_expressions"
        },
        "leaderboard_bbh_causal_judgement": {
            "acc_norm,none": 0.45454545454545453,
            "acc_norm_stderr,none": 0.036509969495568145,
            "alias": "  - leaderboard_bbh_causal_judgement"
        },
        "leaderboard_bbh_date_understanding": {
            "acc_norm,none": 0.196,
            "acc_norm_stderr,none": 0.025156857313255936,
            "alias": "  - leaderboard_bbh_date_understanding"
        },
        "leaderboard_bbh_disambiguation_qa": {
            "acc_norm,none": 0.312,
            "acc_norm_stderr,none": 0.029361067575219817,
            "alias": "  - leaderboard_bbh_disambiguation_qa"
        },
        "leaderboard_bbh_formal_fallacies": {
            "acc_norm,none": 0.5,
            "acc_norm_stderr,none": 0.031686212526223896,
            "alias": "  - leaderboard_bbh_formal_fallacies"
        },
        "leaderboard_bbh_geometric_shapes": {
            "acc_norm,none": 0.1,
            "acc_norm_stderr,none": 0.01901172751573438,
            "alias": "  - leaderboard_bbh_geometric_shapes"
        },
        "leaderboard_bbh_hyperbaton": {
            "acc_norm,none": 0.472,
            "acc_norm_stderr,none": 0.031636489531544396,
            "alias": "  - leaderboard_bbh_hyperbaton"
        },
        "leaderboard_bbh_logical_deduction_five_objects": {
            "acc_norm,none": 0.22,
            "acc_norm_stderr,none": 0.02625179282460584,
            "alias": "  - leaderboard_bbh_logical_deduction_five_objects"
        },
        "leaderboard_bbh_logical_deduction_seven_objects": {
            "acc_norm,none": 0.152,
            "acc_norm_stderr,none": 0.022752024491765468,
            "alias": "  - leaderboard_bbh_logical_deduction_seven_objects"
        },
        "leaderboard_bbh_logical_deduction_three_objects": {
            "acc_norm,none": 0.344,
            "acc_norm_stderr,none": 0.030104503392316392,
            "alias": "  - leaderboard_bbh_logical_deduction_three_objects"
        },
        "leaderboard_bbh_movie_recommendation": {
            "acc_norm,none": 0.28,
            "acc_norm_stderr,none": 0.028454148277832308,
            "alias": "  - leaderboard_bbh_movie_recommendation"
        },
        "leaderboard_bbh_navigate": {
            "acc_norm,none": 0.58,
            "acc_norm_stderr,none": 0.03127799950463661,
            "alias": "  - leaderboard_bbh_navigate"
        },
        "leaderboard_bbh_object_counting": {
            "acc_norm,none": 0.072,
            "acc_norm_stderr,none": 0.016381005750490105,
            "alias": "  - leaderboard_bbh_object_counting"
        },
        "leaderboard_bbh_penguins_in_a_table": {
            "acc_norm,none": 0.2191780821917808,
            "acc_norm_stderr,none": 0.03435504786264927,
            "alias": "  - leaderboard_bbh_penguins_in_a_table"
        },
        "leaderboard_bbh_reasoning_about_colored_objects": {
            "acc_norm,none": 0.096,
            "acc_norm_stderr,none": 0.018668961419477156,
            "alias": "  - leaderboard_bbh_reasoning_about_colored_objects"
        },
        "leaderboard_bbh_ruin_names": {
            "acc_norm,none": 0.16,
            "acc_norm_stderr,none": 0.02323271478206065,
            "alias": "  - leaderboard_bbh_ruin_names"
        },
        "leaderboard_bbh_salient_translation_error_detection": {
            "acc_norm,none": 0.152,
            "acc_norm_stderr,none": 0.02275202449176547,
            "alias": "  - leaderboard_bbh_salient_translation_error_detection"
        },
        "leaderboard_bbh_snarks": {
            "acc_norm,none": 0.5617977528089888,
            "acc_norm_stderr,none": 0.03729414592947276,
            "alias": "  - leaderboard_bbh_snarks"
        },
        "leaderboard_bbh_sports_understanding": {
            "acc_norm,none": 0.46,
            "acc_norm_stderr,none": 0.031584653891499,
            "alias": "  - leaderboard_bbh_sports_understanding"
        },
        "leaderboard_bbh_temporal_sequences": {
            "acc_norm,none": 0.26,
            "acc_norm_stderr,none": 0.027797315752644308,
            "alias": "  - leaderboard_bbh_temporal_sequences"
        },
        "leaderboard_bbh_tracking_shuffled_objects_five_objects": {
            "acc_norm,none": 0.184,
            "acc_norm_stderr,none": 0.02455581299422256,
            "alias": "  - leaderboard_bbh_tracking_shuffled_objects_five_objects"
        },
        "leaderboard_bbh_tracking_shuffled_objects_seven_objects": {
            "acc_norm,none": 0.152,
            "acc_norm_stderr,none": 0.022752024491765464,
            "alias": "  - leaderboard_bbh_tracking_shuffled_objects_seven_objects"
        },
        "leaderboard_bbh_tracking_shuffled_objects_three_objects": {
            "acc_norm,none": 0.328,
            "acc_norm_stderr,none": 0.02975239182447538,
            "alias": "  - leaderboard_bbh_tracking_shuffled_objects_three_objects"
        },
        "leaderboard_bbh_web_of_lies": {
            "acc_norm,none": 0.512,
            "acc_norm_stderr,none": 0.03167708558254709,
            "alias": "  - leaderboard_bbh_web_of_lies"
        },
        "leaderboard_gpqa": {
            "acc_norm,none": 0.25922818791946306,
            "acc_norm_stderr,none": 0.012707335192522795,
            "alias": " - leaderboard_gpqa"
        },
        "leaderboard_gpqa_diamond": {
            "acc_norm,none": 0.2676767676767677,
            "acc_norm_stderr,none": 0.03154449888270285,
            "alias": "  - leaderboard_gpqa_diamond"
        },
        "leaderboard_gpqa_extended": {
            "acc_norm,none": 0.2619047619047619,
            "acc_norm_stderr,none": 0.01883343978951451,
            "alias": "  - leaderboard_gpqa_extended"
        },
        "leaderboard_gpqa_main": {
            "acc_norm,none": 0.25223214285714285,
            "acc_norm_stderr,none": 0.02054139101648797,
            "alias": "  - leaderboard_gpqa_main"
        },
        "leaderboard_ifeval": {
            "prompt_level_strict_acc,none": 0.1645101663585952,
            "prompt_level_strict_acc_stderr,none": 0.015954017926718047,
            "inst_level_strict_acc,none": 0.2745803357314149,
            "inst_level_strict_acc_stderr,none": "N/A",
            "prompt_level_loose_acc,none": 0.17005545286506468,
            "prompt_level_loose_acc_stderr,none": 0.016166758064800228,
            "inst_level_loose_acc,none": 0.2841726618705036,
            "inst_level_loose_acc_stderr,none": "N/A",
            "alias": " - leaderboard_ifeval"
        },
        "leaderboard_math_hard": {
            "exact_match,none": 0.0030211480362537764,
            "exact_match_stderr,none": 0.0015094760120804693,
            "alias": " - leaderboard_math_hard"
        },
        "leaderboard_math_algebra_hard": {
            "exact_match,none": 0.006514657980456026,
            "exact_match_stderr,none": 0.004599025618546266,
            "alias": "  - leaderboard_math_algebra_hard"
        },
        "leaderboard_math_counting_and_prob_hard": {
            "exact_match,none": 0.0,
            "exact_match_stderr,none": 0.0,
            "alias": "  - leaderboard_math_counting_and_prob_hard"
        },
        "leaderboard_math_geometry_hard": {
            "exact_match,none": 0.0,
            "exact_match_stderr,none": 0.0,
            "alias": "  - leaderboard_math_geometry_hard"
        },
        "leaderboard_math_intermediate_algebra_hard": {
            "exact_match,none": 0.0,
            "exact_match_stderr,none": 0.0,
            "alias": "  - leaderboard_math_intermediate_algebra_hard"
        },
        "leaderboard_math_num_theory_hard": {
            "exact_match,none": 0.006493506493506494,
            "exact_match_stderr,none": 0.006493506493506496,
            "alias": "  - leaderboard_math_num_theory_hard"
        },
        "leaderboard_math_prealgebra_hard": {
            "exact_match,none": 0.0,
            "exact_match_stderr,none": 0.0,
            "alias": "  - leaderboard_math_prealgebra_hard"
        },
        "leaderboard_math_precalculus_hard": {
            "exact_match,none": 0.007407407407407408,
            "exact_match_stderr,none": 0.007407407407407407,
            "alias": "  - leaderboard_math_precalculus_hard"
        },
        "leaderboard_mmlu_pro": {
            "acc,none": 0.11278257978723404,
            "acc_stderr,none": 0.002883933082801988,
            "alias": " - leaderboard_mmlu_pro"
        },
        "leaderboard_musr": {
            "acc_norm,none": 0.35714285714285715,
            "acc_norm_stderr,none": 0.017127084208879092,
            "alias": " - leaderboard_musr"
        },
        "leaderboard_musr_murder_mysteries": {
            "acc_norm,none": 0.488,
            "acc_norm_stderr,none": 0.03167708558254709,
            "alias": "  - leaderboard_musr_murder_mysteries"
        },
        "leaderboard_musr_object_placements": {
            "acc_norm,none": 0.2734375,
            "acc_norm_stderr,none": 0.027912287939448926,
            "alias": "  - leaderboard_musr_object_placements"
        },
        "leaderboard_musr_team_allocation": {
            "acc_norm,none": 0.312,
            "acc_norm_stderr,none": 0.029361067575219817,
            "alias": "  - leaderboard_musr_team_allocation"
        }
    },
    "leaderboard": {
        "inst_level_loose_acc,none": 0.2841726618705036,
        "inst_level_loose_acc_stderr,none": "N/A",
        "prompt_level_strict_acc,none": 0.1645101663585952,
        "prompt_level_strict_acc_stderr,none": 0.015954017926718047,
        "acc_norm,none": 0.294448823330706,
        "acc_norm_stderr,none": 0.004632767730932793,
        "inst_level_strict_acc,none": 0.2745803357314149,
        "inst_level_strict_acc_stderr,none": "N/A",
        "exact_match,none": 0.0030211480362537764,
        "exact_match_stderr,none": 0.0015094760120804693,
        "acc,none": 0.12269009391093608,
        "acc_stderr,none": 0.0028419658401793793,
        "prompt_level_loose_acc,none": 0.17005545286506468,
        "prompt_level_loose_acc_stderr,none": 0.016166758064800224,
        "alias": "leaderboard"
    },
    "leaderboard_arc_challenge": {
        "acc,none": 0.22440273037542663,
        "acc_stderr,none": 0.012191404938603836,
        "acc_norm,none": 0.26535836177474403,
        "acc_norm_stderr,none": 0.012902554762313962,
        "alias": " - leaderboard_arc_challenge"
    },
    "leaderboard_bbh": {
        "acc_norm,none": 0.29942718278076724,
        "acc_norm_stderr,none": 0.005670206683862552,
        "alias": " - leaderboard_bbh"
    },
    "leaderboard_bbh_boolean_expressions": {
        "acc_norm,none": 0.5,
        "acc_norm_stderr,none": 0.031686212526223896,
        "alias": "  - leaderboard_bbh_boolean_expressions"
    },
    "leaderboard_bbh_causal_judgement": {
        "acc_norm,none": 0.45454545454545453,
        "acc_norm_stderr,none": 0.036509969495568145,
        "alias": "  - leaderboard_bbh_causal_judgement"
    },
    "leaderboard_bbh_date_understanding": {
        "acc_norm,none": 0.196,
        "acc_norm_stderr,none": 0.025156857313255936,
        "alias": "  - leaderboard_bbh_date_understanding"
    },
    "leaderboard_bbh_disambiguation_qa": {
        "acc_norm,none": 0.312,
        "acc_norm_stderr,none": 0.029361067575219817,
        "alias": "  - leaderboard_bbh_disambiguation_qa"
    },
    "leaderboard_bbh_formal_fallacies": {
        "acc_norm,none": 0.5,
        "acc_norm_stderr,none": 0.031686212526223896,
        "alias": "  - leaderboard_bbh_formal_fallacies"
    },
    "leaderboard_bbh_geometric_shapes": {
        "acc_norm,none": 0.1,
        "acc_norm_stderr,none": 0.01901172751573438,
        "alias": "  - leaderboard_bbh_geometric_shapes"
    },
    "leaderboard_bbh_hyperbaton": {
        "acc_norm,none": 0.472,
        "acc_norm_stderr,none": 0.031636489531544396,
        "alias": "  - leaderboard_bbh_hyperbaton"
    },
    "leaderboard_bbh_logical_deduction_five_objects": {
        "acc_norm,none": 0.22,
        "acc_norm_stderr,none": 0.02625179282460584,
        "alias": "  - leaderboard_bbh_logical_deduction_five_objects"
    },
    "leaderboard_bbh_logical_deduction_seven_objects": {
        "acc_norm,none": 0.152,
        "acc_norm_stderr,none": 0.022752024491765468,
        "alias": "  - leaderboard_bbh_logical_deduction_seven_objects"
    },
    "leaderboard_bbh_logical_deduction_three_objects": {
        "acc_norm,none": 0.344,
        "acc_norm_stderr,none": 0.030104503392316392,
        "alias": "  - leaderboard_bbh_logical_deduction_three_objects"
    },
    "leaderboard_bbh_movie_recommendation": {
        "acc_norm,none": 0.28,
        "acc_norm_stderr,none": 0.028454148277832308,
        "alias": "  - leaderboard_bbh_movie_recommendation"
    },
    "leaderboard_bbh_navigate": {
        "acc_norm,none": 0.58,
        "acc_norm_stderr,none": 0.03127799950463661,
        "alias": "  - leaderboard_bbh_navigate"
    },
    "leaderboard_bbh_object_counting": {
        "acc_norm,none": 0.072,
        "acc_norm_stderr,none": 0.016381005750490105,
        "alias": "  - leaderboard_bbh_object_counting"
    },
    "leaderboard_bbh_penguins_in_a_table": {
        "acc_norm,none": 0.2191780821917808,
        "acc_norm_stderr,none": 0.03435504786264927,
        "alias": "  - leaderboard_bbh_penguins_in_a_table"
    },
    "leaderboard_bbh_reasoning_about_colored_objects": {
        "acc_norm,none": 0.096,
        "acc_norm_stderr,none": 0.018668961419477156,
        "alias": "  - leaderboard_bbh_reasoning_about_colored_objects"
    },
    "leaderboard_bbh_ruin_names": {
        "acc_norm,none": 0.16,
        "acc_norm_stderr,none": 0.02323271478206065,
        "alias": "  - leaderboard_bbh_ruin_names"
    },
    "leaderboard_bbh_salient_translation_error_detection": {
        "acc_norm,none": 0.152,
        "acc_norm_stderr,none": 0.02275202449176547,
        "alias": "  - leaderboard_bbh_salient_translation_error_detection"
    },
    "leaderboard_bbh_snarks": {
        "acc_norm,none": 0.5617977528089888,
        "acc_norm_stderr,none": 0.03729414592947276,
        "alias": "  - leaderboard_bbh_snarks"
    },
    "leaderboard_bbh_sports_understanding": {
        "acc_norm,none": 0.46,
        "acc_norm_stderr,none": 0.031584653891499,
        "alias": "  - leaderboard_bbh_sports_understanding"
    },
    "leaderboard_bbh_temporal_sequences": {
        "acc_norm,none": 0.26,
        "acc_norm_stderr,none": 0.027797315752644308,
        "alias": "  - leaderboard_bbh_temporal_sequences"
    },
    "leaderboard_bbh_tracking_shuffled_objects_five_objects": {
        "acc_norm,none": 0.184,
        "acc_norm_stderr,none": 0.02455581299422256,
        "alias": "  - leaderboard_bbh_tracking_shuffled_objects_five_objects"
    },
    "leaderboard_bbh_tracking_shuffled_objects_seven_objects": {
        "acc_norm,none": 0.152,
        "acc_norm_stderr,none": 0.022752024491765464,
        "alias": "  - leaderboard_bbh_tracking_shuffled_objects_seven_objects"
    },
    "leaderboard_bbh_tracking_shuffled_objects_three_objects": {
        "acc_norm,none": 0.328,
        "acc_norm_stderr,none": 0.02975239182447538,
        "alias": "  - leaderboard_bbh_tracking_shuffled_objects_three_objects"
    },
    "leaderboard_bbh_web_of_lies": {
        "acc_norm,none": 0.512,
        "acc_norm_stderr,none": 0.03167708558254709,
        "alias": "  - leaderboard_bbh_web_of_lies"
    },
    "leaderboard_gpqa": {
        "acc_norm,none": 0.25922818791946306,
        "acc_norm_stderr,none": 0.012707335192522795,
        "alias": " - leaderboard_gpqa"
    },
    "leaderboard_gpqa_diamond": {
        "acc_norm,none": 0.2676767676767677,
        "acc_norm_stderr,none": 0.03154449888270285,
        "alias": "  - leaderboard_gpqa_diamond"
    },
    "leaderboard_gpqa_extended": {
        "acc_norm,none": 0.2619047619047619,
        "acc_norm_stderr,none": 0.01883343978951451,
        "alias": "  - leaderboard_gpqa_extended"
    },
    "leaderboard_gpqa_main": {
        "acc_norm,none": 0.25223214285714285,
        "acc_norm_stderr,none": 0.02054139101648797,
        "alias": "  - leaderboard_gpqa_main"
    },
    "leaderboard_ifeval": {
        "prompt_level_strict_acc,none": 0.1645101663585952,
        "prompt_level_strict_acc_stderr,none": 0.015954017926718047,
        "inst_level_strict_acc,none": 0.2745803357314149,
        "inst_level_strict_acc_stderr,none": "N/A",
        "prompt_level_loose_acc,none": 0.17005545286506468,
        "prompt_level_loose_acc_stderr,none": 0.016166758064800228,
        "inst_level_loose_acc,none": 0.2841726618705036,
        "inst_level_loose_acc_stderr,none": "N/A",
        "alias": " - leaderboard_ifeval"
    },
    "leaderboard_math_hard": {
        "exact_match,none": 0.0030211480362537764,
        "exact_match_stderr,none": 0.0015094760120804693,
        "alias": " - leaderboard_math_hard"
    },
    "leaderboard_math_algebra_hard": {
        "exact_match,none": 0.006514657980456026,
        "exact_match_stderr,none": 0.004599025618546266,
        "alias": "  - leaderboard_math_algebra_hard"
    },
    "leaderboard_math_counting_and_prob_hard": {
        "exact_match,none": 0.0,
        "exact_match_stderr,none": 0.0,
        "alias": "  - leaderboard_math_counting_and_prob_hard"
    },
    "leaderboard_math_geometry_hard": {
        "exact_match,none": 0.0,
        "exact_match_stderr,none": 0.0,
        "alias": "  - leaderboard_math_geometry_hard"
    },
    "leaderboard_math_intermediate_algebra_hard": {
        "exact_match,none": 0.0,
        "exact_match_stderr,none": 0.0,
        "alias": "  - leaderboard_math_intermediate_algebra_hard"
    },
    "leaderboard_math_num_theory_hard": {
        "exact_match,none": 0.006493506493506494,
        "exact_match_stderr,none": 0.006493506493506496,
        "alias": "  - leaderboard_math_num_theory_hard"
    },
    "leaderboard_math_prealgebra_hard": {
        "exact_match,none": 0.0,
        "exact_match_stderr,none": 0.0,
        "alias": "  - leaderboard_math_prealgebra_hard"
    },
    "leaderboard_math_precalculus_hard": {
        "exact_match,none": 0.007407407407407408,
        "exact_match_stderr,none": 0.007407407407407407,
        "alias": "  - leaderboard_math_precalculus_hard"
    },
    "leaderboard_mmlu_pro": {
        "acc,none": 0.11278257978723404,
        "acc_stderr,none": 0.002883933082801988,
        "alias": " - leaderboard_mmlu_pro"
    },
    "leaderboard_musr": {
        "acc_norm,none": 0.35714285714285715,
        "acc_norm_stderr,none": 0.017127084208879092,
        "alias": " - leaderboard_musr"
    },
    "leaderboard_musr_murder_mysteries": {
        "acc_norm,none": 0.488,
        "acc_norm_stderr,none": 0.03167708558254709,
        "alias": "  - leaderboard_musr_murder_mysteries"
    },
    "leaderboard_musr_object_placements": {
        "acc_norm,none": 0.2734375,
        "acc_norm_stderr,none": 0.027912287939448926,
        "alias": "  - leaderboard_musr_object_placements"
    },
    "leaderboard_musr_team_allocation": {
        "acc_norm,none": 0.312,
        "acc_norm_stderr,none": 0.029361067575219817,
        "alias": "  - leaderboard_musr_team_allocation"
    }
}
```

## Dataset Details

### Dataset Description

<!-- Provide a longer summary of what this dataset is. -->



- **Curated by:** [More Information Needed]
- **Funded by [optional]:** [More Information Needed]
- **Shared by [optional]:** [More Information Needed]
- **Language(s) (NLP):** [More Information Needed]
- **License:** [More Information Needed]

### Dataset Sources [optional]

<!-- Provide the basic links for the dataset. -->

- **Repository:** [More Information Needed]
- **Paper [optional]:** [More Information Needed]
- **Demo [optional]:** [More Information Needed]

## Uses

<!-- Address questions around how the dataset is intended to be used. -->

### Direct Use

<!-- This section describes suitable use cases for the dataset. -->

[More Information Needed]

### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the dataset will not work well for. -->

[More Information Needed]

## Dataset Structure

<!-- This section provides a description of the dataset fields, and additional information about the dataset structure such as criteria used to create the splits, relationships between data points, etc. -->

[More Information Needed]

## Dataset Creation

### Curation Rationale

<!-- Motivation for the creation of this dataset. -->

[More Information Needed]

### Source Data

<!-- This section describes the source data (e.g. news text and headlines, social media posts, translated sentences, ...). -->

#### Data Collection and Processing

<!-- This section describes the data collection and processing process such as data selection criteria, filtering and normalization methods, tools and libraries used, etc. -->

[More Information Needed]

#### Who are the source data producers?

<!-- This section describes the people or systems who originally created the data. It should also include self-reported demographic or identity information for the source data creators if this information is available. -->

[More Information Needed]

### Annotations [optional]

<!-- If the dataset contains annotations which are not part of the initial data collection, use this section to describe them. -->

#### Annotation process

<!-- This section describes the annotation process such as annotation tools used in the process, the amount of data annotated, annotation guidelines provided to the annotators, interannotator statistics, annotation validation, etc. -->

[More Information Needed]

#### Who are the annotators?

<!-- This section describes the people or systems who created the annotations. -->

[More Information Needed]

#### Personal and Sensitive Information

<!-- State whether the dataset contains data that might be considered personal, sensitive, or private (e.g., data that reveals addresses, uniquely identifiable names or aliases, racial or ethnic origins, sexual orientations, religious beliefs, political opinions, financial or health data, etc.). If efforts were made to anonymize the data, describe the anonymization process. -->

[More Information Needed]

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

[More Information Needed]

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

Users should be made aware of the risks, biases and limitations of the dataset. More information needed for further recommendations.

## Citation [optional]

<!-- If there is a paper or blog post introducing the dataset, the APA and Bibtex information for that should go in this section. -->

**BibTeX:**

[More Information Needed]

**APA:**

[More Information Needed]

## Glossary [optional]

<!-- If relevant, include terms and calculations in this section that can help readers understand the dataset or dataset card. -->

[More Information Needed]

## More Information [optional]

[More Information Needed]

## Dataset Card Authors [optional]

[More Information Needed]

## Dataset Card Contact

[More Information Needed]