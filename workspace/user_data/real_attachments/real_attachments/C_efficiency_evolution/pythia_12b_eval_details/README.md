---
pretty_name: Evaluation run of EleutherAI/pythia-12b
dataset_summary: "Dataset automatically created during the evaluation run of model\
  \ [EleutherAI/pythia-12b](https://huggingface.co/EleutherAI/pythia-12b)\nThe dataset\
  \ is composed of 44 configuration(s), each one corresponding to one of the evaluated\
  \ task.\n\nThe dataset has been created from 1 run(s). Each run can be found as\
  \ a specific split in each configuration, the split being named using the timestamp\
  \ of the run.The \"train\" split is always pointing to the latest results.\n\nAn\
  \ additional configuration \"results\" store all the aggregated results of the run.\n\
  \nTo load the details from a run, you can for instance do the following:\n```python\n\
  from datasets import load_dataset\ndata = load_dataset(\n\t\"HuggingFaceEvalInternal/EleutherAI__pythia-12b-details-private\"\
  ,\n\tname=\"EleutherAI__pythia-12b__leaderboard_arc_challenge\",\n\tsplit=\"latest\"\
  \n)\n```\n\n## Latest results\n\nThese are the [latest results from run 2024-06-17T17-37-25.144953](https://huggingface.co/datasets/HuggingFaceEvalInternal/EleutherAI__pythia-12b-details-private/blob/main/EleutherAI__pythia-12b/results_2024-06-17T17-37-25.144953.json)\
  \ (note that there might be results for other tasks in the repos if successive evals\
  \ didn't cover the same tasks. You find each in the results and the \"latest\" split\
  \ for each eval):\n\n```python\n{\n    \"all\": {\n        \"leaderboard\": {\n\
  \            \"inst_level_loose_acc,none\": 0.31534772182254195,\n            \"\
  inst_level_loose_acc_stderr,none\": \"N/A\",\n            \"acc_norm,none\": 0.3224862065082761,\n\
  \            \"acc_norm_stderr,none\": 0.004769106493523972,\n            \"prompt_level_strict_acc,none\"\
  : 0.18853974121996303,\n            \"prompt_level_strict_acc_stderr,none\": 0.016832096060176906,\n\
  \            \"acc,none\": 0.13382308391396547,\n            \"acc_stderr,none\"\
  : 0.002893167355275893,\n            \"prompt_level_loose_acc,none\": 0.19408502772643252,\n\
  \            \"prompt_level_loose_acc_stderr,none\": 0.017019380550749422,\n   \
  \         \"inst_level_strict_acc,none\": 0.3057553956834532,\n            \"inst_level_strict_acc_stderr,none\"\
  : \"N/A\",\n            \"exact_match,none\": 0.00906344410876133,\n           \
  \ \"exact_match_stderr,none\": 0.002601527328160649,\n            \"alias\": \"\
  leaderboard\"\n        },\n        \"leaderboard_arc_challenge\": {\n          \
  \  \"acc,none\": 0.36945392491467577,\n            \"acc_stderr,none\": 0.01410457836649191,\n\
  \            \"acc_norm,none\": 0.4044368600682594,\n            \"acc_norm_stderr,none\"\
  : 0.014342036483436172,\n            \"alias\": \" - leaderboard_arc_challenge\"\
  \n        },\n        \"leaderboard_bbh\": {\n            \"acc_norm,none\": 0.31609095643117513,\n\
  \            \"acc_norm_stderr,none\": 0.005821168127128767,\n            \"alias\"\
  : \" - leaderboard_bbh\"\n        },\n        \"leaderboard_bbh_boolean_expressions\"\
  : {\n            \"acc_norm,none\": 0.668,\n            \"acc_norm_stderr,none\"\
  : 0.029844039047465902,\n            \"alias\": \"  - leaderboard_bbh_boolean_expressions\"\
  \n        },\n        \"leaderboard_bbh_causal_judgement\": {\n            \"acc_norm,none\"\
  : 0.5294117647058824,\n            \"acc_norm_stderr,none\": 0.03659829510813268,\n\
  \            \"alias\": \"  - leaderboard_bbh_causal_judgement\"\n        },\n \
  \       \"leaderboard_bbh_date_understanding\": {\n            \"acc_norm,none\"\
  : 0.16,\n            \"acc_norm_stderr,none\": 0.02323271478206065,\n          \
  \  \"alias\": \"  - leaderboard_bbh_date_understanding\"\n        },\n        \"\
  leaderboard_bbh_disambiguation_qa\": {\n            \"acc_norm,none\": 0.336,\n\
  \            \"acc_norm_stderr,none\": 0.029933259094191516,\n            \"alias\"\
  : \"  - leaderboard_bbh_disambiguation_qa\"\n        },\n        \"leaderboard_bbh_formal_fallacies\"\
  : {\n            \"acc_norm,none\": 0.476,\n            \"acc_norm_stderr,none\"\
  : 0.03164968895968782,\n            \"alias\": \"  - leaderboard_bbh_formal_fallacies\"\
  \n        },\n        \"leaderboard_bbh_geometric_shapes\": {\n            \"acc_norm,none\"\
  : 0.104,\n            \"acc_norm_stderr,none\": 0.019345100974843887,\n        \
  \    \"alias\": \"  - leaderboard_bbh_geometric_shapes\"\n        },\n        \"\
  leaderboard_bbh_hyperbaton\": {\n            \"acc_norm,none\": 0.484,\n       \
  \     \"acc_norm_stderr,none\": 0.031669985030107414,\n            \"alias\": \"\
  \  - leaderboard_bbh_hyperbaton\"\n        },\n        \"leaderboard_bbh_logical_deduction_five_objects\"\
  : {\n            \"acc_norm,none\": 0.192,\n            \"acc_norm_stderr,none\"\
  : 0.024960691989172005,\n            \"alias\": \"  - leaderboard_bbh_logical_deduction_five_objects\"\
  \n        },\n        \"leaderboard_bbh_logical_deduction_seven_objects\": {\n \
  \           \"acc_norm,none\": 0.148,\n            \"acc_norm_stderr,none\": 0.022503547243806137,\n\
  \            \"alias\": \"  - leaderboard_bbh_logical_deduction_seven_objects\"\n\
  \        },\n        \"leaderboard_bbh_logical_deduction_three_objects\": {\n  \
  \          \"acc_norm,none\": 0.344,\n            \"acc_norm_stderr,none\": 0.030104503392316392,\n\
  \            \"alias\": \"  - leaderboard_bbh_logical_deduction_three_objects\"\n\
  \        },\n        \"leaderboard_bbh_movie_recommendation\": {\n            \"\
  acc_norm,none\": 0.288,\n            \"acc_norm_stderr,none\": 0.028697004587398225,\n\
  \            \"alias\": \"  - leaderboard_bbh_movie_recommendation\"\n        },\n\
  \        \"leaderboard_bbh_navigate\": {\n            \"acc_norm,none\": 0.468,\n\
  \            \"acc_norm_stderr,none\": 0.031621252575725504,\n            \"alias\"\
  : \"  - leaderboard_bbh_navigate\"\n        },\n        \"leaderboard_bbh_object_counting\"\
  : {\n            \"acc_norm,none\": 0.272,\n            \"acc_norm_stderr,none\"\
  : 0.028200088296310016,\n            \"alias\": \"  - leaderboard_bbh_object_counting\"\
  \n        },\n        \"leaderboard_bbh_penguins_in_a_table\": {\n            \"\
  acc_norm,none\": 0.22602739726027396,\n            \"acc_norm_stderr,none\": 0.034734362688347384,\n\
  \            \"alias\": \"  - leaderboard_bbh_penguins_in_a_table\"\n        },\n\
  \        \"leaderboard_bbh_reasoning_about_colored_objects\": {\n            \"\
  acc_norm,none\": 0.172,\n            \"acc_norm_stderr,none\": 0.023915513944486218,\n\
  \            \"alias\": \"  - leaderboard_bbh_reasoning_about_colored_objects\"\n\
  \        },\n        \"leaderboard_bbh_ruin_names\": {\n            \"acc_norm,none\"\
  : 0.284,\n            \"acc_norm_stderr,none\": 0.02857695873043741,\n         \
  \   \"alias\": \"  - leaderboard_bbh_ruin_names\"\n        },\n        \"leaderboard_bbh_salient_translation_error_detection\"\
  : {\n            \"acc_norm,none\": 0.22,\n            \"acc_norm_stderr,none\"\
  : 0.026251792824605845,\n            \"alias\": \"  - leaderboard_bbh_salient_translation_error_detection\"\
  \n        },\n        \"leaderboard_bbh_snarks\": {\n            \"acc_norm,none\"\
  : 0.4157303370786517,\n            \"acc_norm_stderr,none\": 0.03704468395960965,\n\
  \            \"alias\": \"  - leaderboard_bbh_snarks\"\n        },\n        \"leaderboard_bbh_sports_understanding\"\
  : {\n            \"acc_norm,none\": 0.46,\n            \"acc_norm_stderr,none\"\
  : 0.031584653891499,\n            \"alias\": \"  - leaderboard_bbh_sports_understanding\"\
  \n        },\n        \"leaderboard_bbh_temporal_sequences\": {\n            \"\
  acc_norm,none\": 0.268,\n            \"acc_norm_stderr,none\": 0.02806876238252669,\n\
  \            \"alias\": \"  - leaderboard_bbh_temporal_sequences\"\n        },\n\
  \        \"leaderboard_bbh_tracking_shuffled_objects_five_objects\": {\n       \
  \     \"acc_norm,none\": 0.172,\n            \"acc_norm_stderr,none\": 0.023915513944486218,\n\
  \            \"alias\": \"  - leaderboard_bbh_tracking_shuffled_objects_five_objects\"\
  \n        },\n        \"leaderboard_bbh_tracking_shuffled_objects_seven_objects\"\
  : {\n            \"acc_norm,none\": 0.132,\n            \"acc_norm_stderr,none\"\
  : 0.021450980824038124,\n            \"alias\": \"  - leaderboard_bbh_tracking_shuffled_objects_seven_objects\"\
  \n        },\n        \"leaderboard_bbh_tracking_shuffled_objects_three_objects\"\
  : {\n            \"acc_norm,none\": 0.324,\n            \"acc_norm_stderr,none\"\
  : 0.02965829492454557,\n            \"alias\": \"  - leaderboard_bbh_tracking_shuffled_objects_three_objects\"\
  \n        },\n        \"leaderboard_bbh_web_of_lies\": {\n            \"acc_norm,none\"\
  : 0.488,\n            \"acc_norm_stderr,none\": 0.03167708558254709,\n         \
  \   \"alias\": \"  - leaderboard_bbh_web_of_lies\"\n        },\n        \"leaderboard_gpqa\"\
  : {\n            \"acc_norm,none\": 0.24664429530201343,\n            \"acc_norm_stderr,none\"\
  : 0.012496674738288107,\n            \"alias\": \" - leaderboard_gpqa\"\n      \
  \  },\n        \"leaderboard_gpqa_diamond\": {\n            \"acc_norm,none\": 0.25252525252525254,\n\
  \            \"acc_norm_stderr,none\": 0.030954055470365886,\n            \"alias\"\
  : \"  - leaderboard_gpqa_diamond\"\n        },\n        \"leaderboard_gpqa_extended\"\
  : {\n            \"acc_norm,none\": 0.2564102564102564,\n            \"acc_norm_stderr,none\"\
  : 0.018704070930965995,\n            \"alias\": \"  - leaderboard_gpqa_extended\"\
  \n        },\n        \"leaderboard_gpqa_main\": {\n            \"acc_norm,none\"\
  : 0.23214285714285715,\n            \"acc_norm_stderr,none\": 0.019969358575699175,\n\
  \            \"alias\": \"  - leaderboard_gpqa_main\"\n        },\n        \"leaderboard_ifeval\"\
  : {\n            \"prompt_level_strict_acc,none\": 0.18853974121996303,\n      \
  \      \"prompt_level_strict_acc_stderr,none\": 0.016832096060176906,\n        \
  \    \"inst_level_strict_acc,none\": 0.3057553956834532,\n            \"inst_level_strict_acc_stderr,none\"\
  : \"N/A\",\n            \"prompt_level_loose_acc,none\": 0.19408502772643252,\n\
  \            \"prompt_level_loose_acc_stderr,none\": 0.017019380550749422,\n   \
  \         \"inst_level_loose_acc,none\": 0.31534772182254195,\n            \"inst_level_loose_acc_stderr,none\"\
  : \"N/A\",\n            \"alias\": \" - leaderboard_ifeval\"\n        },\n     \
  \   \"leaderboard_math_hard\": {\n            \"exact_match,none\": 0.00906344410876133,\n\
  \            \"exact_match_stderr,none\": 0.002601527328160649,\n            \"\
  alias\": \" - leaderboard_math_hard\"\n        },\n        \"leaderboard_math_algebra_hard\"\
  : {\n            \"exact_match,none\": 0.006514657980456026,\n            \"exact_match_stderr,none\"\
  : 0.004599025618546253,\n            \"alias\": \"  - leaderboard_math_algebra_hard\"\
  \n        },\n        \"leaderboard_math_counting_and_prob_hard\": {\n         \
  \   \"exact_match,none\": 0.024390243902439025,\n            \"exact_match_stderr,none\"\
  : 0.013965813032045558,\n            \"alias\": \"  - leaderboard_math_counting_and_prob_hard\"\
  \n        },\n        \"leaderboard_math_geometry_hard\": {\n            \"exact_match,none\"\
  : 0.0,\n            \"exact_match_stderr,none\": 0.0,\n            \"alias\": \"\
  \  - leaderboard_math_geometry_hard\"\n        },\n        \"leaderboard_math_intermediate_algebra_hard\"\
  : {\n            \"exact_match,none\": 0.0,\n            \"exact_match_stderr,none\"\
  : 0.0,\n            \"alias\": \"  - leaderboard_math_intermediate_algebra_hard\"\
  \n        },\n        \"leaderboard_math_num_theory_hard\": {\n            \"exact_match,none\"\
  : 0.01948051948051948,\n            \"exact_match_stderr,none\": 0.011173331005571076,\n\
  \            \"alias\": \"  - leaderboard_math_num_theory_hard\"\n        },\n \
  \       \"leaderboard_math_prealgebra_hard\": {\n            \"exact_match,none\"\
  : 0.015544041450777202,\n            \"exact_match_stderr,none\": 0.008927492715084343,\n\
  \            \"alias\": \"  - leaderboard_math_prealgebra_hard\"\n        },\n \
  \       \"leaderboard_math_precalculus_hard\": {\n            \"exact_match,none\"\
  : 0.007407407407407408,\n            \"exact_match_stderr,none\": 0.007407407407407403,\n\
  \            \"alias\": \"  - leaderboard_math_precalculus_hard\"\n        },\n\
  \        \"leaderboard_mmlu_pro\": {\n            \"acc,none\": 0.11087101063829788,\n\
  \            \"acc_stderr,none\": 0.0028624672393866564,\n            \"alias\"\
  : \" - leaderboard_mmlu_pro\"\n        },\n        \"leaderboard_musr\": {\n   \
  \         \"acc_norm,none\": 0.3637566137566138,\n            \"acc_norm_stderr,none\"\
  : 0.016983543757727832,\n            \"alias\": \" - leaderboard_musr\"\n      \
  \  },\n        \"leaderboard_musr_murder_mysteries\": {\n            \"acc_norm,none\"\
  : 0.528,\n            \"acc_norm_stderr,none\": 0.031636489531544396,\n        \
  \    \"alias\": \"  - leaderboard_musr_murder_mysteries\"\n        },\n        \"\
  leaderboard_musr_object_placements\": {\n            \"acc_norm,none\": 0.24609375,\n\
  \            \"acc_norm_stderr,none\": 0.026973597563786113,\n            \"alias\"\
  : \"  - leaderboard_musr_object_placements\"\n        },\n        \"leaderboard_musr_team_allocation\"\
  : {\n            \"acc_norm,none\": 0.32,\n            \"acc_norm_stderr,none\"\
  : 0.029561724955241037,\n            \"alias\": \"  - leaderboard_musr_team_allocation\"\
  \n        }\n    },\n    \"leaderboard\": {\n        \"inst_level_loose_acc,none\"\
  : 0.31534772182254195,\n        \"inst_level_loose_acc_stderr,none\": \"N/A\",\n\
  \        \"acc_norm,none\": 0.3224862065082761,\n        \"acc_norm_stderr,none\"\
  : 0.004769106493523972,\n        \"prompt_level_strict_acc,none\": 0.18853974121996303,\n\
  \        \"prompt_level_strict_acc_stderr,none\": 0.016832096060176906,\n      \
  \  \"acc,none\": 0.13382308391396547,\n        \"acc_stderr,none\": 0.002893167355275893,\n\
  \        \"prompt_level_loose_acc,none\": 0.19408502772643252,\n        \"prompt_level_loose_acc_stderr,none\"\
  : 0.017019380550749422,\n        \"inst_level_strict_acc,none\": 0.3057553956834532,\n\
  \        \"inst_level_strict_acc_stderr,none\": \"N/A\",\n        \"exact_match,none\"\
  : 0.00906344410876133,\n        \"exact_match_stderr,none\": 0.002601527328160649,\n\
  \        \"alias\": \"leaderboard\"\n    },\n    \"leaderboard_arc_challenge\":\
  \ {\n        \"acc,none\": 0.36945392491467577,\n        \"acc_stderr,none\": 0.01410457836649191,\n\
  \        \"acc_norm,none\": 0.4044368600682594,\n        \"acc_norm_stderr,none\"\
  : 0.014342036483436172,\n        \"alias\": \" - leaderboard_arc_challenge\"\n \
  \   },\n    \"leaderboard_bbh\": {\n        \"acc_norm,none\": 0.31609095643117513,\n\
  \        \"acc_norm_stderr,none\": 0.005821168127128767,\n        \"alias\": \"\
  \ - leaderboard_bbh\"\n    },\n    \"leaderboard_bbh_boolean_expressions\": {\n\
  \        \"acc_norm,none\": 0.668,\n        \"acc_norm_stderr,none\": 0.029844039047465902,\n\
  \        \"alias\": \"  - leaderboard_bbh_boolean_expressions\"\n    },\n    \"\
  leaderboard_bbh_causal_judgement\": {\n        \"acc_norm,none\": 0.5294117647058824,\n\
  \        \"acc_norm_stderr,none\": 0.03659829510813268,\n        \"alias\": \" \
  \ - leaderboard_bbh_causal_judgement\"\n    },\n    \"leaderboard_bbh_date_understanding\"\
  : {\n        \"acc_norm,none\": 0.16,\n        \"acc_norm_stderr,none\": 0.02323271478206065,\n\
  \        \"alias\": \"  - leaderboard_bbh_date_understanding\"\n    },\n    \"leaderboard_bbh_disambiguation_qa\"\
  : {\n        \"acc_norm,none\": 0.336,\n        \"acc_norm_stderr,none\": 0.029933259094191516,\n\
  \        \"alias\": \"  - leaderboard_bbh_disambiguation_qa\"\n    },\n    \"leaderboard_bbh_formal_fallacies\"\
  : {\n        \"acc_norm,none\": 0.476,\n        \"acc_norm_stderr,none\": 0.03164968895968782,\n\
  \        \"alias\": \"  - leaderboard_bbh_formal_fallacies\"\n    },\n    \"leaderboard_bbh_geometric_shapes\"\
  : {\n        \"acc_norm,none\": 0.104,\n        \"acc_norm_stderr,none\": 0.019345100974843887,\n\
  \        \"alias\": \"  - leaderboard_bbh_geometric_shapes\"\n    },\n    \"leaderboard_bbh_hyperbaton\"\
  : {\n        \"acc_norm,none\": 0.484,\n        \"acc_norm_stderr,none\": 0.031669985030107414,\n\
  \        \"alias\": \"  - leaderboard_bbh_hyperbaton\"\n    },\n    \"leaderboard_bbh_logical_deduction_five_objects\"\
  : {\n        \"acc_norm,none\": 0.192,\n        \"acc_norm_stderr,none\": 0.024960691989172005,\n\
  \        \"alias\": \"  - leaderboard_bbh_logical_deduction_five_objects\"\n   \
  \ },\n    \"leaderboard_bbh_logical_deduction_seven_objects\": {\n        \"acc_norm,none\"\
  : 0.148,\n        \"acc_norm_stderr,none\": 0.022503547243806137,\n        \"alias\"\
  : \"  - leaderboard_bbh_logical_deduction_seven_objects\"\n    },\n    \"leaderboard_bbh_logical_deduction_three_objects\"\
  : {\n        \"acc_norm,none\": 0.344,\n        \"acc_norm_stderr,none\": 0.030104503392316392,\n\
  \        \"alias\": \"  - leaderboard_bbh_logical_deduction_three_objects\"\n  \
  \  },\n    \"leaderboard_bbh_movie_recommendation\": {\n        \"acc_norm,none\"\
  : 0.288,\n        \"acc_norm_stderr,none\": 0.028697004587398225,\n        \"alias\"\
  : \"  - leaderboard_bbh_movie_recommendation\"\n    },\n    \"leaderboard_bbh_navigate\"\
  : {\n        \"acc_norm,none\": 0.468,\n        \"acc_norm_stderr,none\": 0.031621252575725504,\n\
  \        \"alias\": \"  - leaderboard_bbh_navigate\"\n    },\n    \"leaderboard_bbh_object_counting\"\
  : {\n        \"acc_norm,none\": 0.272,\n        \"acc_norm_stderr,none\": 0.028200088296310016,\n\
  \        \"alias\": \"  - leaderboard_bbh_object_counting\"\n    },\n    \"leaderboard_bbh_penguins_in_a_table\"\
  : {\n        \"acc_norm,none\": 0.22602739726027396,\n        \"acc_norm_stderr,none\"\
  : 0.034734362688347384,\n        \"alias\": \"  - leaderboard_bbh_penguins_in_a_table\"\
  \n    },\n    \"leaderboard_bbh_reasoning_about_colored_objects\": {\n        \"\
  acc_norm,none\": 0.172,\n        \"acc_norm_stderr,none\": 0.023915513944486218,\n\
  \        \"alias\": \"  - leaderboard_bbh_reasoning_about_colored_objects\"\n  \
  \  },\n    \"leaderboard_bbh_ruin_names\": {\n        \"acc_norm,none\": 0.284,\n\
  \        \"acc_norm_stderr,none\": 0.02857695873043741,\n        \"alias\": \" \
  \ - leaderboard_bbh_ruin_names\"\n    },\n    \"leaderboard_bbh_salient_translation_error_detection\"\
  : {\n        \"acc_norm,none\": 0.22,\n        \"acc_norm_stderr,none\": 0.026251792824605845,\n\
  \        \"alias\": \"  - leaderboard_bbh_salient_translation_error_detection\"\n\
  \    },\n    \"leaderboard_bbh_snarks\": {\n        \"acc_norm,none\": 0.4157303370786517,\n\
  \        \"acc_norm_stderr,none\": 0.03704468395960965,\n        \"alias\": \" \
  \ - leaderboard_bbh_snarks\"\n    },\n    \"leaderboard_bbh_sports_understanding\"\
  : {\n        \"acc_norm,none\": 0.46,\n        \"acc_norm_stderr,none\": 0.031584653891499,\n\
  \        \"alias\": \"  - leaderboard_bbh_sports_understanding\"\n    },\n    \"\
  leaderboard_bbh_temporal_sequences\": {\n        \"acc_norm,none\": 0.268,\n   \
  \     \"acc_norm_stderr,none\": 0.02806876238252669,\n        \"alias\": \"  - leaderboard_bbh_temporal_sequences\"\
  \n    },\n    \"leaderboard_bbh_tracking_shuffled_objects_five_objects\": {\n  \
  \      \"acc_norm,none\": 0.172,\n        \"acc_norm_stderr,none\": 0.023915513944486218,\n\
  \        \"alias\": \"  - leaderboard_bbh_tracking_shuffled_objects_five_objects\"\
  \n    },\n    \"leaderboard_bbh_tracking_shuffled_objects_seven_objects\": {\n \
  \       \"acc_norm,none\": 0.132,\n        \"acc_norm_stderr,none\": 0.021450980824038124,\n\
  \        \"alias\": \"  - leaderboard_bbh_tracking_shuffled_objects_seven_objects\"\
  \n    },\n    \"leaderboard_bbh_tracking_shuffled_objects_three_objects\": {\n \
  \       \"acc_norm,none\": 0.324,\n        \"acc_norm_stderr,none\": 0.02965829492454557,\n\
  \        \"alias\": \"  - leaderboard_bbh_tracking_shuffled_objects_three_objects\"\
  \n    },\n    \"leaderboard_bbh_web_of_lies\": {\n        \"acc_norm,none\": 0.488,\n\
  \        \"acc_norm_stderr,none\": 0.03167708558254709,\n        \"alias\": \" \
  \ - leaderboard_bbh_web_of_lies\"\n    },\n    \"leaderboard_gpqa\": {\n       \
  \ \"acc_norm,none\": 0.24664429530201343,\n        \"acc_norm_stderr,none\": 0.012496674738288107,\n\
  \        \"alias\": \" - leaderboard_gpqa\"\n    },\n    \"leaderboard_gpqa_diamond\"\
  : {\n        \"acc_norm,none\": 0.25252525252525254,\n        \"acc_norm_stderr,none\"\
  : 0.030954055470365886,\n        \"alias\": \"  - leaderboard_gpqa_diamond\"\n \
  \   },\n    \"leaderboard_gpqa_extended\": {\n        \"acc_norm,none\": 0.2564102564102564,\n\
  \        \"acc_norm_stderr,none\": 0.018704070930965995,\n        \"alias\": \"\
  \  - leaderboard_gpqa_extended\"\n    },\n    \"leaderboard_gpqa_main\": {\n   \
  \     \"acc_norm,none\": 0.23214285714285715,\n        \"acc_norm_stderr,none\"\
  : 0.019969358575699175,\n        \"alias\": \"  - leaderboard_gpqa_main\"\n    },\n\
  \    \"leaderboard_ifeval\": {\n        \"prompt_level_strict_acc,none\": 0.18853974121996303,\n\
  \        \"prompt_level_strict_acc_stderr,none\": 0.016832096060176906,\n      \
  \  \"inst_level_strict_acc,none\": 0.3057553956834532,\n        \"inst_level_strict_acc_stderr,none\"\
  : \"N/A\",\n        \"prompt_level_loose_acc,none\": 0.19408502772643252,\n    \
  \    \"prompt_level_loose_acc_stderr,none\": 0.017019380550749422,\n        \"inst_level_loose_acc,none\"\
  : 0.31534772182254195,\n        \"inst_level_loose_acc_stderr,none\": \"N/A\",\n\
  \        \"alias\": \" - leaderboard_ifeval\"\n    },\n    \"leaderboard_math_hard\"\
  : {\n        \"exact_match,none\": 0.00906344410876133,\n        \"exact_match_stderr,none\"\
  : 0.002601527328160649,\n        \"alias\": \" - leaderboard_math_hard\"\n    },\n\
  \    \"leaderboard_math_algebra_hard\": {\n        \"exact_match,none\": 0.006514657980456026,\n\
  \        \"exact_match_stderr,none\": 0.004599025618546253,\n        \"alias\":\
  \ \"  - leaderboard_math_algebra_hard\"\n    },\n    \"leaderboard_math_counting_and_prob_hard\"\
  : {\n        \"exact_match,none\": 0.024390243902439025,\n        \"exact_match_stderr,none\"\
  : 0.013965813032045558,\n        \"alias\": \"  - leaderboard_math_counting_and_prob_hard\"\
  \n    },\n    \"leaderboard_math_geometry_hard\": {\n        \"exact_match,none\"\
  : 0.0,\n        \"exact_match_stderr,none\": 0.0,\n        \"alias\": \"  - leaderboard_math_geometry_hard\"\
  \n    },\n    \"leaderboard_math_intermediate_algebra_hard\": {\n        \"exact_match,none\"\
  : 0.0,\n        \"exact_match_stderr,none\": 0.0,\n        \"alias\": \"  - leaderboard_math_intermediate_algebra_hard\"\
  \n    },\n    \"leaderboard_math_num_theory_hard\": {\n        \"exact_match,none\"\
  : 0.01948051948051948,\n        \"exact_match_stderr,none\": 0.011173331005571076,\n\
  \        \"alias\": \"  - leaderboard_math_num_theory_hard\"\n    },\n    \"leaderboard_math_prealgebra_hard\"\
  : {\n        \"exact_match,none\": 0.015544041450777202,\n        \"exact_match_stderr,none\"\
  : 0.008927492715084343,\n        \"alias\": \"  - leaderboard_math_prealgebra_hard\"\
  \n    },\n    \"leaderboard_math_precalculus_hard\": {\n        \"exact_match,none\"\
  : 0.007407407407407408,\n        \"exact_match_stderr,none\": 0.007407407407407403,\n\
  \        \"alias\": \"  - leaderboard_math_precalculus_hard\"\n    },\n    \"leaderboard_mmlu_pro\"\
  : {\n        \"acc,none\": 0.11087101063829788,\n        \"acc_stderr,none\": 0.0028624672393866564,\n\
  \        \"alias\": \" - leaderboard_mmlu_pro\"\n    },\n    \"leaderboard_musr\"\
  : {\n        \"acc_norm,none\": 0.3637566137566138,\n        \"acc_norm_stderr,none\"\
  : 0.016983543757727832,\n        \"alias\": \" - leaderboard_musr\"\n    },\n  \
  \  \"leaderboard_musr_murder_mysteries\": {\n        \"acc_norm,none\": 0.528,\n\
  \        \"acc_norm_stderr,none\": 0.031636489531544396,\n        \"alias\": \"\
  \  - leaderboard_musr_murder_mysteries\"\n    },\n    \"leaderboard_musr_object_placements\"\
  : {\n        \"acc_norm,none\": 0.24609375,\n        \"acc_norm_stderr,none\": 0.026973597563786113,\n\
  \        \"alias\": \"  - leaderboard_musr_object_placements\"\n    },\n    \"leaderboard_musr_team_allocation\"\
  : {\n        \"acc_norm,none\": 0.32,\n        \"acc_norm_stderr,none\": 0.029561724955241037,\n\
  \        \"alias\": \"  - leaderboard_musr_team_allocation\"\n    }\n}\n```"
