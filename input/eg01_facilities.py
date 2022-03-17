# sources/enrichment
natu_source = {'name' : 'SourceNatU',
               'config' : {'Source' : {'outcommod' : 'NatU',
                                       'outrecipe' : 'NU',
                                       'throughput' : 2.1e11
                                      }
                          }
              }
non_source = {'name' : 'SourceNonIsos',
              'config' : {'Source' : {'outcommod' : 'NonIsos',
                                      'outrecipe' : 'NoAdditive_234',
                                      'throughput' : 1e6
                                     }
                         }
             }
add_source = {'name' : 'SourceAddIsos',
              'config' : {'Source' : {'outcommod' : 'AddIsos',
                                      'outrecipe' : 'Additive_232_233_234',
                                      'throughput' : 1e6
                                     }
                         }
             }
enrich = {'name' : 'Enrichment', 
          'config' : {'Enrichment' : {'feed_commod' : 'NatU',
                                      'feed_recipe' : 'NU',
                                      'product_commod' : 'AlmostUOX',
                                      'tails_commod' : 'DepU',
                                      'tails_assay' : 0.0025,
                                      'swu_capacity' : 1e100,
                                      'initial_feed' : 1e100
                                     }
                     }
         }
# mixer/storage scheme for 2 commod streams

# Since we are using recipe-based enrichment & the enr facility can't handle
# more than two isotopes: Making 2 post-enrichment storage-then-mixer facilities
# that will take in AlmostUOX and various other isotopes to produce the UOX
# recipes. (Storage is needed to request specific recipes)

# Non Additive Fuel Material Stream
store_no232 = {'name' : 'UOXStrNon', 
               'config' : {'Storage' : {'in_commods' : {'val' : 'AlmostUOX'}, 
                                        'in_recipe' : 'AlmostUOX_no232', 
                                        'out_commods' : {'val' : 'AlmostUOX_Non'}, 
                                        'residence_time' : 0,
                                        'throughput' : 1e8,
                                        'max_inv_size' : 1e10
                                       }
                          }
              }
######### item may need to be wrapped in a list ###########
mix_no_stream1 = {'info' : {'mixing_ratio' : 0.0004631049477, 
                            'buf_size' : 1e6
                           },
                  'commodities' : {'item' : {'commodity' : 'NonIsos', 
                                             'pref' : 1.0
                                            }
                                  }
                 }
mix_no_stream2 = {'info' : {'mixing_ratio' : 0.9995368950523,
                            'buf_size' : 1e8
                           },
                  'commodities' : {'item' : {'commodity' : 'AlmostUOX_Non',
                                             'pref' : 1.0
                                            }
                                  }
                 }
mix_no232 = {'name' : 'UOXMixNon',
             'config' : {'Mixer' : {'in_streams' : {'stream' : [mix_no_stream1, mix_no_stream2]},
                                    'out_commod' : 'UOX_Non',
                                    'throughput' : 1e10,
                                    'out_buf_size' : 1e20
                                   }
                        }
            }

# Additive Fuel Material Stream
store_232 = {'name' : 'UOXStrAdd', 
             'config' : {'Storage' : {'in_commods' : {'val' : 'AlmostUOX'}, 
                                      'in_recipe' : 'AlmostUOX_232', 
                                      'out_commods' : {'val' : 'AlmostUOX_Add'}, 
                                      'residence_time' : 0,
                                      'throughput' : 1e8,
                                      'max_inv_size' : 1e10
                                     }
                        }
            }
mix_add_stream1 = {'info' : {'mixing_ratio' : 0.0004631072127, 
                             'buf_size' : 1e6
                            },
                   'commodities' : {'item' : {'commodity' : 'AddIsos', 
                                              'pref' : 1.0
                                             }
                                   }
                  }
mix_add_stream2 = {'info' : {'mixing_ratio' : 0.9995368927873,
                             'buf_size' : 1e8
                            },
                   'commodities' : {'item' : {'commodity' : 'AlmostUOX_Add',
                                              'pref' : 1.0
                                             }
                                   }
                  }
mix_232 = {'name' : 'UOXMixAdd',
           'config' : {'Mixer' : {'in_streams' : {'stream' : [mix_add_stream1, mix_add_stream2]},
                                  'out_commod' : 'UOX_Add',
                                  'throughput' : 1e10,
                                  'out_buf_size' : 1e20
                                 }
                      }
          }
