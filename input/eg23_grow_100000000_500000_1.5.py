SIMULATION = {'simulation': {'control': {'duration': 1200, 'startmonth': 1, 'startyear': 2022}, 'archetypes': {'spec': [{'lib': 'cycamore', 'name': 'Source'}, {'lib': 'cycamore', 'name': 'Separations'}, {'lib': 'cycamore', 'name': 'Mixer'}, {'lib': 'cycamore', 'name': 'Reactor'}, {'lib': 'cycamore', 'name': 'Storage'}, {'lib': 'cycamore', 'name': 'Separations'}, {'lib': 'cycamore', 'name': 'Sink'}, {'lib': 'cycamore', 'name': 'DeployInst'}, {'lib': 'cycamore', 'name': 'ManagerInst'}, {'lib': 'cycamore', 'name': 'GrowthRegion'}]}, 'region': {'name': 'GrowthRegion', 'config': {'GrowthRegion': {'growth': {'item': [{'commod': 'PowerLWR', 'piecewise_function': {'piece': [{'start': 18, 'function': {'type': 'exponential', 'params': '100000 0.00125 0'}}, {'start': 360, 'function': {'type': 'exponential', 'params': '178787.589146 -0.0012594698175040153 0'}}]}}, {'commod': 'PowerSFR', 'piecewise_function': {'piece': [{'start': 360, 'function': {'type': 'exponential', 'params': '178787.589146 0.002538267290392381 -178787.589146'}}]}}]}}}, 'institution': [{'name': 'InitFleet', 'config': {'DeployInst': {'prototypes': {'val': ['LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR']}, 'n_build': {'val': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}, 'build_times': {'val': [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16, 17, 17, 17, 17]}, 'lifetimes': {'val': [18, 23, 28, 33, 38, 43, 48, 53, 58, 63, 68, 73, 78, 83, 88, 93, 98, 103, 108, 113, 118, 123, 128, 133, 138, 143, 148, 153, 158, 163, 168, 173, 178, 183, 188, 193, 198, 203, 208, 213, 218, 223, 228, 233, 238, 243, 248, 253, 258, 263, 268, 273, 278, 283, 288, 293, 298, 303, 308, 313, 318, 323, 328, 333, 338, 343, 348, 353, 358, 363, 368, 373, 378, 383, 388, 393, 398, 403, 408, 413, 418, 423, 428, 433, 438, 443, 448, 453, 458, 463, 468, 473, 478, 483, 488, 493, 498, 503, 508, 513]}}}}, {'name': 'FCInstEG01-23', 'initialfacilitylist': {'entry': [{'number': 1, 'prototype': 'SourceInitUOX'}, {'number': 1, 'prototype': 'Source_UNAT'}, {'number': 1, 'prototype': 'Source_UNAT_ADD'}, {'number': 1, 'prototype': 'SourceNonIsos'}, {'number': 1, 'prototype': 'Enrichment'}, {'number': 1, 'prototype': 'Enrichment_ADD'}, {'number': 1, 'prototype': 'StorageDepU'}, {'number': 1, 'prototype': 'UOXCool'}, {'number': 1, 'prototype': 'UOXCool_ADD'}, {'number': 1, 'prototype': 'Waste'}]}, 'config': {'ManagerInst': {'prototypes': {'val': ['Source_UNAT', 'SourceNonIsos', 'Enrichment', 'Source_UNAT_ADD', 'Enrichment_ADD', 'StorageDepU', 'LWR', 'UOXCool', 'UOXCool_ADD', 'Waste', 'SFR']}}}}, {'name': 'EG23Deploy', 'config': {'DeployInst': {'prototypes': {'val': ['UOXSep', 'FFMixNon', 'FFCoolNon', 'FFSep']}, 'n_build': {'val': [1, 1, 1, 1]}, 'build_times': {'val': [360, 360, 360, 360]}}}}]}, 'facility': [{'name': 'SourceInitUOX', 'config': {'Source': {'outcommod': 'c_InitUOX', 'outrecipe': 'r_UOX', 'inventory_size': 8869500}}}, {'name': 'SourceNonIsos', 'config': {'Source': {'outcommod': 'NonIsos', 'outrecipe': 'NoAdditive_234', 'throughput': 1000000.0}}}, {'name': 'Source_UNAT', 'config': {'Source': {'outcommod': 'c_UNAT', 'outrecipe': 'r_UNAT', 'throughput': 180000000000.0, 'inventory_size': 100000000.0}}}, {'name': 'Source_UNAT_ADD', 'config': {'Source': {'outcommod': 'c_UNAT_ADD', 'outrecipe': 'r_UNAT_ADD', 'throughput': 210000000000.0}}}, {'name': 'Enrichment', 'config': {'Separations': {'leftover_commod': 'c_DU', 'throughput': 500000.0, 'feedbuf_size': 6000000.0, 'feed_commods': {'val': ['c_UNAT']}, 'streams': {'item': [{'commod': 'c_UOX', 'info': {'buf_size': 500000.0, 'efficiencies': {'item': [{'comp': 'U234', 'eff': 0.8480036104315597}, {'comp': 'U235', 'eff': 0.6812073348954103}, {'comp': 'U238', 'eff': 0.09282132068864048}]}}}]}}}}, {'name': 'Enrichment_ADD', 'config': {'Separations': {'leftover_commod': 'c_DU', 'throughput': 10000000.0, 'feedbuf_size': 1000000000.0, 'feed_commods': {'val': ['c_UNAT_ADD']}, 'streams': {'item': [{'commod': 'c_UOX_ADD', 'info': {'buf_size': 1e+100, 'efficiencies': {'item': [{'comp': 'U232', 'eff': 0.9508808638800464}, {'comp': 'U233', 'eff': 0.9100757654516153}, {'comp': 'U234', 'eff': 0.8294355333854383}, {'comp': 'U235', 'eff': 0.6825164922095507}, {'comp': 'U238', 'eff': 0.09281811152615514}]}}}]}}}}, {'name': 'StorageDepU', 'config': {'Storage': {'in_commods': {'val': 'c_DU'}, 'in_recipe': 'r_DU', 'out_commods': {'val': 'c_DU_str'}, 'residence_time': 0}}}, {'name': 'LWR', 'lifetime': 480, 'config': {'Reactor': {'fuel_incommods': {'val': ['c_UOX_ADD', 'c_UOX', 'c_InitUOX']}, 'fuel_outcommods': {'val': ['c_S_UOX_ADD', 'c_S_UOX', 'c_S_UOX']}, 'fuel_inrecipes': {'val': ['r_UOX_ADD', 'r_UOX', 'r_UOX']}, 'fuel_outrecipes': {'val': ['r_S_UOX_ADD', 'r_S_UOX', 'r_S_UOX']}, 'fuel_prefs': {'val': [10, 20, 25]}, 'cycle_time': 18, 'refuel_time': 0, 'assem_size': 29565, 'n_assem_core': 3, 'n_assem_batch': 1, 'power_name': 'PowerLWR', 'power_cap': 1000}}}, {'name': 'UOXCool', 'config': {'Storage': {'in_commods': {'val': ['c_S_UOX']}, 'out_commods': {'val': 'c_S_UOX_cool'}, 'residence_time': 81}}}, {'name': 'UOXCool_ADD', 'config': {'Storage': {'in_commods': {'val': ['c_S_UOX_ADD']}, 'out_commods': {'val': 'c_S_UOX_ADD_cool'}, 'residence_time': 81}}}, {'name': 'UOXSep', 'config': {'Separations': {'leftover_commod': 'Waste', 'throughput': 10000000.0, 'feedbuf_size': 1000000000.0, 'feed_commods': {'val': ['c_S_UOX_cool', 'c_S_UOX_ADD_cool']}, 'feed_commod_prefs': {'val': [1, 2]}, 'streams': {'item': [{'commod': 'UOX_Pu', 'info': {'buf_size': 1e+100, 'efficiencies': {'item': {'comp': 'Pu239', 'eff': 0.99}}}}, {'commod': 'UOX_RU', 'info': {'buf_size': 1e+100, 'efficiencies': {'item': {'comp': 'U238', 'eff': 0.99}}}}]}}}}, {'name': 'FFMixNon', 'config': {'Mixer': {'in_streams': {'stream': [{'info': {'mixing_ratio': 0.09, 'buf_size': 1000000000.0}, 'commodities': {'item': [{'commodity': 'UOX_Pu', 'pref': 1}, {'commodity': 'FF_Pu', 'pref': 2}]}}, {'info': {'mixing_ratio': 0.71, 'buf_size': 1000000000.0}, 'commodities': {'item': [{'commodity': 'UOX_RU', 'pref': 1}, {'commodity': 'FF_RU', 'pref': 1}]}}, {'info': {'mixing_ratio': 0.1995, 'buf_size': 1000000000.0}, 'commodities': {'item': [{'commodity': 'c_DU_str', 'pref': 2}, {'commodity': 'NatU', 'pref': 1}]}}, {'info': {'mixing_ratio': 0.0005, 'buf_size': 1000000000.0}, 'commodities': {'item': {'commodity': 'NonIsos', 'pref': 1}}}]}, 'out_commod': 'FF_Non', 'throughput': 10000000000.0, 'out_buf_size': 1e+20}}}, {'name': 'SFR', 'lifetime': 480, 'config': {'Reactor': {'fuel_incommods': {'val': ['FF_Non']}, 'fuel_outcommods': {'val': ['SpentFF_Non']}, 'fuel_inrecipes': {'val': ['FF_no232']}, 'fuel_outrecipes': {'val': ['SpentFF_no232']}, 'fuel_prefs': {'val': [1]}, 'cycle_time': 14, 'refuel_time': 0, 'assem_size': 7490, 'n_assem_core': 5, 'n_assem_batch': 1, 'power_name': 'PowerSFR', 'power_cap': 400}}}, {'name': 'FFSep', 'config': {'Separations': {'leftover_commod': 'Waste', 'throughput': 10000000.0, 'feedbuf_size': 10000000.0, 'feed_commods': {'val': ['CooledSpentFF_Non', 'CooledSpentFF_Add']}, 'feed_commod_prefs': {'val': [1, 2]}, 'streams': {'item': [{'commod': 'FF_Pu', 'info': {'buf_size': 1e+100, 'efficiencies': {'item': {'comp': 'Pu239', 'eff': 0.99}}}}, {'commod': 'FF_RU', 'info': {'buf_size': 1e+100, 'efficiencies': {'item': {'comp': 'U238', 'eff': 0.99}}}}]}}}}, {'name': 'FFCoolNon', 'config': {'Storage': {'in_commods': {'val': 'SpentFF_Non'}, 'out_commods': {'val': 'CooledSpentFF_Non'}, 'in_recipe': 'SpentFF_no232', 'residence_time': 81}}}, {'name': 'Waste', 'config': {'Sink': {'in_commods': {'val': 'Waste'}}}}], 'recipe': [{'name': 'r_DU', 'basis': 'mass', 'nuclide': [{'id': 'U235', 'comp': 0.0025}, {'id': 'U238', 'comp': 0.9975}]}, {'name': 'UOX_no232', 'basis': 'mass', 'nuclide': [{'id': 'U234', 'comp': 0.0004631049477}, {'id': 'U235', 'comp': 0.049906230293}, {'id': 'U238', 'comp': 0.9496306647594}]}, {'name': 'NoAdditive_234', 'basis': 'mass', 'nuclide': [{'id': 'U234', 'comp': 1.0}]}, {'name': 'r_UNAT', 'basis': 'mass', 'nuclide': [{'id': 'U234', 'comp': 5.3e-05}, {'id': 'U235', 'comp': 0.00711}, {'id': 'U238', 'comp': 0.99289}]}, {'name': 'r_UNAT_ADD', 'basis': 'mass', 'nuclide': [{'id': 'U232', 'comp': 1e-10}, {'id': 'U233', 'comp': 1.24824092316352e-10}, {'id': 'U234', 'comp': 5.30944854491094e-05}, {'id': 'U235', 'comp': 0.0071095114738325}, {'id': 'U238', 'comp': 0.992837393814684}]}, {'name': 'r_UOX', 'basis': 'mass', 'nuclide': [{'id': 'U234', 'comp': 0.0004631049477}, {'id': 'U235', 'comp': 0.049906230293}, {'id': 'U238', 'comp': 0.9496306647594}]}, {'name': 'r_S_UOX', 'basis': 'mass', 'nuclide': [{'id': 'U232', 'comp': 2.838e-10}, {'id': 'U233', 'comp': 5.8245e-09}, {'id': 'U234', 'comp': 0.0002961396326}, {'id': 'U235', 'comp': 0.0174611824759}, {'id': 'U236', 'comp': 0.006185388998}, {'id': 'U238', 'comp': 0.9250572827708}, {'id': 'Pu239', 'comp': 0.01}, {'id': 'Am241', 'comp': 0.001}, {'id': 'Cs137', 'comp': 0.04}]}, {'name': 'r_UOX_ADD', 'basis': 'mass', 'nuclide': [{'id': 'U232', 'comp': 9.79787642142e-10}, {'id': 'U233', 'comp': 1.17052802555e-09}, {'id': 'U234', 'comp': 0.000453772218252}, {'id': 'U235', 'comp': 0.0499987054095}, {'id': 'U238', 'comp': 0.949547520216}]}, {'name': 'r_S_UOX_ADD', 'basis': 'mass', 'nuclide': [{'id': 'U232', 'comp': 9.065e-10}, {'id': 'U233', 'comp': 6.2943e-09}, {'id': 'U234', 'comp': 0.0002327879338}, {'id': 'U235', 'comp': 0.0175266370423}, {'id': 'U236', 'comp': 0.0062071106222}, {'id': 'U238', 'comp': 0.9250334572009}, {'id': 'Pu239', 'comp': 0.01}, {'id': 'Am241', 'comp': 0.001}, {'id': 'Cs137', 'comp': 0.04}]}, {'name': 'FF_no232', 'basis': 'mass', 'nuclide': [{'id': 'U234', 'comp': 0.0004}, {'id': 'U235', 'comp': 0.004}, {'id': 'U238', 'comp': 0.9056}, {'id': 'Pu239', 'comp': 0.09}]}, {'name': 'SpentFF_no232', 'basis': 'mass', 'nuclide': [{'id': 'U232', 'comp': 3e-10}, {'id': 'U233', 'comp': 1e-08}, {'id': 'U234', 'comp': 0.0001}, {'id': 'U235', 'comp': 0.0001}, {'id': 'U236', 'comp': 0.0001}, {'id': 'U238', 'comp': 0.8476999897}, {'id': 'Pu239', 'comp': 0.15}, {'id': 'Am241', 'comp': 0.001}, {'id': 'Cs137', 'comp': 0.001}]}]}}