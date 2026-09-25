---
pretty_name: Evaluation run of EleutherAI/pythia-1.4b
dataset_summary: "Dataset automatically created during the evaluation run of model\
  \ [EleutherAI/pythia-1.4b](https://huggingface.co/EleutherAI/pythia-1.4b)\nThe dataset\
  \ is composed of 38 configuration(s), each one corresponding to one of the evaluated\
  \ task.\n\nThe dataset has been created from 1 run(s). Each run can be found as\
  \ a specific split in each configuration, the split being named using the timestamp\
  \ of the run.The \"train\" split is always pointing to the latest results.\n\nAn\
  \ additional configuration \"results\" store all the aggregated results of the run.\n\
  \nTo load the details from a run, you can for instance do the following:\n```python\n\
  from datasets import load_dataset\ndata = load_dataset(\n\t\"open-llm-leaderboard/EleutherAI__pythia-1.4b-details\"\
  ,\n\tname=\"EleutherAI__pythia-1.4b__leaderboard_bbh_boolean_expressions\",\n\t\
  split=\"latest\"\n)\n```\n\n## Latest results\n\nThese are the [latest results from\
  \ run 2025-01-28T10-22-20.980995](https://huggingface.co/datasets/open-llm-leaderboard/EleutherAI__pythia-1.4b-details/blob/main/EleutherAI__pythia-1.4b/results_2025-01-28T10-22-20.980995.json)\
  \ (note that there might be results for other tasks in the repos if successive evals\
  \ didn't cover the same tasks. You find each in the results and the \"latest\" split\
  \ for each eval):\n\n```python\n{\n    \"all\": {\n        \"leaderboard\": {\n\
  \            \"inst_level_loose_acc,none\": 0.3105515587529976,\n            \"\
  inst_level_loose_acc_stderr,none\": \"N/A\",\n            \"acc_norm,none\": 0.30821118173563367,\n\
  \            \"acc_norm_stderr,none\": 0.00500914440369552,\n            \"inst_level_strict_acc,none\"\
  : 0.29856115107913667,\n            \"inst_level_strict_acc_stderr,none\": \"N/A\"\
  ,\n            \"prompt_level_loose_acc,none\": 0.18853974121996303,\n         \
  \   \"prompt_level_loose_acc_stderr,none\": 0.016832096060176906,\n            \"\
  exact_match,none\": 0.0075528700906344415,\n            \"exact_match_stderr,none\"\
  : 0.0023759473096993293,\n            \"acc,none\": 0.11228390957446809,\n     \
  \       \"acc_stderr,none\": 0.002878358904186553,\n            \"prompt_level_strict_acc,none\"\
  : 0.1756007393715342,\n            \"prompt_level_strict_acc_stderr,none\": 0.01637325731205799,\n\
  \            \"alias\": \"leaderboard\"\n        },\n        \"leaderboard_bbh\"\
  : {\n            \"acc_norm,none\": 0.31192501301857317,\n            \"acc_norm_stderr,none\"\
  : 0.00574749250069476,\n            \"alias\": \" - leaderboard_bbh\"\n        },\n\
  \        \"leaderboard_bbh_boolean_expressions\": {\n            \"alias\": \" \
  \ - leaderboard_bbh_boolean_expressions\",\n            \"acc_norm,none\": 0.516,\n\
  \            \"acc_norm_stderr,none\": 0.03166998503010743\n        },\n       \
  \ \"leaderboard_bbh_causal_judgement\": {\n            \"alias\": \"  - leaderboard_bbh_causal_judgement\"\
  ,\n            \"acc_norm,none\": 0.5133689839572193,\n            \"acc_norm_stderr,none\"\
  : 0.03664867131244299\n        },\n        \"leaderboard_bbh_date_understanding\"\
  : {\n            \"alias\": \"  - leaderboard_bbh_date_understanding\",\n      \
  \      \"acc_norm,none\": 0.184,\n            \"acc_norm_stderr,none\": 0.02455581299422255\n\
  \        },\n        \"leaderboard_bbh_disambiguation_qa\": {\n            \"alias\"\
  : \"  - leaderboard_bbh_disambiguation_qa\",\n            \"acc_norm,none\": 0.3,\n\
  \            \"acc_norm_stderr,none\": 0.029040893477575783\n        },\n      \
  \  \"leaderboard_bbh_formal_fallacies\": {\n            \"alias\": \"  - leaderboard_bbh_formal_fallacies\"\
  ,\n            \"acc_norm,none\": 0.468,\n            \"acc_norm_stderr,none\":\
  \ 0.03162125257572558\n        },\n        \"leaderboard_bbh_geometric_shapes\"\
  : {\n            \"alias\": \"  - leaderboard_bbh_geometric_shapes\",\n        \
  \    \"acc_norm,none\": 0.084,\n            \"acc_norm_stderr,none\": 0.017578738526776348\n\
  \        },\n        \"leaderboard_bbh_hyperbaton\": {\n            \"alias\": \"\
  \  - leaderboard_bbh_hyperbaton\",\n            \"acc_norm,none\": 0.5,\n      \
  \      \"acc_norm_stderr,none\": 0.031686212526223896\n        },\n        \"leaderboard_bbh_logical_deduction_five_objects\"\
  : {\n            \"alias\": \"  - leaderboard_bbh_logical_deduction_five_objects\"\
  ,\n            \"acc_norm,none\": 0.232,\n            \"acc_norm_stderr,none\":\
  \ 0.026750070374865202\n        },\n        \"leaderboard_bbh_logical_deduction_seven_objects\"\
  : {\n            \"alias\": \"  - leaderboard_bbh_logical_deduction_seven_objects\"\
  ,\n            \"acc_norm,none\": 0.14,\n            \"acc_norm_stderr,none\": 0.021989409645240245\n\
  \        },\n        \"leaderboard_bbh_logical_deduction_three_objects\": {\n  \
  \          \"alias\": \"  - leaderboard_bbh_logical_deduction_three_objects\",\n\
  \            \"acc_norm,none\": 0.34,\n            \"acc_norm_stderr,none\": 0.030020073605457873\n\
  \        },\n        \"leaderboard_bbh_movie_recommendation\": {\n            \"\
  alias\": \"  - leaderboard_bbh_movie_recommendation\",\n            \"acc_norm,none\"\
  : 0.264,\n            \"acc_norm_stderr,none\": 0.027934518957690866\n        },\n\
  \        \"leaderboard_bbh_navigate\": {\n            \"alias\": \"  - leaderboard_bbh_navigate\"\
  ,\n            \"acc_norm,none\": 0.58,\n            \"acc_norm_stderr,none\": 0.03127799950463661\n\
  \        },\n        \"leaderboard_bbh_object_counting\": {\n            \"alias\"\
  : \"  - leaderboard_bbh_object_counting\",\n            \"acc_norm,none\": 0.172,\n\
  \            \"acc_norm_stderr,none\": 0.02391551394448624\n        },\n       \
  \ \"leaderboard_bbh_penguins_in_a_table\": {\n            \"alias\": \"  - leaderboard_bbh_penguins_in_a_table\"\
  ,\n            \"acc_norm,none\": 0.21232876712328766,\n            \"acc_norm_stderr,none\"\
  : 0.03396197282917473\n        },\n        \"leaderboard_bbh_reasoning_about_colored_objects\"\
  : {\n            \"alias\": \"  - leaderboard_bbh_reasoning_about_colored_objects\"\
  ,\n            \"acc_norm,none\": 0.096,\n            \"acc_norm_stderr,none\":\
  \ 0.01866896141947719\n        },\n        \"leaderboard_bbh_ruin_names\": {\n \
  \           \"alias\": \"  - leaderboard_bbh_ruin_names\",\n            \"acc_norm,none\"\
  : 0.208,\n            \"acc_norm_stderr,none\": 0.02572139890141637\n        },\n\
  \        \"leaderboard_bbh_salient_translation_error_detection\": {\n          \
  \  \"alias\": \"  - leaderboard_bbh_salient_translation_error_detection\",\n   \
  \         \"acc_norm,none\": 0.224,\n            \"acc_norm_stderr,none\": 0.026421361687347884\n\
  \        },\n        \"leaderboard_bbh_snarks\": {\n            \"alias\": \"  -\
  \ leaderboard_bbh_snarks\",\n            \"acc_norm,none\": 0.5393258426966292,\n\
  \            \"acc_norm_stderr,none\": 0.03746587736387869\n        },\n       \
  \ \"leaderboard_bbh_sports_understanding\": {\n            \"alias\": \"  - leaderboard_bbh_sports_understanding\"\
  ,\n            \"acc_norm,none\": 0.552,\n            \"acc_norm_stderr,none\":\
  \ 0.03151438761115348\n        },\n        \"leaderboard_bbh_temporal_sequences\"\
  : {\n            \"alias\": \"  - leaderboard_bbh_temporal_sequences\",\n      \
  \      \"acc_norm,none\": 0.244,\n            \"acc_norm_stderr,none\": 0.02721799546455311\n\
  \        },\n        \"leaderboard_bbh_tracking_shuffled_objects_five_objects\"\
  : {\n            \"alias\": \"  - leaderboard_bbh_tracking_shuffled_objects_five_objects\"\
  ,\n            \"acc_norm,none\": 0.196,\n            \"acc_norm_stderr,none\":\
  \ 0.025156857313255926\n        },\n        \"leaderboard_bbh_tracking_shuffled_objects_seven_objects\"\
  : {\n            \"alias\": \"  - leaderboard_bbh_tracking_shuffled_objects_seven_objects\"\
  ,\n            \"acc_norm,none\": 0.156,\n            \"acc_norm_stderr,none\":\
  \ 0.022995023034068682\n        },\n        \"leaderboard_bbh_tracking_shuffled_objects_three_objects\"\
  : {\n            \"alias\": \"  - leaderboard_bbh_tracking_shuffled_objects_three_objects\"\
  ,\n            \"acc_norm,none\": 0.328,\n            \"acc_norm_stderr,none\":\
  \ 0.029752391824475363\n        },\n        \"leaderboard_bbh_web_of_lies\": {\n\
  \            \"alias\": \"  - leaderboard_bbh_web_of_lies\",\n            \"acc_norm,none\"\
  : 0.512,\n            \"acc_norm_stderr,none\": 0.03167708558254714\n        },\n\
  \        \"leaderboard_gpqa\": {\n            \"acc_norm,none\": 0.26174496644295303,\n\
  \            \"acc_norm_stderr,none\": 0.012746897764299207,\n            \"alias\"\
  : \" - leaderboard_gpqa\"\n        },\n        \"leaderboard_gpqa_diamond\": {\n\
  \            \"alias\": \"  - leaderboard_gpqa_diamond\",\n            \"acc_norm,none\"\
  : 0.2727272727272727,\n            \"acc_norm_stderr,none\": 0.03173071239071728\n\
  \        },\n        \"leaderboard_gpqa_extended\": {\n            \"alias\": \"\
  \  - leaderboard_gpqa_extended\",\n            \"acc_norm,none\": 0.26373626373626374,\n\
  \            \"acc_norm_stderr,none\": 0.018875713580372433\n        },\n      \
  \  \"leaderboard_gpqa_main\": {\n            \"alias\": \"  - leaderboard_gpqa_main\"\
  ,\n            \"acc_norm,none\": 0.2544642857142857,\n            \"acc_norm_stderr,none\"\
  : 0.02060126475832284\n        },\n        \"leaderboard_ifeval\": {\n         \
  \   \"alias\": \" - leaderboard_ifeval\",\n            \"prompt_level_strict_acc,none\"\
  : 0.1756007393715342,\n            \"prompt_level_strict_acc_stderr,none\": 0.01637325731205799,\n\
  \            \"inst_level_strict_acc,none\": 0.29856115107913667,\n            \"\
  inst_level_strict_acc_stderr,none\": \"N/A\",\n            \"prompt_level_loose_acc,none\"\
  : 0.18853974121996303,\n            \"prompt_level_loose_acc_stderr,none\": 0.016832096060176906,\n\
  \            \"inst_level_loose_acc,none\": 0.3105515587529976,\n            \"\
  inst_level_loose_acc_stderr,none\": \"N/A\"\n        },\n        \"leaderboard_math_hard\"\
  : {\n            \"exact_match,none\": 0.0075528700906344415,\n            \"exact_match_stderr,none\"\
  : 0.0023759473096993293,\n            \"alias\": \" - leaderboard_math_hard\"\n\
  \        },\n        \"leaderboard_math_algebra_hard\": {\n            \"alias\"\
  : \"  - leaderboard_math_algebra_hard\",\n            \"exact_match,none\": 0.019543973941368076,\n\
  \            \"exact_match_stderr,none\": 0.007913339243755165\n        },\n   \
  \     \"leaderboard_math_counting_and_prob_hard\": {\n            \"alias\": \"\
  \  - leaderboard_math_counting_and_prob_hard\",\n            \"exact_match,none\"\
  : 0.008130081300813009,\n            \"exact_match_stderr,none\": 0.008130081300813007\n\
  \        },\n        \"leaderboard_math_geometry_hard\": {\n            \"alias\"\
  : \"  - leaderboard_math_geometry_hard\",\n            \"exact_match,none\": 0.0,\n\
  \            \"exact_match_stderr,none\": 0.0\n        },\n        \"leaderboard_math_intermediate_algebra_hard\"\
  : {\n            \"alias\": \"  - leaderboard_math_intermediate_algebra_hard\",\n\
  \            \"exact_match,none\": 0.0,\n            \"exact_match_stderr,none\"\
  : 0.0\n        },\n        \"leaderboard_math_num_theory_hard\": {\n           \
  \ \"alias\": \"  - leaderboard_math_num_theory_hard\",\n            \"exact_match,none\"\
  : 0.012987012987012988,\n            \"exact_match_stderr,none\": 0.009153145279150204\n\
  \        },\n        \"leaderboard_math_prealgebra_hard\": {\n            \"alias\"\
  : \"  - leaderboard_math_prealgebra_hard\",\n            \"exact_match,none\": 0.0051813471502590676,\n\
  \            \"exact_match_stderr,none\": 0.0051813471502590676\n        },\n  \
  \      \"leaderboard_math_precalculus_hard\": {\n            \"alias\": \"  - leaderboard_math_precalculus_hard\"\
  ,\n            \"exact_match,none\": 0.0,\n            \"exact_match_stderr,none\"\
  : 0.0\n        },\n        \"leaderboard_mmlu_pro\": {\n            \"alias\": \"\
  \ - leaderboard_mmlu_pro\",\n            \"acc,none\": 0.11228390957446809,\n  \
  \          \"acc_stderr,none\": 0.002878358904186553\n        },\n        \"leaderboard_musr\"\
  : {\n            \"acc_norm,none\": 0.3531746031746032,\n            \"acc_norm_stderr,none\"\
  : 0.016935716690187123,\n            \"alias\": \" - leaderboard_musr\"\n      \
  \  },\n        \"leaderboard_musr_murder_mysteries\": {\n            \"alias\":\
  \ \"  - leaderboard_musr_murder_mysteries\",\n            \"acc_norm,none\": 0.512,\n\
  \            \"acc_norm_stderr,none\": 0.03167708558254714\n        },\n       \
  \ \"leaderboard_musr_object_placements\": {\n            \"alias\": \"  - leaderboard_musr_object_placements\"\
  ,\n            \"acc_norm,none\": 0.27734375,\n            \"acc_norm_stderr,none\"\
  : 0.02803528549328419\n        },\n        \"leaderboard_musr_team_allocation\"\
  : {\n            \"alias\": \"  - leaderboard_musr_team_allocation\",\n        \
  \    \"acc_norm,none\": 0.272,\n            \"acc_norm_stderr,none\": 0.028200088296309975\n\
  \        }\n    },\n    \"leaderboard\": {\n        \"inst_level_loose_acc,none\"\
  : 0.3105515587529976,\n        \"inst_level_loose_acc_stderr,none\": \"N/A\",\n\
  \        \"acc_norm,none\": 0.30821118173563367,\n        \"acc_norm_stderr,none\"\
  : 0.00500914440369552,\n        \"inst_level_strict_acc,none\": 0.29856115107913667,\n\
  \        \"inst_level_strict_acc_stderr,none\": \"N/A\",\n        \"prompt_level_loose_acc,none\"\
  : 0.18853974121996303,\n        \"prompt_level_loose_acc_stderr,none\": 0.016832096060176906,\n\
  \        \"exact_match,none\": 0.0075528700906344415,\n        \"exact_match_stderr,none\"\
  : 0.0023759473096993293,\n        \"acc,none\": 0.11228390957446809,\n        \"\
  acc_stderr,none\": 0.002878358904186553,\n        \"prompt_level_strict_acc,none\"\
  : 0.1756007393715342,\n        \"prompt_level_strict_acc_stderr,none\": 0.01637325731205799,\n\
  \        \"alias\": \"leaderboard\"\n    },\n    \"leaderboard_bbh\": {\n      \
  \  \"acc_norm,none\": 0.31192501301857317,\n        \"acc_norm_stderr,none\": 0.00574749250069476,\n\
  \        \"alias\": \" - leaderboard_bbh\"\n    },\n    \"leaderboard_bbh_boolean_expressions\"\
  : {\n        \"alias\": \"  - leaderboard_bbh_boolean_expressions\",\n        \"\
  acc_norm,none\": 0.516,\n        \"acc_norm_stderr,none\": 0.03166998503010743\n\
  \    },\n    \"leaderboard_bbh_causal_judgement\": {\n        \"alias\": \"  - leaderboard_bbh_causal_judgement\"\
  ,\n        \"acc_norm,none\": 0.5133689839572193,\n        \"acc_norm_stderr,none\"\
  : 0.03664867131244299\n    },\n    \"leaderboard_bbh_date_understanding\": {\n \
  \       \"alias\": \"  - leaderboard_bbh_date_understanding\",\n        \"acc_norm,none\"\
  : 0.184,\n        \"acc_norm_stderr,none\": 0.02455581299422255\n    },\n    \"\
  leaderboard_bbh_disambiguation_qa\": {\n        \"alias\": \"  - leaderboard_bbh_disambiguation_qa\"\
  ,\n        \"acc_norm,none\": 0.3,\n        \"acc_norm_stderr,none\": 0.029040893477575783\n\
  \    },\n    \"leaderboard_bbh_formal_fallacies\": {\n        \"alias\": \"  - leaderboard_bbh_formal_fallacies\"\
  ,\n        \"acc_norm,none\": 0.468,\n        \"acc_norm_stderr,none\": 0.03162125257572558\n\
  \    },\n    \"leaderboard_bbh_geometric_shapes\": {\n        \"alias\": \"  - leaderboard_bbh_geometric_shapes\"\
  ,\n        \"acc_norm,none\": 0.084,\n        \"acc_norm_stderr,none\": 0.017578738526776348\n\
  \    },\n    \"leaderboard_bbh_hyperbaton\": {\n        \"alias\": \"  - leaderboard_bbh_hyperbaton\"\
  ,\n        \"acc_norm,none\": 0.5,\n        \"acc_norm_stderr,none\": 0.031686212526223896\n\
  \    },\n    \"leaderboard_bbh_logical_deduction_five_objects\": {\n        \"alias\"\
  : \"  - leaderboard_bbh_logical_deduction_five_objects\",\n        \"acc_norm,none\"\
  : 0.232,\n        \"acc_norm_stderr,none\": 0.026750070374865202\n    },\n    \"\
  leaderboard_bbh_logical_deduction_seven_objects\": {\n        \"alias\": \"  - leaderboard_bbh_logical_deduction_seven_objects\"\
  ,\n        \"acc_norm,none\": 0.14,\n        \"acc_norm_stderr,none\": 0.021989409645240245\n\
  \    },\n    \"leaderboard_bbh_logical_deduction_three_objects\": {\n        \"\
  alias\": \"  - leaderboard_bbh_logical_deduction_three_objects\",\n        \"acc_norm,none\"\
  : 0.34,\n        \"acc_norm_stderr,none\": 0.030020073605457873\n    },\n    \"\
  leaderboard_bbh_movie_recommendation\": {\n        \"alias\": \"  - leaderboard_bbh_movie_recommendation\"\
  ,\n        \"acc_norm,none\": 0.264,\n        \"acc_norm_stderr,none\": 0.027934518957690866\n\
  \    },\n    \"leaderboard_bbh_navigate\": {\n        \"alias\": \"  - leaderboard_bbh_navigate\"\
  ,\n        \"acc_norm,none\": 0.58,\n        \"acc_norm_stderr,none\": 0.03127799950463661\n\
  \    },\n    \"leaderboard_bbh_object_counting\": {\n        \"alias\": \"  - leaderboard_bbh_object_counting\"\
  ,\n        \"acc_norm,none\": 0.172,\n        \"acc_norm_stderr,none\": 0.02391551394448624\n\
  \    },\n    \"leaderboard_bbh_penguins_in_a_table\": {\n        \"alias\": \" \
  \ - leaderboard_bbh_penguins_in_a_table\",\n        \"acc_norm,none\": 0.21232876712328766,\n\
  \        \"acc_norm_stderr,none\": 0.03396197282917473\n    },\n    \"leaderboard_bbh_reasoning_about_colored_objects\"\
  : {\n        \"alias\": \"  - leaderboard_bbh_reasoning_about_colored_objects\"\
  ,\n        \"acc_norm,none\": 0.096,\n        \"acc_norm_stderr,none\": 0.01866896141947719\n\
  \    },\n    \"leaderboard_bbh_ruin_names\": {\n        \"alias\": \"  - leaderboard_bbh_ruin_names\"\
  ,\n        \"acc_norm,none\": 0.208,\n        \"acc_norm_stderr,none\": 0.02572139890141637\n\
  \    },\n    \"leaderboard_bbh_salient_translation_error_detection\": {\n      \
  \  \"alias\": \"  - leaderboard_bbh_salient_translation_error_detection\",\n   \
  \     \"acc_norm,none\": 0.224,\n        \"acc_norm_stderr,none\": 0.026421361687347884\n\
  \    },\n    \"leaderboard_bbh_snarks\": {\n        \"alias\": \"  - leaderboard_bbh_snarks\"\
  ,\n        \"acc_norm,none\": 0.5393258426966292,\n        \"acc_norm_stderr,none\"\
  : 0.03746587736387869\n    },\n    \"leaderboard_bbh_sports_understanding\": {\n\
  \        \"alias\": \"  - leaderboard_bbh_sports_understanding\",\n        \"acc_norm,none\"\
  : 0.552,\n        \"acc_norm_stderr,none\": 0.03151438761115348\n    },\n    \"\
  leaderboard_bbh_temporal_sequences\": {\n        \"alias\": \"  - leaderboard_bbh_temporal_sequences\"\
  ,\n        \"acc_norm,none\": 0.244,\n        \"acc_norm_stderr,none\": 0.02721799546455311\n\
  \    },\n    \"leaderboard_bbh_tracking_shuffled_objects_five_objects\": {\n   \
  \     \"alias\": \"  - leaderboard_bbh_tracking_shuffled_objects_five_objects\"\
  ,\n        \"acc_norm,none\": 0.196,\n        \"acc_norm_stderr,none\": 0.025156857313255926\n\
  \    },\n    \"leaderboard_bbh_tracking_shuffled_objects_seven_objects\": {\n  \
  \      \"alias\": \"  - leaderboard_bbh_tracking_shuffled_objects_seven_objects\"\
  ,\n        \"acc_norm,none\": 0.156,\n        \"acc_norm_stderr,none\": 0.022995023034068682\n\
  \    },\n    \"leaderboard_bbh_tracking_shuffled_objects_three_objects\": {\n  \
  \      \"alias\": \"  - leaderboard_bbh_tracking_shuffled_objects_three_objects\"\
  ,\n        \"acc_norm,none\": 0.328,\n        \"acc_norm_stderr,none\": 0.029752391824475363\n\
  \    },\n    \"leaderboard_bbh_web_of_lies\": {\n        \"alias\": \"  - leaderboard_bbh_web_of_lies\"\
  ,\n        \"acc_norm,none\": 0.512,\n        \"acc_norm_stderr,none\": 0.03167708558254714\n\
  \    },\n    \"leaderboard_gpqa\": {\n        \"acc_norm,none\": 0.26174496644295303,\n\
  \        \"acc_norm_stderr,none\": 0.012746897764299207,\n        \"alias\": \"\
  \ - leaderboard_gpqa\"\n    },\n    \"leaderboard_gpqa_diamond\": {\n        \"\
  alias\": \"  - leaderboard_gpqa_diamond\",\n        \"acc_norm,none\": 0.2727272727272727,\n\
  \        \"acc_norm_stderr,none\": 0.03173071239071728\n    },\n    \"leaderboard_gpqa_extended\"\
  : {\n        \"alias\": \"  - leaderboard_gpqa_extended\",\n        \"acc_norm,none\"\
  : 0.26373626373626374,\n        \"acc_norm_stderr,none\": 0.018875713580372433\n\
  \    },\n    \"leaderboard_gpqa_main\": {\n        \"alias\": \"  - leaderboard_gpqa_main\"\
  ,\n        \"acc_norm,none\": 0.2544642857142857,\n        \"acc_norm_stderr,none\"\
  : 0.02060126475832284\n    },\n    \"leaderboard_ifeval\": {\n        \"alias\"\
  : \" - leaderboard_ifeval\",\n        \"prompt_level_strict_acc,none\": 0.1756007393715342,\n\
  \        \"prompt_level_strict_acc_stderr,none\": 0.01637325731205799,\n       \
  \ \"inst_level_strict_acc,none\": 0.29856115107913667,\n        \"inst_level_strict_acc_stderr,none\"\
  : \"N/A\",\n        \"prompt_level_loose_acc,none\": 0.18853974121996303,\n    \
  \    \"prompt_level_loose_acc_stderr,none\": 0.016832096060176906,\n        \"inst_level_loose_acc,none\"\
  : 0.3105515587529976,\n        \"inst_level_loose_acc_stderr,none\": \"N/A\"\n \
  \   },\n    \"leaderboard_math_hard\": {\n        \"exact_match,none\": 0.0075528700906344415,\n\
  \        \"exact_match_stderr,none\": 0.0023759473096993293,\n        \"alias\"\
  : \" - leaderboard_math_hard\"\n    },\n    \"leaderboard_math_algebra_hard\": {\n\
  \        \"alias\": \"  - leaderboard_math_algebra_hard\",\n        \"exact_match,none\"\
  : 0.019543973941368076,\n        \"exact_match_stderr,none\": 0.007913339243755165\n\
  \    },\n    \"leaderboard_math_counting_and_prob_hard\": {\n        \"alias\":\
  \ \"  - leaderboard_math_counting_and_prob_hard\",\n        \"exact_match,none\"\
  : 0.008130081300813009,\n        \"exact_match_stderr,none\": 0.008130081300813007\n\
  \    },\n    \"leaderboard_math_geometry_hard\": {\n        \"alias\": \"  - leaderboard_math_geometry_hard\"\
  ,\n        \"exact_match,none\": 0.0,\n        \"exact_match_stderr,none\": 0.0\n\
  \    },\n    \"leaderboard_math_intermediate_algebra_hard\": {\n        \"alias\"\
  : \"  - leaderboard_math_intermediate_algebra_hard\",\n        \"exact_match,none\"\
  : 0.0,\n        \"exact_match_stderr,none\": 0.0\n    },\n    \"leaderboard_math_num_theory_hard\"\
  : {\n        \"alias\": \"  - leaderboard_math_num_theory_hard\",\n        \"exact_match,none\"\
  : 0.012987012987012988,\n        \"exact_match_stderr,none\": 0.009153145279150204\n\
  \    },\n    \"leaderboard_math_prealgebra_hard\": {\n        \"alias\": \"  - leaderboard_math_prealgebra_hard\"\
  ,\n        \"exact_match,none\": 0.0051813471502590676,\n        \"exact_match_stderr,none\"\
  : 0.0051813471502590676\n    },\n    \"leaderboard_math_precalculus_hard\": {\n\
  \        \"alias\": \"  - leaderboard_math_precalculus_hard\",\n        \"exact_match,none\"\
  : 0.0,\n        \"exact_match_stderr,none\": 0.0\n    },\n    \"leaderboard_mmlu_pro\"\
  : {\n        \"alias\": \" - leaderboard_mmlu_pro\",\n        \"acc,none\": 0.11228390957446809,\n\
  \        \"acc_stderr,none\": 0.002878358904186553\n    },\n    \"leaderboard_musr\"\
  : {\n        \"acc_norm,none\": 0.3531746031746032,\n        \"acc_norm_stderr,none\"\
  : 0.016935716690187123,\n        \"alias\": \" - leaderboard_musr\"\n    },\n  \
  \  \"leaderboard_musr_murder_mysteries\": {\n        \"alias\": \"  - leaderboard_musr_murder_mysteries\"\
  ,\n        \"acc_norm,none\": 0.512,\n        \"acc_norm_stderr,none\": 0.03167708558254714\n\
  \    },\n    \"leaderboard_musr_object_placements\": {\n        \"alias\": \"  -\
  \ leaderboard_musr_object_placements\",\n        \"acc_norm,none\": 0.27734375,\n\
  \        \"acc_norm_stderr,none\": 0.02803528549328419\n    },\n    \"leaderboard_musr_team_allocation\"\
  : {\n        \"alias\": \"  - leaderboard_musr_team_allocation\",\n        \"acc_norm,none\"\
  : 0.272,\n        \"acc_norm_stderr,none\": 0.028200088296309975\n    }\n}\n```"
