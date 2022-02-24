# sources/enrichment
natu_source = {'name' : 'SourceNatU',
               'config' : {'Source' : {'outcommod' : 'NatU',
                                       'outrecipe' : 'NU',
                                       'throughput' : 2.1e11
                                      }
                          }
              }
non_source = {'name' : 'SourceNoAdditiveIsos',
              'config' : {'Source' : {'outcommod' : 'NoAdditiveIsos',
                                      'outrecipe' : 'NoAdditive_234',
                                      'throughput' : 1e6
                                     }
                         }
             }
add_source = {'name' : 'SourceAdditiveIsos',
              'config' : {'Source' : {'outcommod' : 'AdditiveIsos',
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
store_no232 = {'name' : 'StorageNoAdditive', 
               'config' : {'Storage' : {'in_commods' : {'val' : 'AlmostUOX'}, 
                                        'in_recipe' : 'AlmostUOX_no232', 
                                        'out_commods' : {'val' : 'AlmostUOX_NoAdditive'}, 
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
                  'commodities' : {'item' : {'commodity' : 'NoAdditiveIsos', 
                                             'pref' : 1.0
                                            }
                                  }
                 }
mix_no_stream2 = {'info' : {'mixing_ratio' : 0.9995368950523,
                            'buf_size' : 1e8
                           },
                  'commodities' : {'item' : {'commodity' : 'AlmostUOX_NoAdditive',
                                             'pref' : 1.0
                                            }
                                  }
                 }
mix_no232 = {'name' : 'MixerNoAdditive',
             'config' : {'Mixer' : {'in_streams' : {'stream' : [mix_no_stream1, mix_no_stream2]},
                                    'out_commod' : 'UOX_NoAdditive',
                                    'throughput' : 1e10,
                                    'out_buf_size' : 1e20
                                   }
                        }
            }

# Additive Fuel Material Stream
store_232 = {'name' : 'StorageAdditive', 
             'config' : {'Storage' : {'in_commods' : {'val' : 'AlmostUOX'}, 
                                      'in_recipe' : 'AlmostUOX_232', 
                                      'out_commods' : {'val' : 'AlmostUOX_Additive'}, 
                                      'residence_time' : 0,
                                      'throughput' : 1e8,
                                      'max_inv_size' : 1e10
                                     }
                        }
            }
mix_add_stream1 = {'info' : {'mixing_ratio' : 0.0004631072127, 
                             'buf_size' : 1e6
                            },
                   'commodities' : {'item' : {'commodity' : 'AdditiveIsos', 
                                              'pref' : 1.0
                                             }
                                   }
                  }
mix_add_stream2 = {'info' : {'mixing_ratio' : 0.9995368927873,
                             'buf_size' : 1e8
                            },
                   'commodities' : {'item' : {'commodity' : 'AlmostUOX_Additive',
                                              'pref' : 1.0
                                             }
                                   }
                  }
mix_232 = {'name' : 'MixerAdditive',
           'config' : {'Mixer' : {'in_streams' : {'stream' : [mix_add_stream1, mix_add_stream2]},
                                  'out_commod' : 'UOX_Additive',
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
lwr_cool = {'name' : 'CoolingLWR', 
            'config' : {'Storage' : {'in_commods' : {'val' : ['SpentUOX_Additive', 'SpentUOX_NoAdditive']}, 
                                     'out_commods' : {'val' : 'CooledSpentUOX'}, 
                                     'residence_time' : 81
                                    }
                       }
           }
lwr_store = {'name' : 'StorageLWR', 
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

