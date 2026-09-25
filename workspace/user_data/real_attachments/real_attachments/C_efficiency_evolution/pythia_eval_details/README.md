---
pretty_name: Evaluation run of EleutherAI/pythia-1b
dataset_summary: "Dataset automatically created during the evaluation run of model\
  \ [EleutherAI/pythia-1b](https://huggingface.co/EleutherAI/pythia-1b)\nThe dataset\
  \ is composed of 38 configuration(s), each one corresponding to one of the evaluated\
  \ task.\n\nThe dataset has been created from 1 run(s). Each run can be found as\
  \ a specific split in each configuration, the split being named using the timestamp\
  \ of the run.The \"train\" split is always pointing to the latest results.\n\nAn\
  \ additional configuration \"results\" store all the aggregated results of the run.\n\
  \nTo load the details from a run, you can for instance do the following:\n```python\n\
  from datasets import load_dataset\ndata = load_dataset(\n\t\"open-llm-leaderboard/EleutherAI__pythia-1b-details\"\
  ,\n\tname=\"EleutherAI__pythia-1b__leaderboard_bbh_boolean_expressions\",\n\tsplit=\"\
  latest\"\n)\n```\n\n## Latest results\n\nThese are the [latest results from run\
  \ 2025-01-27T10-10-36.877664](https://huggingface.co/datasets/open-llm-leaderboard/EleutherAI__pythia-1b-details/blob/main/EleutherAI__pythia-1b/results_2025-01-27T10-10-36.877664.json)\
  \ (note that there might be results for other tasks in the repos if successive evals\
  \ didn't cover the same tasks. You find each in the results and the \"latest\" split\
  \ for each eval):\n\n```python\n{\n    \"all\": {\n        \"leaderboard\": {\n\
  \            \"acc_norm,none\": 0.29640679724996755,\n            \"acc_norm_stderr,none\"\
  : 0.004985063132748098,\n            \"inst_level_loose_acc,none\": 0.2865707434052758,\n\
  \            \"inst_level_loose_acc_stderr,none\": \"N/A\",\n            \"prompt_level_strict_acc,none\"\
  : 0.16820702402957485,\n            \"prompt_level_strict_acc_stderr,none\": 0.01609655018806301,\n\
  \            \"acc,none\": 0.11361369680851063,\n            \"acc_stderr,none\"\
  : 0.002893183639282246,\n            \"exact_match,none\": 0.0030211480362537764,\n\
  \            \"exact_match_stderr,none\": 0.001510453653531021,\n            \"\
  inst_level_strict_acc,none\": 0.2733812949640288,\n            \"inst_level_strict_acc_stderr,none\"\
  : \"N/A\",\n            \"prompt_level_loose_acc,none\": 0.1756007393715342,\n \
  \           \"prompt_level_loose_acc_stderr,none\": 0.01637325731205799,\n     \
  \       \"alias\": \"leaderboard\"\n        },\n        \"leaderboard_bbh\": {\n\
  \            \"acc_norm,none\": 0.29699704912341607,\n            \"acc_norm_stderr,none\"\
  : 0.005711255426751417,\n            \"alias\": \" - leaderboard_bbh\"\n       \
  \ },\n        \"leaderboard_bbh_boolean_expressions\": {\n            \"alias\"\
  : \"  - leaderboard_bbh_boolean_expressions\",\n            \"acc_norm,none\": 0.468,\n\
  \            \"acc_norm_stderr,none\": 0.03162125257572558\n        },\n       \
  \ \"leaderboard_bbh_causal_judgement\": {\n            \"alias\": \"  - leaderboard_bbh_causal_judgement\"\
  ,\n            \"acc_norm,none\": 0.5187165775401069,\n            \"acc_norm_stderr,none\"\
  : 0.03663608375537843\n        },\n        \"leaderboard_bbh_date_understanding\"\
  : {\n            \"alias\": \"  - leaderboard_bbh_date_understanding\",\n      \
  \      \"acc_norm,none\": 0.204,\n            \"acc_norm_stderr,none\": 0.025537121574548162\n\
  \        },\n        \"leaderboard_bbh_disambiguation_qa\": {\n            \"alias\"\
  : \"  - leaderboard_bbh_disambiguation_qa\",\n            \"acc_norm,none\": 0.332,\n\
  \            \"acc_norm_stderr,none\": 0.029844039047465857\n        },\n      \
  \  \"leaderboard_bbh_formal_fallacies\": {\n            \"alias\": \"  - leaderboard_bbh_formal_fallacies\"\
  ,\n            \"acc_norm,none\": 0.468,\n            \"acc_norm_stderr,none\":\
  \ 0.03162125257572558\n        },\n        \"leaderboard_bbh_geometric_shapes\"\
  : {\n            \"alias\": \"  - leaderboard_bbh_geometric_shapes\",\n        \
  \    \"acc_norm,none\": 0.108,\n            \"acc_norm_stderr,none\": 0.019669559381568776\n\
  \        },\n        \"leaderboard_bbh_hyperbaton\": {\n            \"alias\": \"\
  \  - leaderboard_bbh_hyperbaton\",\n            \"acc_norm,none\": 0.512,\n    \
  \        \"acc_norm_stderr,none\": 0.03167708558254714\n        },\n        \"leaderboard_bbh_logical_deduction_five_objects\"\
  : {\n            \"alias\": \"  - leaderboard_bbh_logical_deduction_five_objects\"\
  ,\n            \"acc_norm,none\": 0.204,\n            \"acc_norm_stderr,none\":\
  \ 0.025537121574548162\n        },\n        \"leaderboard_bbh_logical_deduction_seven_objects\"\
  : {\n            \"alias\": \"  - leaderboard_bbh_logical_deduction_seven_objects\"\
  ,\n            \"acc_norm,none\": 0.128,\n            \"acc_norm_stderr,none\":\
  \ 0.021172081336336534\n        },\n        \"leaderboard_bbh_logical_deduction_three_objects\"\
  : {\n            \"alias\": \"  - leaderboard_bbh_logical_deduction_three_objects\"\
  ,\n            \"acc_norm,none\": 0.36,\n            \"acc_norm_stderr,none\": 0.03041876402517494\n\
  \        },\n        \"leaderboard_bbh_movie_recommendation\": {\n            \"\
  alias\": \"  - leaderboard_bbh_movie_recommendation\",\n            \"acc_norm,none\"\
  : 0.24,\n            \"acc_norm_stderr,none\": 0.027065293652238982\n        },\n\
  \        \"leaderboard_bbh_navigate\": {\n            \"alias\": \"  - leaderboard_bbh_navigate\"\
  ,\n            \"acc_norm,none\": 0.44,\n            \"acc_norm_stderr,none\": 0.03145724452223569\n\
  \        },\n        \"leaderboard_bbh_object_counting\": {\n            \"alias\"\
  : \"  - leaderboard_bbh_object_counting\",\n            \"acc_norm,none\": 0.072,\n\
  \            \"acc_norm_stderr,none\": 0.016381005750490122\n        },\n      \
  \  \"leaderboard_bbh_penguins_in_a_table\": {\n            \"alias\": \"  - leaderboard_bbh_penguins_in_a_table\"\
  ,\n            \"acc_norm,none\": 0.1917808219178082,\n            \"acc_norm_stderr,none\"\
  : 0.032695137069847634\n        },\n        \"leaderboard_bbh_reasoning_about_colored_objects\"\
  : {\n            \"alias\": \"  - leaderboard_bbh_reasoning_about_colored_objects\"\
  ,\n            \"acc_norm,none\": 0.104,\n            \"acc_norm_stderr,none\":\
  \ 0.019345100974843932\n        },\n        \"leaderboard_bbh_ruin_names\": {\n\
  \            \"alias\": \"  - leaderboard_bbh_ruin_names\",\n            \"acc_norm,none\"\
  : 0.2,\n            \"acc_norm_stderr,none\": 0.02534897002097912\n        },\n\
  \        \"leaderboard_bbh_salient_translation_error_detection\": {\n          \
  \  \"alias\": \"  - leaderboard_bbh_salient_translation_error_detection\",\n   \
  \         \"acc_norm,none\": 0.224,\n            \"acc_norm_stderr,none\": 0.026421361687347884\n\
  \        },\n        \"leaderboard_bbh_snarks\": {\n            \"alias\": \"  -\
  \ leaderboard_bbh_snarks\",\n            \"acc_norm,none\": 0.5393258426966292,\n\
  \            \"acc_norm_stderr,none\": 0.03746587736387869\n        },\n       \
  \ \"leaderboard_bbh_sports_understanding\": {\n            \"alias\": \"  - leaderboard_bbh_sports_understanding\"\
  ,\n            \"acc_norm,none\": 0.46,\n            \"acc_norm_stderr,none\": 0.031584653891499004\n\
  \        },\n        \"leaderboard_bbh_temporal_sequences\": {\n            \"alias\"\
  : \"  - leaderboard_bbh_temporal_sequences\",\n            \"acc_norm,none\": 0.26,\n\
  \            \"acc_norm_stderr,none\": 0.027797315752644335\n        },\n      \
  \  \"leaderboard_bbh_tracking_shuffled_objects_five_objects\": {\n            \"\
  alias\": \"  - leaderboard_bbh_tracking_shuffled_objects_five_objects\",\n     \
  \       \"acc_norm,none\": 0.2,\n            \"acc_norm_stderr,none\": 0.02534897002097912\n\
  \        },\n        \"leaderboard_bbh_tracking_shuffled_objects_seven_objects\"\
  : {\n            \"alias\": \"  - leaderboard_bbh_tracking_shuffled_objects_seven_objects\"\
  ,\n            \"acc_norm,none\": 0.16,\n            \"acc_norm_stderr,none\": 0.023232714782060626\n\
  \        },\n        \"leaderboard_bbh_tracking_shuffled_objects_three_objects\"\
  : {\n            \"alias\": \"  - leaderboard_bbh_tracking_shuffled_objects_three_objects\"\
  ,\n            \"acc_norm,none\": 0.32,\n            \"acc_norm_stderr,none\": 0.029561724955240978\n\
  \        },\n        \"leaderboard_bbh_web_of_lies\": {\n            \"alias\":\
  \ \"  - leaderboard_bbh_web_of_lies\",\n            \"acc_norm,none\": 0.496,\n\
  \            \"acc_norm_stderr,none\": 0.0316851985511992\n        },\n        \"\
  leaderboard_gpqa\": {\n            \"acc_norm,none\": 0.25671140939597314,\n   \
  \         \"acc_norm_stderr,none\": 0.012664923317255711,\n            \"alias\"\
  : \" - leaderboard_gpqa\"\n        },\n        \"leaderboard_gpqa_diamond\": {\n\
  \            \"alias\": \"  - leaderboard_gpqa_diamond\",\n            \"acc_norm,none\"\
  : 0.2727272727272727,\n            \"acc_norm_stderr,none\": 0.03173071239071728\n\
  \        },\n        \"leaderboard_gpqa_extended\": {\n            \"alias\": \"\
  \  - leaderboard_gpqa_extended\",\n            \"acc_norm,none\": 0.2600732600732601,\n\
  \            \"acc_norm_stderr,none\": 0.018790743352015988\n        },\n      \
  \  \"leaderboard_gpqa_main\": {\n            \"alias\": \"  - leaderboard_gpqa_main\"\
  ,\n            \"acc_norm,none\": 0.24553571428571427,\n            \"acc_norm_stderr,none\"\
  : 0.020357428454484603\n        },\n        \"leaderboard_ifeval\": {\n        \
  \    \"alias\": \" - leaderboard_ifeval\",\n            \"prompt_level_strict_acc,none\"\
  : 0.16820702402957485,\n            \"prompt_level_strict_acc_stderr,none\": 0.016096550188063007,\n\
  \            \"inst_level_strict_acc,none\": 0.2733812949640288,\n            \"\
  inst_level_strict_acc_stderr,none\": \"N/A\",\n            \"prompt_level_loose_acc,none\"\
  : 0.1756007393715342,\n            \"prompt_level_loose_acc_stderr,none\": 0.01637325731205799,\n\
  \            \"inst_level_loose_acc,none\": 0.2865707434052758,\n            \"\
  inst_level_loose_acc_stderr,none\": \"N/A\"\n        },\n        \"leaderboard_math_hard\"\
  : {\n            \"exact_match,none\": 0.0030211480362537764,\n            \"exact_match_stderr,none\"\
  : 0.001510453653531021,\n            \"alias\": \" - leaderboard_math_hard\"\n \
  \       },\n        \"leaderboard_math_algebra_hard\": {\n            \"alias\"\
  : \"  - leaderboard_math_algebra_hard\",\n            \"exact_match,none\": 0.006514657980456026,\n\
  \            \"exact_match_stderr,none\": 0.004599025618546258\n        },\n   \
  \     \"leaderboard_math_counting_and_prob_hard\": {\n            \"alias\": \"\
  \  - leaderboard_math_counting_and_prob_hard\",\n            \"exact_match,none\"\
  : 0.0,\n            \"exact_match_stderr,none\": 0.0\n        },\n        \"leaderboard_math_geometry_hard\"\
  : {\n            \"alias\": \"  - leaderboard_math_geometry_hard\",\n          \
  \  \"exact_match,none\": 0.0,\n            \"exact_match_stderr,none\": 0.0\n  \
  \      },\n        \"leaderboard_math_intermediate_algebra_hard\": {\n         \
  \   \"alias\": \"  - leaderboard_math_intermediate_algebra_hard\",\n           \
  \ \"exact_match,none\": 0.0035714285714285713,\n            \"exact_match_stderr,none\"\
  : 0.0035714285714285713\n        },\n        \"leaderboard_math_num_theory_hard\"\
  : {\n            \"alias\": \"  - leaderboard_math_num_theory_hard\",\n        \
  \    \"exact_match,none\": 0.0,\n            \"exact_match_stderr,none\": 0.0\n\
  \        },\n        \"leaderboard_math_prealgebra_hard\": {\n            \"alias\"\
  : \"  - leaderboard_math_prealgebra_hard\",\n            \"exact_match,none\": 0.0051813471502590676,\n\
  \            \"exact_match_stderr,none\": 0.0051813471502590676\n        },\n  \
  \      \"leaderboard_math_precalculus_hard\": {\n            \"alias\": \"  - leaderboard_math_precalculus_hard\"\
  ,\n            \"exact_match,none\": 0.0,\n            \"exact_match_stderr,none\"\
  : 0.0\n        },\n        \"leaderboard_mmlu_pro\": {\n            \"alias\": \"\
  \ - leaderboard_mmlu_pro\",\n            \"acc,none\": 0.11361369680851063,\n  \
  \          \"acc_stderr,none\": 0.002893183639282246\n        },\n        \"leaderboard_musr\"\
  : {\n            \"acc_norm,none\": 0.3544973544973545,\n            \"acc_norm_stderr,none\"\
  : 0.017061219716364134,\n            \"alias\": \" - leaderboard_musr\"\n      \
  \  },\n        \"leaderboard_musr_murder_mysteries\": {\n            \"alias\":\
  \ \"  - leaderboard_musr_murder_mysteries\",\n            \"acc_norm,none\": 0.492,\n\
  \            \"acc_norm_stderr,none\": 0.03168215643141386\n        },\n       \
  \ \"leaderboard_musr_object_placements\": {\n            \"alias\": \"  - leaderboard_musr_object_placements\"\
  ,\n            \"acc_norm,none\": 0.265625,\n            \"acc_norm_stderr,none\"\
  : 0.027658162598649488\n        },\n        \"leaderboard_musr_team_allocation\"\
  : {\n            \"alias\": \"  - leaderboard_musr_team_allocation\",\n        \
  \    \"acc_norm,none\": 0.308,\n            \"acc_norm_stderr,none\": 0.02925692860650181\n\
  \        }\n    },\n    \"leaderboard\": {\n        \"acc_norm,none\": 0.29640679724996755,\n\
  \        \"acc_norm_stderr,none\": 0.004985063132748098,\n        \"inst_level_loose_acc,none\"\
  : 0.2865707434052758,\n        \"inst_level_loose_acc_stderr,none\": \"N/A\",\n\
  \        \"prompt_level_strict_acc,none\": 0.16820702402957485,\n        \"prompt_level_strict_acc_stderr,none\"\
  : 0.01609655018806301,\n        \"acc,none\": 0.11361369680851063,\n        \"acc_stderr,none\"\
  : 0.002893183639282246,\n        \"exact_match,none\": 0.0030211480362537764,\n\
  \        \"exact_match_stderr,none\": 0.001510453653531021,\n        \"inst_level_strict_acc,none\"\
  : 0.2733812949640288,\n        \"inst_level_strict_acc_stderr,none\": \"N/A\",\n\
  \        \"prompt_level_loose_acc,none\": 0.1756007393715342,\n        \"prompt_level_loose_acc_stderr,none\"\
  : 0.01637325731205799,\n        \"alias\": \"leaderboard\"\n    },\n    \"leaderboard_bbh\"\
  : {\n        \"acc_norm,none\": 0.29699704912341607,\n        \"acc_norm_stderr,none\"\
  : 0.005711255426751417,\n        \"alias\": \" - leaderboard_bbh\"\n    },\n   \
  \ \"leaderboard_bbh_boolean_expressions\": {\n        \"alias\": \"  - leaderboard_bbh_boolean_expressions\"\
  ,\n        \"acc_norm,none\": 0.468,\n        \"acc_norm_stderr,none\": 0.03162125257572558\n\
  \    },\n    \"leaderboard_bbh_causal_judgement\": {\n        \"alias\": \"  - leaderboard_bbh_causal_judgement\"\
  ,\n        \"acc_norm,none\": 0.5187165775401069,\n        \"acc_norm_stderr,none\"\
  : 0.03663608375537843\n    },\n    \"leaderboard_bbh_date_understanding\": {\n \
  \       \"alias\": \"  - leaderboard_bbh_date_understanding\",\n        \"acc_norm,none\"\
  : 0.204,\n        \"acc_norm_stderr,none\": 0.025537121574548162\n    },\n    \"\
  leaderboard_bbh_disambiguation_qa\": {\n        \"alias\": \"  - leaderboard_bbh_disambiguation_qa\"\
  ,\n        \"acc_norm,none\": 0.332,\n        \"acc_norm_stderr,none\": 0.029844039047465857\n\
  \    },\n    \"leaderboard_bbh_formal_fallacies\": {\n        \"alias\": \"  - leaderboard_bbh_formal_fallacies\"\
  ,\n        \"acc_norm,none\": 0.468,\n        \"acc_norm_stderr,none\": 0.03162125257572558\n\
  \    },\n    \"leaderboard_bbh_geometric_shapes\": {\n        \"alias\": \"  - leaderboard_bbh_geometric_shapes\"\
  ,\n        \"acc_norm,none\": 0.108,\n        \"acc_norm_stderr,none\": 0.019669559381568776\n\
  \    },\n    \"leaderboard_bbh_hyperbaton\": {\n        \"alias\": \"  - leaderboard_bbh_hyperbaton\"\
  ,\n        \"acc_norm,none\": 0.512,\n        \"acc_norm_stderr,none\": 0.03167708558254714\n\
  \    },\n    \"leaderboard_bbh_logical_deduction_five_objects\": {\n        \"alias\"\
  : \"  - leaderboard_bbh_logical_deduction_five_objects\",\n        \"acc_norm,none\"\
  : 0.204,\n        \"acc_norm_stderr,none\": 0.025537121574548162\n    },\n    \"\
  leaderboard_bbh_logical_deduction_seven_objects\": {\n        \"alias\": \"  - leaderboard_bbh_logical_deduction_seven_objects\"\
  ,\n        \"acc_norm,none\": 0.128,\n        \"acc_norm_stderr,none\": 0.021172081336336534\n\
  \    },\n    \"leaderboard_bbh_logical_deduction_three_objects\": {\n        \"\
  alias\": \"  - leaderboard_bbh_logical_deduction_three_objects\",\n        \"acc_norm,none\"\
  : 0.36,\n        \"acc_norm_stderr,none\": 0.03041876402517494\n    },\n    \"leaderboard_bbh_movie_recommendation\"\
  : {\n        \"alias\": \"  - leaderboard_bbh_movie_recommendation\",\n        \"\
  acc_norm,none\": 0.24,\n        \"acc_norm_stderr,none\": 0.027065293652238982\n\
  \    },\n    \"leaderboard_bbh_navigate\": {\n        \"alias\": \"  - leaderboard_bbh_navigate\"\
  ,\n        \"acc_norm,none\": 0.44,\n        \"acc_norm_stderr,none\": 0.03145724452223569\n\
  \    },\n    \"leaderboard_bbh_object_counting\": {\n        \"alias\": \"  - leaderboard_bbh_object_counting\"\
  ,\n        \"acc_norm,none\": 0.072,\n        \"acc_norm_stderr,none\": 0.016381005750490122\n\
  \    },\n    \"leaderboard_bbh_penguins_in_a_table\": {\n        \"alias\": \" \
  \ - leaderboard_bbh_penguins_in_a_table\",\n        \"acc_norm,none\": 0.1917808219178082,\n\
  \        \"acc_norm_stderr,none\": 0.032695137069847634\n    },\n    \"leaderboard_bbh_reasoning_about_colored_objects\"\
  : {\n        \"alias\": \"  - leaderboard_bbh_reasoning_about_colored_objects\"\
  ,\n        \"acc_norm,none\": 0.104,\n        \"acc_norm_stderr,none\": 0.019345100974843932\n\
  \    },\n    \"leaderboard_bbh_ruin_names\": {\n        \"alias\": \"  - leaderboard_bbh_ruin_names\"\
  ,\n        \"acc_norm,none\": 0.2,\n        \"acc_norm_stderr,none\": 0.02534897002097912\n\
  \    },\n    \"leaderboard_bbh_salient_translation_error_detection\": {\n      \
  \  \"alias\": \"  - leaderboard_bbh_salient_translation_error_detection\",\n   \
  \     \"acc_norm,none\": 0.224,\n        \"acc_norm_stderr,none\": 0.026421361687347884\n\
  \    },\n    \"leaderboard_bbh_snarks\": {\n        \"alias\": \"  - leaderboard_bbh_snarks\"\
  ,\n        \"acc_norm,none\": 0.5393258426966292,\n        \"acc_norm_stderr,none\"\
  : 0.03746587736387869\n    },\n    \"leaderboard_bbh_sports_understanding\": {\n\
  \        \"alias\": \"  - leaderboard_bbh_sports_understanding\",\n        \"acc_norm,none\"\
  : 0.46,\n        \"acc_norm_stderr,none\": 0.031584653891499004\n    },\n    \"\
  leaderboard_bbh_temporal_sequences\": {\n        \"alias\": \"  - leaderboard_bbh_temporal_sequences\"\
  ,\n        \"acc_norm,none\": 0.26,\n        \"acc_norm_stderr,none\": 0.027797315752644335\n\
  \    },\n    \"leaderboard_bbh_tracking_shuffled_objects_five_objects\": {\n   \
  \     \"alias\": \"  - leaderboard_bbh_tracking_shuffled_objects_five_objects\"\
  ,\n        \"acc_norm,none\": 0.2,\n        \"acc_norm_stderr,none\": 0.02534897002097912\n\
  \    },\n    \"leaderboard_bbh_tracking_shuffled_objects_seven_objects\": {\n  \
  \      \"alias\": \"  - leaderboard_bbh_tracking_shuffled_objects_seven_objects\"\
  ,\n        \"acc_norm,none\": 0.16,\n        \"acc_norm_stderr,none\": 0.023232714782060626\n\
  \    },\n    \"leaderboard_bbh_tracking_shuffled_objects_three_objects\": {\n  \
  \      \"alias\": \"  - leaderboard_bbh_tracking_shuffled_objects_three_objects\"\
  ,\n        \"acc_norm,none\": 0.32,\n        \"acc_norm_stderr,none\": 0.029561724955240978\n\
  \    },\n    \"leaderboard_bbh_web_of_lies\": {\n        \"alias\": \"  - leaderboard_bbh_web_of_lies\"\
  ,\n        \"acc_norm,none\": 0.496,\n        \"acc_norm_stderr,none\": 0.0316851985511992\n\
  \    },\n    \"leaderboard_gpqa\": {\n        \"acc_norm,none\": 0.25671140939597314,\n\
  \        \"acc_norm_stderr,none\": 0.012664923317255711,\n        \"alias\": \"\
  \ - leaderboard_gpqa\"\n    },\n    \"leaderboard_gpqa_diamond\": {\n        \"\
  alias\": \"  - leaderboard_gpqa_diamond\",\n        \"acc_norm,none\": 0.2727272727272727,\n\
  \        \"acc_norm_stderr,none\": 0.03173071239071728\n    },\n    \"leaderboard_gpqa_extended\"\
  : {\n        \"alias\": \"  - leaderboard_gpqa_extended\",\n        \"acc_norm,none\"\
  : 0.2600732600732601,\n        \"acc_norm_stderr,none\": 0.018790743352015988\n\
  \    },\n    \"leaderboard_gpqa_main\": {\n        \"alias\": \"  - leaderboard_gpqa_main\"\
  ,\n        \"acc_norm,none\": 0.24553571428571427,\n        \"acc_norm_stderr,none\"\
  : 0.020357428454484603\n    },\n    \"leaderboard_ifeval\": {\n        \"alias\"\
  : \" - leaderboard_ifeval\",\n        \"prompt_level_strict_acc,none\": 0.16820702402957485,\n\
  \        \"prompt_level_strict_acc_stderr,none\": 0.016096550188063007,\n      \
  \  \"inst_level_strict_acc,none\": 0.2733812949640288,\n        \"inst_level_strict_acc_stderr,none\"\
  : \"N/A\",\n        \"prompt_level_loose_acc,none\": 0.1756007393715342,\n     \
  \   \"prompt_level_loose_acc_stderr,none\": 0.01637325731205799,\n        \"inst_level_loose_acc,none\"\
  : 0.2865707434052758,\n        \"inst_level_loose_acc_stderr,none\": \"N/A\"\n \
  \   },\n    \"leaderboard_math_hard\": {\n        \"exact_match,none\": 0.0030211480362537764,\n\
  \        \"exact_match_stderr,none\": 0.001510453653531021,\n        \"alias\":\
  \ \" - leaderboard_math_hard\"\n    },\n    \"leaderboard_math_algebra_hard\": {\n\
  \        \"alias\": \"  - leaderboard_math_algebra_hard\",\n        \"exact_match,none\"\
  : 0.006514657980456026,\n        \"exact_match_stderr,none\": 0.004599025618546258\n\
  \    },\n    \"leaderboard_math_counting_and_prob_hard\": {\n        \"alias\":\
  \ \"  - leaderboard_math_counting_and_prob_hard\",\n        \"exact_match,none\"\
  : 0.0,\n        \"exact_match_stderr,none\": 0.0\n    },\n    \"leaderboard_math_geometry_hard\"\
  : {\n        \"alias\": \"  - leaderboard_math_geometry_hard\",\n        \"exact_match,none\"\
  : 0.0,\n        \"exact_match_stderr,none\": 0.0\n    },\n    \"leaderboard_math_intermediate_algebra_hard\"\
  : {\n        \"alias\": \"  - leaderboard_math_intermediate_algebra_hard\",\n  \
  \      \"exact_match,none\": 0.0035714285714285713,\n        \"exact_match_stderr,none\"\
  : 0.0035714285714285713\n    },\n    \"leaderboard_math_num_theory_hard\": {\n \
  \       \"alias\": \"  - leaderboard_math_num_theory_hard\",\n        \"exact_match,none\"\
  : 0.0,\n        \"exact_match_stderr,none\": 0.0\n    },\n    \"leaderboard_math_prealgebra_hard\"\
  : {\n        \"alias\": \"  - leaderboard_math_prealgebra_hard\",\n        \"exact_match,none\"\
  : 0.0051813471502590676,\n        \"exact_match_stderr,none\": 0.0051813471502590676\n\
  \    },\n    \"leaderboard_math_precalculus_hard\": {\n        \"alias\": \"  -\
  \ leaderboard_math_precalculus_hard\",\n        \"exact_match,none\": 0.0,\n   \
  \     \"exact_match_stderr,none\": 0.0\n    },\n    \"leaderboard_mmlu_pro\": {\n\
  \        \"alias\": \" - leaderboard_mmlu_pro\",\n        \"acc,none\": 0.11361369680851063,\n\
  \        \"acc_stderr,none\": 0.002893183639282246\n    },\n    \"leaderboard_musr\"\
  : {\n        \"acc_norm,none\": 0.3544973544973545,\n        \"acc_norm_stderr,none\"\
  : 0.017061219716364134,\n        \"alias\": \" - leaderboard_musr\"\n    },\n  \
  \  \"leaderboard_musr_murder_mysteries\": {\n        \"alias\": \"  - leaderboard_musr_murder_mysteries\"\
  ,\n        \"acc_norm,none\": 0.492,\n        \"acc_norm_stderr,none\": 0.03168215643141386\n\
  \    },\n    \"leaderboard_musr_object_placements\": {\n        \"alias\": \"  -\
  \ leaderboard_musr_object_placements\",\n        \"acc_norm,none\": 0.265625,\n\
  \        \"acc_norm_stderr,none\": 0.027658162598649488\n    },\n    \"leaderboard_musr_team_allocation\"\
  : {\n        \"alias\": \"  - leaderboard_musr_team_allocation\",\n        \"acc_norm,none\"\
  : 0.308,\n        \"acc_norm_stderr,none\": 0.02925692860650181\n    }\n}\n```"