repo_url: https://huggingface.co/EleutherAI/pythia-1.4b
leaderboard_url: ''
point_of_contact: ''
configs:
- config_name: EleutherAI__pythia-1.4b__leaderboard_bbh_boolean_expressions
  data_files:
  - split: 2025_01_28T10_22_20.980995
    path:
    - '**/samples_leaderboard_bbh_boolean_expressions_2025-01-28T10-22-20.980995.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_boolean_expressions_2025-01-28T10-22-20.980995.jsonl'
- config_name: EleutherAI__pythia-1.4b__leaderboard_bbh_causal_judgement
  data_files:
  - split: 2025_01_28T10_22_20.980995
    path:
    - '**/samples_leaderboard_bbh_causal_judgement_2025-01-28T10-22-20.980995.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_causal_judgement_2025-01-28T10-22-20.980995.jsonl'
- config_name: EleutherAI__pythia-1.4b__leaderboard_bbh_date_understanding
  data_files:
  - split: 2025_01_28T10_22_20.980995
    path:
    - '**/samples_leaderboard_bbh_date_understanding_2025-01-28T10-22-20.980995.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_date_understanding_2025-01-28T10-22-20.980995.jsonl'
- config_name: EleutherAI__pythia-1.4b__leaderboard_bbh_disambiguation_qa
  data_files:
  - split: 2025_01_28T10_22_20.980995
    path:
    - '**/samples_leaderboard_bbh_disambiguation_qa_2025-01-28T10-22-20.980995.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_disambiguation_qa_2025-01-28T10-22-20.980995.jsonl'
