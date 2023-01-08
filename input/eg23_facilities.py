
# New sink
eg23_sink = {'name' : 'Waste',
             'config' : {'Sink' : {'in_commods' : {'val' : 'Waste'}
                                  }
                        }
            }

# Post-LWR Facilities

# Storage facilities can take many inputs but only give one output, so unlike in EG01
# am now separating the spent fuel cooling and storage into separate streams
non_lwr_cool = {'name' : 'UOXCoolNon',
                'config' : {'Storage' : {'in_commods' : {'val' : 'SpentUOX_Non'},
                                         'out_commods' : {'val' : 'CooledSpentUOX_Non'},
                                         'in_recipe' : 'SpentUOX_no232',
                                         'residence_time' : 81
                                        }
                           }
               }
add_lwr_cool = {'name' : 'UOXCoolAdd',
                'config' : {'Storage' : {'in_commods' : {'val' : 'SpentUOX_Add'},
                                         'out_commods' : {'val' : 'CooledSpentUOX_Add'},
                                         'in_recipe' : 'SpentUOX_232',
                                         'residence_time' : 81
                                        }
                           }
               }
lwr_sep_streams = {
    'item': [
        {
            'commod': 'UOX_Pu', 'info': {
                'buf_size': 1e100, 'efficiencies': {
                    'item': {
                        'comp': 'Pu239', 'eff': 0.99}}}}, {
                            'commod': 'UOX_RU', 'info': {
                                'buf_size': 1e100, 'efficiencies': {
                                    'item': {
                                        'comp': 'U238', 'eff': 0.99}}}}]}
lwr_sep = {'name' : 'UOXSep',
           'config' : {'Separations' : {'leftover_commod' : 'Waste',
                                        'throughput': 1e7,
                                        'feedbuf_size': 1e8,
                                        # can't use feed recipe unless we split into 2 sep facilities for each commod
                                        'feed_commods' : {'val' : ['CooledSpentUOX_Non', 'CooledSpentUOX_Add']},
                                        'feed_commod_prefs' : {'val' : [1, 2]},
                                        'streams' : lwr_sep_streams
                                       }
                      }
          }

# SFR Additions

mix_pu = {'info': {'mixing_ratio': 0.0900,
                    'buf_size' : 1e8},
          'commodities' : {'item' : [{'commodity' : 'UOX_Pu',
                                      'pref' : 1},
                                     {'commodity' : 'FF_Pu',
                                      'pref' : 2},
                                    ]
                          }
         }
mix_ru = {'info' : {'mixing_ratio' : 0.7100,
                    'buf_size' : 1e8
                    },
          'commodities' : {'item' : [{'commodity' : 'UOX_RU',
                                      'pref' : 1},
                                     {'commodity' : 'FF_RU',
                                      'pref' : 1}
                                    ]
                          }
         }
mix_natu = {'info' : {'mixing_ratio' : 0.1995,
                      'buf_size' : 1e8
                      },
            'commodities' : {'item' : [{'commodity' : 'StoredDepU',
                                        'pref' : 2},
                                       {'commodity' : 'NatU',
                                        'pref' : 1}
                                      ]
                            }
           }
mix_non_iso = {'info' : {'mixing_ratio' : 0.0005,
                         'buf_size' : 1e8
                         },
               'commodities' : {'item' : {'commodity' : 'NonIsos',
                                           'pref' : 1}
                               }
              }
mix_add_iso = {'info' : {'mixing_ratio' : 0.0005,
                         'buf_size' : 1e8
                         },
               'commodities' : {'item' : {'commodity' : 'AddIsos',
                                           'pref' : 1}
                               }
              }
sfr_mix_no232 = {'name' : 'FFMixNon',
                 'config' : {'Mixer' : {'in_streams' : {'stream' : [mix_pu, mix_ru, mix_natu, mix_non_iso]},
                                        'out_commod' : 'FF_Non',
                                        'throughput' : 1e10,
                                        'out_buf_size' : 1e20
                                       }
                            }
                }
sfr_mix_232 = {'name' : 'FFMixAdd',
               'config' : {'Mixer' : {'in_streams' : {'stream' : [mix_pu, mix_ru, mix_natu, mix_add_iso]},
                                      'out_commod' : 'FF_Add',
                                      'throughput' : 1e10,
                                      'out_buf_size' : 1e20
                                     }
                          }
              }
non_sfr_cool = {'name' : 'FFCoolNon',
                'config' : {'Storage' : {'in_commods' : {'val' : 'SpentFF_Non'},
                                         'out_commods' : {'val' : 'CooledSpentFF_Non'},
                                         'in_recipe' : 'SpentFF_no232',
                                         'residence_time' : 81
                                        }
                           }
               }
add_sfr_cool = {'name' : 'FFCoolAdd',
                'config' : {'Storage' : {'in_commods' : {'val' : 'SpentFF_Add'},
                                         'out_commods' : {'val' : 'CooledSpentFF_Add'},
                                         'in_recipe' : 'SpentFF_232',
                                         'residence_time' : 81
                                        }
                           }
               }
sfr_sep_streams = {
    'item': [
        {
            'commod': 'FF_Pu', 'info': {
                'buf_size': 1e100, 'efficiencies': {
                    'item': {
                        'comp': 'Pu239', 'eff': 0.99}}}}, {
                            'commod': 'FF_RU', 'info': {
                                'buf_size': 1e100, 'efficiencies': {
                                    'item': {
                                        'comp': 'U238', 'eff': 0.99}}}}]}
#other studies changed SepSFR values to 1e100
sfr_sep = {'name' : 'FFSep',
           'config' : {'Separations' : {'leftover_commod' : 'Waste',
                                        'throughput': 1e7,
                                        'feedbuf_size': 1e7,
                                        # can't use feed recipe unless we split into 2 sep facilities for each commod
                                        'feed_commods' : {'val' : ['CooledSpentFF_Non', 'CooledSpentFF_Add']},
                                        'feed_commod_prefs' : {'val' : [1, 2]},
                                        'streams' : sfr_sep_streams
                                       }
                      }
          }