repo_url: https://huggingface.co/EleutherAI/pythia-1b
leaderboard_url: ''
point_of_contact: ''
configs:
- config_name: EleutherAI__pythia-1b__leaderboard_bbh_boolean_expressions
  data_files:
  - split: 2025_01_27T10_10_36.877664
    path:
    - '**/samples_leaderboard_bbh_boolean_expressions_2025-01-27T10-10-36.877664.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_boolean_expressions_2025-01-27T10-10-36.877664.jsonl'
- config_name: EleutherAI__pythia-1b__leaderboard_bbh_causal_judgement
  data_files:
  - split: 2025_01_27T10_10_36.877664
    path:
    - '**/samples_leaderboard_bbh_causal_judgement_2025-01-27T10-10-36.877664.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_causal_judgement_2025-01-27T10-10-36.877664.jsonl'
- config_name: EleutherAI__pythia-1b__leaderboard_bbh_date_understanding
  data_files:
  - split: 2025_01_27T10_10_36.877664
    path:
    - '**/samples_leaderboard_bbh_date_understanding_2025-01-27T10-10-36.877664.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_date_understanding_2025-01-27T10-10-36.877664.jsonl'
- config_name: EleutherAI__pythia-1b__leaderboard_bbh_disambiguation_qa
  data_files:
  - split: 2025_01_27T10_10_36.877664
    path:
    - '**/samples_leaderboard_bbh_disambiguation_qa_2025-01-27T10-10-36.877664.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_disambiguation_qa_2025-01-27T10-10-36.877664.jsonl'