- config_name: EleutherAI__pythia-1.4b__leaderboard_bbh_formal_fallacies
  data_files:
  - split: 2025_01_28T10_22_20.980995
    path:
    - '**/samples_leaderboard_bbh_formal_fallacies_2025-01-28T10-22-20.980995.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_formal_fallacies_2025-01-28T10-22-20.980995.jsonl'
- config_name: EleutherAI__pythia-1.4b__leaderboard_bbh_geometric_shapes
  data_files:
  - split: 2025_01_28T10_22_20.980995
    path:
    - '**/samples_leaderboard_bbh_geometric_shapes_2025-01-28T10-22-20.980995.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_geometric_shapes_2025-01-28T10-22-20.980995.jsonl'
- config_name: EleutherAI__pythia-1.4b__leaderboard_bbh_hyperbaton
  data_files:
  - split: 2025_01_28T10_22_20.980995
    path:
    - '**/samples_leaderboard_bbh_hyperbaton_2025-01-28T10-22-20.980995.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_hyperbaton_2025-01-28T10-22-20.980995.jsonl'
- config_name: EleutherAI__pythia-1.4b__leaderboard_bbh_logical_deduction_five_objects
  data_files:
  - split: 2025_01_28T10_22_20.980995
    path:
    - '**/samples_leaderboard_bbh_logical_deduction_five_objects_2025-01-28T10-22-20.980995.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_logical_deduction_five_objects_2025-01-28T10-22-20.980995.jsonl'