repo_url: https://huggingface.co/EleutherAI/pythia-12b
leaderboard_url: ''
point_of_contact: ''
configs:
- config_name: EleutherAI__pythia-12b__leaderboard_arc_challenge
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_arc_challenge_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_arc_challenge_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_bbh
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_bbh_boolean_expressions_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_causal_judgement_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_date_understanding_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_disambiguation_qa_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_formal_fallacies_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_geometric_shapes_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_hyperbaton_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_logical_deduction_five_objects_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_logical_deduction_seven_objects_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_logical_deduction_three_objects_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_movie_recommendation_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_navigate_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_object_counting_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_penguins_in_a_table_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_reasoning_about_colored_objects_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_ruin_names_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_salient_translation_error_detection_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_snarks_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_sports_understanding_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_temporal_sequences_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_five_objects_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_seven_objects_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_three_objects_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_web_of_lies_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_boolean_expressions_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_causal_judgement_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_date_understanding_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_disambiguation_qa_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_formal_fallacies_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_geometric_shapes_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_hyperbaton_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_logical_deduction_five_objects_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_logical_deduction_seven_objects_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_logical_deduction_three_objects_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_movie_recommendation_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_navigate_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_object_counting_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_penguins_in_a_table_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_reasoning_about_colored_objects_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_ruin_names_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_salient_translation_error_detection_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_snarks_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_sports_understanding_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_temporal_sequences_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_five_objects_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_seven_objects_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_three_objects_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_bbh_web_of_lies_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_bbh_boolean_expressions
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_bbh_boolean_expressions_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_boolean_expressions_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_bbh_causal_judgement
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_bbh_causal_judgement_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_causal_judgement_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_bbh_date_understanding
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_bbh_date_understanding_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_date_understanding_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_bbh_disambiguation_qa
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_bbh_disambiguation_qa_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_disambiguation_qa_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_bbh_formal_fallacies
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_bbh_formal_fallacies_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_formal_fallacies_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_bbh_geometric_shapes
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_bbh_geometric_shapes_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_geometric_shapes_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_bbh_hyperbaton
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_bbh_hyperbaton_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_hyperbaton_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_bbh_logical_deduction_five_objects
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_bbh_logical_deduction_five_objects_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_logical_deduction_five_objects_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_bbh_logical_deduction_seven_objects
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_bbh_logical_deduction_seven_objects_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_logical_deduction_seven_objects_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_bbh_logical_deduction_three_objects
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_bbh_logical_deduction_three_objects_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_logical_deduction_three_objects_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_bbh_movie_recommendation
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_bbh_movie_recommendation_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_movie_recommendation_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_bbh_navigate
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_bbh_navigate_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_navigate_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_bbh_object_counting
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_bbh_object_counting_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_object_counting_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_bbh_penguins_in_a_table
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_bbh_penguins_in_a_table_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_penguins_in_a_table_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_bbh_reasoning_about_colored_objects
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_bbh_reasoning_about_colored_objects_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_reasoning_about_colored_objects_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_bbh_ruin_names
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_bbh_ruin_names_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_ruin_names_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_bbh_salient_translation_error_detection
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_bbh_salient_translation_error_detection_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_salient_translation_error_detection_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_bbh_snarks
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_bbh_snarks_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_snarks_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_bbh_sports_understanding
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_bbh_sports_understanding_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_sports_understanding_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_bbh_temporal_sequences
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_bbh_temporal_sequences_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_temporal_sequences_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_bbh_tracking_shuffled_objects_five_objects
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_five_objects_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_five_objects_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_bbh_tracking_shuffled_objects_seven_objects
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_seven_objects_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_seven_objects_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_bbh_tracking_shuffled_objects_three_objects
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_three_objects_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_three_objects_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_bbh_web_of_lies
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_bbh_web_of_lies_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_web_of_lies_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_gpqa
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_gpqa_diamond_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_gpqa_extended_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_gpqa_main_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_gpqa_diamond_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_gpqa_extended_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_gpqa_main_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_gpqa_diamond
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_gpqa_diamond_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_gpqa_diamond_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_gpqa_extended
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_gpqa_extended_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_gpqa_extended_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_gpqa_main
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_gpqa_main_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_gpqa_main_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_ifeval
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_ifeval_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_ifeval_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_math
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_math_algebra_hard_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_math_counting_and_prob_hard_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_math_geometry_hard_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_math_intermediate_algebra_hard_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_math_num_theory_hard_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_math_prealgebra_hard_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_math_precalculus_hard_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_math_algebra_hard_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_math_counting_and_prob_hard_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_math_geometry_hard_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_math_intermediate_algebra_hard_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_math_num_theory_hard_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_math_prealgebra_hard_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_math_precalculus_hard_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_math_algebra_hard
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_math_algebra_hard_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_math_algebra_hard_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_math_counting_and_prob_hard
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_math_counting_and_prob_hard_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_math_counting_and_prob_hard_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_math_geometry_hard
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_math_geometry_hard_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_math_geometry_hard_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_math_intermediate_algebra_hard
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_math_intermediate_algebra_hard_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_math_intermediate_algebra_hard_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_math_num_theory_hard
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_math_num_theory_hard_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_math_num_theory_hard_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_math_prealgebra_hard
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_math_prealgebra_hard_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_math_prealgebra_hard_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_math_precalculus_hard
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_math_precalculus_hard_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_math_precalculus_hard_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_mmlu_pro
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_mmlu_pro_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_mmlu_pro_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_musr
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_musr_murder_mysteries_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_musr_object_placements_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_musr_team_allocation_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_musr_murder_mysteries_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_musr_object_placements_2024-06-17T17-37-25.144953.json'
    - '**/samples_leaderboard_musr_team_allocation_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_musr_murder_mysteries
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_musr_murder_mysteries_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_musr_murder_mysteries_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_musr_object_placements
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_musr_object_placements_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_musr_object_placements_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__leaderboard_musr_team_allocation
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/samples_leaderboard_musr_team_allocation_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/samples_leaderboard_musr_team_allocation_2024-06-17T17-37-25.144953.json'
- config_name: EleutherAI__pythia-12b__results
  data_files:
  - split: 2024_06_17T17_37_25.144953
    path:
    - '**/results_2024-06-17T17-37-25.144953.json'
  - split: latest
    path:
    - '**/results_2024-06-17T17-37-25.144953.json'