- config_name: EleutherAI__pythia-1b__leaderboard_bbh_formal_fallacies
  data_files:
  - split: 2025_01_27T10_10_36.877664
    path:
    - '**/samples_leaderboard_bbh_formal_fallacies_2025-01-27T10-10-36.877664.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_formal_fallacies_2025-01-27T10-10-36.877664.jsonl'
- config_name: EleutherAI__pythia-1b__leaderboard_bbh_geometric_shapes
  data_files:
  - split: 2025_01_27T10_10_36.877664
    path:
    - '**/samples_leaderboard_bbh_geometric_shapes_2025-01-27T10-10-36.877664.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_geometric_shapes_2025-01-27T10-10-36.877664.jsonl'
- config_name: EleutherAI__pythia-1b__leaderboard_bbh_hyperbaton
  data_files:
  - split: 2025_01_27T10_10_36.877664
    path:
    - '**/samples_leaderboard_bbh_hyperbaton_2025-01-27T10-10-36.877664.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_hyperbaton_2025-01-27T10-10-36.877664.jsonl'
- config_name: EleutherAI__pythia-1b__leaderboard_bbh_logical_deduction_five_objects
  data_files:
  - split: 2025_01_27T10_10_36.877664
    path:
    - '**/samples_leaderboard_bbh_logical_deduction_five_objects_2025-01-27T10-10-36.877664.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_logical_deduction_five_objects_2025-01-27T10-10-36.877664.jsonl'
