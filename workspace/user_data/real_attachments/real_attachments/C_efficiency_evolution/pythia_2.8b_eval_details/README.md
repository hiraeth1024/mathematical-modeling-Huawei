---
pretty_name: Evaluation run of EleutherAI/pythia-2.8b
dataset_summary: "Dataset automatically created during the evaluation run of model\
  \ [EleutherAI/pythia-2.8b](https://huggingface.co/EleutherAI/pythia-2.8b)\nThe dataset\
  \ is composed of 44 configuration(s), each one corresponding to one of the evaluated\
  \ task.\n\nThe dataset has been created from 1 run(s). Each run can be found as\
  \ a specific split in each configuration, the split being named using the timestamp\
  \ of the run.The \"train\" split is always pointing to the latest results.\n\nAn\
  \ additional configuration \"results\" store all the aggregated results of the run.\n\
  \nTo load the details from a run, you can for instance do the following:\n```python\n\
  from datasets import load_dataset\ndata = load_dataset(\n\t\"HuggingFaceEvalInternal/EleutherAI__pythia-2.8b-details-private\"\
  ,\n\tname=\"EleutherAI__pythia-2.8b__leaderboard_arc_challenge\",\n\tsplit=\"latest\"\
  \n)\n```\n\n## Latest results\n\nThese are the [latest results from run 2024-06-17T12-07-04.698905](https://huggingface.co/datasets/HuggingFaceEvalInternal/EleutherAI__pythia-2.8b-details-private/blob/main/EleutherAI__pythia-2.8b/results_2024-06-17T12-07-04.698905.json)\
  \ (note that there might be results for other tasks in the repos if successive evals\
  \ didn't cover the same tasks. You find each in the results and the \"latest\" split\
  \ for each eval):\n\n```python\n{\n    \"all\": {\n        \"leaderboard\": {\n\
  \            \"acc,none\": 0.13155104513783702,\n            \"acc_stderr,none\"\
  : 0.00289926789637609,\n            \"exact_match,none\": 0.006797583081570997,\n\
  \            \"exact_match_stderr,none\": 0.0022576874321512206,\n            \"\
  inst_level_strict_acc,none\": 0.2793764988009592,\n            \"inst_level_strict_acc_stderr,none\"\
  : \"N/A\",\n            \"prompt_level_strict_acc,none\": 0.15526802218114602,\n\
  \            \"prompt_level_strict_acc_stderr,none\": 0.015584884858538145,\n  \
  \          \"acc_norm,none\": 0.3183200090079946,\n            \"acc_norm_stderr,none\"\
  : 0.004755193956049788,\n            \"inst_level_loose_acc,none\": 0.290167865707434,\n\
  \            \"inst_level_loose_acc_stderr,none\": \"N/A\",\n            \"prompt_level_loose_acc,none\"\
  : 0.1645101663585952,\n            \"prompt_level_loose_acc_stderr,none\": 0.015954017926718037,\n\
  \            \"alias\": \"leaderboard\"\n        },\n        \"leaderboard_arc_challenge\"\
  : {\n            \"acc,none\": 0.3148464163822526,\n            \"acc_stderr,none\"\
  : 0.013572657703084948,\n            \"acc_norm,none\": 0.3575085324232082,\n  \
  \          \"acc_norm_stderr,none\": 0.01400549427591657,\n            \"alias\"\
  : \" - leaderboard_arc_challenge\"\n        },\n        \"leaderboard_bbh\": {\n\
  \            \"acc_norm,none\": 0.3206040617948273,\n            \"acc_norm_stderr,none\"\
  : 0.005831106872988066,\n            \"alias\": \" - leaderboard_bbh\"\n       \
  \ },\n        \"leaderboard_bbh_boolean_expressions\": {\n            \"acc_norm,none\"\
  : 0.628,\n            \"acc_norm_stderr,none\": 0.030630325944558313,\n        \
  \    \"alias\": \"  - leaderboard_bbh_boolean_expressions\"\n        },\n      \
  \  \"leaderboard_bbh_causal_judgement\": {\n            \"acc_norm,none\": 0.44385026737967914,\n\
  \            \"acc_norm_stderr,none\": 0.03642987131924726,\n            \"alias\"\
  : \"  - leaderboard_bbh_causal_judgement\"\n        },\n        \"leaderboard_bbh_date_understanding\"\
  : {\n            \"acc_norm,none\": 0.192,\n            \"acc_norm_stderr,none\"\
  : 0.024960691989172012,\n            \"alias\": \"  - leaderboard_bbh_date_understanding\"\
  \n        },\n        \"leaderboard_bbh_disambiguation_qa\": {\n            \"acc_norm,none\"\
  : 0.34,\n            \"acc_norm_stderr,none\": 0.030020073605457904,\n         \
  \   \"alias\": \"  - leaderboard_bbh_disambiguation_qa\"\n        },\n        \"\
  leaderboard_bbh_formal_fallacies\": {\n            \"acc_norm,none\": 0.456,\n \
  \           \"acc_norm_stderr,none\": 0.03156328506121339,\n            \"alias\"\
  : \"  - leaderboard_bbh_formal_fallacies\"\n        },\n        \"leaderboard_bbh_geometric_shapes\"\
  : {\n            \"acc_norm,none\": 0.088,\n            \"acc_norm_stderr,none\"\
  : 0.01795308477705287,\n            \"alias\": \"  - leaderboard_bbh_geometric_shapes\"\
  \n        },\n        \"leaderboard_bbh_hyperbaton\": {\n            \"acc_norm,none\"\
  : 0.484,\n            \"acc_norm_stderr,none\": 0.031669985030107414,\n        \
  \    \"alias\": \"  - leaderboard_bbh_hyperbaton\"\n        },\n        \"leaderboard_bbh_logical_deduction_five_objects\"\
  : {\n            \"acc_norm,none\": 0.236,\n            \"acc_norm_stderr,none\"\
  : 0.026909337594953838,\n            \"alias\": \"  - leaderboard_bbh_logical_deduction_five_objects\"\
  \n        },\n        \"leaderboard_bbh_logical_deduction_seven_objects\": {\n \
  \           \"acc_norm,none\": 0.144,\n            \"acc_norm_stderr,none\": 0.02224940773545021,\n\
  \            \"alias\": \"  - leaderboard_bbh_logical_deduction_seven_objects\"\n\
  \        },\n        \"leaderboard_bbh_logical_deduction_three_objects\": {\n  \
  \          \"acc_norm,none\": 0.344,\n            \"acc_norm_stderr,none\": 0.030104503392316392,\n\
  \            \"alias\": \"  - leaderboard_bbh_logical_deduction_three_objects\"\n\
  \        },\n        \"leaderboard_bbh_movie_recommendation\": {\n            \"\
  acc_norm,none\": 0.276,\n            \"acc_norm_stderr,none\": 0.028328537274211342,\n\
  \            \"alias\": \"  - leaderboard_bbh_movie_recommendation\"\n        },\n\
  \        \"leaderboard_bbh_navigate\": {\n            \"acc_norm,none\": 0.5,\n\
  \            \"acc_norm_stderr,none\": 0.031686212526223896,\n            \"alias\"\
  : \"  - leaderboard_bbh_navigate\"\n        },\n        \"leaderboard_bbh_object_counting\"\
  : {\n            \"acc_norm,none\": 0.264,\n            \"acc_norm_stderr,none\"\
  : 0.027934518957690904,\n            \"alias\": \"  - leaderboard_bbh_object_counting\"\
  \n        },\n        \"leaderboard_bbh_penguins_in_a_table\": {\n            \"\
  acc_norm,none\": 0.19863013698630136,\n            \"acc_norm_stderr,none\": 0.03313256608889821,\n\
  \            \"alias\": \"  - leaderboard_bbh_penguins_in_a_table\"\n        },\n\
  \        \"leaderboard_bbh_reasoning_about_colored_objects\": {\n            \"\
  acc_norm,none\": 0.128,\n            \"acc_norm_stderr,none\": 0.02117208133633648,\n\
  \            \"alias\": \"  - leaderboard_bbh_reasoning_about_colored_objects\"\n\
  \        },\n        \"leaderboard_bbh_ruin_names\": {\n            \"acc_norm,none\"\
  : 0.212,\n            \"acc_norm_stderr,none\": 0.025901884690541156,\n        \
  \    \"alias\": \"  - leaderboard_bbh_ruin_names\"\n        },\n        \"leaderboard_bbh_salient_translation_error_detection\"\
  : {\n            \"acc_norm,none\": 0.276,\n            \"acc_norm_stderr,none\"\
  : 0.02832853727421135,\n            \"alias\": \"  - leaderboard_bbh_salient_translation_error_detection\"\
  \n        },\n        \"leaderboard_bbh_snarks\": {\n            \"acc_norm,none\"\
  : 0.5393258426966292,\n            \"acc_norm_stderr,none\": 0.0374658773638787,\n\
  \            \"alias\": \"  - leaderboard_bbh_snarks\"\n        },\n        \"leaderboard_bbh_sports_understanding\"\
  : {\n            \"acc_norm,none\": 0.5,\n            \"acc_norm_stderr,none\":\
  \ 0.031686212526223896,\n            \"alias\": \"  - leaderboard_bbh_sports_understanding\"\
  \n        },\n        \"leaderboard_bbh_temporal_sequences\": {\n            \"\
  acc_norm,none\": 0.284,\n            \"acc_norm_stderr,none\": 0.02857695873043741,\n\
  \            \"alias\": \"  - leaderboard_bbh_temporal_sequences\"\n        },\n\
  \        \"leaderboard_bbh_tracking_shuffled_objects_five_objects\": {\n       \
  \     \"acc_norm,none\": 0.156,\n            \"acc_norm_stderr,none\": 0.022995023034068748,\n\
  \            \"alias\": \"  - leaderboard_bbh_tracking_shuffled_objects_five_objects\"\
  \n        },\n        \"leaderboard_bbh_tracking_shuffled_objects_seven_objects\"\
  : {\n            \"acc_norm,none\": 0.168,\n            \"acc_norm_stderr,none\"\
  : 0.0236928132054926,\n            \"alias\": \"  - leaderboard_bbh_tracking_shuffled_objects_seven_objects\"\
  \n        },\n        \"leaderboard_bbh_tracking_shuffled_objects_three_objects\"\
  : {\n            \"acc_norm,none\": 0.34,\n            \"acc_norm_stderr,none\"\
  : 0.030020073605457907,\n            \"alias\": \"  - leaderboard_bbh_tracking_shuffled_objects_three_objects\"\
  \n        },\n        \"leaderboard_bbh_web_of_lies\": {\n            \"acc_norm,none\"\
  : 0.54,\n            \"acc_norm_stderr,none\": 0.03158465389149899,\n          \
  \  \"alias\": \"  - leaderboard_bbh_web_of_lies\"\n        },\n        \"leaderboard_gpqa\"\
  : {\n            \"acc_norm,none\": 0.25,\n            \"acc_norm_stderr,none\"\
  : 0.012554809228367316,\n            \"alias\": \" - leaderboard_gpqa\"\n      \
  \  },\n        \"leaderboard_gpqa_diamond\": {\n            \"acc_norm,none\": 0.24242424242424243,\n\
  \            \"acc_norm_stderr,none\": 0.030532892233932026,\n            \"alias\"\
  : \"  - leaderboard_gpqa_diamond\"\n        },\n        \"leaderboard_gpqa_extended\"\
  : {\n            \"acc_norm,none\": 0.2600732600732601,\n            \"acc_norm_stderr,none\"\
  : 0.01879074335201598,\n            \"alias\": \"  - leaderboard_gpqa_extended\"\
  \n        },\n        \"leaderboard_gpqa_main\": {\n            \"acc_norm,none\"\
  : 0.24107142857142858,\n            \"acc_norm_stderr,none\": 0.020231102978728707,\n\
  \            \"alias\": \"  - leaderboard_gpqa_main\"\n        },\n        \"leaderboard_ifeval\"\
  : {\n            \"prompt_level_strict_acc,none\": 0.15526802218114602,\n      \
  \      \"prompt_level_strict_acc_stderr,none\": 0.015584884858538145,\n        \
  \    \"inst_level_strict_acc,none\": 0.2793764988009592,\n            \"inst_level_strict_acc_stderr,none\"\
  : \"N/A\",\n            \"prompt_level_loose_acc,none\": 0.1645101663585952,\n \
  \           \"prompt_level_loose_acc_stderr,none\": 0.015954017926718037,\n    \
  \        \"inst_level_loose_acc,none\": 0.290167865707434,\n            \"inst_level_loose_acc_stderr,none\"\
  : \"N/A\",\n            \"alias\": \" - leaderboard_ifeval\"\n        },\n     \
  \   \"leaderboard_math_hard\": {\n            \"exact_match,none\": 0.006797583081570997,\n\
  \            \"exact_match_stderr,none\": 0.0022576874321512206,\n            \"\
  alias\": \" - leaderboard_math_hard\"\n        },\n        \"leaderboard_math_algebra_hard\"\
  : {\n            \"exact_match,none\": 0.009771986970684038,\n            \"exact_match_stderr,none\"\
  : 0.005623391633915882,\n            \"alias\": \"  - leaderboard_math_algebra_hard\"\
  \n        },\n        \"leaderboard_math_counting_and_prob_hard\": {\n         \
  \   \"exact_match,none\": 0.0,\n            \"exact_match_stderr,none\": 0.0,\n\
  \            \"alias\": \"  - leaderboard_math_counting_and_prob_hard\"\n      \
  \  },\n        \"leaderboard_math_geometry_hard\": {\n            \"exact_match,none\"\
  : 0.0,\n            \"exact_match_stderr,none\": 0.0,\n            \"alias\": \"\
  \  - leaderboard_math_geometry_hard\"\n        },\n        \"leaderboard_math_intermediate_algebra_hard\"\
  : {\n            \"exact_match,none\": 0.0035714285714285713,\n            \"exact_match_stderr,none\"\
  : 0.003571428571428562,\n            \"alias\": \"  - leaderboard_math_intermediate_algebra_hard\"\
  \n        },\n        \"leaderboard_math_num_theory_hard\": {\n            \"exact_match,none\"\
  : 0.01948051948051948,\n            \"exact_match_stderr,none\": 0.01117333100557106,\n\
  \            \"alias\": \"  - leaderboard_math_num_theory_hard\"\n        },\n \
  \       \"leaderboard_math_prealgebra_hard\": {\n            \"exact_match,none\"\
  : 0.010362694300518135,\n            \"exact_match_stderr,none\": 0.007308424386792202,\n\
  \            \"alias\": \"  - leaderboard_math_prealgebra_hard\"\n        },\n \
  \       \"leaderboard_math_precalculus_hard\": {\n            \"exact_match,none\"\
  : 0.0,\n            \"exact_match_stderr,none\": 0.0,\n            \"alias\": \"\
  \  - leaderboard_math_precalculus_hard\"\n        },\n        \"leaderboard_mmlu_pro\"\
  : {\n            \"acc,none\": 0.11369680851063829,\n            \"acc_stderr,none\"\
  : 0.0028941059775779744,\n            \"alias\": \" - leaderboard_mmlu_pro\"\n \
  \       },\n        \"leaderboard_musr\": {\n            \"acc_norm,none\": 0.3478835978835979,\n\
  \            \"acc_norm_stderr,none\": 0.016814352504527307,\n            \"alias\"\
  : \" - leaderboard_musr\"\n        },\n        \"leaderboard_musr_murder_mysteries\"\
  : {\n            \"acc_norm,none\": 0.516,\n            \"acc_norm_stderr,none\"\
  : 0.03166998503010742,\n            \"alias\": \"  - leaderboard_musr_murder_mysteries\"\
  \n        },\n        \"leaderboard_musr_object_placements\": {\n            \"\
  acc_norm,none\": 0.26171875,\n            \"acc_norm_stderr,none\": 0.027526959754524398,\n\
  \            \"alias\": \"  - leaderboard_musr_object_placements\"\n        },\n\
  \        \"leaderboard_musr_team_allocation\": {\n            \"acc_norm,none\"\
  : 0.268,\n            \"acc_norm_stderr,none\": 0.02806876238252669,\n         \
  \   \"alias\": \"  - leaderboard_musr_team_allocation\"\n        }\n    },\n   \
  \ \"leaderboard\": {\n        \"acc,none\": 0.13155104513783702,\n        \"acc_stderr,none\"\
  : 0.00289926789637609,\n        \"exact_match,none\": 0.006797583081570997,\n  \
  \      \"exact_match_stderr,none\": 0.0022576874321512206,\n        \"inst_level_strict_acc,none\"\
  : 0.2793764988009592,\n        \"inst_level_strict_acc_stderr,none\": \"N/A\",\n\
  \        \"prompt_level_strict_acc,none\": 0.15526802218114602,\n        \"prompt_level_strict_acc_stderr,none\"\
  : 0.015584884858538145,\n        \"acc_norm,none\": 0.3183200090079946,\n      \
  \  \"acc_norm_stderr,none\": 0.004755193956049788,\n        \"inst_level_loose_acc,none\"\
  : 0.290167865707434,\n        \"inst_level_loose_acc_stderr,none\": \"N/A\",\n \
  \       \"prompt_level_loose_acc,none\": 0.1645101663585952,\n        \"prompt_level_loose_acc_stderr,none\"\
  : 0.015954017926718037,\n        \"alias\": \"leaderboard\"\n    },\n    \"leaderboard_arc_challenge\"\
  : {\n        \"acc,none\": 0.3148464163822526,\n        \"acc_stderr,none\": 0.013572657703084948,\n\
  \        \"acc_norm,none\": 0.3575085324232082,\n        \"acc_norm_stderr,none\"\
  : 0.01400549427591657,\n        \"alias\": \" - leaderboard_arc_challenge\"\n  \
  \  },\n    \"leaderboard_bbh\": {\n        \"acc_norm,none\": 0.3206040617948273,\n\
  \        \"acc_norm_stderr,none\": 0.005831106872988066,\n        \"alias\": \"\
  \ - leaderboard_bbh\"\n    },\n    \"leaderboard_bbh_boolean_expressions\": {\n\
  \        \"acc_norm,none\": 0.628,\n        \"acc_norm_stderr,none\": 0.030630325944558313,\n\
  \        \"alias\": \"  - leaderboard_bbh_boolean_expressions\"\n    },\n    \"\
  leaderboard_bbh_causal_judgement\": {\n        \"acc_norm,none\": 0.44385026737967914,\n\
  \        \"acc_norm_stderr,none\": 0.03642987131924726,\n        \"alias\": \" \
  \ - leaderboard_bbh_causal_judgement\"\n    },\n    \"leaderboard_bbh_date_understanding\"\
  : {\n        \"acc_norm,none\": 0.192,\n        \"acc_norm_stderr,none\": 0.024960691989172012,\n\
  \        \"alias\": \"  - leaderboard_bbh_date_understanding\"\n    },\n    \"leaderboard_bbh_disambiguation_qa\"\
  : {\n        \"acc_norm,none\": 0.34,\n        \"acc_norm_stderr,none\": 0.030020073605457904,\n\
  \        \"alias\": \"  - leaderboard_bbh_disambiguation_qa\"\n    },\n    \"leaderboard_bbh_formal_fallacies\"\
  : {\n        \"acc_norm,none\": 0.456,\n        \"acc_norm_stderr,none\": 0.03156328506121339,\n\
  \        \"alias\": \"  - leaderboard_bbh_formal_fallacies\"\n    },\n    \"leaderboard_bbh_geometric_shapes\"\
  : {\n        \"acc_norm,none\": 0.088,\n        \"acc_norm_stderr,none\": 0.01795308477705287,\n\
  \        \"alias\": \"  - leaderboard_bbh_geometric_shapes\"\n    },\n    \"leaderboard_bbh_hyperbaton\"\
  : {\n        \"acc_norm,none\": 0.484,\n        \"acc_norm_stderr,none\": 0.031669985030107414,\n\
  \        \"alias\": \"  - leaderboard_bbh_hyperbaton\"\n    },\n    \"leaderboard_bbh_logical_deduction_five_objects\"\
  : {\n        \"acc_norm,none\": 0.236,\n        \"acc_norm_stderr,none\": 0.026909337594953838,\n\
  \        \"alias\": \"  - leaderboard_bbh_logical_deduction_five_objects\"\n   \
  \ },\n    \"leaderboard_bbh_logical_deduction_seven_objects\": {\n        \"acc_norm,none\"\
  : 0.144,\n        \"acc_norm_stderr,none\": 0.02224940773545021,\n        \"alias\"\
  : \"  - leaderboard_bbh_logical_deduction_seven_objects\"\n    },\n    \"leaderboard_bbh_logical_deduction_three_objects\"\
  : {\n        \"acc_norm,none\": 0.344,\n        \"acc_norm_stderr,none\": 0.030104503392316392,\n\
  \        \"alias\": \"  - leaderboard_bbh_logical_deduction_three_objects\"\n  \
  \  },\n    \"leaderboard_bbh_movie_recommendation\": {\n        \"acc_norm,none\"\
  : 0.276,\n        \"acc_norm_stderr,none\": 0.028328537274211342,\n        \"alias\"\
  : \"  - leaderboard_bbh_movie_recommendation\"\n    },\n    \"leaderboard_bbh_navigate\"\
  : {\n        \"acc_norm,none\": 0.5,\n        \"acc_norm_stderr,none\": 0.031686212526223896,\n\
  \        \"alias\": \"  - leaderboard_bbh_navigate\"\n    },\n    \"leaderboard_bbh_object_counting\"\
  : {\n        \"acc_norm,none\": 0.264,\n        \"acc_norm_stderr,none\": 0.027934518957690904,\n\
  \        \"alias\": \"  - leaderboard_bbh_object_counting\"\n    },\n    \"leaderboard_bbh_penguins_in_a_table\"\
  : {\n        \"acc_norm,none\": 0.19863013698630136,\n        \"acc_norm_stderr,none\"\
  : 0.03313256608889821,\n        \"alias\": \"  - leaderboard_bbh_penguins_in_a_table\"\
  \n    },\n    \"leaderboard_bbh_reasoning_about_colored_objects\": {\n        \"\
  acc_norm,none\": 0.128,\n        \"acc_norm_stderr,none\": 0.02117208133633648,\n\
  \        \"alias\": \"  - leaderboard_bbh_reasoning_about_colored_objects\"\n  \
  \  },\n    \"leaderboard_bbh_ruin_names\": {\n        \"acc_norm,none\": 0.212,\n\
  \        \"acc_norm_stderr,none\": 0.025901884690541156,\n        \"alias\": \"\
  \  - leaderboard_bbh_ruin_names\"\n    },\n    \"leaderboard_bbh_salient_translation_error_detection\"\
  : {\n        \"acc_norm,none\": 0.276,\n        \"acc_norm_stderr,none\": 0.02832853727421135,\n\
  \        \"alias\": \"  - leaderboard_bbh_salient_translation_error_detection\"\n\
  \    },\n    \"leaderboard_bbh_snarks\": {\n        \"acc_norm,none\": 0.5393258426966292,\n\
  \        \"acc_norm_stderr,none\": 0.0374658773638787,\n        \"alias\": \"  -\
  \ leaderboard_bbh_snarks\"\n    },\n    \"leaderboard_bbh_sports_understanding\"\
  : {\n        \"acc_norm,none\": 0.5,\n        \"acc_norm_stderr,none\": 0.031686212526223896,\n\
  \        \"alias\": \"  - leaderboard_bbh_sports_understanding\"\n    },\n    \"\
  leaderboard_bbh_temporal_sequences\": {\n        \"acc_norm,none\": 0.284,\n   \
  \     \"acc_norm_stderr,none\": 0.02857695873043741,\n        \"alias\": \"  - leaderboard_bbh_temporal_sequences\"\
  \n    },\n    \"leaderboard_bbh_tracking_shuffled_objects_five_objects\": {\n  \
  \      \"acc_norm,none\": 0.156,\n        \"acc_norm_stderr,none\": 0.022995023034068748,\n\
  \        \"alias\": \"  - leaderboard_bbh_tracking_shuffled_objects_five_objects\"\
  \n    },\n    \"leaderboard_bbh_tracking_shuffled_objects_seven_objects\": {\n \
  \       \"acc_norm,none\": 0.168,\n        \"acc_norm_stderr,none\": 0.0236928132054926,\n\
  \        \"alias\": \"  - leaderboard_bbh_tracking_shuffled_objects_seven_objects\"\
  \n    },\n    \"leaderboard_bbh_tracking_shuffled_objects_three_objects\": {\n \
  \       \"acc_norm,none\": 0.34,\n        \"acc_norm_stderr,none\": 0.030020073605457907,\n\
  \        \"alias\": \"  - leaderboard_bbh_tracking_shuffled_objects_three_objects\"\
  \n    },\n    \"leaderboard_bbh_web_of_lies\": {\n        \"acc_norm,none\": 0.54,\n\
  \        \"acc_norm_stderr,none\": 0.03158465389149899,\n        \"alias\": \" \
  \ - leaderboard_bbh_web_of_lies\"\n    },\n    \"leaderboard_gpqa\": {\n       \
  \ \"acc_norm,none\": 0.25,\n        \"acc_norm_stderr,none\": 0.012554809228367316,\n\
  \        \"alias\": \" - leaderboard_gpqa\"\n    },\n    \"leaderboard_gpqa_diamond\"\
  : {\n        \"acc_norm,none\": 0.24242424242424243,\n        \"acc_norm_stderr,none\"\
  : 0.030532892233932026,\n        \"alias\": \"  - leaderboard_gpqa_diamond\"\n \
  \   },\n    \"leaderboard_gpqa_extended\": {\n        \"acc_norm,none\": 0.2600732600732601,\n\
  \        \"acc_norm_stderr,none\": 0.01879074335201598,\n        \"alias\": \" \
  \ - leaderboard_gpqa_extended\"\n    },\n    \"leaderboard_gpqa_main\": {\n    \
  \    \"acc_norm,none\": 0.24107142857142858,\n        \"acc_norm_stderr,none\":\
  \ 0.020231102978728707,\n        \"alias\": \"  - leaderboard_gpqa_main\"\n    },\n\
  \    \"leaderboard_ifeval\": {\n        \"prompt_level_strict_acc,none\": 0.15526802218114602,\n\
  \        \"prompt_level_strict_acc_stderr,none\": 0.015584884858538145,\n      \
  \  \"inst_level_strict_acc,none\": 0.2793764988009592,\n        \"inst_level_strict_acc_stderr,none\"\
  : \"N/A\",\n        \"prompt_level_loose_acc,none\": 0.1645101663585952,\n     \
  \   \"prompt_level_loose_acc_stderr,none\": 0.015954017926718037,\n        \"inst_level_loose_acc,none\"\
  : 0.290167865707434,\n        \"inst_level_loose_acc_stderr,none\": \"N/A\",\n \
  \       \"alias\": \" - leaderboard_ifeval\"\n    },\n    \"leaderboard_math_hard\"\
  : {\n        \"exact_match,none\": 0.006797583081570997,\n        \"exact_match_stderr,none\"\
  : 0.0022576874321512206,\n        \"alias\": \" - leaderboard_math_hard\"\n    },\n\
  \    \"leaderboard_math_algebra_hard\": {\n        \"exact_match,none\": 0.009771986970684038,\n\
  \        \"exact_match_stderr,none\": 0.005623391633915882,\n        \"alias\":\
  \ \"  - leaderboard_math_algebra_hard\"\n    },\n    \"leaderboard_math_counting_and_prob_hard\"\
  : {\n        \"exact_match,none\": 0.0,\n        \"exact_match_stderr,none\": 0.0,\n\
  \        \"alias\": \"  - leaderboard_math_counting_and_prob_hard\"\n    },\n  \
  \  \"leaderboard_math_geometry_hard\": {\n        \"exact_match,none\": 0.0,\n \
  \       \"exact_match_stderr,none\": 0.0,\n        \"alias\": \"  - leaderboard_math_geometry_hard\"\
  \n    },\n    \"leaderboard_math_intermediate_algebra_hard\": {\n        \"exact_match,none\"\
  : 0.0035714285714285713,\n        \"exact_match_stderr,none\": 0.003571428571428562,\n\
  \        \"alias\": \"  - leaderboard_math_intermediate_algebra_hard\"\n    },\n\
  \    \"leaderboard_math_num_theory_hard\": {\n        \"exact_match,none\": 0.01948051948051948,\n\
  \        \"exact_match_stderr,none\": 0.01117333100557106,\n        \"alias\": \"\
  \  - leaderboard_math_num_theory_hard\"\n    },\n    \"leaderboard_math_prealgebra_hard\"\
  : {\n        \"exact_match,none\": 0.010362694300518135,\n        \"exact_match_stderr,none\"\
  : 0.007308424386792202,\n        \"alias\": \"  - leaderboard_math_prealgebra_hard\"\
  \n    },\n    \"leaderboard_math_precalculus_hard\": {\n        \"exact_match,none\"\
  : 0.0,\n        \"exact_match_stderr,none\": 0.0,\n        \"alias\": \"  - leaderboard_math_precalculus_hard\"\
  \n    },\n    \"leaderboard_mmlu_pro\": {\n        \"acc,none\": 0.11369680851063829,\n\
  \        \"acc_stderr,none\": 0.0028941059775779744,\n        \"alias\": \" - leaderboard_mmlu_pro\"\
  \n    },\n    \"leaderboard_musr\": {\n        \"acc_norm,none\": 0.3478835978835979,\n\
  \        \"acc_norm_stderr,none\": 0.016814352504527307,\n        \"alias\": \"\
  \ - leaderboard_musr\"\n    },\n    \"leaderboard_musr_murder_mysteries\": {\n \
  \       \"acc_norm,none\": 0.516,\n        \"acc_norm_stderr,none\": 0.03166998503010742,\n\
  \        \"alias\": \"  - leaderboard_musr_murder_mysteries\"\n    },\n    \"leaderboard_musr_object_placements\"\
  : {\n        \"acc_norm,none\": 0.26171875,\n        \"acc_norm_stderr,none\": 0.027526959754524398,\n\
  \        \"alias\": \"  - leaderboard_musr_object_placements\"\n    },\n    \"leaderboard_musr_team_allocation\"\
  : {\n        \"acc_norm,none\": 0.268,\n        \"acc_norm_stderr,none\": 0.02806876238252669,\n\
  \        \"alias\": \"  - leaderboard_musr_team_allocation\"\n    }\n}\n```"
