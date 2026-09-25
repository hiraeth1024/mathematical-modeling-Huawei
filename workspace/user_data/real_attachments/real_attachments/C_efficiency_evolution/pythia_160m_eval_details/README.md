---
pretty_name: Evaluation run of EleutherAI/pythia-160m
dataset_summary: "Dataset automatically created during the evaluation run of model\
  \ [EleutherAI/pythia-160m](https://huggingface.co/EleutherAI/pythia-160m)\nThe dataset\
  \ is composed of 44 configuration(s), each one corresponding to one of the evaluated\
  \ task.\n\nThe dataset has been created from 2 run(s). Each run can be found as\
  \ a specific split in each configuration, the split being named using the timestamp\
  \ of the run.The \"train\" split is always pointing to the latest results.\n\nAn\
  \ additional configuration \"results\" store all the aggregated results of the run.\n\
  \nTo load the details from a run, you can for instance do the following:\n```python\n\
  from datasets import load_dataset\ndata = load_dataset(\n\t\"HuggingFaceEvalInternal/EleutherAI__pythia-160m-details-private\"\
  ,\n\tname=\"EleutherAI__pythia-160m__leaderboard_arc_challenge\",\n\tsplit=\"latest\"\
  \n)\n```\n\n## Latest results\n\nThese are the [latest results from run 2024-06-16T22-09-58.078705](https://huggingface.co/datasets/HuggingFaceEvalInternal/EleutherAI__pythia-160m-details-private/blob/main/EleutherAI__pythia-160m/results_2024-06-16T22-09-58.078705.json)\
  \ (note that there might be results for other tasks in the repos if successive evals\
  \ didn't cover the same tasks. You find each in the results and the \"latest\" split\
  \ for each eval):\n\n```python\n{\n    \"all\": {\n        \"leaderboard\": {\n\
  \            \"acc,none\": 0.11852468948803394,\n            \"acc_stderr,none\"\
  : 0.0028071506622770566,\n            \"prompt_level_strict_acc,none\": 0.1256931608133087,\n\
  \            \"prompt_level_strict_acc_stderr,none\": 0.01426562756717386,\n   \
  \         \"inst_level_strict_acc,none\": 0.23741007194244604,\n            \"inst_level_strict_acc_stderr,none\"\
  : \"N/A\",\n            \"acc_norm,none\": 0.2900574259655444,\n            \"acc_norm_stderr,none\"\
  : 0.004602123282554274,\n            \"prompt_level_loose_acc,none\": 0.12754158964879853,\n\
  \            \"prompt_level_loose_acc_stderr,none\": 0.014354940597336784,\n   \
  \         \"inst_level_loose_acc,none\": 0.2410071942446043,\n            \"inst_level_loose_acc_stderr,none\"\
  : \"N/A\",\n            \"exact_match,none\": 0.0022658610271903325,\n         \
  \   \"exact_match_stderr,none\": 0.001308399052935896,\n            \"alias\": \"\
  leaderboard\"\n        },\n        \"leaderboard_arc_challenge\": {\n          \
  \  \"acc,none\": 0.18600682593856654,\n            \"acc_stderr,none\": 0.011370940183266705,\n\
  \            \"acc_norm,none\": 0.2235494880546075,\n            \"acc_norm_stderr,none\"\
  : 0.01217489663120261,\n            \"alias\": \" - leaderboard_arc_challenge\"\n\
  \        },\n        \"leaderboard_bbh\": {\n            \"acc_norm,none\": 0.29352542961291445,\n\
  \            \"acc_norm_stderr,none\": 0.005660292699355036,\n            \"alias\"\
  : \" - leaderboard_bbh\"\n        },\n        \"leaderboard_bbh_boolean_expressions\"\
  : {\n            \"acc_norm,none\": 0.44,\n            \"acc_norm_stderr,none\"\
  : 0.03145724452223573,\n            \"alias\": \"  - leaderboard_bbh_boolean_expressions\"\
  \n        },\n        \"leaderboard_bbh_causal_judgement\": {\n            \"acc_norm,none\"\
  : 0.5187165775401069,\n            \"acc_norm_stderr,none\": 0.03663608375537842,\n\
  \            \"alias\": \"  - leaderboard_bbh_causal_judgement\"\n        },\n \
  \       \"leaderboard_bbh_date_understanding\": {\n            \"acc_norm,none\"\
  : 0.2,\n            \"acc_norm_stderr,none\": 0.02534897002097908,\n           \
  \ \"alias\": \"  - leaderboard_bbh_date_understanding\"\n        },\n        \"\
  leaderboard_bbh_disambiguation_qa\": {\n            \"acc_norm,none\": 0.336,\n\
  \            \"acc_norm_stderr,none\": 0.029933259094191516,\n            \"alias\"\
  : \"  - leaderboard_bbh_disambiguation_qa\"\n        },\n        \"leaderboard_bbh_formal_fallacies\"\
  : {\n            \"acc_norm,none\": 0.532,\n            \"acc_norm_stderr,none\"\
  : 0.031621252575725504,\n            \"alias\": \"  - leaderboard_bbh_formal_fallacies\"\
  \n        },\n        \"leaderboard_bbh_geometric_shapes\": {\n            \"acc_norm,none\"\
  : 0.084,\n            \"acc_norm_stderr,none\": 0.01757873852677636,\n         \
  \   \"alias\": \"  - leaderboard_bbh_geometric_shapes\"\n        },\n        \"\
  leaderboard_bbh_hyperbaton\": {\n            \"acc_norm,none\": 0.484,\n       \
  \     \"acc_norm_stderr,none\": 0.031669985030107414,\n            \"alias\": \"\
  \  - leaderboard_bbh_hyperbaton\"\n        },\n        \"leaderboard_bbh_logical_deduction_five_objects\"\
  : {\n            \"acc_norm,none\": 0.184,\n            \"acc_norm_stderr,none\"\
  : 0.02455581299422256,\n            \"alias\": \"  - leaderboard_bbh_logical_deduction_five_objects\"\
  \n        },\n        \"leaderboard_bbh_logical_deduction_seven_objects\": {\n \
  \           \"acc_norm,none\": 0.192,\n            \"acc_norm_stderr,none\": 0.024960691989172015,\n\
  \            \"alias\": \"  - leaderboard_bbh_logical_deduction_seven_objects\"\n\
  \        },\n        \"leaderboard_bbh_logical_deduction_three_objects\": {\n  \
  \          \"acc_norm,none\": 0.328,\n            \"acc_norm_stderr,none\": 0.029752391824475363,\n\
  \            \"alias\": \"  - leaderboard_bbh_logical_deduction_three_objects\"\n\
  \        },\n        \"leaderboard_bbh_movie_recommendation\": {\n            \"\
  acc_norm,none\": 0.18,\n            \"acc_norm_stderr,none\": 0.024346890650293523,\n\
  \            \"alias\": \"  - leaderboard_bbh_movie_recommendation\"\n        },\n\
  \        \"leaderboard_bbh_navigate\": {\n            \"acc_norm,none\": 0.452,\n\
  \            \"acc_norm_stderr,none\": 0.03153986449255662,\n            \"alias\"\
  : \"  - leaderboard_bbh_navigate\"\n        },\n        \"leaderboard_bbh_object_counting\"\
  : {\n            \"acc_norm,none\": 0.076,\n            \"acc_norm_stderr,none\"\
  : 0.016793573067859627,\n            \"alias\": \"  - leaderboard_bbh_object_counting\"\
  \n        },\n        \"leaderboard_bbh_penguins_in_a_table\": {\n            \"\
  acc_norm,none\": 0.2054794520547945,\n            \"acc_norm_stderr,none\": 0.033554654010728435,\n\
  \            \"alias\": \"  - leaderboard_bbh_penguins_in_a_table\"\n        },\n\
  \        \"leaderboard_bbh_reasoning_about_colored_objects\": {\n            \"\
  acc_norm,none\": 0.108,\n            \"acc_norm_stderr,none\": 0.01966955938156875,\n\
  \            \"alias\": \"  - leaderboard_bbh_reasoning_about_colored_objects\"\n\
  \        },\n        \"leaderboard_bbh_ruin_names\": {\n            \"acc_norm,none\"\
  : 0.216,\n            \"acc_norm_stderr,none\": 0.02607865766373273,\n         \
  \   \"alias\": \"  - leaderboard_bbh_ruin_names\"\n        },\n        \"leaderboard_bbh_salient_translation_error_detection\"\
  : {\n            \"acc_norm,none\": 0.144,\n            \"acc_norm_stderr,none\"\
  : 0.022249407735450207,\n            \"alias\": \"  - leaderboard_bbh_salient_translation_error_detection\"\
  \n        },\n        \"leaderboard_bbh_snarks\": {\n            \"acc_norm,none\"\
  : 0.5168539325842697,\n            \"acc_norm_stderr,none\": 0.037560944447344834,\n\
  \            \"alias\": \"  - leaderboard_bbh_snarks\"\n        },\n        \"leaderboard_bbh_sports_understanding\"\
  : {\n            \"acc_norm,none\": 0.46,\n            \"acc_norm_stderr,none\"\
  : 0.031584653891499,\n            \"alias\": \"  - leaderboard_bbh_sports_understanding\"\
  \n        },\n        \"leaderboard_bbh_temporal_sequences\": {\n            \"\
  acc_norm,none\": 0.28,\n            \"acc_norm_stderr,none\": 0.028454148277832315,\n\
  \            \"alias\": \"  - leaderboard_bbh_temporal_sequences\"\n        },\n\
  \        \"leaderboard_bbh_tracking_shuffled_objects_five_objects\": {\n       \
  \     \"acc_norm,none\": 0.22,\n            \"acc_norm_stderr,none\": 0.02625179282460584,\n\
  \            \"alias\": \"  - leaderboard_bbh_tracking_shuffled_objects_five_objects\"\
  \n        },\n        \"leaderboard_bbh_tracking_shuffled_objects_seven_objects\"\
  : {\n            \"acc_norm,none\": 0.112,\n            \"acc_norm_stderr,none\"\
  : 0.019985536939171444,\n            \"alias\": \"  - leaderboard_bbh_tracking_shuffled_objects_seven_objects\"\
  \n        },\n        \"leaderboard_bbh_tracking_shuffled_objects_three_objects\"\
  : {\n            \"acc_norm,none\": 0.328,\n            \"acc_norm_stderr,none\"\
  : 0.029752391824475376,\n            \"alias\": \"  - leaderboard_bbh_tracking_shuffled_objects_three_objects\"\
  \n        },\n        \"leaderboard_bbh_web_of_lies\": {\n            \"acc_norm,none\"\
  : 0.532,\n            \"acc_norm_stderr,none\": 0.031621252575725504,\n        \
  \    \"alias\": \"  - leaderboard_bbh_web_of_lies\"\n        },\n        \"leaderboard_gpqa\"\
  : {\n            \"acc_norm,none\": 0.25838926174496646,\n            \"acc_norm_stderr,none\"\
  : 0.012693385026829939,\n            \"alias\": \" - leaderboard_gpqa\"\n      \
  \  },\n        \"leaderboard_gpqa_diamond\": {\n            \"acc_norm,none\": 0.25757575757575757,\n\
  \            \"acc_norm_stderr,none\": 0.031156269519646836,\n            \"alias\"\
  : \"  - leaderboard_gpqa_diamond\"\n        },\n        \"leaderboard_gpqa_extended\"\
  : {\n            \"acc_norm,none\": 0.26556776556776557,\n            \"acc_norm_stderr,none\"\
  : 0.018917567557968248,\n            \"alias\": \"  - leaderboard_gpqa_extended\"\
  \n        },\n        \"leaderboard_gpqa_main\": {\n            \"acc_norm,none\"\
  : 0.25,\n            \"acc_norm_stderr,none\": 0.02048079801297601,\n          \
  \  \"alias\": \"  - leaderboard_gpqa_main\"\n        },\n        \"leaderboard_ifeval\"\
  : {\n            \"prompt_level_strict_acc,none\": 0.1256931608133087,\n       \
  \     \"prompt_level_strict_acc_stderr,none\": 0.01426562756717386,\n          \
  \  \"inst_level_strict_acc,none\": 0.23741007194244604,\n            \"inst_level_strict_acc_stderr,none\"\
  : \"N/A\",\n            \"prompt_level_loose_acc,none\": 0.12754158964879853,\n\
  \            \"prompt_level_loose_acc_stderr,none\": 0.014354940597336783,\n   \
  \         \"inst_level_loose_acc,none\": 0.24100719424460432,\n            \"inst_level_loose_acc_stderr,none\"\
  : \"N/A\",\n            \"alias\": \" - leaderboard_ifeval\"\n        },\n     \
  \   \"leaderboard_math_hard\": {\n            \"exact_match,none\": 0.0022658610271903325,\n\
  \            \"exact_match_stderr,none\": 0.001308399052935896,\n            \"\
  alias\": \" - leaderboard_math_hard\"\n        },\n        \"leaderboard_math_algebra_hard\"\
  : {\n            \"exact_match,none\": 0.003257328990228013,\n            \"exact_match_stderr,none\"\
  : 0.003257328990228012,\n            \"alias\": \"  - leaderboard_math_algebra_hard\"\
  \n        },\n        \"leaderboard_math_counting_and_prob_hard\": {\n         \
  \   \"exact_match,none\": 0.0,\n            \"exact_match_stderr,none\": 0.0,\n\
  \            \"alias\": \"  - leaderboard_math_counting_and_prob_hard\"\n      \
  \  },\n        \"leaderboard_math_geometry_hard\": {\n            \"exact_match,none\"\
  : 0.0,\n            \"exact_match_stderr,none\": 0.0,\n            \"alias\": \"\
  \  - leaderboard_math_geometry_hard\"\n        },\n        \"leaderboard_math_intermediate_algebra_hard\"\
  : {\n            \"exact_match,none\": 0.0,\n            \"exact_match_stderr,none\"\
  : 0.0,\n            \"alias\": \"  - leaderboard_math_intermediate_algebra_hard\"\
  \n        },\n        \"leaderboard_math_num_theory_hard\": {\n            \"exact_match,none\"\
  : 0.006493506493506494,\n            \"exact_match_stderr,none\": 0.006493506493506494,\n\
  \            \"alias\": \"  - leaderboard_math_num_theory_hard\"\n        },\n \
  \       \"leaderboard_math_prealgebra_hard\": {\n            \"exact_match,none\"\
  : 0.0051813471502590676,\n            \"exact_match_stderr,none\": 0.00518134715025907,\n\
  \            \"alias\": \"  - leaderboard_math_prealgebra_hard\"\n        },\n \
  \       \"leaderboard_math_precalculus_hard\": {\n            \"exact_match,none\"\
  : 0.0,\n            \"exact_match_stderr,none\": 0.0,\n            \"alias\": \"\
  \  - leaderboard_math_precalculus_hard\"\n        },\n        \"leaderboard_mmlu_pro\"\
  : {\n            \"acc,none\": 0.11195146276595745,\n            \"acc_stderr,none\"\
  : 0.0028746327856397384,\n            \"alias\": \" - leaderboard_mmlu_pro\"\n \
  \       },\n        \"leaderboard_musr\": {\n            \"acc_norm,none\": 0.4166666666666667,\n\
  \            \"acc_norm_stderr,none\": 0.017479613589429305,\n            \"alias\"\
  : \" - leaderboard_musr\"\n        },\n        \"leaderboard_musr_murder_mysteries\"\
  : {\n            \"acc_norm,none\": 0.508,\n            \"acc_norm_stderr,none\"\
  : 0.031682156431413803,\n            \"alias\": \"  - leaderboard_musr_murder_mysteries\"\
  \n        },\n        \"leaderboard_musr_object_placements\": {\n            \"\
  acc_norm,none\": 0.2578125,\n            \"acc_norm_stderr,none\": 0.027392944192695272,\n\
  \            \"alias\": \"  - leaderboard_musr_object_placements\"\n        },\n\
  \        \"leaderboard_musr_team_allocation\": {\n            \"acc_norm,none\"\
  : 0.488,\n            \"acc_norm_stderr,none\": 0.03167708558254709,\n         \
  \   \"alias\": \"  - leaderboard_musr_team_allocation\"\n        }\n    },\n   \
  \ \"leaderboard\": {\n        \"acc,none\": 0.11852468948803394,\n        \"acc_stderr,none\"\
  : 0.0028071506622770566,\n        \"prompt_level_strict_acc,none\": 0.1256931608133087,\n\
  \        \"prompt_level_strict_acc_stderr,none\": 0.01426562756717386,\n       \
  \ \"inst_level_strict_acc,none\": 0.23741007194244604,\n        \"inst_level_strict_acc_stderr,none\"\
  : \"N/A\",\n        \"acc_norm,none\": 0.2900574259655444,\n        \"acc_norm_stderr,none\"\
  : 0.004602123282554274,\n        \"prompt_level_loose_acc,none\": 0.12754158964879853,\n\
  \        \"prompt_level_loose_acc_stderr,none\": 0.014354940597336784,\n       \
  \ \"inst_level_loose_acc,none\": 0.2410071942446043,\n        \"inst_level_loose_acc_stderr,none\"\
  : \"N/A\",\n        \"exact_match,none\": 0.0022658610271903325,\n        \"exact_match_stderr,none\"\
  : 0.001308399052935896,\n        \"alias\": \"leaderboard\"\n    },\n    \"leaderboard_arc_challenge\"\
  : {\n        \"acc,none\": 0.18600682593856654,\n        \"acc_stderr,none\": 0.011370940183266705,\n\
  \        \"acc_norm,none\": 0.2235494880546075,\n        \"acc_norm_stderr,none\"\
  : 0.01217489663120261,\n        \"alias\": \" - leaderboard_arc_challenge\"\n  \
  \  },\n    \"leaderboard_bbh\": {\n        \"acc_norm,none\": 0.29352542961291445,\n\
  \        \"acc_norm_stderr,none\": 0.005660292699355036,\n        \"alias\": \"\
  \ - leaderboard_bbh\"\n    },\n    \"leaderboard_bbh_boolean_expressions\": {\n\
  \        \"acc_norm,none\": 0.44,\n        \"acc_norm_stderr,none\": 0.03145724452223573,\n\
  \        \"alias\": \"  - leaderboard_bbh_boolean_expressions\"\n    },\n    \"\
  leaderboard_bbh_causal_judgement\": {\n        \"acc_norm,none\": 0.5187165775401069,\n\
  \        \"acc_norm_stderr,none\": 0.03663608375537842,\n        \"alias\": \" \
  \ - leaderboard_bbh_causal_judgement\"\n    },\n    \"leaderboard_bbh_date_understanding\"\
  : {\n        \"acc_norm,none\": 0.2,\n        \"acc_norm_stderr,none\": 0.02534897002097908,\n\
  \        \"alias\": \"  - leaderboard_bbh_date_understanding\"\n    },\n    \"leaderboard_bbh_disambiguation_qa\"\
  : {\n        \"acc_norm,none\": 0.336,\n        \"acc_norm_stderr,none\": 0.029933259094191516,\n\
  \        \"alias\": \"  - leaderboard_bbh_disambiguation_qa\"\n    },\n    \"leaderboard_bbh_formal_fallacies\"\
  : {\n        \"acc_norm,none\": 0.532,\n        \"acc_norm_stderr,none\": 0.031621252575725504,\n\
  \        \"alias\": \"  - leaderboard_bbh_formal_fallacies\"\n    },\n    \"leaderboard_bbh_geometric_shapes\"\
  : {\n        \"acc_norm,none\": 0.084,\n        \"acc_norm_stderr,none\": 0.01757873852677636,\n\
  \        \"alias\": \"  - leaderboard_bbh_geometric_shapes\"\n    },\n    \"leaderboard_bbh_hyperbaton\"\
  : {\n        \"acc_norm,none\": 0.484,\n        \"acc_norm_stderr,none\": 0.031669985030107414,\n\
  \        \"alias\": \"  - leaderboard_bbh_hyperbaton\"\n    },\n    \"leaderboard_bbh_logical_deduction_five_objects\"\
  : {\n        \"acc_norm,none\": 0.184,\n        \"acc_norm_stderr,none\": 0.02455581299422256,\n\
  \        \"alias\": \"  - leaderboard_bbh_logical_deduction_five_objects\"\n   \
  \ },\n    \"leaderboard_bbh_logical_deduction_seven_objects\": {\n        \"acc_norm,none\"\
  : 0.192,\n        \"acc_norm_stderr,none\": 0.024960691989172015,\n        \"alias\"\
  : \"  - leaderboard_bbh_logical_deduction_seven_objects\"\n    },\n    \"leaderboard_bbh_logical_deduction_three_objects\"\
  : {\n        \"acc_norm,none\": 0.328,\n        \"acc_norm_stderr,none\": 0.029752391824475363,\n\
  \        \"alias\": \"  - leaderboard_bbh_logical_deduction_three_objects\"\n  \
  \  },\n    \"leaderboard_bbh_movie_recommendation\": {\n        \"acc_norm,none\"\
  : 0.18,\n        \"acc_norm_stderr,none\": 0.024346890650293523,\n        \"alias\"\
  : \"  - leaderboard_bbh_movie_recommendation\"\n    },\n    \"leaderboard_bbh_navigate\"\
  : {\n        \"acc_norm,none\": 0.452,\n        \"acc_norm_stderr,none\": 0.03153986449255662,\n\
  \        \"alias\": \"  - leaderboard_bbh_navigate\"\n    },\n    \"leaderboard_bbh_object_counting\"\
  : {\n        \"acc_norm,none\": 0.076,\n        \"acc_norm_stderr,none\": 0.016793573067859627,\n\
  \        \"alias\": \"  - leaderboard_bbh_object_counting\"\n    },\n    \"leaderboard_bbh_penguins_in_a_table\"\
  : {\n        \"acc_norm,none\": 0.2054794520547945,\n        \"acc_norm_stderr,none\"\
  : 0.033554654010728435,\n        \"alias\": \"  - leaderboard_bbh_penguins_in_a_table\"\
  \n    },\n    \"leaderboard_bbh_reasoning_about_colored_objects\": {\n        \"\
  acc_norm,none\": 0.108,\n        \"acc_norm_stderr,none\": 0.01966955938156875,\n\
  \        \"alias\": \"  - leaderboard_bbh_reasoning_about_colored_objects\"\n  \
  \  },\n    \"leaderboard_bbh_ruin_names\": {\n        \"acc_norm,none\": 0.216,\n\
  \        \"acc_norm_stderr,none\": 0.02607865766373273,\n        \"alias\": \" \
  \ - leaderboard_bbh_ruin_names\"\n    },\n    \"leaderboard_bbh_salient_translation_error_detection\"\
  : {\n        \"acc_norm,none\": 0.144,\n        \"acc_norm_stderr,none\": 0.022249407735450207,\n\
  \        \"alias\": \"  - leaderboard_bbh_salient_translation_error_detection\"\n\
  \    },\n    \"leaderboard_bbh_snarks\": {\n        \"acc_norm,none\": 0.5168539325842697,\n\
  \        \"acc_norm_stderr,none\": 0.037560944447344834,\n        \"alias\": \"\
  \  - leaderboard_bbh_snarks\"\n    },\n    \"leaderboard_bbh_sports_understanding\"\
  : {\n        \"acc_norm,none\": 0.46,\n        \"acc_norm_stderr,none\": 0.031584653891499,\n\
  \        \"alias\": \"  - leaderboard_bbh_sports_understanding\"\n    },\n    \"\
  leaderboard_bbh_temporal_sequences\": {\n        \"acc_norm,none\": 0.28,\n    \
  \    \"acc_norm_stderr,none\": 0.028454148277832315,\n        \"alias\": \"  - leaderboard_bbh_temporal_sequences\"\
  \n    },\n    \"leaderboard_bbh_tracking_shuffled_objects_five_objects\": {\n  \
  \      \"acc_norm,none\": 0.22,\n        \"acc_norm_stderr,none\": 0.02625179282460584,\n\
  \        \"alias\": \"  - leaderboard_bbh_tracking_shuffled_objects_five_objects\"\
  \n    },\n    \"leaderboard_bbh_tracking_shuffled_objects_seven_objects\": {\n \
  \       \"acc_norm,none\": 0.112,\n        \"acc_norm_stderr,none\": 0.019985536939171444,\n\
  \        \"alias\": \"  - leaderboard_bbh_tracking_shuffled_objects_seven_objects\"\
  \n    },\n    \"leaderboard_bbh_tracking_shuffled_objects_three_objects\": {\n \
  \       \"acc_norm,none\": 0.328,\n        \"acc_norm_stderr,none\": 0.029752391824475376,\n\
  \        \"alias\": \"  - leaderboard_bbh_tracking_shuffled_objects_three_objects\"\
  \n    },\n    \"leaderboard_bbh_web_of_lies\": {\n        \"acc_norm,none\": 0.532,\n\
  \        \"acc_norm_stderr,none\": 0.031621252575725504,\n        \"alias\": \"\
  \  - leaderboard_bbh_web_of_lies\"\n    },\n    \"leaderboard_gpqa\": {\n      \
  \  \"acc_norm,none\": 0.25838926174496646,\n        \"acc_norm_stderr,none\": 0.012693385026829939,\n\
  \        \"alias\": \" - leaderboard_gpqa\"\n    },\n    \"leaderboard_gpqa_diamond\"\
  : {\n        \"acc_norm,none\": 0.25757575757575757,\n        \"acc_norm_stderr,none\"\
  : 0.031156269519646836,\n        \"alias\": \"  - leaderboard_gpqa_diamond\"\n \
  \   },\n    \"leaderboard_gpqa_extended\": {\n        \"acc_norm,none\": 0.26556776556776557,\n\
  \        \"acc_norm_stderr,none\": 0.018917567557968248,\n        \"alias\": \"\
  \  - leaderboard_gpqa_extended\"\n    },\n    \"leaderboard_gpqa_main\": {\n   \
  \     \"acc_norm,none\": 0.25,\n        \"acc_norm_stderr,none\": 0.02048079801297601,\n\
  \        \"alias\": \"  - leaderboard_gpqa_main\"\n    },\n    \"leaderboard_ifeval\"\
  : {\n        \"prompt_level_strict_acc,none\": 0.1256931608133087,\n        \"prompt_level_strict_acc_stderr,none\"\
  : 0.01426562756717386,\n        \"inst_level_strict_acc,none\": 0.23741007194244604,\n\
  \        \"inst_level_strict_acc_stderr,none\": \"N/A\",\n        \"prompt_level_loose_acc,none\"\
  : 0.12754158964879853,\n        \"prompt_level_loose_acc_stderr,none\": 0.014354940597336783,\n\
  \        \"inst_level_loose_acc,none\": 0.24100719424460432,\n        \"inst_level_loose_acc_stderr,none\"\
  : \"N/A\",\n        \"alias\": \" - leaderboard_ifeval\"\n    },\n    \"leaderboard_math_hard\"\
  : {\n        \"exact_match,none\": 0.0022658610271903325,\n        \"exact_match_stderr,none\"\
  : 0.001308399052935896,\n        \"alias\": \" - leaderboard_math_hard\"\n    },\n\
  \    \"leaderboard_math_algebra_hard\": {\n        \"exact_match,none\": 0.003257328990228013,\n\
  \        \"exact_match_stderr,none\": 0.003257328990228012,\n        \"alias\":\
  \ \"  - leaderboard_math_algebra_hard\"\n    },\n    \"leaderboard_math_counting_and_prob_hard\"\
  : {\n        \"exact_match,none\": 0.0,\n        \"exact_match_stderr,none\": 0.0,\n\
  \        \"alias\": \"  - leaderboard_math_counting_and_prob_hard\"\n    },\n  \
  \  \"leaderboard_math_geometry_hard\": {\n        \"exact_match,none\": 0.0,\n \
  \       \"exact_match_stderr,none\": 0.0,\n        \"alias\": \"  - leaderboard_math_geometry_hard\"\
  \n    },\n    \"leaderboard_math_intermediate_algebra_hard\": {\n        \"exact_match,none\"\
  : 0.0,\n        \"exact_match_stderr,none\": 0.0,\n        \"alias\": \"  - leaderboard_math_intermediate_algebra_hard\"\
  \n    },\n    \"leaderboard_math_num_theory_hard\": {\n        \"exact_match,none\"\
  : 0.006493506493506494,\n        \"exact_match_stderr,none\": 0.006493506493506494,\n\
  \        \"alias\": \"  - leaderboard_math_num_theory_hard\"\n    },\n    \"leaderboard_math_prealgebra_hard\"\
  : {\n        \"exact_match,none\": 0.0051813471502590676,\n        \"exact_match_stderr,none\"\
  : 0.00518134715025907,\n        \"alias\": \"  - leaderboard_math_prealgebra_hard\"\
  \n    },\n    \"leaderboard_math_precalculus_hard\": {\n        \"exact_match,none\"\
  : 0.0,\n        \"exact_match_stderr,none\": 0.0,\n        \"alias\": \"  - leaderboard_math_precalculus_hard\"\
  \n    },\n    \"leaderboard_mmlu_pro\": {\n        \"acc,none\": 0.11195146276595745,\n\
  \        \"acc_stderr,none\": 0.0028746327856397384,\n        \"alias\": \" - leaderboard_mmlu_pro\"\
  \n    },\n    \"leaderboard_musr\": {\n        \"acc_norm,none\": 0.4166666666666667,\n\
  \        \"acc_norm_stderr,none\": 0.017479613589429305,\n        \"alias\": \"\
  \ - leaderboard_musr\"\n    },\n    \"leaderboard_musr_murder_mysteries\": {\n \
  \       \"acc_norm,none\": 0.508,\n        \"acc_norm_stderr,none\": 0.031682156431413803,\n\
  \        \"alias\": \"  - leaderboard_musr_murder_mysteries\"\n    },\n    \"leaderboard_musr_object_placements\"\
  : {\n        \"acc_norm,none\": 0.2578125,\n        \"acc_norm_stderr,none\": 0.027392944192695272,\n\
  \        \"alias\": \"  - leaderboard_musr_object_placements\"\n    },\n    \"leaderboard_musr_team_allocation\"\
  : {\n        \"acc_norm,none\": 0.488,\n        \"acc_norm_stderr,none\": 0.03167708558254709,\n\
  \        \"alias\": \"  - leaderboard_musr_team_allocation\"\n    }\n}\n```"
