---
pretty_name: Evaluation run of EleutherAI/pythia-6.9b
dataset_summary: "Dataset automatically created during the evaluation run of model\
  \ [EleutherAI/pythia-6.9b](https://huggingface.co/EleutherAI/pythia-6.9b)\nThe dataset\
  \ is composed of 44 configuration(s), each one corresponding to one of the evaluated\
  \ task.\n\nThe dataset has been created from 2 run(s). Each run can be found as\
  \ a specific split in each configuration, the split being named using the timestamp\
  \ of the run.The \"train\" split is always pointing to the latest results.\n\nAn\
  \ additional configuration \"results\" store all the aggregated results of the run.\n\
  \nTo load the details from a run, you can for instance do the following:\n```python\n\
  from datasets import load_dataset\ndata = load_dataset(\n\t\"HuggingFaceEvalInternal/EleutherAI__pythia-6.9b-details-private\"\
  ,\n\tname=\"EleutherAI__pythia-6.9b__leaderboard_arc_challenge\",\n\tsplit=\"latest\"\
  \n)\n```\n\n## Latest results\n\nThese are the [latest results from run 2024-06-16T22-34-46.256992](https://huggingface.co/datasets/HuggingFaceEvalInternal/EleutherAI__pythia-6.9b-details-private/blob/main/EleutherAI__pythia-6.9b/results_2024-06-16T22-34-46.256992.json)\
  \ (note that there might be results for other tasks in the repos if successive evals\
  \ didn't cover the same tasks. You find each in the results and the \"latest\" split\
  \ for each eval):\n\n```python\n{\n    \"all\": {\n        \"leaderboard\": {\n\
  \            \"acc,none\": 0.13586791881248106,\n            \"acc_stderr,none\"\
  : 0.0029231067788900054,\n            \"inst_level_strict_acc,none\": 0.3009592326139089,\n\
  \            \"inst_level_strict_acc_stderr,none\": \"N/A\",\n            \"exact_match,none\"\
  : 0.0075528700906344415,\n            \"exact_match_stderr,none\": 0.002382555425404601,\n\
  \            \"inst_level_loose_acc,none\": 0.30935251798561153,\n            \"\
  inst_level_loose_acc_stderr,none\": \"N/A\",\n            \"acc_norm,none\": 0.3244004053597568,\n\
  \            \"acc_norm_stderr,none\": 0.004738972468859114,\n            \"prompt_level_strict_acc,none\"\
  : 0.15526802218114602,\n            \"prompt_level_strict_acc_stderr,none\": 0.015584884858538145,\n\
  \            \"prompt_level_loose_acc,none\": 0.1589648798521257,\n            \"\
  prompt_level_loose_acc_stderr,none\": 0.015734783762341237,\n            \"alias\"\
  : \"leaderboard\"\n        },\n        \"leaderboard_arc_challenge\": {\n      \
  \      \"acc,none\": 0.3532423208191126,\n            \"acc_stderr,none\": 0.013967822714840056,\n\
  \            \"acc_norm,none\": 0.3967576791808874,\n            \"acc_norm_stderr,none\"\
  : 0.014296513020180635,\n            \"alias\": \" - leaderboard_arc_challenge\"\
  \n        },\n        \"leaderboard_bbh\": {\n            \"acc_norm,none\": 0.32025689984377714,\n\
  \            \"acc_norm_stderr,none\": 0.00575480578331762,\n            \"alias\"\
  : \" - leaderboard_bbh\"\n        },\n        \"leaderboard_bbh_boolean_expressions\"\
  : {\n            \"acc_norm,none\": 0.68,\n            \"acc_norm_stderr,none\"\
  : 0.029561724955241037,\n            \"alias\": \"  - leaderboard_bbh_boolean_expressions\"\
  \n        },\n        \"leaderboard_bbh_causal_judgement\": {\n            \"acc_norm,none\"\
  : 0.5133689839572193,\n            \"acc_norm_stderr,none\": 0.03664867131244298,\n\
  \            \"alias\": \"  - leaderboard_bbh_causal_judgement\"\n        },\n \
  \       \"leaderboard_bbh_date_understanding\": {\n            \"acc_norm,none\"\
  : 0.14,\n            \"acc_norm_stderr,none\": 0.021989409645240265,\n         \
  \   \"alias\": \"  - leaderboard_bbh_date_understanding\"\n        },\n        \"\
  leaderboard_bbh_disambiguation_qa\": {\n            \"acc_norm,none\": 0.384,\n\
  \            \"acc_norm_stderr,none\": 0.030821679117375374,\n            \"alias\"\
  : \"  - leaderboard_bbh_disambiguation_qa\"\n        },\n        \"leaderboard_bbh_formal_fallacies\"\
  : {\n            \"acc_norm,none\": 0.532,\n            \"acc_norm_stderr,none\"\
  : 0.031621252575725504,\n            \"alias\": \"  - leaderboard_bbh_formal_fallacies\"\
  \n        },\n        \"leaderboard_bbh_geometric_shapes\": {\n            \"acc_norm,none\"\
  : 0.128,\n            \"acc_norm_stderr,none\": 0.021172081336336482,\n        \
  \    \"alias\": \"  - leaderboard_bbh_geometric_shapes\"\n        },\n        \"\
  leaderboard_bbh_hyperbaton\": {\n            \"acc_norm,none\": 0.484,\n       \
  \     \"acc_norm_stderr,none\": 0.031669985030107414,\n            \"alias\": \"\
  \  - leaderboard_bbh_hyperbaton\"\n        },\n        \"leaderboard_bbh_logical_deduction_five_objects\"\
  : {\n            \"acc_norm,none\": 0.216,\n            \"acc_norm_stderr,none\"\
  : 0.02607865766373272,\n            \"alias\": \"  - leaderboard_bbh_logical_deduction_five_objects\"\
  \n        },\n        \"leaderboard_bbh_logical_deduction_seven_objects\": {\n \
  \           \"acc_norm,none\": 0.176,\n            \"acc_norm_stderr,none\": 0.024133497525457112,\n\
  \            \"alias\": \"  - leaderboard_bbh_logical_deduction_seven_objects\"\n\
  \        },\n        \"leaderboard_bbh_logical_deduction_three_objects\": {\n  \
  \          \"acc_norm,none\": 0.304,\n            \"acc_norm_stderr,none\": 0.029150213374159677,\n\
  \            \"alias\": \"  - leaderboard_bbh_logical_deduction_three_objects\"\n\
  \        },\n        \"leaderboard_bbh_movie_recommendation\": {\n            \"\
  acc_norm,none\": 0.292,\n            \"acc_norm_stderr,none\": 0.02881432040220563,\n\
  \            \"alias\": \"  - leaderboard_bbh_movie_recommendation\"\n        },\n\
  \        \"leaderboard_bbh_navigate\": {\n            \"acc_norm,none\": 0.568,\n\
  \            \"acc_norm_stderr,none\": 0.031391810765429407,\n            \"alias\"\
  : \"  - leaderboard_bbh_navigate\"\n        },\n        \"leaderboard_bbh_object_counting\"\
  : {\n            \"acc_norm,none\": 0.204,\n            \"acc_norm_stderr,none\"\
  : 0.025537121574548183,\n            \"alias\": \"  - leaderboard_bbh_object_counting\"\
  \n        },\n        \"leaderboard_bbh_penguins_in_a_table\": {\n            \"\
  acc_norm,none\": 0.2191780821917808,\n            \"acc_norm_stderr,none\": 0.03435504786264928,\n\
  \            \"alias\": \"  - leaderboard_bbh_penguins_in_a_table\"\n        },\n\
  \        \"leaderboard_bbh_reasoning_about_colored_objects\": {\n            \"\
  acc_norm,none\": 0.148,\n            \"acc_norm_stderr,none\": 0.02250354724380614,\n\
  \            \"alias\": \"  - leaderboard_bbh_reasoning_about_colored_objects\"\n\
  \        },\n        \"leaderboard_bbh_ruin_names\": {\n            \"acc_norm,none\"\
  : 0.244,\n            \"acc_norm_stderr,none\": 0.027217995464553175,\n        \
  \    \"alias\": \"  - leaderboard_bbh_ruin_names\"\n        },\n        \"leaderboard_bbh_salient_translation_error_detection\"\
  : {\n            \"acc_norm,none\": 0.16,\n            \"acc_norm_stderr,none\"\
  : 0.023232714782060647,\n            \"alias\": \"  - leaderboard_bbh_salient_translation_error_detection\"\
  \n        },\n        \"leaderboard_bbh_snarks\": {\n            \"acc_norm,none\"\
  : 0.5449438202247191,\n            \"acc_norm_stderr,none\": 0.03743016495716993,\n\
  \            \"alias\": \"  - leaderboard_bbh_snarks\"\n        },\n        \"leaderboard_bbh_sports_understanding\"\
  : {\n            \"acc_norm,none\": 0.456,\n            \"acc_norm_stderr,none\"\
  : 0.03156328506121339,\n            \"alias\": \"  - leaderboard_bbh_sports_understanding\"\
  \n        },\n        \"leaderboard_bbh_temporal_sequences\": {\n            \"\
  acc_norm,none\": 0.264,\n            \"acc_norm_stderr,none\": 0.02793451895769091,\n\
  \            \"alias\": \"  - leaderboard_bbh_temporal_sequences\"\n        },\n\
  \        \"leaderboard_bbh_tracking_shuffled_objects_five_objects\": {\n       \
  \     \"acc_norm,none\": 0.148,\n            \"acc_norm_stderr,none\": 0.022503547243806148,\n\
  \            \"alias\": \"  - leaderboard_bbh_tracking_shuffled_objects_five_objects\"\
  \n        },\n        \"leaderboard_bbh_tracking_shuffled_objects_seven_objects\"\
  : {\n            \"acc_norm,none\": 0.124,\n            \"acc_norm_stderr,none\"\
  : 0.02088638225867326,\n            \"alias\": \"  - leaderboard_bbh_tracking_shuffled_objects_seven_objects\"\
  \n        },\n        \"leaderboard_bbh_tracking_shuffled_objects_three_objects\"\
  : {\n            \"acc_norm,none\": 0.32,\n            \"acc_norm_stderr,none\"\
  : 0.029561724955241044,\n            \"alias\": \"  - leaderboard_bbh_tracking_shuffled_objects_three_objects\"\
  \n        },\n        \"leaderboard_bbh_web_of_lies\": {\n            \"acc_norm,none\"\
  : 0.508,\n            \"acc_norm_stderr,none\": 0.0316821564314138,\n          \
  \  \"alias\": \"  - leaderboard_bbh_web_of_lies\"\n        },\n        \"leaderboard_gpqa\"\
  : {\n            \"acc_norm,none\": 0.2516778523489933,\n            \"acc_norm_stderr,none\"\
  : 0.012579395838405717,\n            \"alias\": \" - leaderboard_gpqa\"\n      \
  \  },\n        \"leaderboard_gpqa_diamond\": {\n            \"acc_norm,none\": 0.2676767676767677,\n\
  \            \"acc_norm_stderr,none\": 0.03154449888270286,\n            \"alias\"\
  : \"  - leaderboard_gpqa_diamond\"\n        },\n        \"leaderboard_gpqa_extended\"\
  : {\n            \"acc_norm,none\": 0.2600732600732601,\n            \"acc_norm_stderr,none\"\
  : 0.018790743352016005,\n            \"alias\": \"  - leaderboard_gpqa_extended\"\
  \n        },\n        \"leaderboard_gpqa_main\": {\n            \"acc_norm,none\"\
  : 0.234375,\n            \"acc_norm_stderr,none\": 0.020035949758324928,\n     \
  \       \"alias\": \"  - leaderboard_gpqa_main\"\n        },\n        \"leaderboard_ifeval\"\
  : {\n            \"prompt_level_strict_acc,none\": 0.15526802218114602,\n      \
  \      \"prompt_level_strict_acc_stderr,none\": 0.015584884858538145,\n        \
  \    \"inst_level_strict_acc,none\": 0.3009592326139089,\n            \"inst_level_strict_acc_stderr,none\"\
  : \"N/A\",\n            \"prompt_level_loose_acc,none\": 0.1589648798521257,\n \
  \           \"prompt_level_loose_acc_stderr,none\": 0.015734783762341237,\n    \
  \        \"inst_level_loose_acc,none\": 0.30935251798561153,\n            \"inst_level_loose_acc_stderr,none\"\
  : \"N/A\",\n            \"alias\": \" - leaderboard_ifeval\"\n        },\n     \
  \   \"leaderboard_math_hard\": {\n            \"exact_match,none\": 0.0075528700906344415,\n\
  \            \"exact_match_stderr,none\": 0.002382555425404601,\n            \"\
  alias\": \" - leaderboard_math_hard\"\n        },\n        \"leaderboard_math_algebra_hard\"\
  : {\n            \"exact_match,none\": 0.009771986970684038,\n            \"exact_match_stderr,none\"\
  : 0.005623391633915873,\n            \"alias\": \"  - leaderboard_math_algebra_hard\"\
  \n        },\n        \"leaderboard_math_counting_and_prob_hard\": {\n         \
  \   \"exact_match,none\": 0.008130081300813009,\n            \"exact_match_stderr,none\"\
  : 0.008130081300812999,\n            \"alias\": \"  - leaderboard_math_counting_and_prob_hard\"\
  \n        },\n        \"leaderboard_math_geometry_hard\": {\n            \"exact_match,none\"\
  : 0.007575757575757576,\n            \"exact_match_stderr,none\": 0.007575757575757571,\n\
  \            \"alias\": \"  - leaderboard_math_geometry_hard\"\n        },\n   \
  \     \"leaderboard_math_intermediate_algebra_hard\": {\n            \"exact_match,none\"\
  : 0.0035714285714285713,\n            \"exact_match_stderr,none\": 0.0035714285714285657,\n\
  \            \"alias\": \"  - leaderboard_math_intermediate_algebra_hard\"\n   \
  \     },\n        \"leaderboard_math_num_theory_hard\": {\n            \"exact_match,none\"\
  : 0.006493506493506494,\n            \"exact_match_stderr,none\": 0.006493506493506496,\n\
  \            \"alias\": \"  - leaderboard_math_num_theory_hard\"\n        },\n \
  \       \"leaderboard_math_prealgebra_hard\": {\n            \"exact_match,none\"\
  : 0.015544041450777202,\n            \"exact_match_stderr,none\": 0.008927492715084352,\n\
  \            \"alias\": \"  - leaderboard_math_prealgebra_hard\"\n        },\n \
  \       \"leaderboard_math_precalculus_hard\": {\n            \"exact_match,none\"\
  : 0.0,\n            \"exact_match_stderr,none\": 0.0,\n            \"alias\": \"\
  \  - leaderboard_math_precalculus_hard\"\n        },\n        \"leaderboard_mmlu_pro\"\
  : {\n            \"acc,none\": 0.1146941489361702,\n            \"acc_stderr,none\"\
  : 0.002905135781462349,\n            \"alias\": \" - leaderboard_mmlu_pro\"\n  \
  \      },\n        \"leaderboard_musr\": {\n            \"acc_norm,none\": 0.3584656084656085,\n\
  \            \"acc_norm_stderr,none\": 0.017073472513188193,\n            \"alias\"\
  : \" - leaderboard_musr\"\n        },\n        \"leaderboard_musr_murder_mysteries\"\
  : {\n            \"acc_norm,none\": 0.504,\n            \"acc_norm_stderr,none\"\
  : 0.03168519855119917,\n            \"alias\": \"  - leaderboard_musr_murder_mysteries\"\
  \n        },\n        \"leaderboard_musr_object_placements\": {\n            \"\
  acc_norm,none\": 0.28515625,\n            \"acc_norm_stderr,none\": 0.028273327213286358,\n\
  \            \"alias\": \"  - leaderboard_musr_object_placements\"\n        },\n\
  \        \"leaderboard_musr_team_allocation\": {\n            \"acc_norm,none\"\
  : 0.288,\n            \"acc_norm_stderr,none\": 0.028697004587398225,\n        \
  \    \"alias\": \"  - leaderboard_musr_team_allocation\"\n        }\n    },\n  \
  \  \"leaderboard\": {\n        \"acc,none\": 0.13586791881248106,\n        \"acc_stderr,none\"\
  : 0.0029231067788900054,\n        \"inst_level_strict_acc,none\": 0.3009592326139089,\n\
  \        \"inst_level_strict_acc_stderr,none\": \"N/A\",\n        \"exact_match,none\"\
  : 0.0075528700906344415,\n        \"exact_match_stderr,none\": 0.002382555425404601,\n\
  \        \"inst_level_loose_acc,none\": 0.30935251798561153,\n        \"inst_level_loose_acc_stderr,none\"\
  : \"N/A\",\n        \"acc_norm,none\": 0.3244004053597568,\n        \"acc_norm_stderr,none\"\
  : 0.004738972468859114,\n        \"prompt_level_strict_acc,none\": 0.15526802218114602,\n\
  \        \"prompt_level_strict_acc_stderr,none\": 0.015584884858538145,\n      \
  \  \"prompt_level_loose_acc,none\": 0.1589648798521257,\n        \"prompt_level_loose_acc_stderr,none\"\
  : 0.015734783762341237,\n        \"alias\": \"leaderboard\"\n    },\n    \"leaderboard_arc_challenge\"\
  : {\n        \"acc,none\": 0.3532423208191126,\n        \"acc_stderr,none\": 0.013967822714840056,\n\
  \        \"acc_norm,none\": 0.3967576791808874,\n        \"acc_norm_stderr,none\"\
  : 0.014296513020180635,\n        \"alias\": \" - leaderboard_arc_challenge\"\n \
  \   },\n    \"leaderboard_bbh\": {\n        \"acc_norm,none\": 0.32025689984377714,\n\
  \        \"acc_norm_stderr,none\": 0.00575480578331762,\n        \"alias\": \" -\
  \ leaderboard_bbh\"\n    },\n    \"leaderboard_bbh_boolean_expressions\": {\n  \
  \      \"acc_norm,none\": 0.68,\n        \"acc_norm_stderr,none\": 0.029561724955241037,\n\
  \        \"alias\": \"  - leaderboard_bbh_boolean_expressions\"\n    },\n    \"\
  leaderboard_bbh_causal_judgement\": {\n        \"acc_norm,none\": 0.5133689839572193,\n\
  \        \"acc_norm_stderr,none\": 0.03664867131244298,\n        \"alias\": \" \
  \ - leaderboard_bbh_causal_judgement\"\n    },\n    \"leaderboard_bbh_date_understanding\"\
  : {\n        \"acc_norm,none\": 0.14,\n        \"acc_norm_stderr,none\": 0.021989409645240265,\n\
  \        \"alias\": \"  - leaderboard_bbh_date_understanding\"\n    },\n    \"leaderboard_bbh_disambiguation_qa\"\
  : {\n        \"acc_norm,none\": 0.384,\n        \"acc_norm_stderr,none\": 0.030821679117375374,\n\
  \        \"alias\": \"  - leaderboard_bbh_disambiguation_qa\"\n    },\n    \"leaderboard_bbh_formal_fallacies\"\
  : {\n        \"acc_norm,none\": 0.532,\n        \"acc_norm_stderr,none\": 0.031621252575725504,\n\
  \        \"alias\": \"  - leaderboard_bbh_formal_fallacies\"\n    },\n    \"leaderboard_bbh_geometric_shapes\"\
  : {\n        \"acc_norm,none\": 0.128,\n        \"acc_norm_stderr,none\": 0.021172081336336482,\n\
  \        \"alias\": \"  - leaderboard_bbh_geometric_shapes\"\n    },\n    \"leaderboard_bbh_hyperbaton\"\
  : {\n        \"acc_norm,none\": 0.484,\n        \"acc_norm_stderr,none\": 0.031669985030107414,\n\
  \        \"alias\": \"  - leaderboard_bbh_hyperbaton\"\n    },\n    \"leaderboard_bbh_logical_deduction_five_objects\"\
  : {\n        \"acc_norm,none\": 0.216,\n        \"acc_norm_stderr,none\": 0.02607865766373272,\n\
  \        \"alias\": \"  - leaderboard_bbh_logical_deduction_five_objects\"\n   \
  \ },\n    \"leaderboard_bbh_logical_deduction_seven_objects\": {\n        \"acc_norm,none\"\
  : 0.176,\n        \"acc_norm_stderr,none\": 0.024133497525457112,\n        \"alias\"\
  : \"  - leaderboard_bbh_logical_deduction_seven_objects\"\n    },\n    \"leaderboard_bbh_logical_deduction_three_objects\"\
  : {\n        \"acc_norm,none\": 0.304,\n        \"acc_norm_stderr,none\": 0.029150213374159677,\n\
  \        \"alias\": \"  - leaderboard_bbh_logical_deduction_three_objects\"\n  \
  \  },\n    \"leaderboard_bbh_movie_recommendation\": {\n        \"acc_norm,none\"\
  : 0.292,\n        \"acc_norm_stderr,none\": 0.02881432040220563,\n        \"alias\"\
  : \"  - leaderboard_bbh_movie_recommendation\"\n    },\n    \"leaderboard_bbh_navigate\"\
  : {\n        \"acc_norm,none\": 0.568,\n        \"acc_norm_stderr,none\": 0.031391810765429407,\n\
  \        \"alias\": \"  - leaderboard_bbh_navigate\"\n    },\n    \"leaderboard_bbh_object_counting\"\
  : {\n        \"acc_norm,none\": 0.204,\n        \"acc_norm_stderr,none\": 0.025537121574548183,\n\
  \        \"alias\": \"  - leaderboard_bbh_object_counting\"\n    },\n    \"leaderboard_bbh_penguins_in_a_table\"\
  : {\n        \"acc_norm,none\": 0.2191780821917808,\n        \"acc_norm_stderr,none\"\
  : 0.03435504786264928,\n        \"alias\": \"  - leaderboard_bbh_penguins_in_a_table\"\
  \n    },\n    \"leaderboard_bbh_reasoning_about_colored_objects\": {\n        \"\
  acc_norm,none\": 0.148,\n        \"acc_norm_stderr,none\": 0.02250354724380614,\n\
  \        \"alias\": \"  - leaderboard_bbh_reasoning_about_colored_objects\"\n  \
  \  },\n    \"leaderboard_bbh_ruin_names\": {\n        \"acc_norm,none\": 0.244,\n\
  \        \"acc_norm_stderr,none\": 0.027217995464553175,\n        \"alias\": \"\
  \  - leaderboard_bbh_ruin_names\"\n    },\n    \"leaderboard_bbh_salient_translation_error_detection\"\
  : {\n        \"acc_norm,none\": 0.16,\n        \"acc_norm_stderr,none\": 0.023232714782060647,\n\
  \        \"alias\": \"  - leaderboard_bbh_salient_translation_error_detection\"\n\
  \    },\n    \"leaderboard_bbh_snarks\": {\n        \"acc_norm,none\": 0.5449438202247191,\n\
  \        \"acc_norm_stderr,none\": 0.03743016495716993,\n        \"alias\": \" \
  \ - leaderboard_bbh_snarks\"\n    },\n    \"leaderboard_bbh_sports_understanding\"\
  : {\n        \"acc_norm,none\": 0.456,\n        \"acc_norm_stderr,none\": 0.03156328506121339,\n\
  \        \"alias\": \"  - leaderboard_bbh_sports_understanding\"\n    },\n    \"\
  leaderboard_bbh_temporal_sequences\": {\n        \"acc_norm,none\": 0.264,\n   \
  \     \"acc_norm_stderr,none\": 0.02793451895769091,\n        \"alias\": \"  - leaderboard_bbh_temporal_sequences\"\
  \n    },\n    \"leaderboard_bbh_tracking_shuffled_objects_five_objects\": {\n  \
  \      \"acc_norm,none\": 0.148,\n        \"acc_norm_stderr,none\": 0.022503547243806148,\n\
  \        \"alias\": \"  - leaderboard_bbh_tracking_shuffled_objects_five_objects\"\
  \n    },\n    \"leaderboard_bbh_tracking_shuffled_objects_seven_objects\": {\n \
  \       \"acc_norm,none\": 0.124,\n        \"acc_norm_stderr,none\": 0.02088638225867326,\n\
  \        \"alias\": \"  - leaderboard_bbh_tracking_shuffled_objects_seven_objects\"\
  \n    },\n    \"leaderboard_bbh_tracking_shuffled_objects_three_objects\": {\n \
  \       \"acc_norm,none\": 0.32,\n        \"acc_norm_stderr,none\": 0.029561724955241044,\n\
  \        \"alias\": \"  - leaderboard_bbh_tracking_shuffled_objects_three_objects\"\
  \n    },\n    \"leaderboard_bbh_web_of_lies\": {\n        \"acc_norm,none\": 0.508,\n\
  \        \"acc_norm_stderr,none\": 0.0316821564314138,\n        \"alias\": \"  -\
  \ leaderboard_bbh_web_of_lies\"\n    },\n    \"leaderboard_gpqa\": {\n        \"\
  acc_norm,none\": 0.2516778523489933,\n        \"acc_norm_stderr,none\": 0.012579395838405717,\n\
  \        \"alias\": \" - leaderboard_gpqa\"\n    },\n    \"leaderboard_gpqa_diamond\"\
  : {\n        \"acc_norm,none\": 0.2676767676767677,\n        \"acc_norm_stderr,none\"\
  : 0.03154449888270286,\n        \"alias\": \"  - leaderboard_gpqa_diamond\"\n  \
  \  },\n    \"leaderboard_gpqa_extended\": {\n        \"acc_norm,none\": 0.2600732600732601,\n\
  \        \"acc_norm_stderr,none\": 0.018790743352016005,\n        \"alias\": \"\
  \  - leaderboard_gpqa_extended\"\n    },\n    \"leaderboard_gpqa_main\": {\n   \
  \     \"acc_norm,none\": 0.234375,\n        \"acc_norm_stderr,none\": 0.020035949758324928,\n\
  \        \"alias\": \"  - leaderboard_gpqa_main\"\n    },\n    \"leaderboard_ifeval\"\
  : {\n        \"prompt_level_strict_acc,none\": 0.15526802218114602,\n        \"\
  prompt_level_strict_acc_stderr,none\": 0.015584884858538145,\n        \"inst_level_strict_acc,none\"\
  : 0.3009592326139089,\n        \"inst_level_strict_acc_stderr,none\": \"N/A\",\n\
  \        \"prompt_level_loose_acc,none\": 0.1589648798521257,\n        \"prompt_level_loose_acc_stderr,none\"\
  : 0.015734783762341237,\n        \"inst_level_loose_acc,none\": 0.30935251798561153,\n\
  \        \"inst_level_loose_acc_stderr,none\": \"N/A\",\n        \"alias\": \" -\
  \ leaderboard_ifeval\"\n    },\n    \"leaderboard_math_hard\": {\n        \"exact_match,none\"\
  : 0.0075528700906344415,\n        \"exact_match_stderr,none\": 0.002382555425404601,\n\
  \        \"alias\": \" - leaderboard_math_hard\"\n    },\n    \"leaderboard_math_algebra_hard\"\
  : {\n        \"exact_match,none\": 0.009771986970684038,\n        \"exact_match_stderr,none\"\
  : 0.005623391633915873,\n        \"alias\": \"  - leaderboard_math_algebra_hard\"\
  \n    },\n    \"leaderboard_math_counting_and_prob_hard\": {\n        \"exact_match,none\"\
  : 0.008130081300813009,\n        \"exact_match_stderr,none\": 0.008130081300812999,\n\
  \        \"alias\": \"  - leaderboard_math_counting_and_prob_hard\"\n    },\n  \
  \  \"leaderboard_math_geometry_hard\": {\n        \"exact_match,none\": 0.007575757575757576,\n\
  \        \"exact_match_stderr,none\": 0.007575757575757571,\n        \"alias\":\
  \ \"  - leaderboard_math_geometry_hard\"\n    },\n    \"leaderboard_math_intermediate_algebra_hard\"\
  : {\n        \"exact_match,none\": 0.0035714285714285713,\n        \"exact_match_stderr,none\"\
  : 0.0035714285714285657,\n        \"alias\": \"  - leaderboard_math_intermediate_algebra_hard\"\
  \n    },\n    \"leaderboard_math_num_theory_hard\": {\n        \"exact_match,none\"\
  : 0.006493506493506494,\n        \"exact_match_stderr,none\": 0.006493506493506496,\n\
  \        \"alias\": \"  - leaderboard_math_num_theory_hard\"\n    },\n    \"leaderboard_math_prealgebra_hard\"\
  : {\n        \"exact_match,none\": 0.015544041450777202,\n        \"exact_match_stderr,none\"\
  : 0.008927492715084352,\n        \"alias\": \"  - leaderboard_math_prealgebra_hard\"\
  \n    },\n    \"leaderboard_math_precalculus_hard\": {\n        \"exact_match,none\"\
  : 0.0,\n        \"exact_match_stderr,none\": 0.0,\n        \"alias\": \"  - leaderboard_math_precalculus_hard\"\
  \n    },\n    \"leaderboard_mmlu_pro\": {\n        \"acc,none\": 0.1146941489361702,\n\
  \        \"acc_stderr,none\": 0.002905135781462349,\n        \"alias\": \" - leaderboard_mmlu_pro\"\
  \n    },\n    \"leaderboard_musr\": {\n        \"acc_norm,none\": 0.3584656084656085,\n\
  \        \"acc_norm_stderr,none\": 0.017073472513188193,\n        \"alias\": \"\
  \ - leaderboard_musr\"\n    },\n    \"leaderboard_musr_murder_mysteries\": {\n \
  \       \"acc_norm,none\": 0.504,\n        \"acc_norm_stderr,none\": 0.03168519855119917,\n\
  \        \"alias\": \"  - leaderboard_musr_murder_mysteries\"\n    },\n    \"leaderboard_musr_object_placements\"\
  : {\n        \"acc_norm,none\": 0.28515625,\n        \"acc_norm_stderr,none\": 0.028273327213286358,\n\
  \        \"alias\": \"  - leaderboard_musr_object_placements\"\n    },\n    \"leaderboard_musr_team_allocation\"\
  : {\n        \"acc_norm,none\": 0.288,\n        \"acc_norm_stderr,none\": 0.028697004587398225,\n\
  \        \"alias\": \"  - leaderboard_musr_team_allocation\"\n    }\n}\n```"