repo_url: https://huggingface.co/EleutherAI/pythia-2.8b
leaderboard_url: ''
point_of_contact: ''
configs:
- config_name: EleutherAI__pythia-2.8b__leaderboard_arc_challenge
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_arc_challenge_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_arc_challenge_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_bbh
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_bbh_boolean_expressions_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_causal_judgement_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_date_understanding_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_disambiguation_qa_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_formal_fallacies_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_geometric_shapes_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_hyperbaton_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_logical_deduction_five_objects_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_logical_deduction_seven_objects_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_logical_deduction_three_objects_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_movie_recommendation_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_navigate_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_object_counting_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_penguins_in_a_table_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_reasoning_about_colored_objects_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_ruin_names_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_salient_translation_error_detection_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_snarks_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_sports_understanding_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_temporal_sequences_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_five_objects_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_seven_objects_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_three_objects_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_web_of_lies_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_boolean_expressions_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_causal_judgement_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_date_understanding_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_disambiguation_qa_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_formal_fallacies_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_geometric_shapes_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_hyperbaton_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_logical_deduction_five_objects_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_logical_deduction_seven_objects_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_logical_deduction_three_objects_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_movie_recommendation_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_navigate_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_object_counting_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_penguins_in_a_table_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_reasoning_about_colored_objects_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_ruin_names_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_salient_translation_error_detection_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_snarks_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_sports_understanding_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_temporal_sequences_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_five_objects_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_seven_objects_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_three_objects_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_bbh_web_of_lies_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_bbh_boolean_expressions
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_bbh_boolean_expressions_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_boolean_expressions_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_bbh_causal_judgement
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_bbh_causal_judgement_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_causal_judgement_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_bbh_date_understanding
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_bbh_date_understanding_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_date_understanding_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_bbh_disambiguation_qa
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_bbh_disambiguation_qa_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_disambiguation_qa_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_bbh_formal_fallacies
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_bbh_formal_fallacies_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_formal_fallacies_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_bbh_geometric_shapes
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_bbh_geometric_shapes_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_geometric_shapes_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_bbh_hyperbaton
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_bbh_hyperbaton_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_hyperbaton_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_bbh_logical_deduction_five_objects
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_bbh_logical_deduction_five_objects_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_logical_deduction_five_objects_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_bbh_logical_deduction_seven_objects
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_bbh_logical_deduction_seven_objects_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_logical_deduction_seven_objects_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_bbh_logical_deduction_three_objects
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_bbh_logical_deduction_three_objects_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_logical_deduction_three_objects_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_bbh_movie_recommendation
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_bbh_movie_recommendation_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_movie_recommendation_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_bbh_navigate
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_bbh_navigate_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_navigate_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_bbh_object_counting
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_bbh_object_counting_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_object_counting_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_bbh_penguins_in_a_table
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_bbh_penguins_in_a_table_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_penguins_in_a_table_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_bbh_reasoning_about_colored_objects
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_bbh_reasoning_about_colored_objects_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_reasoning_about_colored_objects_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_bbh_ruin_names
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_bbh_ruin_names_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_ruin_names_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_bbh_salient_translation_error_detection
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_bbh_salient_translation_error_detection_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_salient_translation_error_detection_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_bbh_snarks
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_bbh_snarks_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_snarks_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_bbh_sports_understanding
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_bbh_sports_understanding_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_sports_understanding_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_bbh_temporal_sequences
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_bbh_temporal_sequences_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_temporal_sequences_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_bbh_tracking_shuffled_objects_five_objects
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_five_objects_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_five_objects_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_bbh_tracking_shuffled_objects_seven_objects
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_seven_objects_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_seven_objects_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_bbh_tracking_shuffled_objects_three_objects
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_three_objects_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_three_objects_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_bbh_web_of_lies
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_bbh_web_of_lies_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_web_of_lies_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_gpqa
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_gpqa_diamond_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_gpqa_extended_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_gpqa_main_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_gpqa_diamond_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_gpqa_extended_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_gpqa_main_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_gpqa_diamond
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_gpqa_diamond_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_gpqa_diamond_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_gpqa_extended
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_gpqa_extended_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_gpqa_extended_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_gpqa_main
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_gpqa_main_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_gpqa_main_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_ifeval
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_ifeval_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_ifeval_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_math
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_math_algebra_hard_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_math_counting_and_prob_hard_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_math_geometry_hard_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_math_intermediate_algebra_hard_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_math_num_theory_hard_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_math_prealgebra_hard_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_math_precalculus_hard_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_math_algebra_hard_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_math_counting_and_prob_hard_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_math_geometry_hard_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_math_intermediate_algebra_hard_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_math_num_theory_hard_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_math_prealgebra_hard_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_math_precalculus_hard_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_math_algebra_hard
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_math_algebra_hard_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_math_algebra_hard_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_math_counting_and_prob_hard
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_math_counting_and_prob_hard_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_math_counting_and_prob_hard_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_math_geometry_hard
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_math_geometry_hard_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_math_geometry_hard_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_math_intermediate_algebra_hard
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_math_intermediate_algebra_hard_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_math_intermediate_algebra_hard_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_math_num_theory_hard
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_math_num_theory_hard_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_math_num_theory_hard_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_math_prealgebra_hard
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_math_prealgebra_hard_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_math_prealgebra_hard_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_math_precalculus_hard
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_math_precalculus_hard_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_math_precalculus_hard_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_mmlu_pro
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_mmlu_pro_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_mmlu_pro_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_musr
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_musr_murder_mysteries_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_musr_object_placements_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_musr_team_allocation_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_musr_murder_mysteries_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_musr_object_placements_2024-06-17T12-07-04.698905.json'
    - '**/samples_leaderboard_musr_team_allocation_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_musr_murder_mysteries
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_musr_murder_mysteries_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_musr_murder_mysteries_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_musr_object_placements
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_musr_object_placements_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_musr_object_placements_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__leaderboard_musr_team_allocation
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/samples_leaderboard_musr_team_allocation_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/samples_leaderboard_musr_team_allocation_2024-06-17T12-07-04.698905.json'
- config_name: EleutherAI__pythia-2.8b__results
  data_files:
  - split: 2024_06_17T12_07_04.698905
    path:
    - '**/results_2024-06-17T12-07-04.698905.json'
  - split: latest
    path:
    - '**/results_2024-06-17T12-07-04.698905.json'