- config_name: EleutherAI__pythia-1b__leaderboard_bbh_logical_deduction_seven_objects
  data_files:
  - split: 2025_01_27T10_10_36.877664
    path:
    - '**/samples_leaderboard_bbh_logical_deduction_seven_objects_2025-01-27T10-10-36.877664.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_logical_deduction_seven_objects_2025-01-27T10-10-36.877664.jsonl'
- config_name: EleutherAI__pythia-1b__leaderboard_bbh_logical_deduction_three_objects
  data_files:
  - split: 2025_01_27T10_10_36.877664
    path:
    - '**/samples_leaderboard_bbh_logical_deduction_three_objects_2025-01-27T10-10-36.877664.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_logical_deduction_three_objects_2025-01-27T10-10-36.877664.jsonl'
- config_name: EleutherAI__pythia-1b__leaderboard_bbh_movie_recommendation
  data_files:
  - split: 2025_01_27T10_10_36.877664
    path:
    - '**/samples_leaderboard_bbh_movie_recommendation_2025-01-27T10-10-36.877664.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_movie_recommendation_2025-01-27T10-10-36.877664.jsonl'
- config_name: EleutherAI__pythia-1b__leaderboard_bbh_navigate
  data_files:
  - split: 2025_01_27T10_10_36.877664
    path:
    - '**/samples_leaderboard_bbh_navigate_2025-01-27T10-10-36.877664.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_navigate_2025-01-27T10-10-36.877664.jsonl'
