SIMULATION = {'simulation': {'control': {'duration': 864, 'startmonth': 1, 'startyear': 2000, 'dt': 86400}, 'archetypes': {'spec': [{'lib': 'cycamore', 'name': 'Source'}, {'lib': 'cycamore', 'name': 'Enrichment'}, {'lib': 'cycamore', 'name': 'Mixer'}, {'lib': 'cycamore', 'name': 'Reactor'}, {'lib': 'cycamore', 'name': 'Storage'}, {'lib': 'cycamore', 'name': 'Sink'}, {'lib': 'cycamore', 'name': 'DeployInst'}, {'lib': 'cycamore', 'name': 'ManagerInst'}, {'lib': 'cycamore', 'name': 'GrowthRegion'}]}, 'region': {'name': 'GrowthRegion', 'config': {'GrowthRegion': {'growth': {'item': [{'commod': 'power', 'piecewise_function': {'piece': [{'start': 18, 'function': {'type': 'linear', 'params': '0 100000'}}]}}]}}}, 'institution': [{'name': 'InitFleet', 'config': {'DeployInst': {'prototypes': {'val': ['LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR']}, 'n_build': {'val': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}, 'build_times': {'val': [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16, 17, 17, 17, 17]}, 'lifetimes': {'val': [181, 186, 191, 196, 201, 206, 211, 216, 221, 226, 231, 236, 241, 246, 251, 256, 261, 266, 271, 276, 281, 286, 291, 296, 301, 306, 311, 316, 321, 326, 331, 336, 341, 346, 351, 356, 361, 366, 371, 376, 381, 386, 391, 396, 401, 406, 411, 416, 421, 426, 431, 436, 441, 446, 451, 456, 461, 466, 471, 476, 481, 486, 491, 496, 501, 506, 511, 516, 521, 526, 531, 536, 541, 546, 551, 556, 561, 566, 571, 576, 581, 586, 591, 596, 601, 606, 611, 616, 621, 626, 631, 636, 641, 646, 651, 656, 661, 666, 671, 676]}}}}, {'name': 'FCInst', 'initialfacilitylist': {'entry': [{'number': 1, 'prototype': 'SourceInitUOX'}, {'number': 1, 'prototype': 'SourceNatU'}, {'number': 1, 'prototype': 'SourceNoAdditiveIsos'}, {'number': 1, 'prototype': 'SourceAdditiveIsos'}, {'number': 1, 'prototype': 'Enrichment'}, {'number': 1, 'prototype': 'StorageDepU'}, {'number': 1, 'prototype': 'StorageNoAdditive'}, {'number': 1, 'prototype': 'MixerNoAdditive'}, {'number': 1, 'prototype': 'StorageAdditive'}, {'number': 1, 'prototype': 'MixerAdditive'}, {'number': 1, 'prototype': 'CoolingLWR'}, {'number': 1, 'prototype': 'StorageLWR'}, {'number': 1, 'prototype': 'Waste'}]}, 'config': {'ManagerInst': {'prototypes': {'val': ['SourceNatU', 'SourceNoAdditiveIsos', 'SourceAdditiveIsos', 'Enrichment', 'StorageDepU', 'StorageNoAdditive', 'MixerNoAdditive', 'StorageAdditive', 'MixerAdditive', 'LWR', 'CoolingLWR', 'StorageLWR', 'Waste']}}}}, {'name': 'RampInst', 'config': {'DeployInst': {'prototypes': {'val': ['StorageRampNoAdditive', 'StorageRampAdditive', 'Mixer50pctAdditive', 'Mixer10pctAdditive']}, 'n_build': {'val': [1, 1, 1, 1]}, 'build_times': {'val': [264, 264, 264, 264]}}}}]}, 'facility': [{'name': 'SourceInitUOX', 'config': {'Source': {'outcommod': 'InitUOX', 'outrecipe': 'UOX_no232', 'inventory_size': 8869500}}}, {'name': 'SourceNatU', 'config': {'Source': {'outcommod': 'NatU', 'outrecipe': 'NU', 'throughput': 210000000000.0}}}, {'name': 'SourceNoAdditiveIsos', 'config': {'Source': {'outcommod': 'NoAdditiveIsos', 'outrecipe': 'NoAdditive_234', 'throughput': 1000000.0}}}, {'name': 'SourceAdditiveIsos', 'config': {'Source': {'outcommod': 'AdditiveIsos', 'outrecipe': 'Additive_232_233_234', 'throughput': 1000000.0}}}, {'name': 'Enrichment', 'config': {'Enrichment': {'feed_commod': 'NatU', 'feed_recipe': 'NU', 'product_commod': 'AlmostUOX', 'tails_commod': 'DepU', 'tails_assay': 0.0025, 'swu_capacity': 1e+100, 'initial_feed': 1e+100}}}, {'name': 'StorageDepU', 'config': {'Storage': {'in_commods': {'val': 'DepU'}, 'in_recipe': 'DU', 'out_commods': {'val': 'StoredDepU'}, 'residence_time': 0}}}, {'name': 'StorageNoAdditive', 'config': {'Storage': {'in_commods': {'val': 'AlmostUOX'}, 'in_recipe': 'AlmostUOX_no232', 'out_commods': {'val': 'AlmostUOX_NoAdditive'}, 'residence_time': 0, 'throughput': 100000000.0, 'max_inv_size': 10000000000.0}}}, {'name': 'MixerNoAdditive', 'config': {'Mixer': {'in_streams': {'stream': [{'info': {'mixing_ratio': 0.0004631049477, 'buf_size': 1000000.0}, 'commodities': {'item': {'commodity': 'NoAdditiveIsos', 'pref': 1.0}}}, {'info': {'mixing_ratio': 0.9995368950523, 'buf_size': 100000000.0}, 'commodities': {'item': {'commodity': 'AlmostUOX_NoAdditive', 'pref': 1.0}}}]}, 'out_commod': 'UOX_NoAdditive', 'throughput': 10000000000.0, 'out_buf_size': 1e+20}}}, {'name': 'StorageAdditive', 'config': {'Storage': {'in_commods': {'val': 'AlmostUOX'}, 'in_recipe': 'AlmostUOX_232', 'out_commods': {'val': 'AlmostUOX_Additive'}, 'residence_time': 0, 'throughput': 100000000.0, 'max_inv_size': 10000000000.0}}}, {'name': 'MixerAdditive', 'config': {'Mixer': {'in_streams': {'stream': [{'info': {'mixing_ratio': 0.0004631072127, 'buf_size': 1000000.0}, 'commodities': {'item': {'commodity': 'AdditiveIsos', 'pref': 1.0}}}, {'info': {'mixing_ratio': 0.9995368927873, 'buf_size': 100000000.0}, 'commodities': {'item': {'commodity': 'AlmostUOX_Additive', 'pref': 1.0}}}]}, 'out_commod': 'UOX_Additive', 'throughput': 10000000000.0, 'out_buf_size': 1e+20}}}, {'name': 'StorageRampNoAdditive', 'config': {'Storage': {'in_commods': {'val': 'UOX_NoAdditive'}, 'in_recipe': 'UOX_no232', 'out_commods': {'val': 'Mixer_UOX_NoAdditive'}, 'residence_time': 0, 'throughput': 10000000000.0, 'max_inv_size': 1e+20}}}, {'name': 'StorageRampAdditive', 'config': {'Storage': {'in_commods': {'val': 'UOX_Additive'}, 'in_recipe': 'UOX_232', 'out_commods': {'val': 'Mixer_UOX_Additive'}, 'residence_time': 0, 'throughput': 10000000000.0, 'max_inv_size': 1e+20}}}, {'name': 'Mixer50pctAdditive', 'config': {'Mixer': {'in_streams': {'stream': [{'info': {'mixing_ratio': 0.5, 'buf_size': 100000000.0}, 'commodities': {'item': {'commodity': 'Mixer_UOX_NoAdditive', 'pref': 1.0}}}, {'info': {'mixing_ratio': 0.5, 'buf_size': 100000000.0}, 'commodities': {'item': {'commodity': 'Mixer_UOX_Additive', 'pref': 1.0}}}]}, 'out_commod': 'UOX_50pctAdditive', 'throughput': 10000000000.0, 'out_buf_size': 1e+20}}}, {'name': 'Mixer10pctAdditive', 'config': {'Mixer': {'in_streams': {'stream': [{'info': {'mixing_ratio': 0.9, 'buf_size': 100000000.0}, 'commodities': {'item': {'commodity': 'Mixer_UOX_NoAdditive', 'pref': 1.0}}}, {'info': {'mixing_ratio': 0.1, 'buf_size': 100000000.0}, 'commodities': {'item': {'commodity': 'Mixer_UOX_Additive', 'pref': 1.0}}}]}, 'out_commod': 'UOX_10pctAdditive', 'throughput': 10000000000.0, 'out_buf_size': 1e+20}}}, {'name': 'LWR', 'lifetime': 720, 'config': {'Reactor': {'fuel_incommods': {'val': ['UOX_Additive', 'UOX_50pctAdditive', 'UOX_10pctAdditive', 'UOX_NoAdditive', 'InitUOX']}, 'fuel_outcommods': {'val': ['SpentUOX_Additive', 'SpentUOX_50pctAdditive', 'SpentUOX_10pctAdditive', 'SpentUOX_NoAdditive', 'SpentUOX_NoAdditive']}, 'fuel_inrecipes': {'val': ['UOX_232', 'UOX_50pct232', 'UOX_10pct232', 'UOX_no232', 'UOX_no232']}, 'fuel_outrecipes': {'val': ['SpentUOX_232', 'SpentUOX_50pct232', 'SpentUOX_10pct232', 'SpentUOX_no232', 'SpentUOX_no232']}, 'fuel_prefs': {'val': [1, 1, 1, 2, 2.5]}, 'pref_change_times': {'val': [264, 318, 372]}, 'pref_change_commods': {'val': ['UOX_10pctAdditive', 'UOX_50pctAdditive', 'UOX_Additive']}, 'pref_change_values': {'val': [3, 4, 5]}, 'cycle_time': 18, 'refuel_time': 0, 'assem_size': 29565, 'n_assem_core': 3, 'n_assem_batch': 1, 'power_cap': 1000}}}, {'name': 'CoolingLWR', 'config': {'Storage': {'in_commods': {'val': ['SpentUOX_Additive', 'SpentUOX_NoAdditive']}, 'out_commods': {'val': 'CooledSpentUOX'}, 'residence_time': 81}}}, {'name': 'StorageLWR', 'config': {'Storage': {'in_commods': {'val': 'CooledSpentUOX'}, 'out_commods': {'val': 'StoredSpentUOX'}, 'residence_time': 0}}}, {'name': 'Waste', 'config': {'Sink': {'in_commods': {'val': ['StoredSpentUOX', 'StoredDepU']}}}}], 'recipe': [{'name': 'DU', 'basis': 'mass', 'nuclide': [{'id': 'U235', 'comp': 0.0025}, {'id': 'U238', 'comp': 0.9975}]}, {'name': 'NU', 'basis': 'mass', 'nuclide': [{'id': 'U235', 'comp': 0.00711}, {'id': 'U238', 'comp': 0.99289}]}, {'name': 'NoAdditive_234', 'basis': 'mass', 'nuclide': [{'id': 'U234', 'comp': 1.0}]}, {'name': 'Additive_232_233_234', 'basis': 'mass', 'nuclide': [{'id': 'U232', 'comp': 1.0434e-09}, {'id': 'U233', 'comp': 1.2228e-09}, {'id': 'U234', 'comp': 0.0004631049466}]}, {'name': 'AlmostUOX_no232', 'basis': 'mass', 'nuclide': [{'id': 'U235', 'comp': 0.049906230293}, {'id': 'U238', 'comp': 0.9496306647594}]}, {'name': 'AlmostUOX_232', 'basis': 'mass', 'nuclide': [{'id': 'U235', 'comp': 0.0499062301796}, {'id': 'U238', 'comp': 0.9496306626077}]}, {'name': 'UOX_no232', 'basis': 'mass', 'nuclide': [{'id': 'U234', 'comp': 0.0004631049477}, {'id': 'U235', 'comp': 0.049906230293}, {'id': 'U238', 'comp': 0.9496306647594}]}, {'name': 'UOX_10pct232', 'basis': 'mass', 'nuclide': [{'id': 'U232', 'comp': 1.043e-10}, {'id': 'U233', 'comp': 1.223e-10}, {'id': 'U234', 'comp': 0.0004631049475}, {'id': 'U235', 'comp': 0.0499062302816}, {'id': 'U238', 'comp': 0.9496306645442}]}, {'name': 'UOX_50pct232', 'basis': 'mass', 'nuclide': [{'id': 'U232', 'comp': 5.217e-10}, {'id': 'U233', 'comp': 6.114e-10}, {'id': 'U234', 'comp': 0.0004631049471}, {'id': 'U235', 'comp': 0.0499062302363}, {'id': 'U238', 'comp': 0.9496306636835}]}, {'name': 'UOX_232', 'basis': 'mass', 'nuclide': [{'id': 'U232', 'comp': 1.0434e-09}, {'id': 'U233', 'comp': 1.2228e-09}, {'id': 'U234', 'comp': 0.0004631049466}, {'id': 'U235', 'comp': 0.0499062301796}, {'id': 'U238', 'comp': 0.9496306626077}]}, {'name': 'SpentUOX_no232', 'basis': 'mass', 'nuclide': [{'id': 'U232', 'comp': 2.838e-10}, {'id': 'U233', 'comp': 5.8245e-09}, {'id': 'U234', 'comp': 0.0002961396326}, {'id': 'U235', 'comp': 0.0174611824759}, {'id': 'U236', 'comp': 0.006185388998}, {'id': 'U238', 'comp': 0.9250572827708}, {'id': 'Pu239', 'comp': 0.01}, {'id': 'Am241', 'comp': 0.001}, {'id': 'Cs137', 'comp': 0.04}]}, {'name': 'SpentUOX_10pct232', 'basis': 'mass', 'nuclide': [{'id': 'U232', 'comp': 3.461e-10}, {'id': 'U233', 'comp': 5.8714e-09}, {'id': 'U234', 'comp': 0.0002898044627}, {'id': 'U235', 'comp': 0.0174677279326}, {'id': 'U236', 'comp': 0.0061875611604}, {'id': 'U238', 'comp': 0.9250549002138}, {'id': 'Pu239', 'comp': 0.01}, {'id': 'Am241', 'comp': 0.001}, {'id': 'Cs137', 'comp': 0.04}]}, {'name': 'SpentUOX_50pct232', 'basis': 'mass', 'nuclide': [{'id': 'U232', 'comp': 5.952e-10}, {'id': 'U233', 'comp': 6.0594e-09}, {'id': 'U234', 'comp': 0.0002644637832}, {'id': 'U235', 'comp': 0.0174939097591}, {'id': 'U236', 'comp': 0.0061962498101}, {'id': 'U238', 'comp': 0.9250453699858}, {'id': 'Pu239', 'comp': 0.01}, {'id': 'Am241', 'comp': 0.001}, {'id': 'Cs137', 'comp': 0.04}]}, {'name': 'SpentUOX_232', 'basis': 'mass', 'nuclide': [{'id': 'U232', 'comp': 9.065e-10}, {'id': 'U233', 'comp': 6.2943e-09}, {'id': 'U234', 'comp': 0.0002327879338}, {'id': 'U235', 'comp': 0.0175266370423}, {'id': 'U236', 'comp': 0.0062071106222}, {'id': 'U238', 'comp': 0.9250334572009}, {'id': 'Pu239', 'comp': 0.01}, {'id': 'Am241', 'comp': 0.001}, {'id': 'Cs137', 'comp': 0.04}]}]}}