---

# Dataset Card for Evaluation run of EleutherAI/pythia-2.8b

<!-- Provide a quick summary of the dataset. -->

Dataset automatically created during the evaluation run of model [EleutherAI/pythia-2.8b](https://huggingface.co/EleutherAI/pythia-2.8b)
The dataset is composed of 44 configuration(s), each one corresponding to one of the evaluated task.

The dataset has been created from 1 run(s). Each run can be found as a specific split in each configuration, the split being named using the timestamp of the run.The "train" split is always pointing to the latest results.

An additional configuration "results" store all the aggregated results of the run.

To load the details from a run, you can for instance do the following:
```python
from datasets import load_dataset
data = load_dataset(
	"HuggingFaceEvalInternal/EleutherAI__pythia-2.8b-details-private",
	name="EleutherAI__pythia-2.8b__leaderboard_arc_challenge",
	split="latest"
)
```

## Latest results

These are the [latest results from run 2024-06-17T12-07-04.698905](https://huggingface.co/datasets/HuggingFaceEvalInternal/EleutherAI__pythia-2.8b-details-private/blob/main/EleutherAI__pythia-2.8b/results_2024-06-17T12-07-04.698905.json) (note that there might be results for other tasks in the repos if successive evals didn't cover the same tasks. You find each in the results and the "latest" split for each eval):

```python
{
    "all": {
        "leaderboard": {
            "acc,none": 0.13155104513783702,
            "acc_stderr,none": 0.00289926789637609,
            "exact_match,none": 0.006797583081570997,
            "exact_match_stderr,none": 0.0022576874321512206,
            "inst_level_strict_acc,none": 0.2793764988009592,
            "inst_level_strict_acc_stderr,none": "N/A",
            "prompt_level_strict_acc,none": 0.15526802218114602,
            "prompt_level_strict_acc_stderr,none": 0.015584884858538145,
            "acc_norm,none": 0.3183200090079946,
            "acc_norm_stderr,none": 0.004755193956049788,
            "inst_level_loose_acc,none": 0.290167865707434,
            "inst_level_loose_acc_stderr,none": "N/A",
            "prompt_level_loose_acc,none": 0.1645101663585952,
            "prompt_level_loose_acc_stderr,none": 0.015954017926718037,
            "alias": "leaderboard"
        },
        "leaderboard_arc_challenge": {
            "acc,none": 0.3148464163822526,
            "acc_stderr,none": 0.013572657703084948,
            "acc_norm,none": 0.3575085324232082,
            "acc_norm_stderr,none": 0.01400549427591657,
            "alias": " - leaderboard_arc_challenge"
        },
        "leaderboard_bbh": {
            "acc_norm,none": 0.3206040617948273,
            "acc_norm_stderr,none": 0.005831106872988066,
            "alias": " - leaderboard_bbh"
        },
        "leaderboard_bbh_boolean_expressions": {
            "acc_norm,none": 0.628,
            "acc_norm_stderr,none": 0.030630325944558313,
            "alias": "  - leaderboard_bbh_boolean_expressions"
        },
        "leaderboard_bbh_causal_judgement": {
            "acc_norm,none": 0.44385026737967914,
            "acc_norm_stderr,none": 0.03642987131924726,
            "alias": "  - leaderboard_bbh_causal_judgement"
        },
        "leaderboard_bbh_date_understanding": {
            "acc_norm,none": 0.192,
            "acc_norm_stderr,none": 0.024960691989172012,
            "alias": "  - leaderboard_bbh_date_understanding"
        },
        "leaderboard_bbh_disambiguation_qa": {
            "acc_norm,none": 0.34,
            "acc_norm_stderr,none": 0.030020073605457904,
            "alias": "  - leaderboard_bbh_disambiguation_qa"
        },
        "leaderboard_bbh_formal_fallacies": {
            "acc_norm,none": 0.456,
            "acc_norm_stderr,none": 0.03156328506121339,
            "alias": "  - leaderboard_bbh_formal_fallacies"
        },
        "leaderboard_bbh_geometric_shapes": {
            "acc_norm,none": 0.088,
            "acc_norm_stderr,none": 0.01795308477705287,
            "alias": "  - leaderboard_bbh_geometric_shapes"
        },
        "leaderboard_bbh_hyperbaton": {
            "acc_norm,none": 0.484,
            "acc_norm_stderr,none": 0.031669985030107414,
            "alias": "  - leaderboard_bbh_hyperbaton"
        },
        "leaderboard_bbh_logical_deduction_five_objects": {
            "acc_norm,none": 0.236,
            "acc_norm_stderr,none": 0.026909337594953838,
            "alias": "  - leaderboard_bbh_logical_deduction_five_objects"
        },
        "leaderboard_bbh_logical_deduction_seven_objects": {
            "acc_norm,none": 0.144,
            "acc_norm_stderr,none": 0.02224940773545021,
            "alias": "  - leaderboard_bbh_logical_deduction_seven_objects"
        },
        "leaderboard_bbh_logical_deduction_three_objects": {
            "acc_norm,none": 0.344,
            "acc_norm_stderr,none": 0.030104503392316392,
            "alias": "  - leaderboard_bbh_logical_deduction_three_objects"
        },
        "leaderboard_bbh_movie_recommendation": {
            "acc_norm,none": 0.276,
            "acc_norm_stderr,none": 0.028328537274211342,
            "alias": "  - leaderboard_bbh_movie_recommendation"
        },
        "leaderboard_bbh_navigate": {
            "acc_norm,none": 0.5,
            "acc_norm_stderr,none": 0.031686212526223896,
            "alias": "  - leaderboard_bbh_navigate"
        },
        "leaderboard_bbh_object_counting": {
            "acc_norm,none": 0.264,
            "acc_norm_stderr,none": 0.027934518957690904,
            "alias": "  - leaderboard_bbh_object_counting"
        },
        "leaderboard_bbh_penguins_in_a_table": {
            "acc_norm,none": 0.19863013698630136,
            "acc_norm_stderr,none": 0.03313256608889821,
            "alias": "  - leaderboard_bbh_penguins_in_a_table"
        },
        "leaderboard_bbh_reasoning_about_colored_objects": {
            "acc_norm,none": 0.128,
            "acc_norm_stderr,none": 0.02117208133633648,
            "alias": "  - leaderboard_bbh_reasoning_about_colored_objects"
        },
        "leaderboard_bbh_ruin_names": {
            "acc_norm,none": 0.212,
            "acc_norm_stderr,none": 0.025901884690541156,
            "alias": "  - leaderboard_bbh_ruin_names"
        },
        "leaderboard_bbh_salient_translation_error_detection": {
            "acc_norm,none": 0.276,
            "acc_norm_stderr,none": 0.02832853727421135,
            "alias": "  - leaderboard_bbh_salient_translation_error_detection"
        },
        "leaderboard_bbh_snarks": {
            "acc_norm,none": 0.5393258426966292,
            "acc_norm_stderr,none": 0.0374658773638787,
            "alias": "  - leaderboard_bbh_snarks"
        },
        "leaderboard_bbh_sports_understanding": {
            "acc_norm,none": 0.5,
            "acc_norm_stderr,none": 0.031686212526223896,
            "alias": "  - leaderboard_bbh_sports_understanding"
        },
        "leaderboard_bbh_temporal_sequences": {
            "acc_norm,none": 0.284,
            "acc_norm_stderr,none": 0.02857695873043741,
            "alias": "  - leaderboard_bbh_temporal_sequences"
        },
        "leaderboard_bbh_tracking_shuffled_objects_five_objects": {
            "acc_norm,none": 0.156,
            "acc_norm_stderr,none": 0.022995023034068748,
            "alias": "  - leaderboard_bbh_tracking_shuffled_objects_five_objects"
        },
        "leaderboard_bbh_tracking_shuffled_objects_seven_objects": {
            "acc_norm,none": 0.168,
            "acc_norm_stderr,none": 0.0236928132054926,
            "alias": "  - leaderboard_bbh_tracking_shuffled_objects_seven_objects"
        },
        "leaderboard_bbh_tracking_shuffled_objects_three_objects": {
            "acc_norm,none": 0.34,
            "acc_norm_stderr,none": 0.030020073605457907,
            "alias": "  - leaderboard_bbh_tracking_shuffled_objects_three_objects"
        },
        "leaderboard_bbh_web_of_lies": {
            "acc_norm,none": 0.54,
            "acc_norm_stderr,none": 0.03158465389149899,
            "alias": "  - leaderboard_bbh_web_of_lies"
        },
        "leaderboard_gpqa": {
            "acc_norm,none": 0.25,
            "acc_norm_stderr,none": 0.012554809228367316,
            "alias": " - leaderboard_gpqa"
        },
        "leaderboard_gpqa_diamond": {
            "acc_norm,none": 0.24242424242424243,
            "acc_norm_stderr,none": 0.030532892233932026,
            "alias": "  - leaderboard_gpqa_diamond"
        },
        "leaderboard_gpqa_extended": {
            "acc_norm,none": 0.2600732600732601,
            "acc_norm_stderr,none": 0.01879074335201598,
            "alias": "  - leaderboard_gpqa_extended"
        },
        "leaderboard_gpqa_main": {
            "acc_norm,none": 0.24107142857142858,
            "acc_norm_stderr,none": 0.020231102978728707,
            "alias": "  - leaderboard_gpqa_main"
        },
        "leaderboard_ifeval": {
            "prompt_level_strict_acc,none": 0.15526802218114602,
            "prompt_level_strict_acc_stderr,none": 0.015584884858538145,
            "inst_level_strict_acc,none": 0.2793764988009592,
            "inst_level_strict_acc_stderr,none": "N/A",
            "prompt_level_loose_acc,none": 0.1645101663585952,
            "prompt_level_loose_acc_stderr,none": 0.015954017926718037,
            "inst_level_loose_acc,none": 0.290167865707434,
            "inst_level_loose_acc_stderr,none": "N/A",
            "alias": " - leaderboard_ifeval"
        },
        "leaderboard_math_hard": {
            "exact_match,none": 0.006797583081570997,
            "exact_match_stderr,none": 0.0022576874321512206,
            "alias": " - leaderboard_math_hard"
        },
        "leaderboard_math_algebra_hard": {
            "exact_match,none": 0.009771986970684038,
            "exact_match_stderr,none": 0.005623391633915882,
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
            "exact_match,none": 0.0035714285714285713,
            "exact_match_stderr,none": 0.003571428571428562,
            "alias": "  - leaderboard_math_intermediate_algebra_hard"
        },
        "leaderboard_math_num_theory_hard": {
            "exact_match,none": 0.01948051948051948,
            "exact_match_stderr,none": 0.01117333100557106,
            "alias": "  - leaderboard_math_num_theory_hard"
        },
        "leaderboard_math_prealgebra_hard": {
            "exact_match,none": 0.010362694300518135,
            "exact_match_stderr,none": 0.007308424386792202,
            "alias": "  - leaderboard_math_prealgebra_hard"
        },
        "leaderboard_math_precalculus_hard": {
            "exact_match,none": 0.0,
            "exact_match_stderr,none": 0.0,
            "alias": "  - leaderboard_math_precalculus_hard"
        },
        "leaderboard_mmlu_pro": {
            "acc,none": 0.11369680851063829,
            "acc_stderr,none": 0.0028941059775779744,
            "alias": " - leaderboard_mmlu_pro"
        },
        "leaderboard_musr": {
            "acc_norm,none": 0.3478835978835979,
            "acc_norm_stderr,none": 0.016814352504527307,
            "alias": " - leaderboard_musr"
        },
        "leaderboard_musr_murder_mysteries": {
            "acc_norm,none": 0.516,
            "acc_norm_stderr,none": 0.03166998503010742,
            "alias": "  - leaderboard_musr_murder_mysteries"
        },
        "leaderboard_musr_object_placements": {
            "acc_norm,none": 0.26171875,
            "acc_norm_stderr,none": 0.027526959754524398,
            "alias": "  - leaderboard_musr_object_placements"
        },
        "leaderboard_musr_team_allocation": {
            "acc_norm,none": 0.268,
            "acc_norm_stderr,none": 0.02806876238252669,
            "alias": "  - leaderboard_musr_team_allocation"
        }
    },
    "leaderboard": {
        "acc,none": 0.13155104513783702,
        "acc_stderr,none": 0.00289926789637609,
        "exact_match,none": 0.006797583081570997,
        "exact_match_stderr,none": 0.0022576874321512206,
        "inst_level_strict_acc,none": 0.2793764988009592,
        "inst_level_strict_acc_stderr,none": "N/A",
        "prompt_level_strict_acc,none": 0.15526802218114602,
        "prompt_level_strict_acc_stderr,none": 0.015584884858538145,
        "acc_norm,none": 0.3183200090079946,
        "acc_norm_stderr,none": 0.004755193956049788,
        "inst_level_loose_acc,none": 0.290167865707434,
        "inst_level_loose_acc_stderr,none": "N/A",
        "prompt_level_loose_acc,none": 0.1645101663585952,
        "prompt_level_loose_acc_stderr,none": 0.015954017926718037,
        "alias": "leaderboard"
    },
    "leaderboard_arc_challenge": {
        "acc,none": 0.3148464163822526,
        "acc_stderr,none": 0.013572657703084948,
        "acc_norm,none": 0.3575085324232082,
        "acc_norm_stderr,none": 0.01400549427591657,
        "alias": " - leaderboard_arc_challenge"
    },
    "leaderboard_bbh": {
        "acc_norm,none": 0.3206040617948273,
        "acc_norm_stderr,none": 0.005831106872988066,
        "alias": " - leaderboard_bbh"
    },
    "leaderboard_bbh_boolean_expressions": {
        "acc_norm,none": 0.628,
        "acc_norm_stderr,none": 0.030630325944558313,
        "alias": "  - leaderboard_bbh_boolean_expressions"
    },
    "leaderboard_bbh_causal_judgement": {
        "acc_norm,none": 0.44385026737967914,
        "acc_norm_stderr,none": 0.03642987131924726,
        "alias": "  - leaderboard_bbh_causal_judgement"
    },
    "leaderboard_bbh_date_understanding": {
        "acc_norm,none": 0.192,
        "acc_norm_stderr,none": 0.024960691989172012,
        "alias": "  - leaderboard_bbh_date_understanding"
    },
    "leaderboard_bbh_disambiguation_qa": {
        "acc_norm,none": 0.34,
        "acc_norm_stderr,none": 0.030020073605457904,
        "alias": "  - leaderboard_bbh_disambiguation_qa"
    },
    "leaderboard_bbh_formal_fallacies": {
        "acc_norm,none": 0.456,
        "acc_norm_stderr,none": 0.03156328506121339,
        "alias": "  - leaderboard_bbh_formal_fallacies"
    },
    "leaderboard_bbh_geometric_shapes": {
        "acc_norm,none": 0.088,
        "acc_norm_stderr,none": 0.01795308477705287,
        "alias": "  - leaderboard_bbh_geometric_shapes"
    },
    "leaderboard_bbh_hyperbaton": {
        "acc_norm,none": 0.484,
        "acc_norm_stderr,none": 0.031669985030107414,
        "alias": "  - leaderboard_bbh_hyperbaton"
    },
    "leaderboard_bbh_logical_deduction_five_objects": {
        "acc_norm,none": 0.236,
        "acc_norm_stderr,none": 0.026909337594953838,
        "alias": "  - leaderboard_bbh_logical_deduction_five_objects"
    },
    "leaderboard_bbh_logical_deduction_seven_objects": {
        "acc_norm,none": 0.144,
        "acc_norm_stderr,none": 0.02224940773545021,
        "alias": "  - leaderboard_bbh_logical_deduction_seven_objects"
    },
    "leaderboard_bbh_logical_deduction_three_objects": {
        "acc_norm,none": 0.344,
        "acc_norm_stderr,none": 0.030104503392316392,
        "alias": "  - leaderboard_bbh_logical_deduction_three_objects"
    },
    "leaderboard_bbh_movie_recommendation": {
        "acc_norm,none": 0.276,
        "acc_norm_stderr,none": 0.028328537274211342,
        "alias": "  - leaderboard_bbh_movie_recommendation"
    },
    "leaderboard_bbh_navigate": {
        "acc_norm,none": 0.5,
        "acc_norm_stderr,none": 0.031686212526223896,
        "alias": "  - leaderboard_bbh_navigate"
    },
    "leaderboard_bbh_object_counting": {
        "acc_norm,none": 0.264,
        "acc_norm_stderr,none": 0.027934518957690904,
        "alias": "  - leaderboard_bbh_object_counting"
    },
    "leaderboard_bbh_penguins_in_a_table": {
        "acc_norm,none": 0.19863013698630136,
        "acc_norm_stderr,none": 0.03313256608889821,
        "alias": "  - leaderboard_bbh_penguins_in_a_table"
    },
    "leaderboard_bbh_reasoning_about_colored_objects": {
        "acc_norm,none": 0.128,
        "acc_norm_stderr,none": 0.02117208133633648,
        "alias": "  - leaderboard_bbh_reasoning_about_colored_objects"
    },
    "leaderboard_bbh_ruin_names": {
        "acc_norm,none": 0.212,
        "acc_norm_stderr,none": 0.025901884690541156,
        "alias": "  - leaderboard_bbh_ruin_names"
    },
    "leaderboard_bbh_salient_translation_error_detection": {
        "acc_norm,none": 0.276,
        "acc_norm_stderr,none": 0.02832853727421135,
        "alias": "  - leaderboard_bbh_salient_translation_error_detection"
    },
    "leaderboard_bbh_snarks": {
        "acc_norm,none": 0.5393258426966292,
        "acc_norm_stderr,none": 0.0374658773638787,
        "alias": "  - leaderboard_bbh_snarks"
    },
    "leaderboard_bbh_sports_understanding": {
        "acc_norm,none": 0.5,
        "acc_norm_stderr,none": 0.031686212526223896,
        "alias": "  - leaderboard_bbh_sports_understanding"
    },
    "leaderboard_bbh_temporal_sequences": {
        "acc_norm,none": 0.284,
        "acc_norm_stderr,none": 0.02857695873043741,
        "alias": "  - leaderboard_bbh_temporal_sequences"
    },
    "leaderboard_bbh_tracking_shuffled_objects_five_objects": {
        "acc_norm,none": 0.156,
        "acc_norm_stderr,none": 0.022995023034068748,
        "alias": "  - leaderboard_bbh_tracking_shuffled_objects_five_objects"
    },
    "leaderboard_bbh_tracking_shuffled_objects_seven_objects": {
        "acc_norm,none": 0.168,
        "acc_norm_stderr,none": 0.0236928132054926,
        "alias": "  - leaderboard_bbh_tracking_shuffled_objects_seven_objects"
    },
    "leaderboard_bbh_tracking_shuffled_objects_three_objects": {
        "acc_norm,none": 0.34,
        "acc_norm_stderr,none": 0.030020073605457907,
        "alias": "  - leaderboard_bbh_tracking_shuffled_objects_three_objects"
    },
    "leaderboard_bbh_web_of_lies": {
        "acc_norm,none": 0.54,
        "acc_norm_stderr,none": 0.03158465389149899,
        "alias": "  - leaderboard_bbh_web_of_lies"
    },
    "leaderboard_gpqa": {
        "acc_norm,none": 0.25,
        "acc_norm_stderr,none": 0.012554809228367316,
        "alias": " - leaderboard_gpqa"
    },
    "leaderboard_gpqa_diamond": {
        "acc_norm,none": 0.24242424242424243,
        "acc_norm_stderr,none": 0.030532892233932026,
        "alias": "  - leaderboard_gpqa_diamond"
    },
    "leaderboard_gpqa_extended": {
        "acc_norm,none": 0.2600732600732601,
        "acc_norm_stderr,none": 0.01879074335201598,
        "alias": "  - leaderboard_gpqa_extended"
    },
    "leaderboard_gpqa_main": {
        "acc_norm,none": 0.24107142857142858,
        "acc_norm_stderr,none": 0.020231102978728707,
        "alias": "  - leaderboard_gpqa_main"
    },
    "leaderboard_ifeval": {
        "prompt_level_strict_acc,none": 0.15526802218114602,
        "prompt_level_strict_acc_stderr,none": 0.015584884858538145,
        "inst_level_strict_acc,none": 0.2793764988009592,
        "inst_level_strict_acc_stderr,none": "N/A",
        "prompt_level_loose_acc,none": 0.1645101663585952,
        "prompt_level_loose_acc_stderr,none": 0.015954017926718037,
        "inst_level_loose_acc,none": 0.290167865707434,
        "inst_level_loose_acc_stderr,none": "N/A",
        "alias": " - leaderboard_ifeval"
    },
    "leaderboard_math_hard": {
        "exact_match,none": 0.006797583081570997,
        "exact_match_stderr,none": 0.0022576874321512206,
        "alias": " - leaderboard_math_hard"
    },
    "leaderboard_math_algebra_hard": {
        "exact_match,none": 0.009771986970684038,
        "exact_match_stderr,none": 0.005623391633915882,
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
        "exact_match,none": 0.0035714285714285713,
        "exact_match_stderr,none": 0.003571428571428562,
        "alias": "  - leaderboard_math_intermediate_algebra_hard"
    },
    "leaderboard_math_num_theory_hard": {
        "exact_match,none": 0.01948051948051948,
        "exact_match_stderr,none": 0.01117333100557106,
        "alias": "  - leaderboard_math_num_theory_hard"
    },
    "leaderboard_math_prealgebra_hard": {
        "exact_match,none": 0.010362694300518135,
        "exact_match_stderr,none": 0.007308424386792202,
        "alias": "  - leaderboard_math_prealgebra_hard"
    },
    "leaderboard_math_precalculus_hard": {
        "exact_match,none": 0.0,
        "exact_match_stderr,none": 0.0,
        "alias": "  - leaderboard_math_precalculus_hard"
    },
    "leaderboard_mmlu_pro": {
        "acc,none": 0.11369680851063829,
        "acc_stderr,none": 0.0028941059775779744,
        "alias": " - leaderboard_mmlu_pro"
    },
    "leaderboard_musr": {
        "acc_norm,none": 0.3478835978835979,
        "acc_norm_stderr,none": 0.016814352504527307,
        "alias": " - leaderboard_musr"
    },
    "leaderboard_musr_murder_mysteries": {
        "acc_norm,none": 0.516,
        "acc_norm_stderr,none": 0.03166998503010742,
        "alias": "  - leaderboard_musr_murder_mysteries"
    },
    "leaderboard_musr_object_placements": {
        "acc_norm,none": 0.26171875,
        "acc_norm_stderr,none": 0.027526959754524398,
        "alias": "  - leaderboard_musr_object_placements"
    },
    "leaderboard_musr_team_allocation": {
        "acc_norm,none": 0.268,
        "acc_norm_stderr,none": 0.02806876238252669,
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