repo_url: https://huggingface.co/EleutherAI/pythia-160m
leaderboard_url: ''
point_of_contact: ''
configs:
- config_name: EleutherAI__pythia-160m__leaderboard_arc_challenge
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_arc_challenge_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_arc_challenge_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_bbh
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_bbh_boolean_expressions_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_causal_judgement_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_date_understanding_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_disambiguation_qa_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_formal_fallacies_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_geometric_shapes_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_hyperbaton_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_logical_deduction_five_objects_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_logical_deduction_seven_objects_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_logical_deduction_three_objects_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_movie_recommendation_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_navigate_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_object_counting_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_penguins_in_a_table_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_reasoning_about_colored_objects_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_ruin_names_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_salient_translation_error_detection_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_snarks_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_sports_understanding_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_temporal_sequences_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_five_objects_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_seven_objects_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_three_objects_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_web_of_lies_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_boolean_expressions_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_causal_judgement_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_date_understanding_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_disambiguation_qa_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_formal_fallacies_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_geometric_shapes_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_hyperbaton_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_logical_deduction_five_objects_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_logical_deduction_seven_objects_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_logical_deduction_three_objects_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_movie_recommendation_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_navigate_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_object_counting_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_penguins_in_a_table_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_reasoning_about_colored_objects_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_ruin_names_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_salient_translation_error_detection_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_snarks_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_sports_understanding_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_temporal_sequences_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_five_objects_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_seven_objects_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_three_objects_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_bbh_web_of_lies_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_bbh_boolean_expressions
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_bbh_boolean_expressions_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_boolean_expressions_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_bbh_causal_judgement
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_bbh_causal_judgement_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_causal_judgement_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_bbh_date_understanding
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_bbh_date_understanding_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_date_understanding_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_bbh_disambiguation_qa
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_bbh_disambiguation_qa_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_disambiguation_qa_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_bbh_formal_fallacies
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_bbh_formal_fallacies_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_formal_fallacies_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_bbh_geometric_shapes
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_bbh_geometric_shapes_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_geometric_shapes_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_bbh_hyperbaton
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_bbh_hyperbaton_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_hyperbaton_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_bbh_logical_deduction_five_objects
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_bbh_logical_deduction_five_objects_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_logical_deduction_five_objects_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_bbh_logical_deduction_seven_objects
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_bbh_logical_deduction_seven_objects_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_logical_deduction_seven_objects_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_bbh_logical_deduction_three_objects
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_bbh_logical_deduction_three_objects_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_logical_deduction_three_objects_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_bbh_movie_recommendation
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_bbh_movie_recommendation_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_movie_recommendation_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_bbh_navigate
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_bbh_navigate_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_navigate_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_bbh_object_counting
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_bbh_object_counting_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_object_counting_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_bbh_penguins_in_a_table
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_bbh_penguins_in_a_table_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_penguins_in_a_table_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_bbh_reasoning_about_colored_objects
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_bbh_reasoning_about_colored_objects_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_reasoning_about_colored_objects_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_bbh_ruin_names
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_bbh_ruin_names_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_ruin_names_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_bbh_salient_translation_error_detection
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_bbh_salient_translation_error_detection_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_salient_translation_error_detection_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_bbh_snarks
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_bbh_snarks_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_snarks_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_bbh_sports_understanding
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_bbh_sports_understanding_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_sports_understanding_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_bbh_temporal_sequences
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_bbh_temporal_sequences_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_temporal_sequences_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_bbh_tracking_shuffled_objects_five_objects
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_five_objects_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_five_objects_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_bbh_tracking_shuffled_objects_seven_objects
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_seven_objects_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_seven_objects_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_bbh_tracking_shuffled_objects_three_objects
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_three_objects_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_three_objects_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_bbh_web_of_lies
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_bbh_web_of_lies_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_web_of_lies_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_gpqa
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_gpqa_diamond_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_gpqa_extended_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_gpqa_main_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_gpqa_diamond_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_gpqa_extended_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_gpqa_main_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_gpqa_diamond
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_gpqa_diamond_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_gpqa_diamond_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_gpqa_extended
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_gpqa_extended_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_gpqa_extended_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_gpqa_main
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_gpqa_main_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_gpqa_main_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_ifeval
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_ifeval_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_ifeval_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_math
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_math_algebra_hard_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_math_counting_and_prob_hard_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_math_geometry_hard_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_math_intermediate_algebra_hard_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_math_num_theory_hard_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_math_prealgebra_hard_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_math_precalculus_hard_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_math_algebra_hard_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_math_counting_and_prob_hard_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_math_geometry_hard_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_math_intermediate_algebra_hard_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_math_num_theory_hard_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_math_prealgebra_hard_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_math_precalculus_hard_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_math_algebra_hard
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_math_algebra_hard_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_math_algebra_hard_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_math_counting_and_prob_hard
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_math_counting_and_prob_hard_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_math_counting_and_prob_hard_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_math_geometry_hard
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_math_geometry_hard_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_math_geometry_hard_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_math_intermediate_algebra_hard
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_math_intermediate_algebra_hard_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_math_intermediate_algebra_hard_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_math_num_theory_hard
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_math_num_theory_hard_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_math_num_theory_hard_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_math_prealgebra_hard
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_math_prealgebra_hard_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_math_prealgebra_hard_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_math_precalculus_hard
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_math_precalculus_hard_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_math_precalculus_hard_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_mmlu_pro
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_mmlu_pro_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_mmlu_pro_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_musr
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_musr_murder_mysteries_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_musr_object_placements_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_musr_team_allocation_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_musr_murder_mysteries_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_musr_object_placements_2024-06-16T22-09-58.078705.json'
    - '**/samples_leaderboard_musr_team_allocation_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_musr_murder_mysteries
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_musr_murder_mysteries_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_musr_murder_mysteries_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_musr_object_placements
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_musr_object_placements_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_musr_object_placements_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__leaderboard_musr_team_allocation
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/samples_leaderboard_musr_team_allocation_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/samples_leaderboard_musr_team_allocation_2024-06-16T22-09-58.078705.json'
- config_name: EleutherAI__pythia-160m__results
  data_files:
  - split: 2024_06_16T22_09_58.078705
    path:
    - '**/results_2024-06-16T22-09-58.078705.json'
  - split: latest
    path:
    - '**/results_2024-06-16T22-09-58.078705.json'