- config_name: EleutherAI__pythia-1.4b__leaderboard_bbh_logical_deduction_seven_objects
  data_files:
  - split: 2025_01_28T10_22_20.980995
    path:
    - '**/samples_leaderboard_bbh_logical_deduction_seven_objects_2025-01-28T10-22-20.980995.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_logical_deduction_seven_objects_2025-01-28T10-22-20.980995.jsonl'
- config_name: EleutherAI__pythia-1.4b__leaderboard_bbh_logical_deduction_three_objects
  data_files:
  - split: 2025_01_28T10_22_20.980995
    path:
    - '**/samples_leaderboard_bbh_logical_deduction_three_objects_2025-01-28T10-22-20.980995.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_logical_deduction_three_objects_2025-01-28T10-22-20.980995.jsonl'
- config_name: EleutherAI__pythia-1.4b__leaderboard_bbh_movie_recommendation
  data_files:
  - split: 2025_01_28T10_22_20.980995
    path:
    - '**/samples_leaderboard_bbh_movie_recommendation_2025-01-28T10-22-20.980995.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_movie_recommendation_2025-01-28T10-22-20.980995.jsonl'
- config_name: EleutherAI__pythia-1.4b__leaderboard_bbh_navigate
  data_files:
  - split: 2025_01_28T10_22_20.980995
    path:
    - '**/samples_leaderboard_bbh_navigate_2025-01-28T10-22-20.980995.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_navigate_2025-01-28T10-22-20.980995.jsonl'