- config_name: EleutherAI__pythia-1b__leaderboard_bbh_object_counting
  data_files:
  - split: 2025_01_27T10_10_36.877664
    path:
    - '**/samples_leaderboard_bbh_object_counting_2025-01-27T10-10-36.877664.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_object_counting_2025-01-27T10-10-36.877664.jsonl'
- config_name: EleutherAI__pythia-1b__leaderboard_bbh_penguins_in_a_table
  data_files:
  - split: 2025_01_27T10_10_36.877664
    path:
    - '**/samples_leaderboard_bbh_penguins_in_a_table_2025-01-27T10-10-36.877664.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_penguins_in_a_table_2025-01-27T10-10-36.877664.jsonl'
- config_name: EleutherAI__pythia-1b__leaderboard_bbh_reasoning_about_colored_objects
  data_files:
  - split: 2025_01_27T10_10_36.877664
    path:
    - '**/samples_leaderboard_bbh_reasoning_about_colored_objects_2025-01-27T10-10-36.877664.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_reasoning_about_colored_objects_2025-01-27T10-10-36.877664.jsonl'
- config_name: EleutherAI__pythia-1b__leaderboard_bbh_ruin_names
  data_files:
  - split: 2025_01_27T10_10_36.877664
    path:
    - '**/samples_leaderboard_bbh_ruin_names_2025-01-27T10-10-36.877664.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_ruin_names_2025-01-27T10-10-36.877664.jsonl'
- config_name: EleutherAI__pythia-1b__leaderboard_bbh_salient_translation_error_detection
  data_files:
  - split: 2025_01_27T10_10_36.877664
    path:
    - '**/samples_leaderboard_bbh_salient_translation_error_detection_2025-01-27T10-10-36.877664.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_salient_translation_error_detection_2025-01-27T10-10-36.877664.jsonl'
- config_name: EleutherAI__pythia-1b__leaderboard_bbh_snarks
  data_files:
  - split: 2025_01_27T10_10_36.877664
    path:
    - '**/samples_leaderboard_bbh_snarks_2025-01-27T10-10-36.877664.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_snarks_2025-01-27T10-10-36.877664.jsonl'
- config_name: EleutherAI__pythia-1b__leaderboard_bbh_sports_understanding
  data_files:
  - split: 2025_01_27T10_10_36.877664
    path:
    - '**/samples_leaderboard_bbh_sports_understanding_2025-01-27T10-10-36.877664.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_sports_understanding_2025-01-27T10-10-36.877664.jsonl'
- config_name: EleutherAI__pythia-1b__leaderboard_bbh_temporal_sequences
  data_files:
  - split: 2025_01_27T10_10_36.877664
    path:
    - '**/samples_leaderboard_bbh_temporal_sequences_2025-01-27T10-10-36.877664.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_temporal_sequences_2025-01-27T10-10-36.877664.jsonl'
- config_name: EleutherAI__pythia-1b__leaderboard_bbh_tracking_shuffled_objects_five_objects
  data_files:
  - split: 2025_01_27T10_10_36.877664
    path:
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_five_objects_2025-01-27T10-10-36.877664.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_five_objects_2025-01-27T10-10-36.877664.jsonl'
- config_name: EleutherAI__pythia-1b__leaderboard_bbh_tracking_shuffled_objects_seven_objects
  data_files:
  - split: 2025_01_27T10_10_36.877664
    path:
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_seven_objects_2025-01-27T10-10-36.877664.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_seven_objects_2025-01-27T10-10-36.877664.jsonl'
- config_name: EleutherAI__pythia-1b__leaderboard_bbh_tracking_shuffled_objects_three_objects
  data_files:
  - split: 2025_01_27T10_10_36.877664
    path:
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_three_objects_2025-01-27T10-10-36.877664.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_tracking_shuffled_objects_three_objects_2025-01-27T10-10-36.877664.jsonl'
- config_name: EleutherAI__pythia-1b__leaderboard_bbh_web_of_lies
  data_files:
  - split: 2025_01_27T10_10_36.877664
    path:
    - '**/samples_leaderboard_bbh_web_of_lies_2025-01-27T10-10-36.877664.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_bbh_web_of_lies_2025-01-27T10-10-36.877664.jsonl'
- config_name: EleutherAI__pythia-1b__leaderboard_gpqa_diamond
  data_files:
  - split: 2025_01_27T10_10_36.877664
    path:
    - '**/samples_leaderboard_gpqa_diamond_2025-01-27T10-10-36.877664.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_gpqa_diamond_2025-01-27T10-10-36.877664.jsonl'
- config_name: EleutherAI__pythia-1b__leaderboard_gpqa_extended
  data_files:
  - split: 2025_01_27T10_10_36.877664
    path:
    - '**/samples_leaderboard_gpqa_extended_2025-01-27T10-10-36.877664.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_gpqa_extended_2025-01-27T10-10-36.877664.jsonl'
- config_name: EleutherAI__pythia-1b__leaderboard_gpqa_main
  data_files:
  - split: 2025_01_27T10_10_36.877664
    path:
    - '**/samples_leaderboard_gpqa_main_2025-01-27T10-10-36.877664.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_gpqa_main_2025-01-27T10-10-36.877664.jsonl'
- config_name: EleutherAI__pythia-1b__leaderboard_ifeval
  data_files:
  - split: 2025_01_27T10_10_36.877664
    path:
    - '**/samples_leaderboard_ifeval_2025-01-27T10-10-36.877664.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_ifeval_2025-01-27T10-10-36.877664.jsonl'
- config_name: EleutherAI__pythia-1b__leaderboard_math_algebra_hard
  data_files:
  - split: 2025_01_27T10_10_36.877664
    path:
    - '**/samples_leaderboard_math_algebra_hard_2025-01-27T10-10-36.877664.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_math_algebra_hard_2025-01-27T10-10-36.877664.jsonl'
- config_name: EleutherAI__pythia-1b__leaderboard_math_counting_and_prob_hard
  data_files:
  - split: 2025_01_27T10_10_36.877664
    path:
    - '**/samples_leaderboard_math_counting_and_prob_hard_2025-01-27T10-10-36.877664.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_math_counting_and_prob_hard_2025-01-27T10-10-36.877664.jsonl'
