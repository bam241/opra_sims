isos_no232 = {'name' : 'NoAdditive_234',
             'basis' : 'mass',
             'nuclide' : [{'id' : 'U234', 'comp' : 1.0},]
            }
isos_232 = {'name' : 'Additive_232_233_234',
            'basis' : 'mass',
            'nuclide' : [{'id' : 'U232', 'comp' : 0.0000000010434},
                         {'id' : 'U233', 'comp' : 0.0000000012228},
                         {'id' : 'U234', 'comp' : 0.0004631049466}]
           }
enr_no232 = {'name' : 'AlmostUOX_no232',
             'basis' : 'mass',
             'nuclide' : [{'id' : 'U235', 'comp' : 0.0499062302930}, 
                          {'id' : 'U238', 'comp' : 0.9496306647594}]
            }
enr_232 = {'name' : 'AlmostUOX_232',
           'basis' : 'mass',
           'nuclide' : [{'id' : 'U235', 'comp' : 0.0499062301796},
                        {'id' : 'U238', 'comp' : 0.9496306626077}]
          }
uox_no232 = {'name' : 'UOX_no232',
             'basis' : 'mass',
             'nuclide' : [{'id' : 'U234', 'comp' : 0.0004631049477},
                          {'id' : 'U235', 'comp' : 0.0499062302930}, 
                          {'id' : 'U238', 'comp' : 0.9496306647594}]
            }
uox_232 = {'name' : 'UOX_232',
           'basis' : 'mass',
           'nuclide' : [{'id' : 'U232', 'comp' : 0.0000000010434},
                        {'id' : 'U233', 'comp' : 0.0000000012228},
                        {'id' : 'U234', 'comp' : 0.0004631049466}, 
                        {'id' : 'U235', 'comp' : 0.0499062301796},
                        {'id' : 'U238', 'comp' : 0.9496306626077}]
          }
uox_50pct232 = {'name' : 'UOX_50pct232',
                'basis' : 'mass',
                'nuclide' : [{'id' : 'U232', 'comp' : 0.0000000005217},
                             {'id' : 'U233', 'comp' : 0.0000000006114},
                             {'id' : 'U234', 'comp' : 0.0004631049471}, 
                             {'id' : 'U235', 'comp' : 0.0499062302363},
                             {'id' : 'U238', 'comp' : 0.9496306636835}]
               }
uox_10pct232 = {'name' : 'UOX_10pct232',
                'basis' : 'mass',
                'nuclide' : [{'id' : 'U232', 'comp' : 0.0000000001043},
                             {'id' : 'U233', 'comp' : 0.0000000001223},
                             {'id' : 'U234', 'comp' : 0.0004631049475}, 
                             {'id' : 'U235', 'comp' : 0.0499062302816},
                             {'id' : 'U238', 'comp' : 0.9496306645442}]
               }
# All non-U values are fake, and U238 is reduced from 
# 0.9760572827708 to accomodate these fake values
spent_no232 = {'name' : 'SpentUOX_no232',
               'basis' : 'mass',
               'nuclide' : [{'id' : 'U232',  'comp' : 0.0000000002838},
                            {'id' : 'U233',  'comp' : 0.0000000058245},
                            {'id' : 'U234',  'comp' : 0.0002961396326}, 
                            {'id' : 'U235',  'comp' : 0.0174611824759},
                            {'id' : 'U236',  'comp' : 0.0061853889980},
                            {'id' : 'U238',  'comp' : 0.9250572827708},
                            {'id' : 'Pu239', 'comp' : 0.0100000000000},
                            {'id' : 'Am241', 'comp' : 0.0010000000000},
                            {'id' : 'Cs137', 'comp' : 0.0400000000000}]
              }
# All non-U values are fake, and U238 is reduced from 
# 0.9760334572009 to accomodate these fake values
spent_232 = {'name' : 'SpentUOX_232',
             'basis' : 'mass',
             'nuclide' : [{'id' : 'U232',  'comp' : 0.0000000009065},
                          {'id' : 'U233',  'comp' : 0.0000000062943},
                          {'id' : 'U234',  'comp' : 0.0002327879338}, 
                          {'id' : 'U235',  'comp' : 0.0175266370423},
                          {'id' : 'U236',  'comp' : 0.0062071106222},
                          {'id' : 'U238',  'comp' : 0.9250334572009},
                          {'id' : 'Pu239', 'comp' : 0.0100000000000},
                          {'id' : 'Am241', 'comp' : 0.0010000000000},
                          {'id' : 'Cs137', 'comp' : 0.0400000000000}]
            }
