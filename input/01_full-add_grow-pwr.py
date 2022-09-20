SIMULATION = {'simulation': {'control': {'duration': 1200, 'startmonth': 1, 'startyear': 2022}, 'archetypes': {'spec': [{'lib': 'cycamore', 'name': 'Source'}, {'lib': 'cycvt', 'name': 'SEnrichment'}, {'lib': 'cycamore', 'name': 'Mixer'}, {'lib': 'cycamore', 'name': 'Reactor'}, {'lib': 'cycamore', 'name': 'Storage'}, {'lib': 'cycamore', 'name': 'Sink'}, {'lib': 'cycamore', 'name': 'DeployInst'}, {'lib': 'cycamore', 'name': 'ManagerInst'}, {'lib': 'cycamore', 'name': 'GrowthRegion'}]}, 'region': {'name': 'GrowthRegion', 'config': {'GrowthRegion': {'growth': {'item': [{'commod': 'PowerLWR', 'piecewise_function': {'piece': [{'start': 18, 'function': {'type': 'exponential', 'params': '100000 0.0008333333333333334 0'}}]}}]}}}, 'institution': [{'name': 'InitFleet', 'config': {'DeployInst': {'prototypes': {'val': ['LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR']}, 'n_build': {'val': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}, 'build_times': {'val': [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16, 17, 17, 17, 17]}, 'lifetimes': {'val': [18, 23, 28, 33, 38, 43, 48, 53, 58, 63, 68, 73, 78, 83, 88, 93, 98, 103, 108, 113, 118, 123, 128, 133, 138, 143, 148, 153, 158, 163, 168, 173, 178, 183, 188, 193, 198, 203, 208, 213, 218, 223, 228, 233, 238, 243, 248, 253, 258, 263, 268, 273, 278, 283, 288, 293, 298, 303, 308, 313, 318, 323, 328, 333, 338, 343, 348, 353, 358, 363, 368, 373, 378, 383, 388, 393, 398, 403, 408, 413, 418, 423, 428, 433, 438, 443, 448, 453, 458, 463, 468, 473, 478, 483, 488, 493, 498, 503, 508, 513]}}}}, {'name': 'FCInstEG01', 'initialfacilitylist': {'entry': [{'number': 1, 'prototype': 'SourceInitUOX'}, {'number': 1, 'prototype': 'Source_UNAT'}, {'number': 1, 'prototype': 'Source_UNAT_ADD'}, {'number': 1, 'prototype': 'SourceNonIsos'}, {'number': 1, 'prototype': 'Enrichment'}, {'number': 1, 'prototype': 'Enrichment_ADD'}, {'number': 1, 'prototype': 'StorageDepU'}, {'number': 1, 'prototype': 'UOXCool'}, {'number': 1, 'prototype': 'UOXCool_ADD'}, {'number': 1, 'prototype': 'Waste'}]}, 'config': {'ManagerInst': {'prototypes': {'val': ['Source_UNAT', 'SourceNonIsos', 'Enrichment', 'Source_UNAT_ADD', 'Enrichment_ADD', 'StorageDepU', 'LWR', 'UOXCool', 'UOXCool_ADD', 'Waste']}}}}]}, 'facility': [{'name': 'SourceInitUOX', 'config': {'Source': {'outcommod': 'c_InitUOX', 'outrecipe': 'r_UOX', 'inventory_size': 8870500}}}, {'name': 'SourceNonIsos', 'config': {'Source': {'outcommod': 'NonIsos', 'outrecipe': 'NoAdditive_234', 'throughput': 1000000.0}}}, {'name': 'Source_UNAT', 'config': {'Source': {'outcommod': 'c_NU', 'outrecipe': 'r_NU', 'throughput': 210000000000.0}}}, {'name': 'Source_UNAT_ADD', 'config': {'Source': {'outcommod': 'c_NU_ADD', 'outrecipe': 'r_NU_ADD', 'throughput': 210000000000.0}}}, {'name': 'Enrichment', 'config': {'SEnrichment': {'feed_commod': 'c_NU', 'feed_recipe': 'r_NU', 'product_commod': 'c_UOX', 'tails_commod': 'c_DU', 'tails_assay': 0.0025, 'swu_capacity': 1e+100, 'initial_feed': 0, 'enrich_efficiencies': [{'item': {'comp': 922340000, 'eff': 1.2425193125083018}}]}}}, {'name': 'Enrichment_ADD', 'config': {'SEnrichment': {'feed_commod': 'c_NU_ADD', 'feed_recipe': 'r_NU_ADD', 'product_commod': 'c_UOX_ADD', 'tails_commod': 'c_DU', 'tails_assay': 0.0025, 'swu_capacity': 1e+100, 'initial_feed': 0, 'enrich_efficiencies': {'item': {'comp': 'U234', 'eff': 1.2402226006684631}}}}}, {'name': 'StorageDepU', 'config': {'Storage': {'in_commods': {'val': 'c_DU'}, 'in_recipe': 'r_DU', 'out_commods': {'val': 'c_DU_str'}, 'residence_time': 0}}}, {'name': 'LWR', 'lifetime': 480, 'config': {'Reactor': {'fuel_incommods': {'val': ['c_UOX_ADD', 'c_UOX', 'c_InitUOX']}, 'fuel_outcommods': {'val': ['c_S_UOX_ADD', 'c_S_UOX', 'c_S_UOX']}, 'fuel_inrecipes': {'val': ['r_UOX_ADD', 'r_UOX', 'r_UOX']}, 'fuel_outrecipes': {'val': ['r_S_UOX_ADD', 'r_S_UOX', 'r_S_UOX']}, 'fuel_prefs': {'val': [10, 20, 25]}, 'pref_change_times': {'val': 60}, 'pref_change_commods': {'val': 'c_UOX_ADD'}, 'pref_change_values': {'val': 10000}, 'cycle_time': 18, 'refuel_time': 0, 'assem_size': 29565, 'n_assem_core': 3, 'n_assem_batch': 1, 'power_name': 'PowerLWR', 'power_cap': 1000}}}, {'name': 'UOXCool', 'config': {'Storage': {'in_commods': {'val': ['c_S_UOX']}, 'out_commods': {'val': 'c_S_UOX_cool'}, 'residence_time': 81}}}, {'name': 'UOXCool_ADD', 'config': {'Storage': {'in_commods': {'val': ['c_S_UOX_ADD']}, 'out_commods': {'val': 'c_S_UOX_ADD_cool'}, 'residence_time': 81}}}, {'name': 'UOXStr', 'config': {'Storage': {'in_commods': {'val': 'c_S_UOX_cool'}, 'out_commods': {'val': 'c_S_UOX_stored'}, 'residence_time': 0}}}, {'name': 'Waste', 'config': {'Sink': {'in_commods': {'val': ['c_S_UOX_stored', 'StoredDepU']}}}}], 'recipe': [{'name': 'r_DU', 'basis': 'mass', 'nuclide': [{'id': 'U235', 'comp': 0.0025}, {'id': 'U238', 'comp': 0.9975}]}, {'name': 'UOX_no232', 'basis': 'mass', 'nuclide': [{'id': 'U234', 'comp': 0.0004631049477}, {'id': 'U235', 'comp': 0.049906230293}, {'id': 'U238', 'comp': 0.9496306647594}]}, {'name': 'NoAdditive_234', 'basis': 'mass', 'nuclide': [{'id': 'U234', 'comp': 1.0}]}, {'name': 'r_NU', 'basis': 'mass', 'nuclide': [{'id': 'U234', 'comp': 5.3e-05}, {'id': 'U235', 'comp': 0.00711}, {'id': 'U238', 'comp': 0.99289}]}, {'name': 'r_NU_ADD', 'basis': 'mass', 'nuclide': [{'id': 'U232', 'comp': 1e-10}, {'id': 'U233', 'comp': 1e-10}, {'id': 'U234', 'comp': 5.30945e-05}, {'id': 'U235', 'comp': 0.0071095115}, {'id': 'U238', 'comp': 0.9928373938}]}, {'name': 'r_UOX', 'basis': 'mass', 'nuclide': [{'id': 'U234', 'comp': 0.0004631049477}, {'id': 'U235', 'comp': 0.049906230293}, {'id': 'U238', 'comp': 0.9496306647594}]}, {'name': 'r_S_UOX', 'basis': 'mass', 'nuclide': [{'id': 'U232', 'comp': 2.838e-10}, {'id': 'U233', 'comp': 5.8245e-09}, {'id': 'U234', 'comp': 0.0002961396326}, {'id': 'U235', 'comp': 0.0174611824759}, {'id': 'U236', 'comp': 0.006185388998}, {'id': 'U238', 'comp': 0.9250572827708}, {'id': 'Pu239', 'comp': 0.01}, {'id': 'Am241', 'comp': 0.001}, {'id': 'Cs137', 'comp': 0.04}]}, {'name': 'r_UOX_ADD', 'basis': 'mass', 'nuclide': [{'id': 'U232', 'comp': 1.0434e-09}, {'id': 'U233', 'comp': 1.2228e-09}, {'id': 'U234', 'comp': 0.0004631049466}, {'id': 'U235', 'comp': 0.0499062301796}, {'id': 'U238', 'comp': 0.9496306626077}]}, {'name': 'r_S_UOX_ADD', 'basis': 'mass', 'nuclide': [{'id': 'U232', 'comp': 9.065e-10}, {'id': 'U233', 'comp': 6.2943e-09}, {'id': 'U234', 'comp': 0.0002327879338}, {'id': 'U235', 'comp': 0.0175266370423}, {'id': 'U236', 'comp': 0.0062071106222}, {'id': 'U238', 'comp': 0.9250334572009}, {'id': 'Pu239', 'comp': 0.01}, {'id': 'Am241', 'comp': 0.001}, {'id': 'Cs137', 'comp': 0.04}]}]}}