- config_name: EleutherAI__pythia-1b__leaderboard_math_geometry_hard
  data_files:
  - split: 2025_01_27T10_10_36.877664
    path:
    - '**/samples_leaderboard_math_geometry_hard_2025-01-27T10-10-36.877664.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_math_geometry_hard_2025-01-27T10-10-36.877664.jsonl'
- config_name: EleutherAI__pythia-1b__leaderboard_math_intermediate_algebra_hard
  data_files:
  - split: 2025_01_27T10_10_36.877664
    path:
    - '**/samples_leaderboard_math_intermediate_algebra_hard_2025-01-27T10-10-36.877664.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_math_intermediate_algebra_hard_2025-01-27T10-10-36.877664.jsonl'
- config_name: EleutherAI__pythia-1b__leaderboard_math_num_theory_hard
  data_files:
  - split: 2025_01_27T10_10_36.877664
    path:
    - '**/samples_leaderboard_math_num_theory_hard_2025-01-27T10-10-36.877664.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_math_num_theory_hard_2025-01-27T10-10-36.877664.jsonl'
- config_name: EleutherAI__pythia-1b__leaderboard_math_prealgebra_hard
  data_files:
  - split: 2025_01_27T10_10_36.877664
    path:
    - '**/samples_leaderboard_math_prealgebra_hard_2025-01-27T10-10-36.877664.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_math_prealgebra_hard_2025-01-27T10-10-36.877664.jsonl'
- config_name: EleutherAI__pythia-1b__leaderboard_math_precalculus_hard
  data_files:
  - split: 2025_01_27T10_10_36.877664
    path:
    - '**/samples_leaderboard_math_precalculus_hard_2025-01-27T10-10-36.877664.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_math_precalculus_hard_2025-01-27T10-10-36.877664.jsonl'
- config_name: EleutherAI__pythia-1b__leaderboard_mmlu_pro
  data_files:
  - split: 2025_01_27T10_10_36.877664
    path:
    - '**/samples_leaderboard_mmlu_pro_2025-01-27T10-10-36.877664.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_mmlu_pro_2025-01-27T10-10-36.877664.jsonl'
- config_name: EleutherAI__pythia-1b__leaderboard_musr_murder_mysteries
  data_files:
  - split: 2025_01_27T10_10_36.877664
    path:
    - '**/samples_leaderboard_musr_murder_mysteries_2025-01-27T10-10-36.877664.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_musr_murder_mysteries_2025-01-27T10-10-36.877664.jsonl'
- config_name: EleutherAI__pythia-1b__leaderboard_musr_object_placements
  data_files:
  - split: 2025_01_27T10_10_36.877664
    path:
    - '**/samples_leaderboard_musr_object_placements_2025-01-27T10-10-36.877664.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_musr_object_placements_2025-01-27T10-10-36.877664.jsonl'
- config_name: EleutherAI__pythia-1b__leaderboard_musr_team_allocation
  data_files:
  - split: 2025_01_27T10_10_36.877664
    path:
    - '**/samples_leaderboard_musr_team_allocation_2025-01-27T10-10-36.877664.jsonl'
  - split: latest
    path:
    - '**/samples_leaderboard_musr_team_allocation_2025-01-27T10-10-36.877664.jsonl'
---

# Dataset Card for Evaluation run of EleutherAI/pythia-1b

<!-- Provide a quick summary of the dataset. -->