- config_name: EleutherAI__pythia-1.4b__leaderboard_bbh_object_counting
  data_files:
  - split: 2025_01_28T10_22_20.980995
    path:
    - '**/samples_leaderboard_bbh_object_counting_2025-01-28T10-22-20.980995.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_object_counting_2025-01-28T10-22-20.980995.jsonl'
- config_name: EleutherAI__pythia-1.4b__leaderboard_bbh_penguins_in_a_table
  data_files:
  - split: 2025_01_28T10_22_20.980995
    path:
    - '**/samples_leaderboard_bbh_penguins_in_a_table_2025-01-28T10-22-20.980995.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_penguins_in_a_table_2025-01-28T10-22-20.980995.jsonl'
- config_name: EleutherAI__pythia-1.4b__leaderboard_bbh_reasoning_about_colored_objects
  data_files:
  - split: 2025_01_28T10_22_20.980995
    path:
    - '**/samples_leaderboard_bbh_reasoning_about_colored_objects_2025-01-28T10-22-20.980995.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_reasoning_about_colored_objects_2025-01-28T10-22-20.980995.jsonl'
- config_name: EleutherAI__pythia-1.4b__leaderboard_bbh_ruin_names
  data_files:
  - split: 2025_01_28T10_22_20.980995
    path:
    - '**/samples_leaderboard_bbh_ruin_names_2025-01-28T10-22-20.980995.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_ruin_names_2025-01-28T10-22-20.980995.jsonl'
- config_name: EleutherAI__pythia-1.4b__leaderboard_bbh_salient_translation_error_detection
  data_files:
  - split: 2025_01_28T10_22_20.980995
    path:
    - '**/samples_leaderboard_bbh_salient_translation_error_detection_2025-01-28T10-22-20.980995.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_salient_translation_error_detection_2025-01-28T10-22-20.980995.jsonl'
- config_name: EleutherAI__pythia-1.4b__leaderboard_bbh_snarks
  data_files:
  - split: 2025_01_28T10_22_20.980995
    path:
    - '**/samples_leaderboard_bbh_snarks_2025-01-28T10-22-20.980995.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_snarks_2025-01-28T10-22-20.980995.jsonl'
- config_name: EleutherAI__pythia-1.4b__leaderboard_bbh_sports_understanding
  data_files:
  - split: 2025_01_28T10_22_20.980995
    path:
    - '**/samples_leaderboard_bbh_sports_understanding_2025-01-28T10-22-20.980995.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_sports_understanding_2025-01-28T10-22-20.980995.jsonl'
- config_name: EleutherAI__pythia-1.4b__leaderboard_bbh_temporal_sequences
  data_files:
  - split: 2025_01_28T10_22_20.980995
    path:
    - '**/samples_leaderboard_bbh_temporal_sequences_2025-01-28T10-22-20.980995.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_temporal_sequences_2025-01-28T10-22-20.980995.jsonl'
- config_name: EleutherAI__pythia-1.4b__leaderboard_bbh_tracking_shuffled_objects_five_objects
  data_files:
  - split: 2025_01_28T10_22_20.980995
    path:
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_five_objects_2025-01-28T10-22-20.980995.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_five_objects_2025-01-28T10-22-20.980995.jsonl'
- config_name: EleutherAI__pythia-1.4b__leaderboard_bbh_tracking_shuffled_objects_seven_objects
  data_files:
  - split: 2025_01_28T10_22_20.980995
    path:
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_seven_objects_2025-01-28T10-22-20.980995.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_seven_objects_2025-01-28T10-22-20.980995.jsonl'
- config_name: EleutherAI__pythia-1.4b__leaderboard_bbh_tracking_shuffled_objects_three_objects
  data_files:
  - split: 2025_01_28T10_22_20.980995
    path:
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_three_objects_2025-01-28T10-22-20.980995.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_three_objects_2025-01-28T10-22-20.980995.jsonl'
- config_name: EleutherAI__pythia-1.4b__leaderboard_bbh_web_of_lies
  data_files:
  - split: 2025_01_28T10_22_20.980995
    path:
    - '**/samples_leaderboard_bbh_web_of_lies_2025-01-28T10-22-20.980995.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_web_of_lies_2025-01-28T10-22-20.980995.jsonl'
- config_name: EleutherAI__pythia-1.4b__leaderboard_gpqa_diamond
  data_files:
  - split: 2025_01_28T10_22_20.980995
    path:
    - '**/samples_leaderboard_gpqa_diamond_2025-01-28T10-22-20.980995.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_gpqa_diamond_2025-01-28T10-22-20.980995.jsonl'
- config_name: EleutherAI__pythia-1.4b__leaderboard_gpqa_extended
  data_files:
  - split: 2025_01_28T10_22_20.980995
    path:
    - '**/samples_leaderboard_gpqa_extended_2025-01-28T10-22-20.980995.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_gpqa_extended_2025-01-28T10-22-20.980995.jsonl'
- config_name: EleutherAI__pythia-1.4b__leaderboard_gpqa_main
  data_files:
  - split: 2025_01_28T10_22_20.980995
    path:
    - '**/samples_leaderboard_gpqa_main_2025-01-28T10-22-20.980995.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_gpqa_main_2025-01-28T10-22-20.980995.jsonl'
- config_name: EleutherAI__pythia-1.4b__leaderboard_ifeval
  data_files:
  - split: 2025_01_28T10_22_20.980995
    path:
    - '**/samples_leaderboard_ifeval_2025-01-28T10-22-20.980995.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_ifeval_2025-01-28T10-22-20.980995.jsonl'
- config_name: EleutherAI__pythia-1.4b__leaderboard_math_algebra_hard
  data_files:
  - split: 2025_01_28T10_22_20.980995
    path:
    - '**/samples_leaderboard_math_algebra_hard_2025-01-28T10-22-20.980995.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_math_algebra_hard_2025-01-28T10-22-20.980995.jsonl'
- config_name: EleutherAI__pythia-1.4b__leaderboard_math_counting_and_prob_hard
  data_files:
  - split: 2025_01_28T10_22_20.980995
    path:
    - '**/samples_leaderboard_math_counting_and_prob_hard_2025-01-28T10-22-20.980995.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_math_counting_and_prob_hard_2025-01-28T10-22-20.980995.jsonl'
- config_name: EleutherAI__pythia-1.4b__leaderboard_math_geometry_hard
  data_files:
  - split: 2025_01_28T10_22_20.980995
    path:
    - '**/samples_leaderboard_math_geometry_hard_2025-01-28T10-22-20.980995.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_math_geometry_hard_2025-01-28T10-22-20.980995.jsonl'
- config_name: EleutherAI__pythia-1.4b__leaderboard_math_intermediate_algebra_hard
  data_files:
  - split: 2025_01_28T10_22_20.980995
    path:
    - '**/samples_leaderboard_math_intermediate_algebra_hard_2025-01-28T10-22-20.980995.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_math_intermediate_algebra_hard_2025-01-28T10-22-20.980995.jsonl'
- config_name: EleutherAI__pythia-1.4b__leaderboard_math_num_theory_hard
  data_files:
  - split: 2025_01_28T10_22_20.980995
    path:
    - '**/samples_leaderboard_math_num_theory_hard_2025-01-28T10-22-20.980995.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_math_num_theory_hard_2025-01-28T10-22-20.980995.jsonl'
- config_name: EleutherAI__pythia-1.4b__leaderboard_math_prealgebra_hard
  data_files:
  - split: 2025_01_28T10_22_20.980995
    path:
    - '**/samples_leaderboard_math_prealgebra_hard_2025-01-28T10-22-20.980995.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_math_prealgebra_hard_2025-01-28T10-22-20.980995.jsonl'