# fake spent fuel recipes for 10 and 50 pct additive fuels:
# All non-U values are fake, and U238 is reduced from 
# 0.9760453699858 to accomodate these fake values
spent_50pct232 = {'name' : 'SpentUOX_50pct232',
                  'basis' : 'mass',
                  'nuclide' : [{'id' : 'U232',  'comp' : 0.0000000005952},
                               {'id' : 'U233',  'comp' : 0.0000000060594},
                               {'id' : 'U234',  'comp' : 0.0002644637832}, 
                               {'id' : 'U235',  'comp' : 0.0174939097591},
                               {'id' : 'U236',  'comp' : 0.0061962498101},
                               {'id' : 'U238',  'comp' : 0.9250453699858},
                               {'id' : 'Pu239', 'comp' : 0.0100000000000},
                               {'id' : 'Am241', 'comp' : 0.0010000000000},
                               {'id' : 'Cs137', 'comp' : 0.0400000000000}]
                 }
# All non-U values are fake, and U238 is reduced from 
# 0.9760549002138 to accomodate these fake values
spent_10pct232 = {'name' : 'SpentUOX_10pct232',
                  'basis' : 'mass',
                  'nuclide' : [{'id' : 'U232',  'comp' : 0.0000000003461},
                               {'id' : 'U233',  'comp' : 0.0000000058714},
                               {'id' : 'U234',  'comp' : 0.0002898044627}, 
                               {'id' : 'U235',  'comp' : 0.0174677279326},
                               {'id' : 'U236',  'comp' : 0.0061875611604},
                               {'id' : 'U238',  'comp' : 0.9250549002138},
                               {'id' : 'Pu239', 'comp' : 0.0100000000000},
                               {'id' : 'Am241', 'comp' : 0.0010000000000},
                               {'id' : 'Cs137', 'comp' : 0.0400000000000}]
                 }
###############################################################################
# Some placeholder, i.e., fake, recipes for SFRs. Not sure yet if we will do  #
# HALEU metal or U/PU metal.                                                  #
###############################################################################
ff_no232 = {'name' : 'FF_no232',
            'basis' : 'mass',
            'nuclide' : [{'id' : 'U234',  'comp' : 0.0004},
                         {'id' : 'U235',  'comp' : 0.0040}, 
                         {'id' : 'U238',  'comp' : 0.9056}, 
                         {'id' : 'Pu239', 'comp' : 0.0900}]
           }
ff_232 = {'name' : 'FF_232',
          'basis' : 'mass',
          'nuclide' : [{'id' : 'U232',  'comp' : 0.000000001},
                       {'id' : 'U233',  'comp' : 0.000000001},
                       {'id' : 'U234',  'comp' : 0.000400000}, 
                       {'id' : 'U235',  'comp' : 0.004000000},
                       {'id' : 'U238',  'comp' : 0.905599998},
                       {'id' : 'Pu239', 'comp' : 0.090000000}]
         }
spentff_no232 = {'name' : 'SpentFF_no232',
                 'basis' : 'mass',
                 'nuclide' : [{'id' : 'U232',  'comp' : 0.0000000003},
                              {'id' : 'U233',  'comp' : 0.0000000100},
                              {'id' : 'U234',  'comp' : 0.0001000000}, 
                              {'id' : 'U235',  'comp' : 0.0001000000},
                              {'id' : 'U236',  'comp' : 0.0001000000},
                              {'id' : 'U238',  'comp' : 0.8476999897},
                              {'id' : 'Pu239', 'comp' : 0.1500000000},
                              {'id' : 'Am241', 'comp' : 0.0010000000},
                              {'id' : 'Cs137', 'comp' : 0.0010000000}]
                }
spentff_232 = {'name' : 'SpentFF_232',
               'basis' : 'mass',
               'nuclide' : [{'id' : 'U232',  'comp' : 0.0000000009},
                            {'id' : 'U233',  'comp' : 0.0000000100},
                            {'id' : 'U234',  'comp' : 0.0001000000}, 
                            {'id' : 'U235',  'comp' : 0.0001000000},
                            {'id' : 'U236',  'comp' : 0.0001000000},
                            {'id' : 'U238',  'comp' : 0.8476999891},
                            {'id' : 'Pu239', 'comp' : 0.1500000000},
                            {'id' : 'Am241', 'comp' : 0.0010000000},
                            {'id' : 'Cs137', 'comp' : 0.0010000000}]
              }