Dataset automatically created during the evaluation run of model [EleutherAI/pythia-1b](https://huggingface.co/EleutherAI/pythia-1b)
The dataset is composed of 38 configuration(s), each one corresponding to one of the evaluated task.

The dataset has been created from 1 run(s). Each run can be found as a specific split in each configuration, the split being named using the timestamp of the run.The "train" split is always pointing to the latest results.

An additional configuration "results" store all the aggregated results of the run.

To load the details from a run, you can for instance do the following:
```python
from datasets import load_dataset
data = load_dataset(
	"open-llm-leaderboard/EleutherAI__pythia-1b-details",
	name="EleutherAI__pythia-1b__leaderboard_bbh_boolean_expressions",
	split="latest"
)
```

## Latest results

These are the [latest results from run 2025-01-27T10-10-36.877664](https://huggingface.co/datasets/open-llm-leaderboard/EleutherAI__pythia-1b-details/blob/main/EleutherAI__pythia-1b/results_2025-01-27T10-10-36.877664.json) (note that there might be results for other tasks in the repos if successive evals didn't cover the same tasks. You find each in the results and the "latest" split for each eval):

```python
{
    "all": {
        "leaderboard": {
            "acc_norm,none": 0.29640679724996755,
            "acc_norm_stderr,none": 0.004985063132748098,
            "inst_level_loose_acc,none": 0.2865707434052758,
            "inst_level_loose_acc_stderr,none": "N/A",
            "prompt_level_strict_acc,none": 0.16820702402957485,
            "prompt_level_strict_acc_stderr,none": 0.01609655018806301,
            "acc,none": 0.11361369680851063,
            "acc_stderr,none": 0.002893183639282246,
            "exact_match,none": 0.0030211480362537764,
            "exact_match_stderr,none": 0.001510453653531021,
            "inst_level_strict_acc,none": 0.2733812949640288,
            "inst_level_strict_acc_stderr,none": "N/A",
            "prompt_level_loose_acc,none": 0.1756007393715342,
            "prompt_level_loose_acc_stderr,none": 0.01637325731205799,
            "alias": "leaderboard"
        },
        "leaderboard_bbh": {
            "acc_norm,none": 0.29699704912341607,
            "acc_norm_stderr,none": 0.005711255426751417,
            "alias": " - leaderboard_bbh"
        },
        "leaderboard_bbh_boolean_expressions": {
            "alias": "  - leaderboard_bbh_boolean_expressions",
            "acc_norm,none": 0.468,
            "acc_norm_stderr,none": 0.03162125257572558
        },
        "leaderboard_bbh_causal_judgement": {
            "alias": "  - leaderboard_bbh_causal_judgement",
            "acc_norm,none": 0.5187165775401069,
            "acc_norm_stderr,none": 0.03663608375537843
        },
        "leaderboard_bbh_date_understanding": {
            "alias": "  - leaderboard_bbh_date_understanding",
            "acc_norm,none": 0.204,
            "acc_norm_stderr,none": 0.025537121574548162
        },
        "leaderboard_bbh_disambiguation_qa": {
            "alias": "  - leaderboard_bbh_disambiguation_qa",
            "acc_norm,none": 0.332,
            "acc_norm_stderr,none": 0.029844039047465857
        },
        "leaderboard_bbh_formal_fallacies": {
            "alias": "  - leaderboard_bbh_formal_fallacies",
            "acc_norm,none": 0.468,
            "acc_norm_stderr,none": 0.03162125257572558
        },
        "leaderboard_bbh_geometric_shapes": {
            "alias": "  - leaderboard_bbh_geometric_shapes",
            "acc_norm,none": 0.108,
            "acc_norm_stderr,none": 0.019669559381568776
        },
        "leaderboard_bbh_hyperbaton": {
            "alias": "  - leaderboard_bbh_hyperbaton",
            "acc_norm,none": 0.512,
            "acc_norm_stderr,none": 0.03167708558254714
        },
        "leaderboard_bbh_logical_deduction_five_objects": {
            "alias": "  - leaderboard_bbh_logical_deduction_five_objects",
            "acc_norm,none": 0.204,
            "acc_norm_stderr,none": 0.025537121574548162
        },
        "leaderboard_bbh_logical_deduction_seven_objects": {
            "alias": "  - leaderboard_bbh_logical_deduction_seven_objects",
            "acc_norm,none": 0.128,
            "acc_norm_stderr,none": 0.021172081336336534
        },
        "leaderboard_bbh_logical_deduction_three_objects": {
            "alias": "  - leaderboard_bbh_logical_deduction_three_objects",
            "acc_norm,none": 0.36,
            "acc_norm_stderr,none": 0.03041876402517494
        },
        "leaderboard_bbh_movie_recommendation": {
            "alias": "  - leaderboard_bbh_movie_recommendation",
            "acc_norm,none": 0.24,
            "acc_norm_stderr,none": 0.027065293652238982
        },
        "leaderboard_bbh_navigate": {
            "alias": "  - leaderboard_bbh_navigate",
            "acc_norm,none": 0.44,
            "acc_norm_stderr,none": 0.03145724452223569
        },
        "leaderboard_bbh_object_counting": {
            "alias": "  - leaderboard_bbh_object_counting",
            "acc_norm,none": 0.072,
            "acc_norm_stderr,none": 0.016381005750490122
        },
        "leaderboard_bbh_penguins_in_a_table": {
            "alias": "  - leaderboard_bbh_penguins_in_a_table",
            "acc_norm,none": 0.1917808219178082,
            "acc_norm_stderr,none": 0.032695137069847634
        },
        "leaderboard_bbh_reasoning_about_colored_objects": {
            "alias": "  - leaderboard_bbh_reasoning_about_colored_objects",
            "acc_norm,none": 0.104,
            "acc_norm_stderr,none": 0.019345100974843932
        },
        "leaderboard_bbh_ruin_names": {
            "alias": "  - leaderboard_bbh_ruin_names",
            "acc_norm,none": 0.2,
            "acc_norm_stderr,none": 0.02534897002097912
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
            "acc_norm,none": 0.46,
            "acc_norm_stderr,none": 0.031584653891499004
        },
        "leaderboard_bbh_temporal_sequences": {
            "alias": "  - leaderboard_bbh_temporal_sequences",
            "acc_norm,none": 0.26,
            "acc_norm_stderr,none": 0.027797315752644335
        },
        "leaderboard_bbh_tracking_shuffled_objects_five_objects": {
            "alias": "  - leaderboard_bbh_tracking_shuffled_objects_five_objects",
            "acc_norm,none": 0.2,
            "acc_norm_stderr,none": 0.02534897002097912
        },
        "leaderboard_bbh_tracking_shuffled_objects_seven_objects": {
            "alias": "  - leaderboard_bbh_tracking_shuffled_objects_seven_objects",
            "acc_norm,none": 0.16,
            "acc_norm_stderr,none": 0.023232714782060626
        },
        "leaderboard_bbh_tracking_shuffled_objects_three_objects": {
            "alias": "  - leaderboard_bbh_tracking_shuffled_objects_three_objects",
            "acc_norm,none": 0.32,
            "acc_norm_stderr,none": 0.029561724955240978
        },
        "leaderboard_bbh_web_of_lies": {
            "alias": "  - leaderboard_bbh_web_of_lies",
            "acc_norm,none": 0.496,
            "acc_norm_stderr,none": 0.0316851985511992
        },
        "leaderboard_gpqa": {
            "acc_norm,none": 0.25671140939597314,
            "acc_norm_stderr,none": 0.012664923317255711,
            "alias": " - leaderboard_gpqa"
        },
        "leaderboard_gpqa_diamond": {
            "alias": "  - leaderboard_gpqa_diamond",
            "acc_norm,none": 0.2727272727272727,
            "acc_norm_stderr,none": 0.03173071239071728
        },
        "leaderboard_gpqa_extended": {
            "alias": "  - leaderboard_gpqa_extended",
            "acc_norm,none": 0.2600732600732601,
            "acc_norm_stderr,none": 0.018790743352015988
        },
        "leaderboard_gpqa_main": {
            "alias": "  - leaderboard_gpqa_main",
            "acc_norm,none": 0.24553571428571427,
            "acc_norm_stderr,none": 0.020357428454484603
        },
        "leaderboard_ifeval": {
            "alias": " - leaderboard_ifeval",
            "prompt_level_strict_acc,none": 0.16820702402957485,
            "prompt_level_strict_acc_stderr,none": 0.016096550188063007,
            "inst_level_strict_acc,none": 0.2733812949640288,
            "inst_level_strict_acc_stderr,none": "N/A",
            "prompt_level_loose_acc,none": 0.1756007393715342,
            "prompt_level_loose_acc_stderr,none": 0.01637325731205799,
            "inst_level_loose_acc,none": 0.2865707434052758,
            "inst_level_loose_acc_stderr,none": "N/A"
        },
        "leaderboard_math_hard": {
            "exact_match,none": 0.0030211480362537764,
            "exact_match_stderr,none": 0.001510453653531021,
            "alias": " - leaderboard_math_hard"
        },
        "leaderboard_math_algebra_hard": {
            "alias": "  - leaderboard_math_algebra_hard",
            "exact_match,none": 0.006514657980456026,
            "exact_match_stderr,none": 0.004599025618546258
        },
        "leaderboard_math_counting_and_prob_hard": {
            "alias": "  - leaderboard_math_counting_and_prob_hard",
            "exact_match,none": 0.0,
            "exact_match_stderr,none": 0.0
        },
        "leaderboard_math_geometry_hard": {
            "alias": "  - leaderboard_math_geometry_hard",
            "exact_match,none": 0.0,
            "exact_match_stderr,none": 0.0
        },
        "leaderboard_math_intermediate_algebra_hard": {
            "alias": "  - leaderboard_math_intermediate_algebra_hard",
            "exact_match,none": 0.0035714285714285713,
            "exact_match_stderr,none": 0.0035714285714285713
        },
        "leaderboard_math_num_theory_hard": {
            "alias": "  - leaderboard_math_num_theory_hard",
            "exact_match,none": 0.0,
            "exact_match_stderr,none": 0.0
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
            "acc,none": 0.11361369680851063,
            "acc_stderr,none": 0.002893183639282246
        },
        "leaderboard_musr": {
            "acc_norm,none": 0.3544973544973545,
            "acc_norm_stderr,none": 0.017061219716364134,
            "alias": " - leaderboard_musr"
        },
        "leaderboard_musr_murder_mysteries": {
            "alias": "  - leaderboard_musr_murder_mysteries",
            "acc_norm,none": 0.492,
            "acc_norm_stderr,none": 0.03168215643141386
        },
        "leaderboard_musr_object_placements": {
            "alias": "  - leaderboard_musr_object_placements",
            "acc_norm,none": 0.265625,
            "acc_norm_stderr,none": 0.027658162598649488
        },
        "leaderboard_musr_team_allocation": {
            "alias": "  - leaderboard_musr_team_allocation",
            "acc_norm,none": 0.308,
            "acc_norm_stderr,none": 0.02925692860650181
        }
    },
    "leaderboard": {
        "acc_norm,none": 0.29640679724996755,
        "acc_norm_stderr,none": 0.004985063132748098,
        "inst_level_loose_acc,none": 0.2865707434052758,
        "inst_level_loose_acc_stderr,none": "N/A",
        "prompt_level_strict_acc,none": 0.16820702402957485,
        "prompt_level_strict_acc_stderr,none": 0.01609655018806301,
        "acc,none": 0.11361369680851063,
        "acc_stderr,none": 0.002893183639282246,
        "exact_match,none": 0.0030211480362537764,
        "exact_match_stderr,none": 0.001510453653531021,
        "inst_level_strict_acc,none": 0.2733812949640288,
        "inst_level_strict_acc_stderr,none": "N/A",
        "prompt_level_loose_acc,none": 0.1756007393715342,
        "prompt_level_loose_acc_stderr,none": 0.01637325731205799,
        "alias": "leaderboard"
    },
    "leaderboard_bbh": {
        "acc_norm,none": 0.29699704912341607,
        "acc_norm_stderr,none": 0.005711255426751417,
        "alias": " - leaderboard_bbh"
    },
    "leaderboard_bbh_boolean_expressions": {
        "alias": "  - leaderboard_bbh_boolean_expressions",
        "acc_norm,none": 0.468,
        "acc_norm_stderr,none": 0.03162125257572558
    },
    "leaderboard_bbh_causal_judgement": {
        "alias": "  - leaderboard_bbh_causal_judgement",
        "acc_norm,none": 0.5187165775401069,
        "acc_norm_stderr,none": 0.03663608375537843
    },
    "leaderboard_bbh_date_understanding": {
        "alias": "  - leaderboard_bbh_date_understanding",
        "acc_norm,none": 0.204,
        "acc_norm_stderr,none": 0.025537121574548162
    },
    "leaderboard_bbh_disambiguation_qa": {
        "alias": "  - leaderboard_bbh_disambiguation_qa",
        "acc_norm,none": 0.332,
        "acc_norm_stderr,none": 0.029844039047465857
    },
    "leaderboard_bbh_formal_fallacies": {
        "alias": "  - leaderboard_bbh_formal_fallacies",
        "acc_norm,none": 0.468,
        "acc_norm_stderr,none": 0.03162125257572558
    },
    "leaderboard_bbh_geometric_shapes": {
        "alias": "  - leaderboard_bbh_geometric_shapes",
        "acc_norm,none": 0.108,
        "acc_norm_stderr,none": 0.019669559381568776
    },
    "leaderboard_bbh_hyperbaton": {
        "alias": "  - leaderboard_bbh_hyperbaton",
        "acc_norm,none": 0.512,
        "acc_norm_stderr,none": 0.03167708558254714
    },
    "leaderboard_bbh_logical_deduction_five_objects": {
        "alias": "  - leaderboard_bbh_logical_deduction_five_objects",
        "acc_norm,none": 0.204,
        "acc_norm_stderr,none": 0.025537121574548162
    },
    "leaderboard_bbh_logical_deduction_seven_objects": {
        "alias": "  - leaderboard_bbh_logical_deduction_seven_objects",
        "acc_norm,none": 0.128,
        "acc_norm_stderr,none": 0.021172081336336534
    },
    "leaderboard_bbh_logical_deduction_three_objects": {
        "alias": "  - leaderboard_bbh_logical_deduction_three_objects",
        "acc_norm,none": 0.36,
        "acc_norm_stderr,none": 0.03041876402517494
    },
    "leaderboard_bbh_movie_recommendation": {
        "alias": "  - leaderboard_bbh_movie_recommendation",
        "acc_norm,none": 0.24,
        "acc_norm_stderr,none": 0.027065293652238982
    },
    "leaderboard_bbh_navigate": {
        "alias": "  - leaderboard_bbh_navigate",
        "acc_norm,none": 0.44,
        "acc_norm_stderr,none": 0.03145724452223569
    },
    "leaderboard_bbh_object_counting": {
        "alias": "  - leaderboard_bbh_object_counting",
        "acc_norm,none": 0.072,
        "acc_norm_stderr,none": 0.016381005750490122
    },
    "leaderboard_bbh_penguins_in_a_table": {
        "alias": "  - leaderboard_bbh_penguins_in_a_table",
        "acc_norm,none": 0.1917808219178082,
        "acc_norm_stderr,none": 0.032695137069847634
    },
    "leaderboard_bbh_reasoning_about_colored_objects": {
        "alias": "  - leaderboard_bbh_reasoning_about_colored_objects",
        "acc_norm,none": 0.104,
        "acc_norm_stderr,none": 0.019345100974843932
    },
    "leaderboard_bbh_ruin_names": {
        "alias": "  - leaderboard_bbh_ruin_names",
        "acc_norm,none": 0.2,
        "acc_norm_stderr,none": 0.02534897002097912
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
        "acc_norm,none": 0.46,
        "acc_norm_stderr,none": 0.031584653891499004
    },
    "leaderboard_bbh_temporal_sequences": {
        "alias": "  - leaderboard_bbh_temporal_sequences",
        "acc_norm,none": 0.26,
        "acc_norm_stderr,none": 0.027797315752644335
    },
    "leaderboard_bbh_tracking_shuffled_objects_five_objects": {
        "alias": "  - leaderboard_bbh_tracking_shuffled_objects_five_objects",
        "acc_norm,none": 0.2,
        "acc_norm_stderr,none": 0.02534897002097912
    },
    "leaderboard_bbh_tracking_shuffled_objects_seven_objects": {
        "alias": "  - leaderboard_bbh_tracking_shuffled_objects_seven_objects",
        "acc_norm,none": 0.16,
        "acc_norm_stderr,none": 0.023232714782060626
    },
    "leaderboard_bbh_tracking_shuffled_objects_three_objects": {
        "alias": "  - leaderboard_bbh_tracking_shuffled_objects_three_objects",
        "acc_norm,none": 0.32,
        "acc_norm_stderr,none": 0.029561724955240978
    },
    "leaderboard_bbh_web_of_lies": {
        "alias": "  - leaderboard_bbh_web_of_lies",
        "acc_norm,none": 0.496,
        "acc_norm_stderr,none": 0.0316851985511992
    },
    "leaderboard_gpqa": {
        "acc_norm,none": 0.25671140939597314,
        "acc_norm_stderr,none": 0.012664923317255711,
        "alias": " - leaderboard_gpqa"
    },
    "leaderboard_gpqa_diamond": {
        "alias": "  - leaderboard_gpqa_diamond",
        "acc_norm,none": 0.2727272727272727,
        "acc_norm_stderr,none": 0.03173071239071728
    },
    "leaderboard_gpqa_extended": {
        "alias": "  - leaderboard_gpqa_extended",
        "acc_norm,none": 0.2600732600732601,
        "acc_norm_stderr,none": 0.018790743352015988
    },
    "leaderboard_gpqa_main": {
        "alias": "  - leaderboard_gpqa_main",
        "acc_norm,none": 0.24553571428571427,
        "acc_norm_stderr,none": 0.020357428454484603
    },
    "leaderboard_ifeval": {
        "alias": " - leaderboard_ifeval",
        "prompt_level_strict_acc,none": 0.16820702402957485,
        "prompt_level_strict_acc_stderr,none": 0.016096550188063007,
        "inst_level_strict_acc,none": 0.2733812949640288,
        "inst_level_strict_acc_stderr,none": "N/A",
        "prompt_level_loose_acc,none": 0.1756007393715342,
        "prompt_level_loose_acc_stderr,none": 0.01637325731205799,
        "inst_level_loose_acc,none": 0.2865707434052758,
        "inst_level_loose_acc_stderr,none": "N/A"
    },
    "leaderboard_math_hard": {
        "exact_match,none": 0.0030211480362537764,
        "exact_match_stderr,none": 0.001510453653531021,
        "alias": " - leaderboard_math_hard"
    },
    "leaderboard_math_algebra_hard": {
        "alias": "  - leaderboard_math_algebra_hard",
        "exact_match,none": 0.006514657980456026,
        "exact_match_stderr,none": 0.004599025618546258
    },
    "leaderboard_math_counting_and_prob_hard": {
        "alias": "  - leaderboard_math_counting_and_prob_hard",
        "exact_match,none": 0.0,
        "exact_match_stderr,none": 0.0
    },
    "leaderboard_math_geometry_hard": {
        "alias": "  - leaderboard_math_geometry_hard",
        "exact_match,none": 0.0,
        "exact_match_stderr,none": 0.0
    },
    "leaderboard_math_intermediate_algebra_hard": {
        "alias": "  - leaderboard_math_intermediate_algebra_hard",
        "exact_match,none": 0.0035714285714285713,
        "exact_match_stderr,none": 0.0035714285714285713
    },
    "leaderboard_math_num_theory_hard": {
        "alias": "  - leaderboard_math_num_theory_hard",
        "exact_match,none": 0.0,
        "exact_match_stderr,none": 0.0
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
        "acc,none": 0.11361369680851063,
        "acc_stderr,none": 0.002893183639282246
    },
    "leaderboard_musr": {
        "acc_norm,none": 0.3544973544973545,
        "acc_norm_stderr,none": 0.017061219716364134,
        "alias": " - leaderboard_musr"
    },
    "leaderboard_musr_murder_mysteries": {
        "alias": "  - leaderboard_musr_murder_mysteries",
        "acc_norm,none": 0.492,
        "acc_norm_stderr,none": 0.03168215643141386
    },
    "leaderboard_musr_object_placements": {
        "alias": "  - leaderboard_musr_object_placements",
        "acc_norm,none": 0.265625,
        "acc_norm_stderr,none": 0.027658162598649488
    },
    "leaderboard_musr_team_allocation": {
        "alias": "  - leaderboard_musr_team_allocation",
        "acc_norm,none": 0.308,
        "acc_norm_stderr,none": 0.02925692860650181
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