test = [199,
200,
208,
210,
200,
207,
240,
269,
260,
263]

puzzle = '''134
138
142
143
141
142
145
140
144
156
158
163
164
170
192
193
194
218
216
229
210
212
217
219
252
254
253
256
257
258
259
270
271
273
289
314
289
315
321
330
331
307
316
325
326
330
344
347
330
342
344
337
338
341
345
347
364
394
395
418
421
422
425
426
434
432
442
443
445
446
459
460
469
464
449
466
484
485
488
489
495
499
501
504
505
508
520
530
535
537
533
534
538
539
542
544
545
546
547
565
566
579
586
596
601
602
615
623
625
626
641
645
654
657
659
658
661
678
680
682
673
682
686
689
694
704
705
706
734
735
741
746
747
756
772
773
806
807
819
820
824
837
835
837
834
842
844
860
855
862
863
873
898
904
908
909
910
911
921
922
928
930
943
949
951
947
953
963
965
967
970
975
976
979
986
1009
1017
1021
1022
1047
1073
1075
1100
1101
1136
1143
1149
1148
1149
1150
1154
1167
1169
1175
1178
1181
1191
1194
1195
1196
1203
1204
1188
1196
1197
1198
1211
1213
1221
1225
1227
1232
1233
1244
1245
1251
1252
1253
1254
1281
1292
1293
1296
1306
1320
1312
1313
1318
1319
1322
1323
1324
1344
1345
1348
1354
1357
1356
1359
1360
1362
1363
1364
1366
1384
1388
1389
1388
1390
1391
1412
1415
1416
1415
1414
1424
1429
1430
1453
1459
1470
1472
1491
1494
1499
1497
1498
1491
1496
1497
1496
1523
1527
1532
1525
1555
1559
1576
1586
1593
1609
1610
1612
1619
1645
1650
1657
1677
1705
1706
1709
1713
1722
1737
1773
1783
1795
1796
1807
1806
1807
1808
1828
1829
1835
1837
1845
1848
1847
1854
1862
1860
1861
1862
1863
1868
1882
1892
1904
1876
1875
1877
1907
1922
1936
1932
1938
1948
1950
1953
1955
1957
1958
1956
1961
1966
1964
1968
1987
1984
1988
1990
1991
2009
2012
2018
2022
2041
2042
2057
2058
2056
2064
2070
2073
2077
2080
2041
2044
2042
2045
2053
2052
2054
2055
2058
2064
2068
2067
2078
2086
2085
2090
2093
2108
2109
2110
2118
2114
2121
2124
2125
2111
2112
2126
2127
2138
2141
2153
2158
2170
2161
2162
2163
2164
2165
2175
2196
2205
2210
2209
2210
2218
2234
2254
2255
2266
2267
2269
2270
2274
2276
2263
2264
2266
2267
2264
2267
2276
2283
2284
2287
2298
2299
2309
2310
2321
2322
2323
2328
2330
2333
2336
2366
2367
2368
2365
2371
2372
2373
2371
2375
2376
2373
2379
2380
2382
2392
2394
2398
2420
2427
2438
2439
2440
2441
2452
2453
2478
2482
2484
2495
2510
2514
2516
2531
2536
2563
2564
2559
2585
2599
2608
2613
2611
2619
2633
2644
2645
2646
2649
2632
2649
2656
2651
2663
2678
2684
2682
2684
2685
2686
2687
2708
2709
2718
2720
2721
2727
2733
2751
2740
2742
2749
2748
2750
2780
2757
2762
2760
2771
2758
2777
2781
2785
2787
2812
2825
2830
2838
2840
2852
2857
2862
2865
2847
2846
2847
2848
2849
2852
2854
2859
2868
2870
2872
2873
2882
2889
2890
2893
2890
2891
2895
2901
2907
2911
2912
2920
2921
2925
2924
2942
2952
2961
2965
2964
2978
2981
2992
3010
3005
3019
3013
3015
3019
3022
3024
3027
3037
3038
3041
3043
3047
3065
3075
3083
3092
3093
3117
3118
3119
3125
3126
3130
3145
3137
3149
3153
3154
3155
3180
3182
3183
3182
3200
3202
3214
3197
3207
3185
3203
3208
3209
3208
3231
3233
3234
3242
3255
3256
3257
3258
3265
3268
3290
3291
3297
3311
3301
3309
3314
3317
3319
3320
3337
3347
3362
3376
3390
3404
3412
3417
3418
3421
3425
3436
3438
3439
3453
3467
3484
3485
3486
3515
3516
3521
3527
3534
3551
3561
3572
3573
3574
3596
3612
3595
3616
3617
3619
3620
3624
3634
3657
3663
3671
3686
3687
3694
3704
3695
3697
3698
3699
3700
3701
3702
3704
3705
3707
3716
3717
3732
3747
3748
3745
3746
3748
3756
3757
3764
3765
3766
3768
3784
3807
3810
3805
3811
3812
3813
3828
3840
3847
3848
3851
3850
3851
3855
3861
3862
3867
3864
3871
3879
3884
3885
3887
3888
3928
3948
3949
3950
3960
3959
3965
3973
3970
3971
3972
3974
3969
3997
3998
4014
4016
4017
4026
4039
4043
4052
4053
4051
4054
4058
4066
4067
4073
4077
4084
4072
4078
4083
4094
4101
4107
4115
4138
4141
4143
4166
4177
4184
4194
4192
4198
4203
4204
4209
4215
4217
4226
4231
4252
4253
4260
4294
4306
4307
4314
4316
4317
4325
4326
4334
4344
4348
4344
4348
4350
4358
4383
4384
4390
4383
4378
4374
4377
4398
4399
4431
4432
4433
4432
4443
4441
4442
4443
4439
4441
4444
4445
4446
4449
4452
4458
4463
4469
4472
4475
4478
4491
4504
4507
4509
4510
4511
4513
4525
4532
4533
4541
4552
4551
4552
4573
4594
4597
4601
4602
4617
4621
4622
4621
4601
4604
4606
4607
4611
4591
4604
4608
4615
4613
4621
4625
4642
4637
4641
4659
4674
4678
4680
4700
4701
4702
4703
4706
4712
4699
4701
4704
4706
4707
4714
4717
4721
4722
4731
4735
4748
4749
4753
4757
4779
4783
4788
4790
4791
4794
4813
4814
4815
4801
4803
4806
4807
4837
4838
4842
4844
4854
4855
4859
4856
4847
4849
4850
4852
4866
4868
4880
4902
4901
4905
4909
4921
4922
4939
4920
4922
4938
4944
4947
4948
4960
4961
4971
4986
4992
4996
5004
5003
5008
5002
5004
5021
5023
5009
5012
5014
5019
5033
5047
5048
5046
5047
5072
5078
5080
5081
5067
5097
5103
5109
5114
5121
5126
5127
5128
5129
5150
5154
5131
5113
5115
5116
5118
5134
5135
5152
5158
5160
5171
5188
5195
5196
5198
5202
5204
5205
5209
5225
5232
5235
5242
5243
5244
5234
5254
5255
5272
5273
5282
5288
5311
5312
5302
5304
5307
5316
5319
5322
5323
5324
5326
5327
5337
5342
5346
5353
5363
5376
5378
5403
5405
5406
5402
5412
5424
5428
5430
5431
5435
5436
5439
5444
5446
5447
5456
5470
5474
5500
5513
5515
5505
5508
5509
5511
5512
5520
5523
5526
5532
5534
5564
5568
5579
5598
5599
5600
5608
5609
5636
5648
5655
5667
5668
5674
5678
5679
5692
5693
5694
5696
5711
5703
5711
5717
5716
5733
5734
5735
5736
5740
5757
5762
5788
5797
5798
5809
5814
5815
5826
5827
5829
5809
5815
5817
5818
5819
5820
5822
5831
5837
5838
5844
5850
5846
5851
5865
5870
5882
5885
5888
5892
5901
5906
5908
5910
5911
5909
5915
5912
5914
5932
5934
5940
5949
5951
5952
5954
5963
5962
5961
5962
5964
5966
5969
6009
6013
6015
6024
6043
6041
6047
6057
6061
6062
6061
6070
6074
6075
6084
6113
6138
6139
6146
6148
6157
6191
6193
6194
6200
6219
6226
6228
6230
6235
6236
6241
6265
6267
6268
6270
6271
6273
6275
6274
6275
6289
6290
6294
6303
6306
6311
6312
6313
6319
6320
6332
6344
6339
6350
6355
6357
6359
6362
6344
6345
6362
6372
6376
6389
6393
6395
6398
6401
6420
6422
6425
6433
6445
6446
6464
6472
6487
6498
6505
6484
6496
6511
6510
6501
6503
6513
6542
6553
6561
6575
6585
6593
6612
6613
6614
6619
6618
6614
6615
6617
6627
6634
6638
6640
6642
6662
6663
6664
6669
6677
6689
6709
6710
6711
6712
6713
6721
6722
6743
6740
6729
6731
6728
6729
6734
6739
6748
6751
6752
6753
6759
6738
6739
6761
6765
6764
6772
6773
6798
6821
6828
6829
6831
6837
6843
6844
6845
6849
6851
6854
6855
6856
6863
6860
6874
6881
6893
6896
6901
6899
6906
6915
6920
6930
6942
6944
6956
6977
6980
6982
6984
6991
6990
7006
7018
7034
7036
7041
7042
7043
7066
7069
7062
7066
7082
7087
7112
7131
7132
7139
7140
7145
7146
7148
7146
7147
7151
7152
7142
7126
7127
7123
7120
7131
7132
7136
7139
7140
7144
7148
7153
7154
7158
7174
7188
7190
7191
7212
7216
7215
7218
7237
7241
7242
7247
7251
7265
7289
7295
7298
7302
7323
7324
7333
7321
7320
7328
7326
7328
7349
7359
7361
7362
7379
7380
7381
7387
7391
7404
7408
7417
7418
7429
7430
7451
7456
7460
7466
7470
7487
7514
7520
7522
7523
7519
7546
7557
7567
7572
7573
7566
7567
7568
7571
7579
7548
7551
7552
7555
7559
7568
7570
7573
7576
7568
7571
7570
7573
7586
7589
7590
7589
7586
7587
7588
7592
7611
7626
7627
7633
7632
7633
7634
7641
7645
7644
7666
7662
7658
7662
7663
7669
7672
7665
7674
7660
7668
7673
7694
7712
7715
7737
7738
7740
7741
7756
7764
7801
7802
7804
7814
7845
7885
7889
7888
7886
7889
7890
7894
7895
7918
7919
7941
7942
7943
7952
7953
7954
7957
7958
7959
7960
7967
7968
7970
7987
7988
7990
7991
7993
8000
8002
7990
7999
8002
8001
8003
8009
8023
8037
8040
8041
8045
8063
8061
8065
8067
8072
8091
8097
8116
8117
8118
8102
8104
8105
8142
8141
8149
8168
8176
8178
8183
8186
8219
8221
8226
8239
8244
8246
8268
8293
8299
8310
8312
8314
8315
8310
8320
8321
8322
8341
8342
8369
8402
8406
8407
8408
8409
8412
8416
8419
8420
8419
8418
8415
8420
8421
8442
8446
8449
8452
8448
8458
8459
8468
8485
8488
8502
8504
8505
8506
8510
8526
8541
8574
8575
8576
8546
8557
8565
8566
8567
8583
8596
8606
8616
8612
8607
8608
8611
8612
8642
8647
8651
8653
8671
8686
8682
8686
8688
8702
8705
8704
8712
8717
8718
8719
8724
8727
8728
8729
8746
8751
8750
8757
8715
8719
8720
8721
8747
8748
8766
8772
8792
8796
8795
8800
8810
8811
8822
8823
8824
8830
8860
8861
8867
8877
8878
8885
8894
8895
8903
8914
8916
8919
8940
8968
8969
8984
8982
8984
8983
8982
8988
8989
8993
8994
9001
9008
9026
9029
9037
9038
9039
9050
9053
9055
9056
9059
9076
9075
9081
9092
9100
9101
9123
9124
9147
9143
9146
9180
9181
9191
9200
9201
9202
9210
9224
9228
9229
9234
9235
9237
9241
9260
9261
9262
9271
9272
9271
9275
9289
9290
9320
9322
9356
9371
9372
9373
9374
9386
9387
9388
9414
9409
9420
9422
9430
9442
9443
9445
9449
9467
9472
9473
9487
9489
9493
9498
9501
9502
9507
9518
9521
9522
9523
9503
9509
9545
9546
9562
9546
9531
9535
9558
9559
9561
9560
9561
9562
9561
9570
9564
9562
9563
9568
9569
9577
9606
9607
9608
9602
9606
9608
9622
9623
9630
9652
9653
9650
9651
9673
9675
9676
9678
9684
9685
9690
9695
9706
9725
9750
9762
9769
9770
9772
9770
9806
9828
9837
9836
9844
9845
9849
9875
9897
9901
9916
9923
9944
9945
9952
9961
9973
9977
9987
9986
9989
9992
9993
9994
10019
10023
10021
10015
10016
10017
10018
10026
10027
10037
10039
10040
10041
10042
10040
10041
10044
10055
10066
10059
10060
10063
10062
10055
10062
10068
10076
10086
10101
10104
10107
10100
10116
10120
10121
10128
10136
10139
10154
10166
10167
10170
10171
10172
10179
10182
10184
10189
10191
10204
10207
10214
10213
10214
10220
10222
10225
10223
10220
10238
10240
10243
10247
10241
10273
10281
10282
10286
10311
10313
10318
10319
10324
10331
10338
10320
10322
10323
10328
10336
10339
10352
10366
10367
10375
10385
10386
10388
10389
10387
10388
10392
10399
10404
10405
10408
10417
10413
10416
10417
10427
10432
10434
10433
10445
10446
10448
10449
10450
10451
10452
10445
10446
10453
10452
10461
10462
10463
10470
10473
10487
10491
10514
10517
10518
10522
10528
10540
10541
10543
10561
10564
10573
10544
10550
10552
10562
10567
10568
10567
10563
10559
10566
10571
10573
10577
10578
10580
10596
10603
10574
10575
10570
10571
10579
10580
10581
10600
10603
10615
10617
10618
10637
10639
10641
10642
10652
10688
10696
10702
10706
10688
10689
10694
10689
10704
10721
10722
10725
10727
10737
10739
10747
10750
10751
10755
10756
10753'''