repo_url: https://huggingface.co/EleutherAI/pythia-6.9b
leaderboard_url: ''
point_of_contact: ''
configs:
- config_name: EleutherAI__pythia-6.9b__leaderboard_arc_challenge
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_arc_challenge_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_arc_challenge_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_bbh
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_bbh_boolean_expressions_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_causal_judgement_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_date_understanding_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_disambiguation_qa_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_formal_fallacies_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_geometric_shapes_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_hyperbaton_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_logical_deduction_five_objects_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_logical_deduction_seven_objects_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_logical_deduction_three_objects_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_movie_recommendation_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_navigate_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_object_counting_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_penguins_in_a_table_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_reasoning_about_colored_objects_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_ruin_names_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_salient_translation_error_detection_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_snarks_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_sports_understanding_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_temporal_sequences_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_five_objects_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_seven_objects_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_three_objects_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_web_of_lies_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_boolean_expressions_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_causal_judgement_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_date_understanding_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_disambiguation_qa_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_formal_fallacies_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_geometric_shapes_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_hyperbaton_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_logical_deduction_five_objects_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_logical_deduction_seven_objects_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_logical_deduction_three_objects_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_movie_recommendation_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_navigate_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_object_counting_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_penguins_in_a_table_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_reasoning_about_colored_objects_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_ruin_names_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_salient_translation_error_detection_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_snarks_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_sports_understanding_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_temporal_sequences_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_five_objects_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_seven_objects_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_three_objects_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_bbh_web_of_lies_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_bbh_boolean_expressions
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_bbh_boolean_expressions_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_boolean_expressions_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_bbh_causal_judgement
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_bbh_causal_judgement_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_causal_judgement_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_bbh_date_understanding
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_bbh_date_understanding_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_date_understanding_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_bbh_disambiguation_qa
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_bbh_disambiguation_qa_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_disambiguation_qa_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_bbh_formal_fallacies
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_bbh_formal_fallacies_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_formal_fallacies_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_bbh_geometric_shapes
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_bbh_geometric_shapes_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_geometric_shapes_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_bbh_hyperbaton
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_bbh_hyperbaton_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_hyperbaton_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_bbh_logical_deduction_five_objects
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_bbh_logical_deduction_five_objects_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_logical_deduction_five_objects_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_bbh_logical_deduction_seven_objects
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_bbh_logical_deduction_seven_objects_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_logical_deduction_seven_objects_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_bbh_logical_deduction_three_objects
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_bbh_logical_deduction_three_objects_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_logical_deduction_three_objects_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_bbh_movie_recommendation
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_bbh_movie_recommendation_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_movie_recommendation_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_bbh_navigate
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_bbh_navigate_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_navigate_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_bbh_object_counting
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_bbh_object_counting_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_object_counting_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_bbh_penguins_in_a_table
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_bbh_penguins_in_a_table_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_penguins_in_a_table_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_bbh_reasoning_about_colored_objects
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_bbh_reasoning_about_colored_objects_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_reasoning_about_colored_objects_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_bbh_ruin_names
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_bbh_ruin_names_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_ruin_names_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_bbh_salient_translation_error_detection
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_bbh_salient_translation_error_detection_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_salient_translation_error_detection_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_bbh_snarks
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_bbh_snarks_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_snarks_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_bbh_sports_understanding
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_bbh_sports_understanding_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_sports_understanding_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_bbh_temporal_sequences
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_bbh_temporal_sequences_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_temporal_sequences_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_bbh_tracking_shuffled_objects_five_objects
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_five_objects_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_five_objects_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_bbh_tracking_shuffled_objects_seven_objects
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_seven_objects_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_seven_objects_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_bbh_tracking_shuffled_objects_three_objects
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_three_objects_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_three_objects_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_bbh_web_of_lies
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_bbh_web_of_lies_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_web_of_lies_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_gpqa
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_gpqa_diamond_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_gpqa_extended_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_gpqa_main_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_gpqa_diamond_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_gpqa_extended_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_gpqa_main_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_gpqa_diamond
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_gpqa_diamond_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_gpqa_diamond_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_gpqa_extended
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_gpqa_extended_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_gpqa_extended_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_gpqa_main
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_gpqa_main_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_gpqa_main_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_ifeval
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_ifeval_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_ifeval_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_math
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_math_algebra_hard_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_math_counting_and_prob_hard_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_math_geometry_hard_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_math_intermediate_algebra_hard_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_math_num_theory_hard_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_math_prealgebra_hard_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_math_precalculus_hard_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_math_algebra_hard_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_math_counting_and_prob_hard_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_math_geometry_hard_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_math_intermediate_algebra_hard_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_math_num_theory_hard_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_math_prealgebra_hard_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_math_precalculus_hard_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_math_algebra_hard
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_math_algebra_hard_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_math_algebra_hard_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_math_counting_and_prob_hard
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_math_counting_and_prob_hard_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_math_counting_and_prob_hard_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_math_geometry_hard
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_math_geometry_hard_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_math_geometry_hard_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_math_intermediate_algebra_hard
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_math_intermediate_algebra_hard_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_math_intermediate_algebra_hard_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_math_num_theory_hard
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_math_num_theory_hard_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_math_num_theory_hard_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_math_prealgebra_hard
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_math_prealgebra_hard_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_math_prealgebra_hard_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_math_precalculus_hard
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_math_precalculus_hard_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_math_precalculus_hard_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_mmlu_pro
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_mmlu_pro_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_mmlu_pro_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_musr
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_musr_murder_mysteries_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_musr_object_placements_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_musr_team_allocation_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_musr_murder_mysteries_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_musr_object_placements_2024-06-16T22-34-46.256992.json'
    - '**/samples_leaderboard_musr_team_allocation_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_musr_murder_mysteries
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_musr_murder_mysteries_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_musr_murder_mysteries_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_musr_object_placements
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_musr_object_placements_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_musr_object_placements_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__leaderboard_musr_team_allocation
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/samples_leaderboard_musr_team_allocation_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/samples_leaderboard_musr_team_allocation_2024-06-16T22-34-46.256992.json'
- config_name: EleutherAI__pythia-6.9b__results
  data_files:
  - split: 2024_06_16T22_34_46.256992
    path:
    - '**/results_2024-06-16T22-34-46.256992.json'
  - split: latest
    path:
    - '**/results_2024-06-16T22-34-46.256992.json'