---

# Dataset Card for Evaluation run of EleutherAI/pythia-160m

<!-- Provide a quick summary of the dataset. -->

Dataset automatically created during the evaluation run of model [EleutherAI/pythia-160m](https://huggingface.co/EleutherAI/pythia-160m)
The dataset is composed of 44 configuration(s), each one corresponding to one of the evaluated task.

The dataset has been created from 2 run(s). Each run can be found as a specific split in each configuration, the split being named using the timestamp of the run.The "train" split is always pointing to the latest results.

An additional configuration "results" store all the aggregated results of the run.

To load the details from a run, you can for instance do the following:
```python
from datasets import load_dataset
data = load_dataset(
	"HuggingFaceEvalInternal/EleutherAI__pythia-160m-details-private",
	name="EleutherAI__pythia-160m__leaderboard_arc_challenge",
	split="latest"
)
```

## Latest results

These are the [latest results from run 2024-06-16T22-09-58.078705](https://huggingface.co/datasets/HuggingFaceEvalInternal/EleutherAI__pythia-160m-details-private/blob/main/EleutherAI__pythia-160m/results_2024-06-16T22-09-58.078705.json) (note that there might be results for other tasks in the repos if successive evals didn't cover the same tasks. You find each in the results and the "latest" split for each eval):

```python
{
    "all": {
        "leaderboard": {
            "acc,none": 0.11852468948803394,
            "acc_stderr,none": 0.0028071506622770566,
            "prompt_level_strict_acc,none": 0.1256931608133087,
            "prompt_level_strict_acc_stderr,none": 0.01426562756717386,
            "inst_level_strict_acc,none": 0.23741007194244604,
            "inst_level_strict_acc_stderr,none": "N/A",
            "acc_norm,none": 0.2900574259655444,
            "acc_norm_stderr,none": 0.004602123282554274,
            "prompt_level_loose_acc,none": 0.12754158964879853,
            "prompt_level_loose_acc_stderr,none": 0.014354940597336784,
            "inst_level_loose_acc,none": 0.2410071942446043,
            "inst_level_loose_acc_stderr,none": "N/A",
            "exact_match,none": 0.0022658610271903325,
            "exact_match_stderr,none": 0.001308399052935896,
            "alias": "leaderboard"
        },
        "leaderboard_arc_challenge": {
            "acc,none": 0.18600682593856654,
            "acc_stderr,none": 0.011370940183266705,
            "acc_norm,none": 0.2235494880546075,
            "acc_norm_stderr,none": 0.01217489663120261,
            "alias": " - leaderboard_arc_challenge"
        },
        "leaderboard_bbh": {
            "acc_norm,none": 0.29352542961291445,
            "acc_norm_stderr,none": 0.005660292699355036,
            "alias": " - leaderboard_bbh"
        },
        "leaderboard_bbh_boolean_expressions": {
            "acc_norm,none": 0.44,
            "acc_norm_stderr,none": 0.03145724452223573,
            "alias": "  - leaderboard_bbh_boolean_expressions"
        },
        "leaderboard_bbh_causal_judgement": {
            "acc_norm,none": 0.5187165775401069,
            "acc_norm_stderr,none": 0.03663608375537842,
            "alias": "  - leaderboard_bbh_causal_judgement"
        },
        "leaderboard_bbh_date_understanding": {
            "acc_norm,none": 0.2,
            "acc_norm_stderr,none": 0.02534897002097908,
            "alias": "  - leaderboard_bbh_date_understanding"
        },
        "leaderboard_bbh_disambiguation_qa": {
            "acc_norm,none": 0.336,
            "acc_norm_stderr,none": 0.029933259094191516,
            "alias": "  - leaderboard_bbh_disambiguation_qa"
        },
        "leaderboard_bbh_formal_fallacies": {
            "acc_norm,none": 0.532,
            "acc_norm_stderr,none": 0.031621252575725504,
            "alias": "  - leaderboard_bbh_formal_fallacies"
        },
        "leaderboard_bbh_geometric_shapes": {
            "acc_norm,none": 0.084,
            "acc_norm_stderr,none": 0.01757873852677636,
            "alias": "  - leaderboard_bbh_geometric_shapes"
        },
        "leaderboard_bbh_hyperbaton": {
            "acc_norm,none": 0.484,
            "acc_norm_stderr,none": 0.031669985030107414,
            "alias": "  - leaderboard_bbh_hyperbaton"
        },
        "leaderboard_bbh_logical_deduction_five_objects": {
            "acc_norm,none": 0.184,
            "acc_norm_stderr,none": 0.02455581299422256,
            "alias": "  - leaderboard_bbh_logical_deduction_five_objects"
        },
        "leaderboard_bbh_logical_deduction_seven_objects": {
            "acc_norm,none": 0.192,
            "acc_norm_stderr,none": 0.024960691989172015,
            "alias": "  - leaderboard_bbh_logical_deduction_seven_objects"
        },
        "leaderboard_bbh_logical_deduction_three_objects": {
            "acc_norm,none": 0.328,
            "acc_norm_stderr,none": 0.029752391824475363,
            "alias": "  - leaderboard_bbh_logical_deduction_three_objects"
        },
        "leaderboard_bbh_movie_recommendation": {
            "acc_norm,none": 0.18,
            "acc_norm_stderr,none": 0.024346890650293523,
            "alias": "  - leaderboard_bbh_movie_recommendation"
        },
        "leaderboard_bbh_navigate": {
            "acc_norm,none": 0.452,
            "acc_norm_stderr,none": 0.03153986449255662,
            "alias": "  - leaderboard_bbh_navigate"
        },
        "leaderboard_bbh_object_counting": {
            "acc_norm,none": 0.076,
            "acc_norm_stderr,none": 0.016793573067859627,
            "alias": "  - leaderboard_bbh_object_counting"
        },
        "leaderboard_bbh_penguins_in_a_table": {
            "acc_norm,none": 0.2054794520547945,
            "acc_norm_stderr,none": 0.033554654010728435,
            "alias": "  - leaderboard_bbh_penguins_in_a_table"
        },
        "leaderboard_bbh_reasoning_about_colored_objects": {
            "acc_norm,none": 0.108,
            "acc_norm_stderr,none": 0.01966955938156875,
            "alias": "  - leaderboard_bbh_reasoning_about_colored_objects"
        },
        "leaderboard_bbh_ruin_names": {
            "acc_norm,none": 0.216,
            "acc_norm_stderr,none": 0.02607865766373273,
            "alias": "  - leaderboard_bbh_ruin_names"
        },
        "leaderboard_bbh_salient_translation_error_detection": {
            "acc_norm,none": 0.144,
            "acc_norm_stderr,none": 0.022249407735450207,
            "alias": "  - leaderboard_bbh_salient_translation_error_detection"
        },
        "leaderboard_bbh_snarks": {
            "acc_norm,none": 0.5168539325842697,
            "acc_norm_stderr,none": 0.037560944447344834,
            "alias": "  - leaderboard_bbh_snarks"
        },
        "leaderboard_bbh_sports_understanding": {
            "acc_norm,none": 0.46,
            "acc_norm_stderr,none": 0.031584653891499,
            "alias": "  - leaderboard_bbh_sports_understanding"
        },
        "leaderboard_bbh_temporal_sequences": {
            "acc_norm,none": 0.28,
            "acc_norm_stderr,none": 0.028454148277832315,
            "alias": "  - leaderboard_bbh_temporal_sequences"
        },
        "leaderboard_bbh_tracking_shuffled_objects_five_objects": {
            "acc_norm,none": 0.22,
            "acc_norm_stderr,none": 0.02625179282460584,
            "alias": "  - leaderboard_bbh_tracking_shuffled_objects_five_objects"
        },
        "leaderboard_bbh_tracking_shuffled_objects_seven_objects": {
            "acc_norm,none": 0.112,
            "acc_norm_stderr,none": 0.019985536939171444,
            "alias": "  - leaderboard_bbh_tracking_shuffled_objects_seven_objects"
        },
        "leaderboard_bbh_tracking_shuffled_objects_three_objects": {
            "acc_norm,none": 0.328,
            "acc_norm_stderr,none": 0.029752391824475376,
            "alias": "  - leaderboard_bbh_tracking_shuffled_objects_three_objects"
        },
        "leaderboard_bbh_web_of_lies": {
            "acc_norm,none": 0.532,
            "acc_norm_stderr,none": 0.031621252575725504,
            "alias": "  - leaderboard_bbh_web_of_lies"
        },
        "leaderboard_gpqa": {
            "acc_norm,none": 0.25838926174496646,
            "acc_norm_stderr,none": 0.012693385026829939,
            "alias": " - leaderboard_gpqa"
        },
        "leaderboard_gpqa_diamond": {
            "acc_norm,none": 0.25757575757575757,
            "acc_norm_stderr,none": 0.031156269519646836,
            "alias": "  - leaderboard_gpqa_diamond"
        },
        "leaderboard_gpqa_extended": {
            "acc_norm,none": 0.26556776556776557,
            "acc_norm_stderr,none": 0.018917567557968248,
            "alias": "  - leaderboard_gpqa_extended"
        },
        "leaderboard_gpqa_main": {
            "acc_norm,none": 0.25,
            "acc_norm_stderr,none": 0.02048079801297601,
            "alias": "  - leaderboard_gpqa_main"
        },
        "leaderboard_ifeval": {
            "prompt_level_strict_acc,none": 0.1256931608133087,
            "prompt_level_strict_acc_stderr,none": 0.01426562756717386,
            "inst_level_strict_acc,none": 0.23741007194244604,
            "inst_level_strict_acc_stderr,none": "N/A",
            "prompt_level_loose_acc,none": 0.12754158964879853,
            "prompt_level_loose_acc_stderr,none": 0.014354940597336783,
            "inst_level_loose_acc,none": 0.24100719424460432,
            "inst_level_loose_acc_stderr,none": "N/A",
            "alias": " - leaderboard_ifeval"
        },
        "leaderboard_math_hard": {
            "exact_match,none": 0.0022658610271903325,
            "exact_match_stderr,none": 0.001308399052935896,
            "alias": " - leaderboard_math_hard"
        },
        "leaderboard_math_algebra_hard": {
            "exact_match,none": 0.003257328990228013,
            "exact_match_stderr,none": 0.003257328990228012,
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
            "exact_match_stderr,none": 0.006493506493506494,
            "alias": "  - leaderboard_math_num_theory_hard"
        },
        "leaderboard_math_prealgebra_hard": {
            "exact_match,none": 0.0051813471502590676,
            "exact_match_stderr,none": 0.00518134715025907,
            "alias": "  - leaderboard_math_prealgebra_hard"
        },
        "leaderboard_math_precalculus_hard": {
            "exact_match,none": 0.0,
            "exact_match_stderr,none": 0.0,
            "alias": "  - leaderboard_math_precalculus_hard"
        },
        "leaderboard_mmlu_pro": {
            "acc,none": 0.11195146276595745,
            "acc_stderr,none": 0.0028746327856397384,
            "alias": " - leaderboard_mmlu_pro"
        },
        "leaderboard_musr": {
            "acc_norm,none": 0.4166666666666667,
            "acc_norm_stderr,none": 0.017479613589429305,
            "alias": " - leaderboard_musr"
        },
        "leaderboard_musr_murder_mysteries": {
            "acc_norm,none": 0.508,
            "acc_norm_stderr,none": 0.031682156431413803,
            "alias": "  - leaderboard_musr_murder_mysteries"
        },
        "leaderboard_musr_object_placements": {
            "acc_norm,none": 0.2578125,
            "acc_norm_stderr,none": 0.027392944192695272,
            "alias": "  - leaderboard_musr_object_placements"
        },
        "leaderboard_musr_team_allocation": {
            "acc_norm,none": 0.488,
            "acc_norm_stderr,none": 0.03167708558254709,
            "alias": "  - leaderboard_musr_team_allocation"
        }
    },
    "leaderboard": {
        "acc,none": 0.11852468948803394,
        "acc_stderr,none": 0.0028071506622770566,
        "prompt_level_strict_acc,none": 0.1256931608133087,
        "prompt_level_strict_acc_stderr,none": 0.01426562756717386,
        "inst_level_strict_acc,none": 0.23741007194244604,
        "inst_level_strict_acc_stderr,none": "N/A",
        "acc_norm,none": 0.2900574259655444,
        "acc_norm_stderr,none": 0.004602123282554274,
        "prompt_level_loose_acc,none": 0.12754158964879853,
        "prompt_level_loose_acc_stderr,none": 0.014354940597336784,
        "inst_level_loose_acc,none": 0.2410071942446043,
        "inst_level_loose_acc_stderr,none": "N/A",
        "exact_match,none": 0.0022658610271903325,
        "exact_match_stderr,none": 0.001308399052935896,
        "alias": "leaderboard"
    },
    "leaderboard_arc_challenge": {
        "acc,none": 0.18600682593856654,
        "acc_stderr,none": 0.011370940183266705,
        "acc_norm,none": 0.2235494880546075,
        "acc_norm_stderr,none": 0.01217489663120261,
        "alias": " - leaderboard_arc_challenge"
    },
    "leaderboard_bbh": {
        "acc_norm,none": 0.29352542961291445,
        "acc_norm_stderr,none": 0.005660292699355036,
        "alias": " - leaderboard_bbh"
    },
    "leaderboard_bbh_boolean_expressions": {
        "acc_norm,none": 0.44,
        "acc_norm_stderr,none": 0.03145724452223573,
        "alias": "  - leaderboard_bbh_boolean_expressions"
    },
    "leaderboard_bbh_causal_judgement": {
        "acc_norm,none": 0.5187165775401069,
        "acc_norm_stderr,none": 0.03663608375537842,
        "alias": "  - leaderboard_bbh_causal_judgement"
    },
    "leaderboard_bbh_date_understanding": {
        "acc_norm,none": 0.2,
        "acc_norm_stderr,none": 0.02534897002097908,
        "alias": "  - leaderboard_bbh_date_understanding"
    },
    "leaderboard_bbh_disambiguation_qa": {
        "acc_norm,none": 0.336,
        "acc_norm_stderr,none": 0.029933259094191516,
        "alias": "  - leaderboard_bbh_disambiguation_qa"
    },
    "leaderboard_bbh_formal_fallacies": {
        "acc_norm,none": 0.532,
        "acc_norm_stderr,none": 0.031621252575725504,
        "alias": "  - leaderboard_bbh_formal_fallacies"
    },
    "leaderboard_bbh_geometric_shapes": {
        "acc_norm,none": 0.084,
        "acc_norm_stderr,none": 0.01757873852677636,
        "alias": "  - leaderboard_bbh_geometric_shapes"
    },
    "leaderboard_bbh_hyperbaton": {
        "acc_norm,none": 0.484,
        "acc_norm_stderr,none": 0.031669985030107414,
        "alias": "  - leaderboard_bbh_hyperbaton"
    },
    "leaderboard_bbh_logical_deduction_five_objects": {
        "acc_norm,none": 0.184,
        "acc_norm_stderr,none": 0.02455581299422256,
        "alias": "  - leaderboard_bbh_logical_deduction_five_objects"
    },
    "leaderboard_bbh_logical_deduction_seven_objects": {
        "acc_norm,none": 0.192,
        "acc_norm_stderr,none": 0.024960691989172015,
        "alias": "  - leaderboard_bbh_logical_deduction_seven_objects"
    },
    "leaderboard_bbh_logical_deduction_three_objects": {
        "acc_norm,none": 0.328,
        "acc_norm_stderr,none": 0.029752391824475363,
        "alias": "  - leaderboard_bbh_logical_deduction_three_objects"
    },
    "leaderboard_bbh_movie_recommendation": {
        "acc_norm,none": 0.18,
        "acc_norm_stderr,none": 0.024346890650293523,
        "alias": "  - leaderboard_bbh_movie_recommendation"
    },
    "leaderboard_bbh_navigate": {
        "acc_norm,none": 0.452,
        "acc_norm_stderr,none": 0.03153986449255662,
        "alias": "  - leaderboard_bbh_navigate"
    },
    "leaderboard_bbh_object_counting": {
        "acc_norm,none": 0.076,
        "acc_norm_stderr,none": 0.016793573067859627,
        "alias": "  - leaderboard_bbh_object_counting"
    },
    "leaderboard_bbh_penguins_in_a_table": {
        "acc_norm,none": 0.2054794520547945,
        "acc_norm_stderr,none": 0.033554654010728435,
        "alias": "  - leaderboard_bbh_penguins_in_a_table"
    },
    "leaderboard_bbh_reasoning_about_colored_objects": {
        "acc_norm,none": 0.108,
        "acc_norm_stderr,none": 0.01966955938156875,
        "alias": "  - leaderboard_bbh_reasoning_about_colored_objects"
    },
    "leaderboard_bbh_ruin_names": {
        "acc_norm,none": 0.216,
        "acc_norm_stderr,none": 0.02607865766373273,
        "alias": "  - leaderboard_bbh_ruin_names"
    },
    "leaderboard_bbh_salient_translation_error_detection": {
        "acc_norm,none": 0.144,
        "acc_norm_stderr,none": 0.022249407735450207,
        "alias": "  - leaderboard_bbh_salient_translation_error_detection"
    },
    "leaderboard_bbh_snarks": {
        "acc_norm,none": 0.5168539325842697,
        "acc_norm_stderr,none": 0.037560944447344834,
        "alias": "  - leaderboard_bbh_snarks"
    },
    "leaderboard_bbh_sports_understanding": {
        "acc_norm,none": 0.46,
        "acc_norm_stderr,none": 0.031584653891499,
        "alias": "  - leaderboard_bbh_sports_understanding"
    },
    "leaderboard_bbh_temporal_sequences": {
        "acc_norm,none": 0.28,
        "acc_norm_stderr,none": 0.028454148277832315,
        "alias": "  - leaderboard_bbh_temporal_sequences"
    },
    "leaderboard_bbh_tracking_shuffled_objects_five_objects": {
        "acc_norm,none": 0.22,
        "acc_norm_stderr,none": 0.02625179282460584,
        "alias": "  - leaderboard_bbh_tracking_shuffled_objects_five_objects"
    },
    "leaderboard_bbh_tracking_shuffled_objects_seven_objects": {
        "acc_norm,none": 0.112,
        "acc_norm_stderr,none": 0.019985536939171444,
        "alias": "  - leaderboard_bbh_tracking_shuffled_objects_seven_objects"
    },
    "leaderboard_bbh_tracking_shuffled_objects_three_objects": {
        "acc_norm,none": 0.328,
        "acc_norm_stderr,none": 0.029752391824475376,
        "alias": "  - leaderboard_bbh_tracking_shuffled_objects_three_objects"
    },
    "leaderboard_bbh_web_of_lies": {
        "acc_norm,none": 0.532,
        "acc_norm_stderr,none": 0.031621252575725504,
        "alias": "  - leaderboard_bbh_web_of_lies"
    },
    "leaderboard_gpqa": {
        "acc_norm,none": 0.25838926174496646,
        "acc_norm_stderr,none": 0.012693385026829939,
        "alias": " - leaderboard_gpqa"
    },
    "leaderboard_gpqa_diamond": {
        "acc_norm,none": 0.25757575757575757,
        "acc_norm_stderr,none": 0.031156269519646836,
        "alias": "  - leaderboard_gpqa_diamond"
    },
    "leaderboard_gpqa_extended": {
        "acc_norm,none": 0.26556776556776557,
        "acc_norm_stderr,none": 0.018917567557968248,
        "alias": "  - leaderboard_gpqa_extended"
    },
    "leaderboard_gpqa_main": {
        "acc_norm,none": 0.25,
        "acc_norm_stderr,none": 0.02048079801297601,
        "alias": "  - leaderboard_gpqa_main"
    },
    "leaderboard_ifeval": {
        "prompt_level_strict_acc,none": 0.1256931608133087,
        "prompt_level_strict_acc_stderr,none": 0.01426562756717386,
        "inst_level_strict_acc,none": 0.23741007194244604,
        "inst_level_strict_acc_stderr,none": "N/A",
        "prompt_level_loose_acc,none": 0.12754158964879853,
        "prompt_level_loose_acc_stderr,none": 0.014354940597336783,
        "inst_level_loose_acc,none": 0.24100719424460432,
        "inst_level_loose_acc_stderr,none": "N/A",
        "alias": " - leaderboard_ifeval"
    },
    "leaderboard_math_hard": {
        "exact_match,none": 0.0022658610271903325,
        "exact_match_stderr,none": 0.001308399052935896,
        "alias": " - leaderboard_math_hard"
    },
    "leaderboard_math_algebra_hard": {
        "exact_match,none": 0.003257328990228013,
        "exact_match_stderr,none": 0.003257328990228012,
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
        "exact_match_stderr,none": 0.006493506493506494,
        "alias": "  - leaderboard_math_num_theory_hard"
    },
    "leaderboard_math_prealgebra_hard": {
        "exact_match,none": 0.0051813471502590676,
        "exact_match_stderr,none": 0.00518134715025907,
        "alias": "  - leaderboard_math_prealgebra_hard"
    },
    "leaderboard_math_precalculus_hard": {
        "exact_match,none": 0.0,
        "exact_match_stderr,none": 0.0,
        "alias": "  - leaderboard_math_precalculus_hard"
    },
    "leaderboard_mmlu_pro": {
        "acc,none": 0.11195146276595745,
        "acc_stderr,none": 0.0028746327856397384,
        "alias": " - leaderboard_mmlu_pro"
    },
    "leaderboard_musr": {
        "acc_norm,none": 0.4166666666666667,
        "acc_norm_stderr,none": 0.017479613589429305,
        "alias": " - leaderboard_musr"
    },
    "leaderboard_musr_murder_mysteries": {
        "acc_norm,none": 0.508,
        "acc_norm_stderr,none": 0.031682156431413803,
        "alias": "  - leaderboard_musr_murder_mysteries"
    },
    "leaderboard_musr_object_placements": {
        "acc_norm,none": 0.2578125,
        "acc_norm_stderr,none": 0.027392944192695272,
        "alias": "  - leaderboard_musr_object_placements"
    },
    "leaderboard_musr_team_allocation": {
        "acc_norm,none": 0.488,
        "acc_norm_stderr,none": 0.03167708558254709,
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