- config_name: EleutherAI__pythia-1.4b__leaderboard_math_precalculus_hard
  data_files:
  - split: 2025_01_28T10_22_20.980995
    path:
    - '**/samples_leaderboard_math_precalculus_hard_2025-01-28T10-22-20.980995.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_math_precalculus_hard_2025-01-28T10-22-20.980995.jsonl'
- config_name: EleutherAI__pythia-1.4b__leaderboard_mmlu_pro
  data_files:
  - split: 2025_01_28T10_22_20.980995
    path:
    - '**/samples_leaderboard_mmlu_pro_2025-01-28T10-22-20.980995.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_mmlu_pro_2025-01-28T10-22-20.980995.jsonl'
- config_name: EleutherAI__pythia-1.4b__leaderboard_musr_murder_mysteries
  data_files:
  - split: 2025_01_28T10_22_20.980995
    path:
    - '**/samples_leaderboard_musr_murder_mysteries_2025-01-28T10-22-20.980995.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_musr_murder_mysteries_2025-01-28T10-22-20.980995.jsonl'
- config_name: EleutherAI__pythia-1.4b__leaderboard_musr_object_placements
  data_files:
  - split: 2025_01_28T10_22_20.980995
    path:
    - '**/samples_leaderboard_musr_object_placements_2025-01-28T10-22-20.980995.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_musr_object_placements_2025-01-28T10-22-20.980995.jsonl'
- config_name: EleutherAI__pythia-1.4b__leaderboard_musr_team_allocation
  data_files:
  - split: 2025_01_28T10_22_20.980995
    path:
    - '**/samples_leaderboard_musr_team_allocation_2025-01-28T10-22-20.980995.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_musr_team_allocation_2025-01-28T10-22-20.980995.jsonl'
---

# Dataset Card for Evaluation run of EleutherAI/pythia-1.4b

<!-- Provide a quick summary of the dataset. -->