---

# Dataset Card for Evaluation run of EleutherAI/pythia-6.9b

<!-- Provide a quick summary of the dataset. -->

Dataset automatically created during the evaluation run of model [EleutherAI/pythia-6.9b](https://huggingface.co/EleutherAI/pythia-6.9b)
The dataset is composed of 44 configuration(s), each one corresponding to one of the evaluated task.

The dataset has been created from 2 run(s). Each run can be found as a specific split in each configuration, the split being named using the timestamp of the run.The "train" split is always pointing to the latest results.

An additional configuration "results" store all the aggregated results of the run.

To load the details from a run, you can for instance do the following:
```python
from datasets import load_dataset
data = load_dataset(
	"HuggingFaceEvalInternal/EleutherAI__pythia-6.9b-details-private",
	name="EleutherAI__pythia-6.9b__leaderboard_arc_challenge",
	split="latest"
)
```

## Latest results

These are the [latest results from run 2024-06-16T22-34-46.256992](https://huggingface.co/datasets/HuggingFaceEvalInternal/EleutherAI__pythia-6.9b-details-private/blob/main/EleutherAI__pythia-6.9b/results_2024-06-16T22-34-46.256992.json) (note that there might be results for other tasks in the repos if successive evals didn't cover the same tasks. You find each in the results and the "latest" split for each eval):

```python
{
    "all": {
        "leaderboard": {
            "acc,none": 0.13586791881248106,
            "acc_stderr,none": 0.0029231067788900054,
            "inst_level_strict_acc,none": 0.3009592326139089,
            "inst_level_strict_acc_stderr,none": "N/A",
            "exact_match,none": 0.0075528700906344415,
            "exact_match_stderr,none": 0.002382555425404601,
            "inst_level_loose_acc,none": 0.30935251798561153,
            "inst_level_loose_acc_stderr,none": "N/A",
            "acc_norm,none": 0.3244004053597568,
            "acc_norm_stderr,none": 0.004738972468859114,
            "prompt_level_strict_acc,none": 0.15526802218114602,
            "prompt_level_strict_acc_stderr,none": 0.015584884858538145,
            "prompt_level_loose_acc,none": 0.1589648798521257,
            "prompt_level_loose_acc_stderr,none": 0.015734783762341237,
            "alias": "leaderboard"
        },
        "leaderboard_arc_challenge": {
            "acc,none": 0.3532423208191126,
            "acc_stderr,none": 0.013967822714840056,
            "acc_norm,none": 0.3967576791808874,
            "acc_norm_stderr,none": 0.014296513020180635,
            "alias": " - leaderboard_arc_challenge"
        },
        "leaderboard_bbh": {
            "acc_norm,none": 0.32025689984377714,
            "acc_norm_stderr,none": 0.00575480578331762,
            "alias": " - leaderboard_bbh"
        },
        "leaderboard_bbh_boolean_expressions": {
            "acc_norm,none": 0.68,
            "acc_norm_stderr,none": 0.029561724955241037,
            "alias": "  - leaderboard_bbh_boolean_expressions"
        },
        "leaderboard_bbh_causal_judgement": {
            "acc_norm,none": 0.5133689839572193,
            "acc_norm_stderr,none": 0.03664867131244298,
            "alias": "  - leaderboard_bbh_causal_judgement"
        },
        "leaderboard_bbh_date_understanding": {
            "acc_norm,none": 0.14,
            "acc_norm_stderr,none": 0.021989409645240265,
            "alias": "  - leaderboard_bbh_date_understanding"
        },
        "leaderboard_bbh_disambiguation_qa": {
            "acc_norm,none": 0.384,
            "acc_norm_stderr,none": 0.030821679117375374,
            "alias": "  - leaderboard_bbh_disambiguation_qa"
        },
        "leaderboard_bbh_formal_fallacies": {
            "acc_norm,none": 0.532,
            "acc_norm_stderr,none": 0.031621252575725504,
            "alias": "  - leaderboard_bbh_formal_fallacies"
        },
        "leaderboard_bbh_geometric_shapes": {
            "acc_norm,none": 0.128,
            "acc_norm_stderr,none": 0.021172081336336482,
            "alias": "  - leaderboard_bbh_geometric_shapes"
        },
        "leaderboard_bbh_hyperbaton": {
            "acc_norm,none": 0.484,
            "acc_norm_stderr,none": 0.031669985030107414,
            "alias": "  - leaderboard_bbh_hyperbaton"
        },
        "leaderboard_bbh_logical_deduction_five_objects": {
            "acc_norm,none": 0.216,
            "acc_norm_stderr,none": 0.02607865766373272,
            "alias": "  - leaderboard_bbh_logical_deduction_five_objects"
        },
        "leaderboard_bbh_logical_deduction_seven_objects": {
            "acc_norm,none": 0.176,
            "acc_norm_stderr,none": 0.024133497525457112,
            "alias": "  - leaderboard_bbh_logical_deduction_seven_objects"
        },
        "leaderboard_bbh_logical_deduction_three_objects": {
            "acc_norm,none": 0.304,
            "acc_norm_stderr,none": 0.029150213374159677,
            "alias": "  - leaderboard_bbh_logical_deduction_three_objects"
        },
        "leaderboard_bbh_movie_recommendation": {
            "acc_norm,none": 0.292,
            "acc_norm_stderr,none": 0.02881432040220563,
            "alias": "  - leaderboard_bbh_movie_recommendation"
        },
        "leaderboard_bbh_navigate": {
            "acc_norm,none": 0.568,
            "acc_norm_stderr,none": 0.031391810765429407,
            "alias": "  - leaderboard_bbh_navigate"
        },
        "leaderboard_bbh_object_counting": {
            "acc_norm,none": 0.204,
            "acc_norm_stderr,none": 0.025537121574548183,
            "alias": "  - leaderboard_bbh_object_counting"
        },
        "leaderboard_bbh_penguins_in_a_table": {
            "acc_norm,none": 0.2191780821917808,
            "acc_norm_stderr,none": 0.03435504786264928,
            "alias": "  - leaderboard_bbh_penguins_in_a_table"
        },
        "leaderboard_bbh_reasoning_about_colored_objects": {
            "acc_norm,none": 0.148,
            "acc_norm_stderr,none": 0.02250354724380614,
            "alias": "  - leaderboard_bbh_reasoning_about_colored_objects"
        },
        "leaderboard_bbh_ruin_names": {
            "acc_norm,none": 0.244,
            "acc_norm_stderr,none": 0.027217995464553175,
            "alias": "  - leaderboard_bbh_ruin_names"
        },
        "leaderboard_bbh_salient_translation_error_detection": {
            "acc_norm,none": 0.16,
            "acc_norm_stderr,none": 0.023232714782060647,
            "alias": "  - leaderboard_bbh_salient_translation_error_detection"
        },
        "leaderboard_bbh_snarks": {
            "acc_norm,none": 0.5449438202247191,
            "acc_norm_stderr,none": 0.03743016495716993,
            "alias": "  - leaderboard_bbh_snarks"
        },
        "leaderboard_bbh_sports_understanding": {
            "acc_norm,none": 0.456,
            "acc_norm_stderr,none": 0.03156328506121339,
            "alias": "  - leaderboard_bbh_sports_understanding"
        },
        "leaderboard_bbh_temporal_sequences": {
            "acc_norm,none": 0.264,
            "acc_norm_stderr,none": 0.02793451895769091,
            "alias": "  - leaderboard_bbh_temporal_sequences"
        },
        "leaderboard_bbh_tracking_shuffled_objects_five_objects": {
            "acc_norm,none": 0.148,
            "acc_norm_stderr,none": 0.022503547243806148,
            "alias": "  - leaderboard_bbh_tracking_shuffled_objects_five_objects"
        },
        "leaderboard_bbh_tracking_shuffled_objects_seven_objects": {
            "acc_norm,none": 0.124,
            "acc_norm_stderr,none": 0.02088638225867326,
            "alias": "  - leaderboard_bbh_tracking_shuffled_objects_seven_objects"
        },
        "leaderboard_bbh_tracking_shuffled_objects_three_objects": {
            "acc_norm,none": 0.32,
            "acc_norm_stderr,none": 0.029561724955241044,
            "alias": "  - leaderboard_bbh_tracking_shuffled_objects_three_objects"
        },
        "leaderboard_bbh_web_of_lies": {
            "acc_norm,none": 0.508,
            "acc_norm_stderr,none": 0.0316821564314138,
            "alias": "  - leaderboard_bbh_web_of_lies"
        },
        "leaderboard_gpqa": {
            "acc_norm,none": 0.2516778523489933,
            "acc_norm_stderr,none": 0.012579395838405717,
            "alias": " - leaderboard_gpqa"
        },
        "leaderboard_gpqa_diamond": {
            "acc_norm,none": 0.2676767676767677,
            "acc_norm_stderr,none": 0.03154449888270286,
            "alias": "  - leaderboard_gpqa_diamond"
        },
        "leaderboard_gpqa_extended": {
            "acc_norm,none": 0.2600732600732601,
            "acc_norm_stderr,none": 0.018790743352016005,
            "alias": "  - leaderboard_gpqa_extended"
        },
        "leaderboard_gpqa_main": {
            "acc_norm,none": 0.234375,
            "acc_norm_stderr,none": 0.020035949758324928,
            "alias": "  - leaderboard_gpqa_main"
        },
        "leaderboard_ifeval": {
            "prompt_level_strict_acc,none": 0.15526802218114602,
            "prompt_level_strict_acc_stderr,none": 0.015584884858538145,
            "inst_level_strict_acc,none": 0.3009592326139089,
            "inst_level_strict_acc_stderr,none": "N/A",
            "prompt_level_loose_acc,none": 0.1589648798521257,
            "prompt_level_loose_acc_stderr,none": 0.015734783762341237,
            "inst_level_loose_acc,none": 0.30935251798561153,
            "inst_level_loose_acc_stderr,none": "N/A",
            "alias": " - leaderboard_ifeval"
        },
        "leaderboard_math_hard": {
            "exact_match,none": 0.0075528700906344415,
            "exact_match_stderr,none": 0.002382555425404601,
            "alias": " - leaderboard_math_hard"
        },
        "leaderboard_math_algebra_hard": {
            "exact_match,none": 0.009771986970684038,
            "exact_match_stderr,none": 0.005623391633915873,
            "alias": "  - leaderboard_math_algebra_hard"
        },
        "leaderboard_math_counting_and_prob_hard": {
            "exact_match,none": 0.008130081300813009,
            "exact_match_stderr,none": 0.008130081300812999,
            "alias": "  - leaderboard_math_counting_and_prob_hard"
        },
        "leaderboard_math_geometry_hard": {
            "exact_match,none": 0.007575757575757576,
            "exact_match_stderr,none": 0.007575757575757571,
            "alias": "  - leaderboard_math_geometry_hard"
        },
        "leaderboard_math_intermediate_algebra_hard": {
            "exact_match,none": 0.0035714285714285713,
            "exact_match_stderr,none": 0.0035714285714285657,
            "alias": "  - leaderboard_math_intermediate_algebra_hard"
        },
        "leaderboard_math_num_theory_hard": {
            "exact_match,none": 0.006493506493506494,
            "exact_match_stderr,none": 0.006493506493506496,
            "alias": "  - leaderboard_math_num_theory_hard"
        },
        "leaderboard_math_prealgebra_hard": {
            "exact_match,none": 0.015544041450777202,
            "exact_match_stderr,none": 0.008927492715084352,
            "alias": "  - leaderboard_math_prealgebra_hard"
        },
        "leaderboard_math_precalculus_hard": {
            "exact_match,none": 0.0,
            "exact_match_stderr,none": 0.0,
            "alias": "  - leaderboard_math_precalculus_hard"
        },
        "leaderboard_mmlu_pro": {
            "acc,none": 0.1146941489361702,
            "acc_stderr,none": 0.002905135781462349,
            "alias": " - leaderboard_mmlu_pro"
        },
        "leaderboard_musr": {
            "acc_norm,none": 0.3584656084656085,
            "acc_norm_stderr,none": 0.017073472513188193,
            "alias": " - leaderboard_musr"
        },
        "leaderboard_musr_murder_mysteries": {
            "acc_norm,none": 0.504,
            "acc_norm_stderr,none": 0.03168519855119917,
            "alias": "  - leaderboard_musr_murder_mysteries"
        },
        "leaderboard_musr_object_placements": {
            "acc_norm,none": 0.28515625,
            "acc_norm_stderr,none": 0.028273327213286358,
            "alias": "  - leaderboard_musr_object_placements"
        },
        "leaderboard_musr_team_allocation": {
            "acc_norm,none": 0.288,
            "acc_norm_stderr,none": 0.028697004587398225,
            "alias": "  - leaderboard_musr_team_allocation"
        }
    },
    "leaderboard": {
        "acc,none": 0.13586791881248106,
        "acc_stderr,none": 0.0029231067788900054,
        "inst_level_strict_acc,none": 0.3009592326139089,
        "inst_level_strict_acc_stderr,none": "N/A",
        "exact_match,none": 0.0075528700906344415,
        "exact_match_stderr,none": 0.002382555425404601,
        "inst_level_loose_acc,none": 0.30935251798561153,
        "inst_level_loose_acc_stderr,none": "N/A",
        "acc_norm,none": 0.3244004053597568,
        "acc_norm_stderr,none": 0.004738972468859114,
        "prompt_level_strict_acc,none": 0.15526802218114602,
        "prompt_level_strict_acc_stderr,none": 0.015584884858538145,
        "prompt_level_loose_acc,none": 0.1589648798521257,
        "prompt_level_loose_acc_stderr,none": 0.015734783762341237,
        "alias": "leaderboard"
    },
    "leaderboard_arc_challenge": {
        "acc,none": 0.3532423208191126,
        "acc_stderr,none": 0.013967822714840056,
        "acc_norm,none": 0.3967576791808874,
        "acc_norm_stderr,none": 0.014296513020180635,
        "alias": " - leaderboard_arc_challenge"
    },
    "leaderboard_bbh": {
        "acc_norm,none": 0.32025689984377714,
        "acc_norm_stderr,none": 0.00575480578331762,
        "alias": " - leaderboard_bbh"
    },
    "leaderboard_bbh_boolean_expressions": {
        "acc_norm,none": 0.68,
        "acc_norm_stderr,none": 0.029561724955241037,
        "alias": "  - leaderboard_bbh_boolean_expressions"
    },
    "leaderboard_bbh_causal_judgement": {
        "acc_norm,none": 0.5133689839572193,
        "acc_norm_stderr,none": 0.03664867131244298,
        "alias": "  - leaderboard_bbh_causal_judgement"
    },
    "leaderboard_bbh_date_understanding": {
        "acc_norm,none": 0.14,
        "acc_norm_stderr,none": 0.021989409645240265,
        "alias": "  - leaderboard_bbh_date_understanding"
    },
    "leaderboard_bbh_disambiguation_qa": {
        "acc_norm,none": 0.384,
        "acc_norm_stderr,none": 0.030821679117375374,
        "alias": "  - leaderboard_bbh_disambiguation_qa"
    },
    "leaderboard_bbh_formal_fallacies": {
        "acc_norm,none": 0.532,
        "acc_norm_stderr,none": 0.031621252575725504,
        "alias": "  - leaderboard_bbh_formal_fallacies"
    },
    "leaderboard_bbh_geometric_shapes": {
        "acc_norm,none": 0.128,
        "acc_norm_stderr,none": 0.021172081336336482,
        "alias": "  - leaderboard_bbh_geometric_shapes"
    },
    "leaderboard_bbh_hyperbaton": {
        "acc_norm,none": 0.484,
        "acc_norm_stderr,none": 0.031669985030107414,
        "alias": "  - leaderboard_bbh_hyperbaton"
    },
    "leaderboard_bbh_logical_deduction_five_objects": {
        "acc_norm,none": 0.216,
        "acc_norm_stderr,none": 0.02607865766373272,
        "alias": "  - leaderboard_bbh_logical_deduction_five_objects"
    },
    "leaderboard_bbh_logical_deduction_seven_objects": {
        "acc_norm,none": 0.176,
        "acc_norm_stderr,none": 0.024133497525457112,
        "alias": "  - leaderboard_bbh_logical_deduction_seven_objects"
    },
    "leaderboard_bbh_logical_deduction_three_objects": {
        "acc_norm,none": 0.304,
        "acc_norm_stderr,none": 0.029150213374159677,
        "alias": "  - leaderboard_bbh_logical_deduction_three_objects"
    },
    "leaderboard_bbh_movie_recommendation": {
        "acc_norm,none": 0.292,
        "acc_norm_stderr,none": 0.02881432040220563,
        "alias": "  - leaderboard_bbh_movie_recommendation"
    },
    "leaderboard_bbh_navigate": {
        "acc_norm,none": 0.568,
        "acc_norm_stderr,none": 0.031391810765429407,
        "alias": "  - leaderboard_bbh_navigate"
    },
    "leaderboard_bbh_object_counting": {
        "acc_norm,none": 0.204,
        "acc_norm_stderr,none": 0.025537121574548183,
        "alias": "  - leaderboard_bbh_object_counting"
    },
    "leaderboard_bbh_penguins_in_a_table": {
        "acc_norm,none": 0.2191780821917808,
        "acc_norm_stderr,none": 0.03435504786264928,
        "alias": "  - leaderboard_bbh_penguins_in_a_table"
    },
    "leaderboard_bbh_reasoning_about_colored_objects": {
        "acc_norm,none": 0.148,
        "acc_norm_stderr,none": 0.02250354724380614,
        "alias": "  - leaderboard_bbh_reasoning_about_colored_objects"
    },
    "leaderboard_bbh_ruin_names": {
        "acc_norm,none": 0.244,
        "acc_norm_stderr,none": 0.027217995464553175,
        "alias": "  - leaderboard_bbh_ruin_names"
    },
    "leaderboard_bbh_salient_translation_error_detection": {
        "acc_norm,none": 0.16,
        "acc_norm_stderr,none": 0.023232714782060647,
        "alias": "  - leaderboard_bbh_salient_translation_error_detection"
    },
    "leaderboard_bbh_snarks": {
        "acc_norm,none": 0.5449438202247191,
        "acc_norm_stderr,none": 0.03743016495716993,
        "alias": "  - leaderboard_bbh_snarks"
    },
    "leaderboard_bbh_sports_understanding": {
        "acc_norm,none": 0.456,
        "acc_norm_stderr,none": 0.03156328506121339,
        "alias": "  - leaderboard_bbh_sports_understanding"
    },
    "leaderboard_bbh_temporal_sequences": {
        "acc_norm,none": 0.264,
        "acc_norm_stderr,none": 0.02793451895769091,
        "alias": "  - leaderboard_bbh_temporal_sequences"
    },
    "leaderboard_bbh_tracking_shuffled_objects_five_objects": {
        "acc_norm,none": 0.148,
        "acc_norm_stderr,none": 0.022503547243806148,
        "alias": "  - leaderboard_bbh_tracking_shuffled_objects_five_objects"
    },
    "leaderboard_bbh_tracking_shuffled_objects_seven_objects": {
        "acc_norm,none": 0.124,
        "acc_norm_stderr,none": 0.02088638225867326,
        "alias": "  - leaderboard_bbh_tracking_shuffled_objects_seven_objects"
    },
    "leaderboard_bbh_tracking_shuffled_objects_three_objects": {
        "acc_norm,none": 0.32,
        "acc_norm_stderr,none": 0.029561724955241044,
        "alias": "  - leaderboard_bbh_tracking_shuffled_objects_three_objects"
    },
    "leaderboard_bbh_web_of_lies": {
        "acc_norm,none": 0.508,
        "acc_norm_stderr,none": 0.0316821564314138,
        "alias": "  - leaderboard_bbh_web_of_lies"
    },
    "leaderboard_gpqa": {
        "acc_norm,none": 0.2516778523489933,
        "acc_norm_stderr,none": 0.012579395838405717,
        "alias": " - leaderboard_gpqa"
    },
    "leaderboard_gpqa_diamond": {
        "acc_norm,none": 0.2676767676767677,
        "acc_norm_stderr,none": 0.03154449888270286,
        "alias": "  - leaderboard_gpqa_diamond"
    },
    "leaderboard_gpqa_extended": {
        "acc_norm,none": 0.2600732600732601,
        "acc_norm_stderr,none": 0.018790743352016005,
        "alias": "  - leaderboard_gpqa_extended"
    },
    "leaderboard_gpqa_main": {
        "acc_norm,none": 0.234375,
        "acc_norm_stderr,none": 0.020035949758324928,
        "alias": "  - leaderboard_gpqa_main"
    },
    "leaderboard_ifeval": {
        "prompt_level_strict_acc,none": 0.15526802218114602,
        "prompt_level_strict_acc_stderr,none": 0.015584884858538145,
        "inst_level_strict_acc,none": 0.3009592326139089,
        "inst_level_strict_acc_stderr,none": "N/A",
        "prompt_level_loose_acc,none": 0.1589648798521257,
        "prompt_level_loose_acc_stderr,none": 0.015734783762341237,
        "inst_level_loose_acc,none": 0.30935251798561153,
        "inst_level_loose_acc_stderr,none": "N/A",
        "alias": " - leaderboard_ifeval"
    },
    "leaderboard_math_hard": {
        "exact_match,none": 0.0075528700906344415,
        "exact_match_stderr,none": 0.002382555425404601,
        "alias": " - leaderboard_math_hard"
    },
    "leaderboard_math_algebra_hard": {
        "exact_match,none": 0.009771986970684038,
        "exact_match_stderr,none": 0.005623391633915873,
        "alias": "  - leaderboard_math_algebra_hard"
    },
    "leaderboard_math_counting_and_prob_hard": {
        "exact_match,none": 0.008130081300813009,
        "exact_match_stderr,none": 0.008130081300812999,
        "alias": "  - leaderboard_math_counting_and_prob_hard"
    },
    "leaderboard_math_geometry_hard": {
        "exact_match,none": 0.007575757575757576,
        "exact_match_stderr,none": 0.007575757575757571,
        "alias": "  - leaderboard_math_geometry_hard"
    },
    "leaderboard_math_intermediate_algebra_hard": {
        "exact_match,none": 0.0035714285714285713,
        "exact_match_stderr,none": 0.0035714285714285657,
        "alias": "  - leaderboard_math_intermediate_algebra_hard"
    },
    "leaderboard_math_num_theory_hard": {
        "exact_match,none": 0.006493506493506494,
        "exact_match_stderr,none": 0.006493506493506496,
        "alias": "  - leaderboard_math_num_theory_hard"
    },
    "leaderboard_math_prealgebra_hard": {
        "exact_match,none": 0.015544041450777202,
        "exact_match_stderr,none": 0.008927492715084352,
        "alias": "  - leaderboard_math_prealgebra_hard"
    },
    "leaderboard_math_precalculus_hard": {
        "exact_match,none": 0.0,
        "exact_match_stderr,none": 0.0,
        "alias": "  - leaderboard_math_precalculus_hard"
    },
    "leaderboard_mmlu_pro": {
        "acc,none": 0.1146941489361702,
        "acc_stderr,none": 0.002905135781462349,
        "alias": " - leaderboard_mmlu_pro"
    },
    "leaderboard_musr": {
        "acc_norm,none": 0.3584656084656085,
        "acc_norm_stderr,none": 0.017073472513188193,
        "alias": " - leaderboard_musr"
    },
    "leaderboard_musr_murder_mysteries": {
        "acc_norm,none": 0.504,
        "acc_norm_stderr,none": 0.03168519855119917,
        "alias": "  - leaderboard_musr_murder_mysteries"
    },
    "leaderboard_musr_object_placements": {
        "acc_norm,none": 0.28515625,
        "acc_norm_stderr,none": 0.028273327213286358,
        "alias": "  - leaderboard_musr_object_placements"
    },
    "leaderboard_musr_team_allocation": {
        "acc_norm,none": 0.288,
        "acc_norm_stderr,none": 0.028697004587398225,
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