# storage/waste
du_store = {'name' : 'StorageDepU', 
            'config' : {'Storage' : {'in_commods' : {'val' : 'DepU'}, 
                                     'in_recipe' : 'DU', 
                                     'out_commods' : {'val' : 'StoredDepU'}, 
                                     'residence_time' : 0
                                    }
                       }
           }
lwr_cool = {'name' : 'UOXCool', 
            'config' : {'Storage' : {'in_commods' : {'val' : ['SpentUOX_Add', 'SpentUOX_Non']}, 
                                     'out_commods' : {'val' : 'CooledSpentUOX'}, 
                                     'residence_time' : 81
                                    }
                       }
           }
lwr_store = {'name' : 'UOXStr', 
             'config' : {'Storage' : {'in_commods' : {'val' : 'CooledSpentUOX'}, 
                                      'out_commods' : {'val' : 'StoredSpentUOX'}, 
                                      'residence_time' : 0
                                     }
                        }
            }
sink = {'name' : 'Waste', 
        'config' : {'Sink' : {'in_commods' : {'val' : ['StoredSpentUOX', 'StoredDepU']}
                             }
                   }
       }

# Extra facilities for ramp-up : mixer scheme for 10, 50 pct additive UOX streams

# first need extra storage to request separate stream/recipe
store_pct_no232 = {'name' : 'StorageRampNon', 
                   'config' : {'Storage' : {'in_commods' : {'val' : 'UOX_Non'}, 
                                            'in_recipe' : 'UOX_no232', 
                                            'out_commods' : {'val' : 'Mixer_UOX_Non'}, 
                                            'residence_time' : 0,
                                            'throughput' : 1e9,
                                            'max_inv_size' : 1e10
                                           }
                              }
                   }
store_pct_232 = {'name' : 'StorageRampAdd', 
                 'config' : {'Storage' : {'in_commods' : {'val' : 'UOX_Add'}, 
                                          'in_recipe' : 'UOX_232', 
                                          'out_commods' : {'val' : 'Mixer_UOX_Add'}, 
                                          'residence_time' : 0,
                                          'throughput' : 1e9,
                                          'max_inv_size' : 1e10
                                         }
                            }
                }

# 50 pct additive material stream
mix_non_stream50 = {'info' : {'mixing_ratio' : 0.5, 
                              'buf_size' : 1e8
                             },
                    'commodities' : {'item' : {'commodity' : 'Mixer_UOX_Non', 
                                               'pref' : 1.0
                                              }
                                    }
                   }
mix_add_stream50 = {'info' : {'mixing_ratio' : 0.5,
                              'buf_size' : 1e8
                             },
                    'commodities' : {'item' : {'commodity' : 'Mixer_UOX_Add',
                                               'pref' : 1.0
                                              }
                                    }
                   }
mix_50pct232 = {'name' : 'Mixer50pctAdd',
                'config' : {'Mixer' : {'in_streams' : {'stream' : [mix_non_stream50, mix_add_stream50]},
                                       'out_commod' : 'UOX_50pctAdd',
                                       'throughput' : 1e10,
                                       'out_buf_size' : 1e20
                                      }
                           }
               }

# 10 pct additive material stream
mix_non_stream10 = {'info' : {'mixing_ratio' : 0.9, 
                              'buf_size' : 1e8
                             },
                    'commodities' : {'item' : {'commodity' : 'Mixer_UOX_Non', 
                                               'pref' : 1.0
                                              }
                                    }
                   }
mix_add_stream10 = {'info' : {'mixing_ratio' : 0.1,
                              'buf_size' : 1e8
                             },
                    'commodities' : {'item' : {'commodity' : 'Mixer_UOX_Add',
                                               'pref' : 1.0
                                              }
                                    }
                   }
mix_10pct232 = {'name' : 'Mixer10pctAdd',
                'config' : {'Mixer' : {'in_streams' : {'stream' : [mix_non_stream10, mix_add_stream10]},
                                       'out_commod' : 'UOX_10pctAdd',
                                       'throughput' : 1e10,
                                       'out_buf_size' : 1e20
                                      }
                           }
               }