Dataset automatically created during the evaluation run of model [EleutherAI/pythia-1.4b](https://huggingface.co/EleutherAI/pythia-1.4b)
The dataset is composed of 38 configuration(s), each one corresponding to one of the evaluated task.

The dataset has been created from 1 run(s). Each run can be found as a specific split in each configuration, the split being named using the timestamp of the run.The "train" split is always pointing to the latest results.

An additional configuration "results" store all the aggregated results of the run.

To load the details from a run, you can for instance do the following:
```python
from datasets import load_dataset
data = load_dataset(
	"open-llm-leaderboard/EleutherAI__pythia-1.4b-details",
	name="EleutherAI__pythia-1.4b__leaderboard_bbh_boolean_expressions",
	split="latest"
)
```

## Latest results

These are the [latest results from run 2025-01-28T10-22-20.980995](https://huggingface.co/datasets/open-llm-leaderboard/EleutherAI__pythia-1.4b-details/blob/main/EleutherAI__pythia-1.4b/results_2025-01-28T10-22-20.980995.json) (note that there might be results for other tasks in the repos if successive evals didn't cover the same tasks. You find each in the results and the "latest" split for each eval):

```python
{
    "all": {
        "leaderboard": {
            "inst_level_loose_acc,none": 0.3105515587529976,
            "inst_level_loose_acc_stderr,none": "N/A",
            "acc_norm,none": 0.30821118173563367,
            "acc_norm_stderr,none": 0.00500914440369552,
            "inst_level_strict_acc,none": 0.29856115107913667,
            "inst_level_strict_acc_stderr,none": "N/A",
            "prompt_level_loose_acc,none": 0.18853974121996303,
            "prompt_level_loose_acc_stderr,none": 0.016832096060176906,
            "exact_match,none": 0.0075528700906344415,
            "exact_match_stderr,none": 0.0023759473096993293,
            "acc,none": 0.11228390957446809,
            "acc_stderr,none": 0.002878358904186553,
            "prompt_level_strict_acc,none": 0.1756007393715342,
            "prompt_level_strict_acc_stderr,none": 0.01637325731205799,
            "alias": "leaderboard"
        },
        "leaderboard_bbh": {
            "acc_norm,none": 0.31192501301857317,
            "acc_norm_stderr,none": 0.00574749250069476,
            "alias": " - leaderboard_bbh"
        },
        "leaderboard_bbh_boolean_expressions": {
            "alias": "  - leaderboard_bbh_boolean_expressions",
            "acc_norm,none": 0.516,
            "acc_norm_stderr,none": 0.03166998503010743
        },
        "leaderboard_bbh_causal_judgement": {
            "alias": "  - leaderboard_bbh_causal_judgement",
            "acc_norm,none": 0.5133689839572193,
            "acc_norm_stderr,none": 0.03664867131244299
        },
        "leaderboard_bbh_date_understanding": {
            "alias": "  - leaderboard_bbh_date_understanding",
            "acc_norm,none": 0.184,
            "acc_norm_stderr,none": 0.02455581299422255
        },
        "leaderboard_bbh_disambiguation_qa": {
            "alias": "  - leaderboard_bbh_disambiguation_qa",
            "acc_norm,none": 0.3,
            "acc_norm_stderr,none": 0.029040893477575783
        },
        "leaderboard_bbh_formal_fallacies": {
            "alias": "  - leaderboard_bbh_formal_fallacies",
            "acc_norm,none": 0.468,
            "acc_norm_stderr,none": 0.03162125257572558
        },
        "leaderboard_bbh_geometric_shapes": {
            "alias": "  - leaderboard_bbh_geometric_shapes",
            "acc_norm,none": 0.084,
            "acc_norm_stderr,none": 0.017578738526776348
        },
        "leaderboard_bbh_hyperbaton": {
            "alias": "  - leaderboard_bbh_hyperbaton",
            "acc_norm,none": 0.5,
            "acc_norm_stderr,none": 0.031686212526223896
        },
        "leaderboard_bbh_logical_deduction_five_objects": {
            "alias": "  - leaderboard_bbh_logical_deduction_five_objects",
            "acc_norm,none": 0.232,
            "acc_norm_stderr,none": 0.026750070374865202
        },
        "leaderboard_bbh_logical_deduction_seven_objects": {
            "alias": "  - leaderboard_bbh_logical_deduction_seven_objects",
            "acc_norm,none": 0.14,
            "acc_norm_stderr,none": 0.021989409645240245
        },
        "leaderboard_bbh_logical_deduction_three_objects": {
            "alias": "  - leaderboard_bbh_logical_deduction_three_objects",
            "acc_norm,none": 0.34,
            "acc_norm_stderr,none": 0.030020073605457873
        },
        "leaderboard_bbh_movie_recommendation": {
            "alias": "  - leaderboard_bbh_movie_recommendation",
            "acc_norm,none": 0.264,
            "acc_norm_stderr,none": 0.027934518957690866
        },
        "leaderboard_bbh_navigate": {
            "alias": "  - leaderboard_bbh_navigate",
            "acc_norm,none": 0.58,
            "acc_norm_stderr,none": 0.03127799950463661
        },
        "leaderboard_bbh_object_counting": {
            "alias": "  - leaderboard_bbh_object_counting",
            "acc_norm,none": 0.172,
            "acc_norm_stderr,none": 0.02391551394448624
        },
        "leaderboard_bbh_penguins_in_a_table": {
            "alias": "  - leaderboard_bbh_penguins_in_a_table",
            "acc_norm,none": 0.21232876712328766,
            "acc_norm_stderr,none": 0.03396197282917473
        },
        "leaderboard_bbh_reasoning_about_colored_objects": {
            "alias": "  - leaderboard_bbh_reasoning_about_colored_objects",
            "acc_norm,none": 0.096,
            "acc_norm_stderr,none": 0.01866896141947719
        },
        "leaderboard_bbh_ruin_names": {
            "alias": "  - leaderboard_bbh_ruin_names",
            "acc_norm,none": 0.208,
            "acc_norm_stderr,none": 0.02572139890141637
        },
        "leaderboard_bbh_salient_translation_error_detection": {
            "alias": "  - leaderboard_bbh_salient_translation_error_detection",
            "acc_norm,none": 0.224,
            "acc_norm_stderr,none": 0.026421361687347884
        },
        "leaderboard_bbh_snarks": {
            "alias": "  - leaderboard_bbh_snarks",
            "acc_norm,none": 0.5393258426966292,
            "acc_norm_stderr,none": 0.03746587736387869
        },
        "leaderboard_bbh_sports_understanding": {
            "alias": "  - leaderboard_bbh_sports_understanding",
            "acc_norm,none": 0.552,
            "acc_norm_stderr,none": 0.03151438761115348
        },
        "leaderboard_bbh_temporal_sequences": {
            "alias": "  - leaderboard_bbh_temporal_sequences",
            "acc_norm,none": 0.244,
            "acc_norm_stderr,none": 0.02721799546455311
        },
        "leaderboard_bbh_tracking_shuffled_objects_five_objects": {
            "alias": "  - leaderboard_bbh_tracking_shuffled_objects_five_objects",
            "acc_norm,none": 0.196,
            "acc_norm_stderr,none": 0.025156857313255926
        },
        "leaderboard_bbh_tracking_shuffled_objects_seven_objects": {
            "alias": "  - leaderboard_bbh_tracking_shuffled_objects_seven_objects",
            "acc_norm,none": 0.156,
            "acc_norm_stderr,none": 0.022995023034068682
        },
        "leaderboard_bbh_tracking_shuffled_objects_three_objects": {
            "alias": "  - leaderboard_bbh_tracking_shuffled_objects_three_objects",
            "acc_norm,none": 0.328,
            "acc_norm_stderr,none": 0.029752391824475363
        },
        "leaderboard_bbh_web_of_lies": {
            "alias": "  - leaderboard_bbh_web_of_lies",
            "acc_norm,none": 0.512,
            "acc_norm_stderr,none": 0.03167708558254714
        },
        "leaderboard_gpqa": {
            "acc_norm,none": 0.26174496644295303,
            "acc_norm_stderr,none": 0.012746897764299207,
            "alias": " - leaderboard_gpqa"
        },
        "leaderboard_gpqa_diamond": {
            "alias": "  - leaderboard_gpqa_diamond",
            "acc_norm,none": 0.2727272727272727,
            "acc_norm_stderr,none": 0.03173071239071728
        },
        "leaderboard_gpqa_extended": {
            "alias": "  - leaderboard_gpqa_extended",
            "acc_norm,none": 0.26373626373626374,
            "acc_norm_stderr,none": 0.018875713580372433
        },
        "leaderboard_gpqa_main": {
            "alias": "  - leaderboard_gpqa_main",
            "acc_norm,none": 0.2544642857142857,
            "acc_norm_stderr,none": 0.02060126475832284
        },
        "leaderboard_ifeval": {
            "alias": " - leaderboard_ifeval",
            "prompt_level_strict_acc,none": 0.1756007393715342,
            "prompt_level_strict_acc_stderr,none": 0.01637325731205799,
            "inst_level_strict_acc,none": 0.29856115107913667,
            "inst_level_strict_acc_stderr,none": "N/A",
            "prompt_level_loose_acc,none": 0.18853974121996303,
            "prompt_level_loose_acc_stderr,none": 0.016832096060176906,
            "inst_level_loose_acc,none": 0.3105515587529976,
            "inst_level_loose_acc_stderr,none": "N/A"
        },
        "leaderboard_math_hard": {
            "exact_match,none": 0.0075528700906344415,
            "exact_match_stderr,none": 0.0023759473096993293,
            "alias": " - leaderboard_math_hard"
        },
        "leaderboard_math_algebra_hard": {
            "alias": "  - leaderboard_math_algebra_hard",
            "exact_match,none": 0.019543973941368076,
            "exact_match_stderr,none": 0.007913339243755165
        },
        "leaderboard_math_counting_and_prob_hard": {
            "alias": "  - leaderboard_math_counting_and_prob_hard",
            "exact_match,none": 0.008130081300813009,
            "exact_match_stderr,none": 0.008130081300813007
        },
        "leaderboard_math_geometry_hard": {
            "alias": "  - leaderboard_math_geometry_hard",
            "exact_match,none": 0.0,
            "exact_match_stderr,none": 0.0
        },
        "leaderboard_math_intermediate_algebra_hard": {
            "alias": "  - leaderboard_math_intermediate_algebra_hard",
            "exact_match,none": 0.0,
            "exact_match_stderr,none": 0.0
        },
        "leaderboard_math_num_theory_hard": {
            "alias": "  - leaderboard_math_num_theory_hard",
            "exact_match,none": 0.012987012987012988,
            "exact_match_stderr,none": 0.009153145279150204
        },
        "leaderboard_math_prealgebra_hard": {
            "alias": "  - leaderboard_math_prealgebra_hard",
            "exact_match,none": 0.0051813471502590676,
            "exact_match_stderr,none": 0.0051813471502590676
        },
        "leaderboard_math_precalculus_hard": {
            "alias": "  - leaderboard_math_precalculus_hard",
            "exact_match,none": 0.0,
            "exact_match_stderr,none": 0.0
        },
        "leaderboard_mmlu_pro": {
            "alias": " - leaderboard_mmlu_pro",
            "acc,none": 0.11228390957446809,
            "acc_stderr,none": 0.002878358904186553
        },
        "leaderboard_musr": {
            "acc_norm,none": 0.3531746031746032,
            "acc_norm_stderr,none": 0.016935716690187123,
            "alias": " - leaderboard_musr"
        },
        "leaderboard_musr_murder_mysteries": {
            "alias": "  - leaderboard_musr_murder_mysteries",
            "acc_norm,none": 0.512,
            "acc_norm_stderr,none": 0.03167708558254714
        },
        "leaderboard_musr_object_placements": {
            "alias": "  - leaderboard_musr_object_placements",
            "acc_norm,none": 0.27734375,
            "acc_norm_stderr,none": 0.02803528549328419
        },
        "leaderboard_musr_team_allocation": {
            "alias": "  - leaderboard_musr_team_allocation",
            "acc_norm,none": 0.272,
            "acc_norm_stderr,none": 0.028200088296309975
        }
    },
    "leaderboard": {
        "inst_level_loose_acc,none": 0.3105515587529976,
        "inst_level_loose_acc_stderr,none": "N/A",
        "acc_norm,none": 0.30821118173563367,
        "acc_norm_stderr,none": 0.00500914440369552,
        "inst_level_strict_acc,none": 0.29856115107913667,
        "inst_level_strict_acc_stderr,none": "N/A",
        "prompt_level_loose_acc,none": 0.18853974121996303,
        "prompt_level_loose_acc_stderr,none": 0.016832096060176906,
        "exact_match,none": 0.0075528700906344415,
        "exact_match_stderr,none": 0.0023759473096993293,
        "acc,none": 0.11228390957446809,
        "acc_stderr,none": 0.002878358904186553,
        "prompt_level_strict_acc,none": 0.1756007393715342,
        "prompt_level_strict_acc_stderr,none": 0.01637325731205799,
        "alias": "leaderboard"
    },
    "leaderboard_bbh": {
        "acc_norm,none": 0.31192501301857317,
        "acc_norm_stderr,none": 0.00574749250069476,
        "alias": " - leaderboard_bbh"
    },
    "leaderboard_bbh_boolean_expressions": {
        "alias": "  - leaderboard_bbh_boolean_expressions",
        "acc_norm,none": 0.516,
        "acc_norm_stderr,none": 0.03166998503010743
    },
    "leaderboard_bbh_causal_judgement": {
        "alias": "  - leaderboard_bbh_causal_judgement",
        "acc_norm,none": 0.5133689839572193,
        "acc_norm_stderr,none": 0.03664867131244299
    },
    "leaderboard_bbh_date_understanding": {
        "alias": "  - leaderboard_bbh_date_understanding",
        "acc_norm,none": 0.184,
        "acc_norm_stderr,none": 0.02455581299422255
    },
    "leaderboard_bbh_disambiguation_qa": {
        "alias": "  - leaderboard_bbh_disambiguation_qa",
        "acc_norm,none": 0.3,
        "acc_norm_stderr,none": 0.029040893477575783
    },
    "leaderboard_bbh_formal_fallacies": {
        "alias": "  - leaderboard_bbh_formal_fallacies",
        "acc_norm,none": 0.468,
        "acc_norm_stderr,none": 0.03162125257572558
    },
    "leaderboard_bbh_geometric_shapes": {
        "alias": "  - leaderboard_bbh_geometric_shapes",
        "acc_norm,none": 0.084,
        "acc_norm_stderr,none": 0.017578738526776348
    },
    "leaderboard_bbh_hyperbaton": {
        "alias": "  - leaderboard_bbh_hyperbaton",
        "acc_norm,none": 0.5,
        "acc_norm_stderr,none": 0.031686212526223896
    },
    "leaderboard_bbh_logical_deduction_five_objects": {
        "alias": "  - leaderboard_bbh_logical_deduction_five_objects",
        "acc_norm,none": 0.232,
        "acc_norm_stderr,none": 0.026750070374865202
    },
    "leaderboard_bbh_logical_deduction_seven_objects": {
        "alias": "  - leaderboard_bbh_logical_deduction_seven_objects",
        "acc_norm,none": 0.14,
        "acc_norm_stderr,none": 0.021989409645240245
    },
    "leaderboard_bbh_logical_deduction_three_objects": {
        "alias": "  - leaderboard_bbh_logical_deduction_three_objects",
        "acc_norm,none": 0.34,
        "acc_norm_stderr,none": 0.030020073605457873
    },
    "leaderboard_bbh_movie_recommendation": {
        "alias": "  - leaderboard_bbh_movie_recommendation",
        "acc_norm,none": 0.264,
        "acc_norm_stderr,none": 0.027934518957690866
    },
    "leaderboard_bbh_navigate": {
        "alias": "  - leaderboard_bbh_navigate",
        "acc_norm,none": 0.58,
        "acc_norm_stderr,none": 0.03127799950463661
    },
    "leaderboard_bbh_object_counting": {
        "alias": "  - leaderboard_bbh_object_counting",
        "acc_norm,none": 0.172,
        "acc_norm_stderr,none": 0.02391551394448624
    },
    "leaderboard_bbh_penguins_in_a_table": {
        "alias": "  - leaderboard_bbh_penguins_in_a_table",
        "acc_norm,none": 0.21232876712328766,
        "acc_norm_stderr,none": 0.03396197282917473
    },
    "leaderboard_bbh_reasoning_about_colored_objects": {
        "alias": "  - leaderboard_bbh_reasoning_about_colored_objects",
        "acc_norm,none": 0.096,
        "acc_norm_stderr,none": 0.01866896141947719
    },
    "leaderboard_bbh_ruin_names": {
        "alias": "  - leaderboard_bbh_ruin_names",
        "acc_norm,none": 0.208,
        "acc_norm_stderr,none": 0.02572139890141637
    },
    "leaderboard_bbh_salient_translation_error_detection": {
        "alias": "  - leaderboard_bbh_salient_translation_error_detection",
        "acc_norm,none": 0.224,
        "acc_norm_stderr,none": 0.026421361687347884
    },
    "leaderboard_bbh_snarks": {
        "alias": "  - leaderboard_bbh_snarks",
        "acc_norm,none": 0.5393258426966292,
        "acc_norm_stderr,none": 0.03746587736387869
    },
    "leaderboard_bbh_sports_understanding": {
        "alias": "  - leaderboard_bbh_sports_understanding",
        "acc_norm,none": 0.552,
        "acc_norm_stderr,none": 0.03151438761115348
    },
    "leaderboard_bbh_temporal_sequences": {
        "alias": "  - leaderboard_bbh_temporal_sequences",
        "acc_norm,none": 0.244,
        "acc_norm_stderr,none": 0.02721799546455311
    },
    "leaderboard_bbh_tracking_shuffled_objects_five_objects": {
        "alias": "  - leaderboard_bbh_tracking_shuffled_objects_five_objects",
        "acc_norm,none": 0.196,
        "acc_norm_stderr,none": 0.025156857313255926
    },
    "leaderboard_bbh_tracking_shuffled_objects_seven_objects": {
        "alias": "  - leaderboard_bbh_tracking_shuffled_objects_seven_objects",
        "acc_norm,none": 0.156,
        "acc_norm_stderr,none": 0.022995023034068682
    },
    "leaderboard_bbh_tracking_shuffled_objects_three_objects": {
        "alias": "  - leaderboard_bbh_tracking_shuffled_objects_three_objects",
        "acc_norm,none": 0.328,
        "acc_norm_stderr,none": 0.029752391824475363
    },
    "leaderboard_bbh_web_of_lies": {
        "alias": "  - leaderboard_bbh_web_of_lies",
        "acc_norm,none": 0.512,
        "acc_norm_stderr,none": 0.03167708558254714
    },
    "leaderboard_gpqa": {
        "acc_norm,none": 0.26174496644295303,
        "acc_norm_stderr,none": 0.012746897764299207,
        "alias": " - leaderboard_gpqa"
    },
    "leaderboard_gpqa_diamond": {
        "alias": "  - leaderboard_gpqa_diamond",
        "acc_norm,none": 0.2727272727272727,
        "acc_norm_stderr,none": 0.03173071239071728
    },
    "leaderboard_gpqa_extended": {
        "alias": "  - leaderboard_gpqa_extended",
        "acc_norm,none": 0.26373626373626374,
        "acc_norm_stderr,none": 0.018875713580372433
    },
    "leaderboard_gpqa_main": {
        "alias": "  - leaderboard_gpqa_main",
        "acc_norm,none": 0.2544642857142857,
        "acc_norm_stderr,none": 0.02060126475832284
    },
    "leaderboard_ifeval": {
        "alias": " - leaderboard_ifeval",
        "prompt_level_strict_acc,none": 0.1756007393715342,
        "prompt_level_strict_acc_stderr,none": 0.01637325731205799,
        "inst_level_strict_acc,none": 0.29856115107913667,
        "inst_level_strict_acc_stderr,none": "N/A",
        "prompt_level_loose_acc,none": 0.18853974121996303,
        "prompt_level_loose_acc_stderr,none": 0.016832096060176906,
        "inst_level_loose_acc,none": 0.3105515587529976,
        "inst_level_loose_acc_stderr,none": "N/A"
    },
    "leaderboard_math_hard": {
        "exact_match,none": 0.0075528700906344415,
        "exact_match_stderr,none": 0.0023759473096993293,
        "alias": " - leaderboard_math_hard"
    },
    "leaderboard_math_algebra_hard": {
        "alias": "  - leaderboard_math_algebra_hard",
        "exact_match,none": 0.019543973941368076,
        "exact_match_stderr,none": 0.007913339243755165
    },
    "leaderboard_math_counting_and_prob_hard": {
        "alias": "  - leaderboard_math_counting_and_prob_hard",
        "exact_match,none": 0.008130081300813009,
        "exact_match_stderr,none": 0.008130081300813007
    },
    "leaderboard_math_geometry_hard": {
        "alias": "  - leaderboard_math_geometry_hard",
        "exact_match,none": 0.0,
        "exact_match_stderr,none": 0.0
    },
    "leaderboard_math_intermediate_algebra_hard": {
        "alias": "  - leaderboard_math_intermediate_algebra_hard",
        "exact_match,none": 0.0,
        "exact_match_stderr,none": 0.0
    },
    "leaderboard_math_num_theory_hard": {
        "alias": "  - leaderboard_math_num_theory_hard",
        "exact_match,none": 0.012987012987012988,
        "exact_match_stderr,none": 0.009153145279150204
    },
    "leaderboard_math_prealgebra_hard": {
        "alias": "  - leaderboard_math_prealgebra_hard",
        "exact_match,none": 0.0051813471502590676,
        "exact_match_stderr,none": 0.0051813471502590676
    },
    "leaderboard_math_precalculus_hard": {
        "alias": "  - leaderboard_math_precalculus_hard",
        "exact_match,none": 0.0,
        "exact_match_stderr,none": 0.0
    },
    "leaderboard_mmlu_pro": {
        "alias": " - leaderboard_mmlu_pro",
        "acc,none": 0.11228390957446809,
        "acc_stderr,none": 0.002878358904186553
    },
    "leaderboard_musr": {
        "acc_norm,none": 0.3531746031746032,
        "acc_norm_stderr,none": 0.016935716690187123,
        "alias": " - leaderboard_musr"
    },
    "leaderboard_musr_murder_mysteries": {
        "alias": "  - leaderboard_musr_murder_mysteries",
        "acc_norm,none": 0.512,
        "acc_norm_stderr,none": 0.03167708558254714
    },
    "leaderboard_musr_object_placements": {
        "alias": "  - leaderboard_musr_object_placements",
        "acc_norm,none": 0.27734375,
        "acc_norm_stderr,none": 0.02803528549328419
    },
    "leaderboard_musr_team_allocation": {
        "alias": "  - leaderboard_musr_team_allocation",
        "acc_norm,none": 0.272,
        "acc_norm_stderr,none": 0.028200088296309975
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