---

# Dataset Card for Evaluation run of EleutherAI/pythia-12b

<!-- Provide a quick summary of the dataset. -->

Dataset automatically created during the evaluation run of model [EleutherAI/pythia-12b](https://huggingface.co/EleutherAI/pythia-12b)
The dataset is composed of 44 configuration(s), each one corresponding to one of the evaluated task.

The dataset has been created from 1 run(s). Each run can be found as a specific split in each configuration, the split being named using the timestamp of the run.The "train" split is always pointing to the latest results.

An additional configuration "results" store all the aggregated results of the run.

To load the details from a run, you can for instance do the following:
```python
from datasets import load_dataset
data = load_dataset(
	"HuggingFaceEvalInternal/EleutherAI__pythia-12b-details-private",
	name="EleutherAI__pythia-12b__leaderboard_arc_challenge",
	split="latest"
)
```

## Latest results

These are the [latest results from run 2024-06-17T17-37-25.144953](https://huggingface.co/datasets/HuggingFaceEvalInternal/EleutherAI__pythia-12b-details-private/blob/main/EleutherAI__pythia-12b/results_2024-06-17T17-37-25.144953.json) (note that there might be results for other tasks in the repos if successive evals didn't cover the same tasks. You find each in the results and the "latest" split for each eval):

```python
{
    "all": {
        "leaderboard": {
            "inst_level_loose_acc,none": 0.31534772182254195,
            "inst_level_loose_acc_stderr,none": "N/A",
            "acc_norm,none": 0.3224862065082761,
            "acc_norm_stderr,none": 0.004769106493523972,
            "prompt_level_strict_acc,none": 0.18853974121996303,
            "prompt_level_strict_acc_stderr,none": 0.016832096060176906,
            "acc,none": 0.13382308391396547,
            "acc_stderr,none": 0.002893167355275893,
            "prompt_level_loose_acc,none": 0.19408502772643252,
            "prompt_level_loose_acc_stderr,none": 0.017019380550749422,
            "inst_level_strict_acc,none": 0.3057553956834532,
            "inst_level_strict_acc_stderr,none": "N/A",
            "exact_match,none": 0.00906344410876133,
            "exact_match_stderr,none": 0.002601527328160649,
            "alias": "leaderboard"
        },
        "leaderboard_arc_challenge": {
            "acc,none": 0.36945392491467577,
            "acc_stderr,none": 0.01410457836649191,
            "acc_norm,none": 0.4044368600682594,
            "acc_norm_stderr,none": 0.014342036483436172,
            "alias": " - leaderboard_arc_challenge"
        },
        "leaderboard_bbh": {
            "acc_norm,none": 0.31609095643117513,
            "acc_norm_stderr,none": 0.005821168127128767,
            "alias": " - leaderboard_bbh"
        },
        "leaderboard_bbh_boolean_expressions": {
            "acc_norm,none": 0.668,
            "acc_norm_stderr,none": 0.029844039047465902,
            "alias": "  - leaderboard_bbh_boolean_expressions"
        },
        "leaderboard_bbh_causal_judgement": {
            "acc_norm,none": 0.5294117647058824,
            "acc_norm_stderr,none": 0.03659829510813268,
            "alias": "  - leaderboard_bbh_causal_judgement"
        },
        "leaderboard_bbh_date_understanding": {
            "acc_norm,none": 0.16,
            "acc_norm_stderr,none": 0.02323271478206065,
            "alias": "  - leaderboard_bbh_date_understanding"
        },
        "leaderboard_bbh_disambiguation_qa": {
            "acc_norm,none": 0.336,
            "acc_norm_stderr,none": 0.029933259094191516,
            "alias": "  - leaderboard_bbh_disambiguation_qa"
        },
        "leaderboard_bbh_formal_fallacies": {
            "acc_norm,none": 0.476,
            "acc_norm_stderr,none": 0.03164968895968782,
            "alias": "  - leaderboard_bbh_formal_fallacies"
        },
        "leaderboard_bbh_geometric_shapes": {
            "acc_norm,none": 0.104,
            "acc_norm_stderr,none": 0.019345100974843887,
            "alias": "  - leaderboard_bbh_geometric_shapes"
        },
        "leaderboard_bbh_hyperbaton": {
            "acc_norm,none": 0.484,
            "acc_norm_stderr,none": 0.031669985030107414,
            "alias": "  - leaderboard_bbh_hyperbaton"
        },
        "leaderboard_bbh_logical_deduction_five_objects": {
            "acc_norm,none": 0.192,
            "acc_norm_stderr,none": 0.024960691989172005,
            "alias": "  - leaderboard_bbh_logical_deduction_five_objects"
        },
        "leaderboard_bbh_logical_deduction_seven_objects": {
            "acc_norm,none": 0.148,
            "acc_norm_stderr,none": 0.022503547243806137,
            "alias": "  - leaderboard_bbh_logical_deduction_seven_objects"
        },
        "leaderboard_bbh_logical_deduction_three_objects": {
            "acc_norm,none": 0.344,
            "acc_norm_stderr,none": 0.030104503392316392,
            "alias": "  - leaderboard_bbh_logical_deduction_three_objects"
        },
        "leaderboard_bbh_movie_recommendation": {
            "acc_norm,none": 0.288,
            "acc_norm_stderr,none": 0.028697004587398225,
            "alias": "  - leaderboard_bbh_movie_recommendation"
        },
        "leaderboard_bbh_navigate": {
            "acc_norm,none": 0.468,
            "acc_norm_stderr,none": 0.031621252575725504,
            "alias": "  - leaderboard_bbh_navigate"
        },
        "leaderboard_bbh_object_counting": {
            "acc_norm,none": 0.272,
            "acc_norm_stderr,none": 0.028200088296310016,
            "alias": "  - leaderboard_bbh_object_counting"
        },
        "leaderboard_bbh_penguins_in_a_table": {
            "acc_norm,none": 0.22602739726027396,
            "acc_norm_stderr,none": 0.034734362688347384,
            "alias": "  - leaderboard_bbh_penguins_in_a_table"
        },
        "leaderboard_bbh_reasoning_about_colored_objects": {
            "acc_norm,none": 0.172,
            "acc_norm_stderr,none": 0.023915513944486218,
            "alias": "  - leaderboard_bbh_reasoning_about_colored_objects"
        },
        "leaderboard_bbh_ruin_names": {
            "acc_norm,none": 0.284,
            "acc_norm_stderr,none": 0.02857695873043741,
            "alias": "  - leaderboard_bbh_ruin_names"
        },
        "leaderboard_bbh_salient_translation_error_detection": {
            "acc_norm,none": 0.22,
            "acc_norm_stderr,none": 0.026251792824605845,
            "alias": "  - leaderboard_bbh_salient_translation_error_detection"
        },
        "leaderboard_bbh_snarks": {
            "acc_norm,none": 0.4157303370786517,
            "acc_norm_stderr,none": 0.03704468395960965,
            "alias": "  - leaderboard_bbh_snarks"
        },
        "leaderboard_bbh_sports_understanding": {
            "acc_norm,none": 0.46,
            "acc_norm_stderr,none": 0.031584653891499,
            "alias": "  - leaderboard_bbh_sports_understanding"
        },
        "leaderboard_bbh_temporal_sequences": {
            "acc_norm,none": 0.268,
            "acc_norm_stderr,none": 0.02806876238252669,
            "alias": "  - leaderboard_bbh_temporal_sequences"
        },
        "leaderboard_bbh_tracking_shuffled_objects_five_objects": {
            "acc_norm,none": 0.172,
            "acc_norm_stderr,none": 0.023915513944486218,
            "alias": "  - leaderboard_bbh_tracking_shuffled_objects_five_objects"
        },
        "leaderboard_bbh_tracking_shuffled_objects_seven_objects": {
            "acc_norm,none": 0.132,
            "acc_norm_stderr,none": 0.021450980824038124,
            "alias": "  - leaderboard_bbh_tracking_shuffled_objects_seven_objects"
        },
        "leaderboard_bbh_tracking_shuffled_objects_three_objects": {
            "acc_norm,none": 0.324,
            "acc_norm_stderr,none": 0.02965829492454557,
            "alias": "  - leaderboard_bbh_tracking_shuffled_objects_three_objects"
        },
        "leaderboard_bbh_web_of_lies": {
            "acc_norm,none": 0.488,
            "acc_norm_stderr,none": 0.03167708558254709,
            "alias": "  - leaderboard_bbh_web_of_lies"
        },
        "leaderboard_gpqa": {
            "acc_norm,none": 0.24664429530201343,
            "acc_norm_stderr,none": 0.012496674738288107,
            "alias": " - leaderboard_gpqa"
        },
        "leaderboard_gpqa_diamond": {
            "acc_norm,none": 0.25252525252525254,
            "acc_norm_stderr,none": 0.030954055470365886,
            "alias": "  - leaderboard_gpqa_diamond"
        },
        "leaderboard_gpqa_extended": {
            "acc_norm,none": 0.2564102564102564,
            "acc_norm_stderr,none": 0.018704070930965995,
            "alias": "  - leaderboard_gpqa_extended"
        },
        "leaderboard_gpqa_main": {
            "acc_norm,none": 0.23214285714285715,
            "acc_norm_stderr,none": 0.019969358575699175,
            "alias": "  - leaderboard_gpqa_main"
        },
        "leaderboard_ifeval": {
            "prompt_level_strict_acc,none": 0.18853974121996303,
            "prompt_level_strict_acc_stderr,none": 0.016832096060176906,
            "inst_level_strict_acc,none": 0.3057553956834532,
            "inst_level_strict_acc_stderr,none": "N/A",
            "prompt_level_loose_acc,none": 0.19408502772643252,
            "prompt_level_loose_acc_stderr,none": 0.017019380550749422,
            "inst_level_loose_acc,none": 0.31534772182254195,
            "inst_level_loose_acc_stderr,none": "N/A",
            "alias": " - leaderboard_ifeval"
        },
        "leaderboard_math_hard": {
            "exact_match,none": 0.00906344410876133,
            "exact_match_stderr,none": 0.002601527328160649,
            "alias": " - leaderboard_math_hard"
        },
        "leaderboard_math_algebra_hard": {
            "exact_match,none": 0.006514657980456026,
            "exact_match_stderr,none": 0.004599025618546253,
            "alias": "  - leaderboard_math_algebra_hard"
        },
        "leaderboard_math_counting_and_prob_hard": {
            "exact_match,none": 0.024390243902439025,
            "exact_match_stderr,none": 0.013965813032045558,
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
            "exact_match,none": 0.01948051948051948,
            "exact_match_stderr,none": 0.011173331005571076,
            "alias": "  - leaderboard_math_num_theory_hard"
        },
        "leaderboard_math_prealgebra_hard": {
            "exact_match,none": 0.015544041450777202,
            "exact_match_stderr,none": 0.008927492715084343,
            "alias": "  - leaderboard_math_prealgebra_hard"
        },
        "leaderboard_math_precalculus_hard": {
            "exact_match,none": 0.007407407407407408,
            "exact_match_stderr,none": 0.007407407407407403,
            "alias": "  - leaderboard_math_precalculus_hard"
        },
        "leaderboard_mmlu_pro": {
            "acc,none": 0.11087101063829788,
            "acc_stderr,none": 0.0028624672393866564,
            "alias": " - leaderboard_mmlu_pro"
        },
        "leaderboard_musr": {
            "acc_norm,none": 0.3637566137566138,
            "acc_norm_stderr,none": 0.016983543757727832,
            "alias": " - leaderboard_musr"
        },
        "leaderboard_musr_murder_mysteries": {
            "acc_norm,none": 0.528,
            "acc_norm_stderr,none": 0.031636489531544396,
            "alias": "  - leaderboard_musr_murder_mysteries"
        },
        "leaderboard_musr_object_placements": {
            "acc_norm,none": 0.24609375,
            "acc_norm_stderr,none": 0.026973597563786113,
            "alias": "  - leaderboard_musr_object_placements"
        },
        "leaderboard_musr_team_allocation": {
            "acc_norm,none": 0.32,
            "acc_norm_stderr,none": 0.029561724955241037,
            "alias": "  - leaderboard_musr_team_allocation"
        }
    },
    "leaderboard": {
        "inst_level_loose_acc,none": 0.31534772182254195,
        "inst_level_loose_acc_stderr,none": "N/A",
        "acc_norm,none": 0.3224862065082761,
        "acc_norm_stderr,none": 0.004769106493523972,
        "prompt_level_strict_acc,none": 0.18853974121996303,
        "prompt_level_strict_acc_stderr,none": 0.016832096060176906,
        "acc,none": 0.13382308391396547,
        "acc_stderr,none": 0.002893167355275893,
        "prompt_level_loose_acc,none": 0.19408502772643252,
        "prompt_level_loose_acc_stderr,none": 0.017019380550749422,
        "inst_level_strict_acc,none": 0.3057553956834532,
        "inst_level_strict_acc_stderr,none": "N/A",
        "exact_match,none": 0.00906344410876133,
        "exact_match_stderr,none": 0.002601527328160649,
        "alias": "leaderboard"
    },
    "leaderboard_arc_challenge": {
        "acc,none": 0.36945392491467577,
        "acc_stderr,none": 0.01410457836649191,
        "acc_norm,none": 0.4044368600682594,
        "acc_norm_stderr,none": 0.014342036483436172,
        "alias": " - leaderboard_arc_challenge"
    },
    "leaderboard_bbh": {
        "acc_norm,none": 0.31609095643117513,
        "acc_norm_stderr,none": 0.005821168127128767,
        "alias": " - leaderboard_bbh"
    },
    "leaderboard_bbh_boolean_expressions": {
        "acc_norm,none": 0.668,
        "acc_norm_stderr,none": 0.029844039047465902,
        "alias": "  - leaderboard_bbh_boolean_expressions"
    },
    "leaderboard_bbh_causal_judgement": {
        "acc_norm,none": 0.5294117647058824,
        "acc_norm_stderr,none": 0.03659829510813268,
        "alias": "  - leaderboard_bbh_causal_judgement"
    },
    "leaderboard_bbh_date_understanding": {
        "acc_norm,none": 0.16,
        "acc_norm_stderr,none": 0.02323271478206065,
        "alias": "  - leaderboard_bbh_date_understanding"
    },
    "leaderboard_bbh_disambiguation_qa": {
        "acc_norm,none": 0.336,
        "acc_norm_stderr,none": 0.029933259094191516,
        "alias": "  - leaderboard_bbh_disambiguation_qa"
    },
    "leaderboard_bbh_formal_fallacies": {
        "acc_norm,none": 0.476,
        "acc_norm_stderr,none": 0.03164968895968782,
        "alias": "  - leaderboard_bbh_formal_fallacies"
    },
    "leaderboard_bbh_geometric_shapes": {
        "acc_norm,none": 0.104,
        "acc_norm_stderr,none": 0.019345100974843887,
        "alias": "  - leaderboard_bbh_geometric_shapes"
    },
    "leaderboard_bbh_hyperbaton": {
        "acc_norm,none": 0.484,
        "acc_norm_stderr,none": 0.031669985030107414,
        "alias": "  - leaderboard_bbh_hyperbaton"
    },
    "leaderboard_bbh_logical_deduction_five_objects": {
        "acc_norm,none": 0.192,
        "acc_norm_stderr,none": 0.024960691989172005,
        "alias": "  - leaderboard_bbh_logical_deduction_five_objects"
    },
    "leaderboard_bbh_logical_deduction_seven_objects": {
        "acc_norm,none": 0.148,
        "acc_norm_stderr,none": 0.022503547243806137,
        "alias": "  - leaderboard_bbh_logical_deduction_seven_objects"
    },
    "leaderboard_bbh_logical_deduction_three_objects": {
        "acc_norm,none": 0.344,
        "acc_norm_stderr,none": 0.030104503392316392,
        "alias": "  - leaderboard_bbh_logical_deduction_three_objects"
    },
    "leaderboard_bbh_movie_recommendation": {
        "acc_norm,none": 0.288,
        "acc_norm_stderr,none": 0.028697004587398225,
        "alias": "  - leaderboard_bbh_movie_recommendation"
    },
    "leaderboard_bbh_navigate": {
        "acc_norm,none": 0.468,
        "acc_norm_stderr,none": 0.031621252575725504,
        "alias": "  - leaderboard_bbh_navigate"
    },
    "leaderboard_bbh_object_counting": {
        "acc_norm,none": 0.272,
        "acc_norm_stderr,none": 0.028200088296310016,
        "alias": "  - leaderboard_bbh_object_counting"
    },
    "leaderboard_bbh_penguins_in_a_table": {
        "acc_norm,none": 0.22602739726027396,
        "acc_norm_stderr,none": 0.034734362688347384,
        "alias": "  - leaderboard_bbh_penguins_in_a_table"
    },
    "leaderboard_bbh_reasoning_about_colored_objects": {
        "acc_norm,none": 0.172,
        "acc_norm_stderr,none": 0.023915513944486218,
        "alias": "  - leaderboard_bbh_reasoning_about_colored_objects"
    },
    "leaderboard_bbh_ruin_names": {
        "acc_norm,none": 0.284,
        "acc_norm_stderr,none": 0.02857695873043741,
        "alias": "  - leaderboard_bbh_ruin_names"
    },
    "leaderboard_bbh_salient_translation_error_detection": {
        "acc_norm,none": 0.22,
        "acc_norm_stderr,none": 0.026251792824605845,
        "alias": "  - leaderboard_bbh_salient_translation_error_detection"
    },
    "leaderboard_bbh_snarks": {
        "acc_norm,none": 0.4157303370786517,
        "acc_norm_stderr,none": 0.03704468395960965,
        "alias": "  - leaderboard_bbh_snarks"
    },
    "leaderboard_bbh_sports_understanding": {
        "acc_norm,none": 0.46,
        "acc_norm_stderr,none": 0.031584653891499,
        "alias": "  - leaderboard_bbh_sports_understanding"
    },
    "leaderboard_bbh_temporal_sequences": {
        "acc_norm,none": 0.268,
        "acc_norm_stderr,none": 0.02806876238252669,
        "alias": "  - leaderboard_bbh_temporal_sequences"
    },
    "leaderboard_bbh_tracking_shuffled_objects_five_objects": {
        "acc_norm,none": 0.172,
        "acc_norm_stderr,none": 0.023915513944486218,
        "alias": "  - leaderboard_bbh_tracking_shuffled_objects_five_objects"
    },
    "leaderboard_bbh_tracking_shuffled_objects_seven_objects": {
        "acc_norm,none": 0.132,
        "acc_norm_stderr,none": 0.021450980824038124,
        "alias": "  - leaderboard_bbh_tracking_shuffled_objects_seven_objects"
    },
    "leaderboard_bbh_tracking_shuffled_objects_three_objects": {
        "acc_norm,none": 0.324,
        "acc_norm_stderr,none": 0.02965829492454557,
        "alias": "  - leaderboard_bbh_tracking_shuffled_objects_three_objects"
    },
    "leaderboard_bbh_web_of_lies": {
        "acc_norm,none": 0.488,
        "acc_norm_stderr,none": 0.03167708558254709,
        "alias": "  - leaderboard_bbh_web_of_lies"
    },
    "leaderboard_gpqa": {
        "acc_norm,none": 0.24664429530201343,
        "acc_norm_stderr,none": 0.012496674738288107,
        "alias": " - leaderboard_gpqa"
    },
    "leaderboard_gpqa_diamond": {
        "acc_norm,none": 0.25252525252525254,
        "acc_norm_stderr,none": 0.030954055470365886,
        "alias": "  - leaderboard_gpqa_diamond"
    },
    "leaderboard_gpqa_extended": {
        "acc_norm,none": 0.2564102564102564,
        "acc_norm_stderr,none": 0.018704070930965995,
        "alias": "  - leaderboard_gpqa_extended"
    },
    "leaderboard_gpqa_main": {
        "acc_norm,none": 0.23214285714285715,
        "acc_norm_stderr,none": 0.019969358575699175,
        "alias": "  - leaderboard_gpqa_main"
    },
    "leaderboard_ifeval": {
        "prompt_level_strict_acc,none": 0.18853974121996303,
        "prompt_level_strict_acc_stderr,none": 0.016832096060176906,
        "inst_level_strict_acc,none": 0.3057553956834532,
        "inst_level_strict_acc_stderr,none": "N/A",
        "prompt_level_loose_acc,none": 0.19408502772643252,
        "prompt_level_loose_acc_stderr,none": 0.017019380550749422,
        "inst_level_loose_acc,none": 0.31534772182254195,
        "inst_level_loose_acc_stderr,none": "N/A",
        "alias": " - leaderboard_ifeval"
    },
    "leaderboard_math_hard": {
        "exact_match,none": 0.00906344410876133,
        "exact_match_stderr,none": 0.002601527328160649,
        "alias": " - leaderboard_math_hard"
    },
    "leaderboard_math_algebra_hard": {
        "exact_match,none": 0.006514657980456026,
        "exact_match_stderr,none": 0.004599025618546253,
        "alias": "  - leaderboard_math_algebra_hard"
    },
    "leaderboard_math_counting_and_prob_hard": {
        "exact_match,none": 0.024390243902439025,
        "exact_match_stderr,none": 0.013965813032045558,
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
        "exact_match,none": 0.01948051948051948,
        "exact_match_stderr,none": 0.011173331005571076,
        "alias": "  - leaderboard_math_num_theory_hard"
    },
    "leaderboard_math_prealgebra_hard": {
        "exact_match,none": 0.015544041450777202,
        "exact_match_stderr,none": 0.008927492715084343,
        "alias": "  - leaderboard_math_prealgebra_hard"
    },
    "leaderboard_math_precalculus_hard": {
        "exact_match,none": 0.007407407407407408,
        "exact_match_stderr,none": 0.007407407407407403,
        "alias": "  - leaderboard_math_precalculus_hard"
    },
    "leaderboard_mmlu_pro": {
        "acc,none": 0.11087101063829788,
        "acc_stderr,none": 0.0028624672393866564,
        "alias": " - leaderboard_mmlu_pro"
    },
    "leaderboard_musr": {
        "acc_norm,none": 0.3637566137566138,
        "acc_norm_stderr,none": 0.016983543757727832,
        "alias": " - leaderboard_musr"
    },
    "leaderboard_musr_murder_mysteries": {
        "acc_norm,none": 0.528,
        "acc_norm_stderr,none": 0.031636489531544396,
        "alias": "  - leaderboard_musr_murder_mysteries"
    },
    "leaderboard_musr_object_placements": {
        "acc_norm,none": 0.24609375,
        "acc_norm_stderr,none": 0.026973597563786113,
        "alias": "  - leaderboard_musr_object_placements"
    },
    "leaderboard_musr_team_allocation": {
        "acc_norm,none": 0.32,
        "acc_norm_stderr,none": 0.029561724955241037,
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