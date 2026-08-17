# Selected Nova1492 Decompilation

## `004804a0`

- Function: `FUN_004804a0`
- Entry: `004804a0`

```c

void FUN_004804a0(void)

{
  int iVar1;
  undefined4 *puVar2;
  undefined4 *puVar3;
  undefined4 local_50 [4];
  undefined4 local_40;
  undefined4 local_3c;
  undefined4 local_38;
  undefined4 local_34;
  undefined4 local_30;
  undefined4 local_2c;
  undefined4 local_28;
  undefined4 local_24;
  undefined4 local_20;
  undefined4 local_1c;
  undefined4 local_18;
  undefined4 local_14;
  
  local_50[0] = DAT_008b22e0;
  local_50[1] = DAT_008b22e4;
  local_50[2] = DAT_008b22e8;
  local_50[3] = DAT_008b22ec;
  local_40 = DAT_008b22f0;
  local_3c = DAT_008b22f4;
  local_38 = DAT_008b22f8;
  local_34 = DAT_008b22fc;
  local_30 = DAT_008b2300;
  local_2c = DAT_008b2304;
  local_28 = DAT_008b2308;
  local_24 = DAT_008b230c;
  local_20 = DAT_008b2310;
  local_1c = DAT_008b2314;
  local_18 = DAT_008b2318;
  local_14 = DAT_008b231c;
  puVar2 = local_50;
  puVar3 = &DAT_00736d50;
  for (iVar1 = 0x10; iVar1 != 0; iVar1 = iVar1 + -1) {
    *puVar3 = *puVar2;
    puVar2 = puVar2 + 1;
    puVar3 = puVar3 + 1;
  }
  puVar2 = local_50;
  puVar3 = &DAT_00736d90;
  for (iVar1 = 0x10; iVar1 != 0; iVar1 = iVar1 + -1) {
    *puVar3 = *puVar2;
    puVar2 = puVar2 + 1;
    puVar3 = puVar3 + 1;
  }
  puVar2 = local_50;
  puVar3 = &DAT_00736d10;
  for (iVar1 = 0x10; iVar1 != 0; iVar1 = iVar1 + -1) {
    *puVar3 = *puVar2;
    puVar2 = puVar2 + 1;
    puVar3 = puVar3 + 1;
  }
  return;
}


```

## `00480b30`

- Function: `FUN_00480b30`
- Entry: `00480b30`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00480b30(void)

{
  undefined1 auVar1 [16];
  undefined1 auVar2 [16];
  undefined1 auVar3 [16];
  float *pfVar4;
  undefined4 *puVar5;
  int iVar6;
  uint *puVar7;
  uint *puVar8;
  undefined4 *puVar9;
  float10 fVar10;
  undefined1 auVar11 [16];
  undefined1 auVar12 [16];
  undefined1 auVar13 [16];
  undefined1 auVar14 [16];
  undefined1 auVar15 [16];
  undefined1 auVar16 [16];
  undefined1 auVar17 [16];
  undefined1 auVar18 [16];
  undefined1 auVar19 [16];
  float fVar20;
  float fVar21;
  float fVar22;
  float fVar23;
  undefined1 auVar24 [16];
  undefined1 auVar25 [16];
  undefined1 auVar26 [16];
  undefined1 auVar27 [16];
  undefined1 auVar28 [16];
  undefined1 auVar29 [16];
  undefined1 auVar30 [16];
  undefined1 auVar31 [16];
  undefined1 auVar32 [16];
  float fVar33;
  float fVar35;
  float fVar36;
  float fVar37;
  float fVar38;
  undefined1 auVar34 [16];
  float fVar39;
  float fVar40;
  float fVar41;
  float fVar42;
  float fVar44;
  float fVar45;
  undefined1 auVar43 [16];
  float fVar46;
  undefined1 auStack_508 [4];
  float local_504;
  undefined1 local_500 [8];
  float fStack_4f8;
  float fStack_4f4;
  undefined1 local_4f0 [8];
  float fStack_4e8;
  float fStack_4e4;
  undefined1 local_4e0 [16];
  float local_4d0;
  float fStack_4cc;
  float fStack_4c8;
  float fStack_4c4;
  float local_4c0;
  float fStack_4bc;
  float fStack_4b8;
  float fStack_4b4;
  float local_4b0;
  float fStack_4ac;
  float fStack_4a8;
  float fStack_4a4;
  float local_4a0;
  float fStack_49c;
  float fStack_498;
  float fStack_494;
  float local_484;
  float local_480;
  float local_47c;
  undefined4 local_478;
  undefined4 local_474;
  undefined4 local_470;
  float local_46c;
  float local_468;
  float local_464;
  uint local_460;
  uint uStack_45c;
  uint uStack_458;
  uint uStack_454;
  uint local_450;
  uint uStack_44c;
  uint uStack_448;
  uint uStack_444;
  float local_440;
  float fStack_43c;
  float fStack_438;
  float fStack_434;
  float local_430;
  float fStack_42c;
  float fStack_428;
  float fStack_424;
  undefined1 local_420 [16];
  float local_410;
  float fStack_40c;
  float fStack_408;
  float fStack_404;
  float local_400;
  float fStack_3fc;
  float fStack_3f8;
  float fStack_3f4;
  float local_3f0;
  float fStack_3ec;
  float fStack_3e8;
  float fStack_3e4;
  float local_3e0;
  float fStack_3dc;
  float fStack_3d8;
  float fStack_3d4;
  float local_3d0;
  float fStack_3cc;
  float fStack_3c8;
  float fStack_3c4;
  float local_3c0;
  float fStack_3bc;
  float fStack_3b8;
  float fStack_3b4;
  float local_3b0;
  float fStack_3ac;
  float fStack_3a8;
  float fStack_3a4;
  float local_3a0;
  float fStack_39c;
  float fStack_398;
  float fStack_394;
  float local_390;
  float fStack_38c;
  float fStack_388;
  float fStack_384;
  float local_380;
  float fStack_37c;
  float fStack_378;
  float fStack_374;
  float local_370;
  float fStack_36c;
  float fStack_368;
  float fStack_364;
  float local_360;
  float fStack_35c;
  float fStack_358;
  float fStack_354;
  float local_350;
  float fStack_34c;
  float fStack_348;
  float fStack_344;
  float local_340;
  float fStack_33c;
  float fStack_338;
  float fStack_334;
  float local_330;
  float fStack_32c;
  float fStack_328;
  float fStack_324;
  float local_320;
  float fStack_31c;
  float fStack_318;
  float fStack_314;
  float local_310;
  float fStack_30c;
  float fStack_308;
  float fStack_304;
  float local_300;
  float fStack_2fc;
  float fStack_2f8;
  float fStack_2f4;
  float local_2f0;
  float fStack_2ec;
  float fStack_2e8;
  float fStack_2e4;
  float local_2e0;
  float fStack_2dc;
  float fStack_2d8;
  float fStack_2d4;
  float local_2d0;
  float fStack_2cc;
  float fStack_2c8;
  float fStack_2c4;
  undefined1 local_2c0 [16];
  undefined1 local_2b0 [16];
  undefined1 local_2a0 [16];
  undefined1 local_290 [16];
  undefined1 local_280 [16];
  undefined1 local_270 [16];
  undefined1 local_260 [16];
  undefined1 local_250 [16];
  undefined1 local_240 [16];
  undefined1 local_230 [16];
  undefined1 local_220 [16];
  undefined1 local_210 [16];
  undefined1 local_200 [16];
  undefined1 local_1f0 [16];
  undefined1 local_1e0 [16];
  undefined1 local_1d0 [16];
  undefined1 local_1c0 [16];
  undefined1 local_1b0 [16];
  undefined1 local_1a0 [16];
  undefined1 local_190 [16];
  undefined1 local_180 [16];
  undefined1 local_170 [16];
  undefined1 local_160 [16];
  undefined1 local_150 [16];
  undefined1 local_140 [16];
  undefined1 local_130 [16];
  undefined4 local_120 [16];
  undefined1 local_e0 [64];
  uint local_a0 [4];
  uint local_90;
  uint local_8c;
  uint local_88;
  uint local_84;
  uint local_80;
  uint local_7c;
  uint local_78;
  uint local_74;
  undefined4 local_70;
  undefined4 local_6c;
  undefined4 local_68;
  undefined4 local_64;
  uint local_60 [19];
  uint local_14;
  
  local_14 = DAT_007360c8 ^ (uint)auStack_508;
  iVar6 = 0x10;
  fVar10 = (float10)fptan((float10)DAT_007388ac * (float10)DAT_006da974);
  fVar20 = DAT_007388b8 / (DAT_007388b4 - DAT_007388b8);
  local_504 = (float)((float10)1 / fVar10);
  fVar41 = fVar20 * DAT_007388b4;
  fVar23 = local_504 / ((float)DAT_007c3920 / (float)DAT_007c3924);
  auVar43._0_4_ = DAT_00738870 - DAT_00738880;
  auVar43._4_4_ = DAT_00738874 - DAT_00738884;
  auVar43._8_4_ = DAT_00738878 - DAT_00738888;
  auVar43._12_4_ = DAT_0073887c - DAT_0073888c;
  local_460 = (uint)fVar23 & _DAT_008b34a0;
  uStack_45c = (uint)local_504 & uRam008b34a4;
  uStack_458 = (uint)fVar20 & uRam008b34a8;
  uStack_454 = (uint)fVar41 & uRam008b34ac;
  local_450 = (uint)fVar23 & _DAT_008b34b0;
  uStack_44c = (uint)local_504 & uRam008b34b4;
  uStack_448 = (uint)fVar20 & uRam008b34b8;
  uStack_444 = (uint)fVar41 & uRam008b34bc;
  local_a0[0] = local_460;
  local_a0[1] = uStack_45c;
  local_a0[2] = uStack_458;
  local_a0[3] = uStack_454;
  local_90 = local_450;
  local_8c = uStack_44c;
  local_88 = uStack_448;
  local_84 = uStack_444;
  local_4e0._4_4_ = (uint)local_504 & uRam008b34c4;
  local_4e0._0_4_ = (uint)fVar23 & _DAT_008b34c0;
  local_4e0._8_4_ = (uint)fVar20 & uRam008b34c8;
  local_4e0._12_4_ = (uint)fVar41 & uRam008b34cc;
  local_80 = (uint)fVar23 & _DAT_008b34c0;
  local_7c = (uint)local_504 & uRam008b34c4;
  local_78 = (uint)fVar20 & uRam008b34c8;
  local_74 = (uint)fVar41 & uRam008b34cc;
  local_70 = DAT_008b34d0;
  local_6c = DAT_008b34d4;
  local_68 = DAT_008b34d8;
  local_64 = DAT_008b34dc;
  fVar20 = auVar43._0_4_ * auVar43._0_4_;
  fVar23 = auVar43._4_4_ * auVar43._4_4_;
  fVar41 = auVar43._8_4_ * auVar43._8_4_;
  fVar21 = auVar43._12_4_ * auVar43._12_4_;
  puVar7 = local_a0;
  puVar8 = local_60;
  for (; iVar6 != 0; iVar6 = iVar6 + -1) {
    *puVar8 = *puVar7;
    puVar7 = puVar7 + 1;
    puVar8 = puVar8 + 1;
  }
  local_410 = fVar20;
  fStack_40c = fVar23;
  fStack_408 = fVar41;
  fStack_404 = fVar21;
  pfVar4 = (float *)FUN_004356f0(local_2c0);
  fVar20 = *pfVar4 + fVar20;
  fVar23 = pfVar4[1] + fVar23;
  fVar41 = pfVar4[2] + fVar41;
  fVar21 = pfVar4[3] + fVar21;
  local_400 = fVar20;
  fStack_3fc = fVar23;
  fStack_3f8 = fVar41;
  fStack_3f4 = fVar21;
  pfVar4 = (float *)FUN_00435710(local_2b0);
  auVar11._0_4_ = *pfVar4 + fVar20;
  auVar11._4_4_ = pfVar4[1] + fVar23;
  auVar11._8_4_ = pfVar4[2] + fVar41;
  auVar11._12_4_ = pfVar4[3] + fVar21;
  auVar12 = sqrtps(auVar11,auVar11);
  auVar43 = divps(auVar43,auVar12);
  auVar12._4_4_ = DAT_00738894;
  auVar12._0_4_ = DAT_00738890;
  auVar12._8_4_ = DAT_00738898;
  auVar12._12_4_ = _DAT_0073889c;
  fVar42 = (float)(auVar43._0_4_ ^ _DAT_008b2370);
  fVar44 = (float)(auVar43._4_4_ ^ uRam008b2374);
  fVar45 = (float)(auVar43._8_4_ ^ uRam008b2378);
  fVar46 = (float)(auVar43._12_4_ ^ uRam008b237c);
  fVar33 = fVar44 * DAT_00738890 - DAT_00738894 * fVar42;
  fVar35 = fVar45 * DAT_00738894 - DAT_00738898 * fVar44;
  fVar37 = fVar42 * DAT_00738898 - DAT_00738890 * fVar45;
  auVar34._12_4_ = fVar46 * _DAT_0073889c - _DAT_0073889c * fVar46;
  auVar34._4_4_ = fVar37;
  auVar34._0_4_ = fVar35;
  auVar34._8_4_ = fVar33;
  fVar35 = fVar35 * fVar35;
  fVar37 = fVar37 * fVar37;
  fVar33 = fVar33 * fVar33;
  fVar22 = auVar34._12_4_ * auVar34._12_4_;
  fVar20 = fVar42;
  fVar23 = fVar44;
  fVar41 = fVar45;
  fVar21 = fVar46;
  local_430 = fVar42;
  fStack_42c = fVar44;
  fStack_428 = fVar45;
  fStack_424 = fVar46;
  local_3f0 = fVar35;
  fStack_3ec = fVar37;
  fStack_3e8 = fVar33;
  fStack_3e4 = fVar22;
  pfVar4 = (float *)FUN_004356f0(local_2a0);
  fVar35 = *pfVar4 + fVar35;
  fVar37 = pfVar4[1] + fVar37;
  fVar33 = pfVar4[2] + fVar33;
  fVar22 = pfVar4[3] + fVar22;
  local_3e0 = fVar35;
  fStack_3dc = fVar37;
  fStack_3d8 = fVar33;
  fStack_3d4 = fVar22;
  pfVar4 = (float *)FUN_00435710(local_290);
  auVar24._0_4_ = fVar35 + *pfVar4;
  auVar24._4_4_ = fVar37 + pfVar4[1];
  auVar24._8_4_ = fVar33 + pfVar4[2];
  auVar24._12_4_ = fVar22 + pfVar4[3];
  local_4c0 = DAT_00738880;
  fStack_4bc = DAT_00738884;
  auVar43 = sqrtps(auVar12,auVar24);
  fStack_4b8 = DAT_00738888;
  fStack_4b4 = DAT_0073888c;
  local_420 = divps(auVar34,auVar43);
  fVar36 = local_420._0_4_;
  fVar38 = local_420._4_4_;
  fVar40 = local_420._8_4_;
  fVar39 = local_420._12_4_;
  fVar35 = DAT_00738880 * fVar36;
  fVar37 = DAT_00738884 * fVar38;
  fVar33 = DAT_00738888 * fVar40;
  fVar22 = DAT_0073888c * fVar39;
  fStack_4c8 = fVar38 * fVar20 - fVar44 * fVar36;
  local_4d0 = fVar40 * fVar23 - fVar45 * fVar38;
  fStack_4cc = fVar36 * fVar41 - fVar42 * fVar40;
  fStack_4c4 = fVar39 * fVar21 - fVar46 * fVar39;
  local_3d0 = fVar35;
  fStack_3cc = fVar37;
  fStack_3c8 = fVar33;
  fStack_3c4 = fVar22;
  pfVar4 = (float *)FUN_004356f0(local_280);
  fVar35 = fVar35 + *pfVar4;
  fStack_4bc = fVar37 + pfVar4[1];
  fStack_4b8 = fVar33 + pfVar4[2];
  fStack_4b4 = fVar22 + pfVar4[3];
  local_4c0 = fVar35;
  pfVar4 = (float *)FUN_00435710(local_270);
  local_504 = fVar35 + *pfVar4;
  local_4b0 = DAT_00738880;
  fStack_4ac = DAT_00738884;
  fStack_4a8 = DAT_00738888;
  fStack_4a4 = DAT_0073888c;
  fVar20 = local_4d0 * DAT_00738880;
  fVar23 = fStack_4cc * DAT_00738884;
  fVar41 = fStack_4c8 * DAT_00738888;
  fVar21 = fStack_4c4 * DAT_0073888c;
  local_420._12_4_ = -local_504;
  local_3c0 = fVar20;
  fStack_3bc = fVar23;
  fStack_3b8 = fVar41;
  fStack_3b4 = fVar21;
  pfVar4 = (float *)FUN_004356f0(local_260);
  fVar20 = fVar20 + *pfVar4;
  fVar23 = fVar23 + pfVar4[1];
  fVar41 = fVar41 + pfVar4[2];
  fVar21 = fVar21 + pfVar4[3];
  local_4b0 = fVar20;
  fStack_4ac = fVar23;
  fStack_4a8 = fVar41;
  fStack_4a4 = fVar21;
  pfVar4 = (float *)FUN_00435710(local_250);
  auVar13._0_4_ = *pfVar4 + fVar20;
  auVar13._4_4_ = pfVar4[1] + fVar23;
  auVar13._8_4_ = pfVar4[2] + fVar41;
  auVar13._12_4_ = pfVar4[3] + fVar21;
  fStack_4c4 = -auVar13._0_4_;
  local_4a0 = DAT_00738880;
  fStack_49c = DAT_00738884;
  fStack_498 = DAT_00738888;
  fStack_494 = DAT_0073888c;
  fVar20 = DAT_00738880 * local_430;
  fVar23 = DAT_00738884 * fStack_42c;
  fVar41 = DAT_00738888 * fStack_428;
  fVar21 = DAT_0073888c * fStack_424;
  local_504 = auVar13._0_4_;
  local_3b0 = fVar20;
  fStack_3ac = fVar23;
  fStack_3a8 = fVar41;
  fStack_3a4 = fVar21;
  pfVar4 = (float *)FUN_004356f0(local_240);
  fVar20 = fVar20 + *pfVar4;
  fStack_49c = fVar23 + pfVar4[1];
  fStack_498 = fVar41 + pfVar4[2];
  fStack_494 = fVar21 + pfVar4[3];
  local_4a0 = fVar20;
  pfVar4 = (float *)FUN_00435710(local_230);
  local_504 = fVar20 + *pfVar4;
  fStack_424 = -local_504;
  FUN_004358f0(local_420,&local_4d0,&local_430,&DAT_008b2310);
  puVar7 = local_a0;
  puVar8 = &DAT_00738720;
  for (iVar6 = 0x10; iVar6 != 0; iVar6 = iVar6 + -1) {
    *puVar8 = *puVar7;
    puVar7 = puVar7 + 1;
    puVar8 = puVar8 + 1;
  }
  FUN_00444400();
  puVar5 = local_120;
  puVar9 = &DAT_00738760;
  for (iVar6 = 0x10; iVar6 != 0; iVar6 = iVar6 + -1) {
    *puVar9 = *puVar5;
    puVar5 = puVar5 + 1;
    puVar9 = puVar9 + 1;
  }
  puVar5 = (undefined4 *)FUN_00435620(local_e0,&DAT_00738720);
  auVar30._0_4_ = DAT_00738870 - DAT_00738880;
  auVar30._4_4_ = DAT_00738874 - DAT_00738884;
  auVar30._8_4_ = DAT_00738878 - DAT_00738888;
  auVar30._12_4_ = DAT_0073887c - DAT_0073888c;
  puVar9 = &DAT_00764380;
  for (iVar6 = 0x10; iVar6 != 0; iVar6 = iVar6 + -1) {
    *puVar9 = *puVar5;
    puVar5 = puVar5 + 1;
    puVar9 = puVar9 + 1;
  }
  fVar20 = auVar30._0_4_ * auVar30._0_4_;
  fVar23 = auVar30._4_4_ * auVar30._4_4_;
  fVar41 = auVar30._8_4_ * auVar30._8_4_;
  fVar21 = auVar30._12_4_ * auVar30._12_4_;
  local_3a0 = fVar20;
  fStack_39c = fVar23;
  fStack_398 = fVar41;
  fStack_394 = fVar21;
  pfVar4 = (float *)FUN_004356f0(local_220);
  fVar20 = *pfVar4 + fVar20;
  fVar23 = pfVar4[1] + fVar23;
  fVar41 = pfVar4[2] + fVar41;
  fVar21 = pfVar4[3] + fVar21;
  local_390 = fVar20;
  fStack_38c = fVar23;
  fStack_388 = fVar41;
  fStack_384 = fVar21;
  pfVar4 = (float *)FUN_00435710(local_210);
  auVar25._0_4_ = fVar20 + *pfVar4;
  auVar25._4_4_ = fVar23 + pfVar4[1];
  auVar25._8_4_ = fVar41 + pfVar4[2];
  auVar25._12_4_ = fVar21 + pfVar4[3];
  local_484 = DAT_00738890;
  local_480 = DAT_00738894;
  auVar43 = sqrtps(auVar13,auVar25);
  local_47c = DAT_00738898;
  _local_500 = divps(auVar30,auVar43);
  local_478 = local_500._0_4_;
  local_474 = local_500._4_4_;
  local_470 = fStack_4f8;
  local_46c = DAT_00738880;
  local_468 = DAT_00738884;
  local_464 = DAT_00738888;
  FUN_00593750(&local_46c,&local_478,&local_484);
  fVar46 = _DAT_006db510 * DAT_00738860;
  fVar36 = _UNK_006db514 * DAT_00738864;
  fVar38 = _UNK_006db518 * DAT_00738868;
  fVar40 = _UNK_006db51c * DAT_0073886c;
  auVar14._0_4_ = _UNK_006dafe4 * fVar46;
  auVar14._4_4_ = _UNK_006dafe8 * fVar36;
  auVar14._8_4_ = _DAT_006dafe0 * fVar38;
  auVar14._12_4_ = _UNK_006dafec * fVar40;
  fVar33 = fVar36 * _DAT_006dafe0 - auVar14._0_4_;
  fVar20 = fVar38 * _UNK_006dafe4 - auVar14._4_4_;
  fVar23 = fVar46 * _UNK_006dafe8 - auVar14._8_4_;
  auVar31._12_4_ = fVar40 * _UNK_006dafec - auVar14._12_4_;
  auVar31._4_4_ = fVar23;
  auVar31._0_4_ = fVar20;
  auVar31._8_4_ = fVar33;
  fVar20 = fVar20 * fVar20;
  fVar23 = fVar23 * fVar23;
  fVar33 = fVar33 * fVar33;
  fVar22 = auVar31._12_4_ * auVar31._12_4_;
  fVar41 = fVar36;
  fVar21 = fVar38;
  fVar35 = fVar46;
  fVar37 = fVar40;
  local_440 = fVar46;
  fStack_43c = fVar36;
  fStack_438 = fVar38;
  fStack_434 = fVar40;
  local_380 = fVar20;
  fStack_37c = fVar23;
  fStack_378 = fVar33;
  fStack_374 = fVar22;
  pfVar4 = (float *)FUN_004356f0(local_200);
  fVar20 = *pfVar4 + fVar20;
  fVar23 = pfVar4[1] + fVar23;
  fVar33 = pfVar4[2] + fVar33;
  fVar22 = pfVar4[3] + fVar22;
  local_370 = fVar20;
  fStack_36c = fVar23;
  fStack_368 = fVar33;
  fStack_364 = fVar22;
  pfVar4 = (float *)FUN_00435710(local_1f0);
  auVar26._0_4_ = fVar20 + *pfVar4;
  auVar26._4_4_ = fVar23 + pfVar4[1];
  auVar26._8_4_ = fVar33 + pfVar4[2];
  auVar26._12_4_ = fVar22 + pfVar4[3];
  auVar43 = sqrtps(auVar14,auVar26);
  auVar43 = divps(auVar31,auVar43);
  auVar15._0_4_ = auVar43._0_4_ * fVar41;
  auVar15._4_4_ = auVar43._4_4_ * fVar21;
  auVar15._8_4_ = auVar43._8_4_ * fVar35;
  auVar15._12_4_ = auVar43._12_4_ * fVar37;
  fVar33 = auVar43._4_4_ * fVar46 - auVar15._0_4_;
  fVar20 = auVar43._8_4_ * fVar36 - auVar15._4_4_;
  fVar23 = auVar43._0_4_ * fVar38 - auVar15._8_4_;
  auVar27._12_4_ = auVar43._12_4_ * fVar40 - auVar15._12_4_;
  auVar27._4_4_ = fVar23;
  auVar27._0_4_ = fVar20;
  auVar27._8_4_ = fVar33;
  fVar20 = fVar20 * fVar20;
  fVar23 = fVar23 * fVar23;
  fVar33 = fVar33 * fVar33;
  fVar22 = auVar27._12_4_ * auVar27._12_4_;
  _local_4f0 = auVar43;
  local_360 = fVar20;
  fStack_35c = fVar23;
  fStack_358 = fVar33;
  fStack_354 = fVar22;
  pfVar4 = (float *)FUN_004356f0(local_1e0);
  fVar20 = fVar20 + *pfVar4;
  fVar23 = fVar23 + pfVar4[1];
  fVar33 = fVar33 + pfVar4[2];
  fVar22 = fVar22 + pfVar4[3];
  local_350 = fVar20;
  fStack_34c = fVar23;
  fStack_348 = fVar33;
  fStack_344 = fVar22;
  pfVar4 = (float *)FUN_00435710(local_1d0);
  DAT_007387a0 = auVar43._0_4_;
  fVar44 = auVar43._4_4_ - fVar36;
  fVar45 = auVar43._8_4_ - fVar38;
  fVar42 = auVar43._12_4_ - fVar40;
  DAT_007387b8 = fStack_43c;
  auVar1._4_4_ = fVar23 + pfVar4[1];
  auVar1._0_4_ = fVar20 + *pfVar4;
  auVar1._8_4_ = fVar33 + pfVar4[2];
  auVar1._12_4_ = fVar22 + pfVar4[3];
  auVar43 = sqrtps(auVar15,auVar1);
  fVar33 = (DAT_007387a0 - fVar46) * (DAT_007387a0 - fVar46);
  fVar44 = fVar44 * fVar44;
  fVar45 = fVar45 * fVar45;
  fVar42 = fVar42 * fVar42;
  _local_500 = divps(auVar27,auVar43);
  DAT_007387b0 = local_4f0._4_4_;
  DAT_007387c0 = fStack_4e8;
  DAT_007387b4 = local_500._4_4_;
  DAT_007387a4 = local_500._0_4_;
  DAT_007387c4 = fStack_4f8;
  DAT_007387c8 = fStack_438;
  fVar20 = fStack_43c;
  fVar23 = fStack_438;
  DAT_007387a8 = fVar46;
  local_440 = fVar33;
  fStack_43c = fVar44;
  fStack_438 = fVar45;
  fStack_434 = fVar42;
  pfVar4 = (float *)FUN_004356f0(local_1c0);
  fVar33 = fVar33 + *pfVar4;
  local_500._4_4_ = fVar44 + pfVar4[1];
  local_500._0_4_ = fVar33;
  fStack_4f8 = fVar45 + pfVar4[2];
  fStack_4f4 = fVar42 + pfVar4[3];
  pfVar4 = (float *)FUN_00435710(local_1b0);
  local_4f0._4_4_ = _UNK_006db254;
  local_4f0._0_4_ = _DAT_006db250;
  fStack_4e8 = _UNK_006db258;
  fStack_4e4 = _UNK_006db25c;
  auVar16._0_4_ = _DAT_006db250 * fVar41;
  auVar16._4_4_ = _UNK_006db254 * fVar21;
  auVar16._8_4_ = _UNK_006db258 * fVar35;
  auVar16._12_4_ = _UNK_006db25c * fVar37;
  local_504 = fVar33 + *pfVar4;
  fVar45 = _UNK_006db254 * fVar46 - auVar16._0_4_;
  fVar22 = _UNK_006db258 * fVar36 - auVar16._4_4_;
  fVar44 = _DAT_006db250 * fVar38 - auVar16._8_4_;
  auVar32._12_4_ = _UNK_006db25c * fVar40 - auVar16._12_4_;
  auVar32._4_4_ = fVar44;
  auVar32._0_4_ = fVar22;
  auVar32._8_4_ = fVar45;
  fVar22 = fVar22 * fVar22;
  fVar44 = fVar44 * fVar44;
  fVar45 = fVar45 * fVar45;
  fVar42 = auVar32._12_4_ * auVar32._12_4_;
  fVar33 = _DAT_006db250;
  if (_DAT_006da840 <= local_504) {
    local_320 = fVar22;
    fStack_31c = fVar44;
    fStack_318 = fVar45;
    fStack_314 = fVar42;
    pfVar4 = (float *)FUN_004356f0(local_180);
    fVar22 = fVar22 + *pfVar4;
    fVar44 = fVar44 + pfVar4[1];
    fVar45 = fVar45 + pfVar4[2];
    fVar42 = fVar42 + pfVar4[3];
    local_310 = fVar22;
    fStack_30c = fVar44;
    fStack_308 = fVar45;
    fStack_304 = fVar42;
    pfVar4 = (float *)FUN_00435710(local_170);
    auVar17._0_4_ = *pfVar4 + fVar22;
    auVar17._4_4_ = pfVar4[1] + fVar44;
    auVar17._8_4_ = pfVar4[2] + fVar45;
    auVar17._12_4_ = pfVar4[3] + fVar42;
    auVar43 = sqrtps(auVar17,auVar17);
  }
  else {
    local_340 = fVar22;
    fStack_33c = fVar44;
    fStack_338 = fVar45;
    fStack_334 = fVar42;
    pfVar4 = (float *)FUN_004356f0(local_1a0);
    fVar22 = fVar22 + *pfVar4;
    fVar44 = fVar44 + pfVar4[1];
    fVar45 = fVar45 + pfVar4[2];
    fVar42 = fVar42 + pfVar4[3];
    local_330 = fVar22;
    fStack_32c = fVar44;
    fStack_328 = fVar45;
    fStack_324 = fVar42;
    pfVar4 = (float *)FUN_00435710(local_190);
    auVar2._4_4_ = fVar44 + pfVar4[1];
    auVar2._0_4_ = fVar22 + *pfVar4;
    auVar2._8_4_ = fVar45 + pfVar4[2];
    auVar2._12_4_ = fVar42 + pfVar4[3];
    auVar43 = sqrtps(auVar16,auVar2);
  }
  auVar43 = divps(auVar32,auVar43);
  DAT_007387f0 = local_4f0._4_4_;
  DAT_00738800 = fStack_4e8;
  local_500._4_4_ = auVar43._4_4_;
  DAT_007387f4 = local_500._4_4_;
  fStack_4f8 = auVar43._8_4_;
  DAT_00738804 = fStack_4f8;
  DAT_007387e4 = auVar43._0_4_;
  auVar18._0_4_ = _UNK_006db294 * fVar46;
  auVar18._4_4_ = _UNK_006db298 * fVar36;
  auVar18._8_4_ = _DAT_006db290 * fVar38;
  auVar18._12_4_ = _UNK_006db29c * fVar40;
  fVar22 = _DAT_006db290 * fVar41 - auVar18._0_4_;
  fVar21 = _UNK_006db294 * fVar21 - auVar18._4_4_;
  fVar35 = _UNK_006db298 * fVar35 - auVar18._8_4_;
  auVar28._12_4_ = _UNK_006db29c * fVar37 - auVar18._12_4_;
  local_500._4_4_ = _UNK_006db294;
  local_500._0_4_ = _DAT_006db290;
  fStack_4f8 = _UNK_006db298;
  fStack_4f4 = _UNK_006db29c;
  auVar28._4_4_ = fVar35;
  auVar28._0_4_ = fVar21;
  auVar28._8_4_ = fVar22;
  fVar21 = fVar21 * fVar21;
  fVar35 = fVar35 * fVar35;
  fVar22 = fVar22 * fVar22;
  fVar37 = auVar28._12_4_ * auVar28._12_4_;
  fVar41 = _DAT_006db290;
  DAT_007387e0 = fVar33;
  DAT_007387e8 = fVar46;
  DAT_007387f8 = fVar20;
  DAT_00738808 = fVar23;
  local_300 = fVar21;
  fStack_2fc = fVar35;
  fStack_2f8 = fVar22;
  fStack_2f4 = fVar37;
  pfVar4 = (float *)FUN_004356f0(local_160);
  fVar21 = fVar21 + *pfVar4;
  fVar35 = fVar35 + pfVar4[1];
  fVar22 = fVar22 + pfVar4[2];
  fVar37 = fVar37 + pfVar4[3];
  local_2f0 = fVar21;
  fStack_2ec = fVar35;
  fStack_2e8 = fVar22;
  fStack_2e4 = fVar37;
  pfVar4 = (float *)FUN_00435710(local_150);
  auVar3._4_4_ = fVar35 + pfVar4[1];
  auVar3._0_4_ = fVar21 + *pfVar4;
  auVar3._8_4_ = fVar22 + pfVar4[2];
  auVar3._12_4_ = fVar37 + pfVar4[3];
  auVar43 = sqrtps(auVar18,auVar3);
  _local_4f0 = divps(auVar28,auVar43);
  DAT_00738820 = local_4f0._0_4_;
  auVar29._0_4_ = DAT_00738870 - DAT_00738880;
  auVar29._4_4_ = DAT_00738874 - DAT_00738884;
  auVar29._8_4_ = DAT_00738878 - DAT_00738888;
  auVar29._12_4_ = DAT_0073887c - DAT_0073888c;
  DAT_00738830 = local_4f0._4_4_;
  DAT_00738840 = fStack_4e8;
  DAT_00738834 = local_500._4_4_;
  fVar21 = auVar29._0_4_ * auVar29._0_4_;
  fVar35 = auVar29._4_4_ * auVar29._4_4_;
  fVar37 = auVar29._8_4_ * auVar29._8_4_;
  fVar33 = auVar29._12_4_ * auVar29._12_4_;
  DAT_00738844 = fStack_4f8;
  DAT_00738824 = fVar41;
  DAT_00738828 = fVar46;
  DAT_00738838 = fVar20;
  DAT_00738848 = fVar23;
  local_2e0 = fVar21;
  fStack_2dc = fVar35;
  fStack_2d8 = fVar37;
  fStack_2d4 = fVar33;
  pfVar4 = (float *)FUN_004356f0(local_140);
  fVar21 = fVar21 + *pfVar4;
  fVar35 = fVar35 + pfVar4[1];
  fVar37 = fVar37 + pfVar4[2];
  fVar33 = fVar33 + pfVar4[3];
  local_2d0 = fVar21;
  fStack_2cc = fVar35;
  fStack_2c8 = fVar37;
  fStack_2c4 = fVar33;
  pfVar4 = (float *)FUN_00435710(local_130);
  auVar19._0_4_ = *pfVar4 + fVar21;
  auVar19._4_4_ = pfVar4[1] + fVar35;
  auVar19._8_4_ = pfVar4[2] + fVar37;
  auVar19._12_4_ = pfVar4[3] + fVar33;
  auVar43 = sqrtps(auVar19,auVar19);
  local_4e0 = divps(auVar29,auVar43);
  DAT_00738860 = (float)local_4e0._0_4_;
  DAT_00738864 = (float)local_4e0._4_4_;
  DAT_00738868 = (float)local_4e0._8_4_;
  DAT_007388a0 = (float)(local_4e0._0_4_ ^ _DAT_008b2370);
  DAT_007388a4 = local_4e0._4_4_ ^ uRam008b2374;
  DAT_007388a8 = local_4e0._8_4_ ^ uRam008b2378;
  fStack_4c4 = (float)(local_4e0._12_4_ ^ uRam008b237c);
  DAT_0073886c = (float)local_4e0._12_4_;
  local_4d0 = DAT_007388a0;
  fStack_4cc = (float)DAT_007388a4;
  fStack_4c8 = (float)DAT_007388a8;
  __security_check_cookie(local_14 ^ (uint)auStack_508);
  return;
}


```

## `004388f0`

- Function: `FUN_004388f0`
- Entry: `004388f0`

```c

void FUN_004388f0(void)

{
  undefined4 *puVar1;
  undefined4 *puVar2;
  uint uVar3;
  uint uVar4;
  undefined4 *_Memory;
  int iVar5;
  int *piVar6;
  int *piVar7;
  int *piVar8;
  undefined8 uVar9;
  int *local_20;
  undefined4 *local_1c;
  int local_18;
  uint local_14;
  void *local_10;
  undefined1 *puStack_c;
  undefined4 local_8;
  
  local_8 = 0xffffffff;
  puStack_c = &LAB_0065bff8;
  local_10 = ExceptionList;
  uVar3 = DAT_007360c8 ^ (uint)&stack0xfffffffc;
  ExceptionList = &local_10;
  piVar8 = (int *)*DAT_00785230;
  piVar6 = DAT_00785230;
  local_14 = uVar3;
  if (piVar8 != DAT_00785230) {
    do {
      uVar9 = __allmul(DAT_007c3908 - DAT_007c3910,
                       (DAT_007c390c - DAT_007c3914) - (uint)(DAT_007c3908 < DAT_007c3910),1000,0);
      uVar4 = __alldiv(uVar9,DAT_008b3b48,DAT_008b3b4c);
      if ((uint)piVar8[2] < uVar4) {
        FUN_00438760(piVar8[3],0);
        piVar7 = (int *)*piVar8;
        *(int **)piVar8[1] = piVar7;
        *(int *)(*piVar8 + 4) = piVar8[1];
        DAT_00785234 = DAT_00785234 + -1;
        FID_conflict__free(piVar8);
        piVar6 = DAT_00785230;
        if (DAT_00785234 == 0) break;
      }
      else {
        piVar7 = (int *)*piVar8;
      }
      piVar8 = piVar7;
    } while (piVar7 != piVar6);
  }
  piVar8 = (int *)*DAT_00785238;
  local_1c = (undefined4 *)0x0;
  local_18 = 0;
  _Memory = (undefined4 *)FUN_00433c50(0,0);
  local_8 = 2;
  local_1c = _Memory;
  if (piVar8 != DAT_00785238) {
    do {
      local_20 = (int *)piVar8[2];
      if (local_20[1] == 0) {
        piVar6 = (int *)*piVar8;
        *(int **)piVar8[1] = piVar6;
        *(int *)(*piVar8 + 4) = piVar8[1];
        DAT_0078523c = DAT_0078523c + -1;
        FID_conflict__free(piVar8);
        iVar5 = FUN_00434330(_Memory,_Memory[1],&local_20);
        if (local_18 == 0x15555554) {
                    /* WARNING: Subroutine does not return */
          FUN_00627726("list<T> too long");
        }
        local_18 = local_18 + 1;
        _Memory[1] = iVar5;
        **(int **)(iVar5 + 4) = iVar5;
        if (DAT_0078523c == 0) break;
      }
      else {
        (**(code **)(*local_20 + 4))(uVar3);
        piVar6 = (int *)*piVar8;
      }
      piVar8 = piVar6;
    } while (piVar6 != DAT_00785238);
  }
  for (puVar1 = (undefined4 *)*_Memory; puVar1 != _Memory; puVar1 = (undefined4 *)*puVar1) {
    puVar2 = (undefined4 *)puVar1[2];
    if (puVar2 != (undefined4 *)0x0) {
      (**(code **)*puVar2)(0);
      thunk_FUN_00640afb(puVar2);
    }
  }
  puVar1 = (undefined4 *)*_Memory;
  *_Memory = _Memory;
  _Memory[1] = _Memory;
  local_18 = 0;
  while (puVar1 != _Memory) {
    puVar2 = (undefined4 *)*puVar1;
    FID_conflict__free(puVar1);
    puVar1 = puVar2;
  }
  local_8 = 3;
  puVar1 = (undefined4 *)*_Memory;
  *_Memory = _Memory;
  _Memory[1] = _Memory;
  local_18 = 0;
  while (puVar1 != _Memory) {
    puVar2 = (undefined4 *)*puVar1;
    FID_conflict__free(puVar1);
    puVar1 = puVar2;
  }
  local_8 = 0xffffffff;
  FID_conflict__free(_Memory);
  ExceptionList = local_10;
  __security_check_cookie(local_14 ^ (uint)&stack0xfffffffc);
  return;
}


```

## `00445b40`

- Function: `FUN_00445b40`
- Entry: `00445b40`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00445b40(int param_1)

{
  float fVar1;
  float fVar2;
  float fVar3;
  uint *puVar4;
  longlong lVar5;
  undefined4 *puVar6;
  undefined4 *puVar7;
  uint uVar8;
  byte bVar9;
  int *piVar10;
  int extraout_EDX;
  int extraout_EDX_00;
  int iVar11;
  float *pfVar12;
  uint uVar13;
  int iVar14;
  float *pfVar15;
  ushort in_FPUControlWord;
  float fVar16;
  float fVar17;
  undefined8 uVar18;
  undefined1 auStack_68 [12];
  float *local_5c;
  float *local_58;
  undefined4 *local_54;
  int *local_50;
  undefined4 *local_4c;
  undefined4 *local_48;
  float *local_44;
  undefined8 local_40;
  undefined8 local_38;
  float fStack_30;
  float fStack_28;
  undefined8 local_20;
  uint local_14;
  
  local_14 = DAT_007360c8 ^ (uint)auStack_68;
  if (DAT_007b5320 == 0) goto LAB_00446828;
  local_40 = CONCAT44(DAT_007c393c,DAT_007c3938);
  local_20 = CONCAT44(DAT_007c3944,DAT_007c3940);
  if ((param_1 != 0) || (puVar6 = DAT_007c24dc, DAT_007852e9 != '\0')) {
    DAT_007852e9 = '\0';
    SetRect((LPRECT)&DAT_007c24e4,0x80,0x80,0,0);
    if ((*(int **)(DAT_007b5320 + 0x48) == (int *)0x0) || (**(int **)(DAT_007b5320 + 0x48) == 0))
    goto LAB_00446828;
    local_48 = (undefined4 *)(float)DAT_007c3920;
    local_4c = (undefined4 *)(float)DAT_007c3924;
    uVar13 = FUN_0046bbc0(0);
    local_44 = (float *)uVar13;
    local_50 = (int *)FUN_0046bc40(0);
    pfVar12 = DAT_007b53ec;
    _memset(DAT_007b5404,0,(uVar13 + 0x1f >> 5) << 2);
    uVar8 = 0;
    puVar6 = local_4c;
    if (uVar13 != 0) {
      local_54 = (undefined4 *)((int)pfVar12 - (int)local_50);
      local_58 = (float *)(local_50 + 2);
      do {
        fVar16 = local_58[-2];
        fVar1 = local_58[-1];
        fVar2 = *local_58;
        puVar6 = (undefined4 *)(uVar8 >> 5);
        fVar17 = DAT_006daa00 /
                 (DAT_00736d40 * fVar16 + DAT_00736d44 * fVar1 + DAT_00736d48 * fVar2 +
                 _DAT_00736d4c);
        *pfVar12 = ((DAT_00736d10 * fVar16 + DAT_00736d14 * fVar1 + DAT_00736d18 * fVar2 +
                    _DAT_00736d1c) * fVar17 + DAT_006daa00) * (float)(float *)local_20 +
                   (float)local_40;
        pfVar12[1] = local_40._4_4_ -
                     ((DAT_00736d20 * fVar16 + DAT_00736d24 * fVar1 + DAT_00736d28 * fVar2 +
                      _DAT_00736d2c) * fVar17 - DAT_006daa00) * (float)local_20._4_4_;
        fVar3 = *pfVar12;
        *(float *)((int)local_54 + (int)local_58) =
             (DAT_00736d30 * fVar16 + DAT_00736d34 * fVar1 + DAT_00736d38 * fVar2 + _DAT_00736d3c) *
             fVar17;
        if ((((0.0 < fVar3) && (fVar3 < (float)local_48)) && (0.0 < pfVar12[1])) &&
           (pfVar12[1] < (float)local_4c)) {
          *(uint *)((int)DAT_007b5404 + (int)puVar6 * 4) =
               *(uint *)((int)DAT_007b5404 + (int)puVar6 * 4) | 1 << (uVar8 & 0x1f);
        }
        uVar8 = uVar8 + 1;
        local_58 = local_58 + 3;
        pfVar12 = pfVar12 + 3;
      } while (uVar8 < local_44);
    }
    local_4c = puVar6;
    _memset(DAT_007c2490,0,(int)DAT_007c24e0 * (int)DAT_007c24dc);
    _memset(DAT_007c2488,0xff,(int)DAT_007c24e0 * 2 + 2);
    _memset(DAT_007c248c,0xff,(int)DAT_007c24e0 * 2);
    local_4c = (undefined4 *)0x80;
    puVar6 = (undefined4 *)0x0;
    local_58 = (float *)0x80;
    local_54 = (undefined4 *)0x0;
    local_5c = (float *)0x0;
    local_44 = (float *)0x0;
    puVar7 = DAT_007c24dc;
    if (0 < (int)DAT_007c24e0) {
      do {
        local_50 = (int *)0x0;
        local_48 = (undefined4 *)0x0;
        if (-1 < (int)puVar7) {
          do {
            puVar6 = (undefined4 *)(((int)puVar7 + 1) * (int)local_44 + (int)local_48);
            if ((*(uint *)((int)DAT_007b5404 + ((uint)puVar6 >> 5) * 4) & 1 << ((byte)puVar6 & 0x1f)
                ) != 0) {
              if ((int)local_48 < (int)local_4c) {
                local_4c = local_48;
              }
              if ((int)local_54 < (int)local_48) {
                local_54 = local_48;
              }
              if ((int)local_44 < (int)local_58) {
                local_58 = local_44;
              }
              if ((int)local_5c < (int)local_44) {
                local_5c = local_44;
              }
              if (local_50 == (int *)0x0) {
                local_50 = (int *)0x1;
                *(char *)((int)DAT_007c2488 + (int)local_44 * 2) = (char)local_48;
              }
              *(char *)((int)DAT_007c2488 + (int)local_44 * 2 + 1) = (char)local_48;
              if (local_44 != (float *)0x0) {
                if (local_48 != (undefined4 *)0x0) {
                  *(undefined1 *)
                   ((int)DAT_007c2490 + ((int)local_44 + -1) * (int)DAT_007c24dc + -1 +
                   (int)local_48) = 1;
                }
                if (local_48 != DAT_007c24dc) {
                  *(undefined1 *)
                   ((int)(((int)local_44 + -1) * (int)DAT_007c24dc + (int)DAT_007c2490) +
                   (int)local_48) = 1;
                }
              }
              puVar7 = DAT_007c24dc;
              if (local_44 != DAT_007c24e0) {
                if (local_48 != (undefined4 *)0x0) {
                  *(undefined1 *)
                   ((int)DAT_007c2490 + (int)DAT_007c24dc * (int)local_44 + -1 + (int)local_48) = 1;
                }
                puVar7 = DAT_007c24dc;
                if (local_48 != DAT_007c24dc) {
                  *(undefined1 *)
                   ((int)((int)DAT_007c24dc * (int)local_44 + (int)DAT_007c2490) + (int)local_48) =
                       1;
                  puVar7 = DAT_007c24dc;
                }
              }
            }
            local_48 = (undefined4 *)((int)local_48 + 1);
            puVar6 = local_54;
          } while ((int)local_48 <= (int)puVar7);
        }
        local_44 = (float *)((int)local_44 + 1);
      } while ((int)local_44 < (int)DAT_007c24e0);
    }
    pfVar12 = local_5c;
    SetRect((LPRECT)&DAT_007c24e4,-1,-1,-1,-1);
    if ((int)local_4c <= (int)puVar6) {
      if ((int)local_4c < 1) {
        DAT_007c24e4 = 0;
      }
      else {
        DAT_007c24e4 = (int)local_4c + -1;
      }
      DAT_007c24ec = local_54;
      if ((int)DAT_007c24dc <= (int)local_54) {
        DAT_007c24ec = (undefined4 *)((int)DAT_007c24dc + -1);
      }
    }
    if ((int)local_58 <= (int)pfVar12) {
      if ((int)local_58 < 1) {
        DAT_007c24e8 = 0;
      }
      else {
        DAT_007c24e8 = (int)local_58 + -1;
      }
      DAT_007c24f0 = pfVar12;
      if ((int)DAT_007c24e0 <= (int)pfVar12) {
        DAT_007c24f0 = (float *)((int)DAT_007c24e0 + -1);
      }
    }
    uVar13 = 0;
    if (DAT_007b5398 != 0) {
      do {
        (&DAT_007b53c4)[uVar13] = 0;
        uVar13 = uVar13 + 1;
      } while (uVar13 < DAT_007b5398);
    }
    local_54 = (undefined4 *)0x0;
    iVar14 = DAT_007b5344;
    puVar6 = DAT_007c24dc;
    if (0 < (int)DAT_007c24e0) {
      do {
        local_50 = (int *)0x0;
        local_5c = (float *)0x0;
        if (0 < (int)puVar6) {
          do {
            pfVar12 = (float *)((int)puVar6 * (int)local_54 + (int)local_5c);
            if ((*(char *)((int)DAT_007c2490 + (int)pfVar12) != '\0') &&
               (((uVar13 = *(uint *)(iVar14 + (int)pfVar12 * 4), (~(uVar13 >> 7) & 1) != 0 ||
                 ((~(uVar13 >> 0xf) & 1) != 0)) ||
                (((~(uVar13 >> 0x17) & 1) != 0 || ((~(uVar13 >> 0x1f) & 1) != 0)))))) {
              if (local_50 == (int *)0x0) {
                local_50 = (int *)0x1;
                *(char *)((int)DAT_007c248c + (int)local_54 * 2) = (char)local_5c;
              }
              uVar13 = 0;
              *(char *)((int)DAT_007c248c + (int)local_54 * 2 + 1) = (char)local_5c;
              local_58 = (float *)0x3;
              iVar14 = DAT_007b5344;
              do {
                if ((_DAT_007b532c & 1 << ((byte)local_58 & 0x1f)) != 0) {
                  local_48 = (undefined4 *)(3 - uVar13);
                  bVar9 = (char)local_48 * '\b';
                  local_4c = *(undefined4 **)(DAT_007b5344 + (int)pfVar12 * 4);
                  uVar8 = (0x3f << (bVar9 & 0x1f) & (uint)local_4c) >> (bVar9 & 0x1f) & 0xff;
                  iVar14 = DAT_007b5344;
                  if (((&DAT_007b539c)[uVar8] != 0) &&
                     ((0x80 << (bVar9 & 0x1f) & (uint)local_4c) == 0)) {
                    *(float **)((&DAT_007b539c)[uVar8] + (&DAT_007b53c4)[uVar8] * 4) = pfVar12;
                    (&DAT_007b53c4)[uVar8] = (&DAT_007b53c4)[uVar8] + 1;
                    iVar14 = DAT_007b5344;
                    puVar6 = DAT_007c24dc;
                    if ((0x40 << ((char)local_48 * '\b' & 0x1fU) &
                        *(uint *)(DAT_007b5344 + (int)pfVar12 * 4)) != 0) break;
                  }
                }
                local_58 = (float *)((int)local_58 + -1);
                uVar13 = uVar13 + 1;
                puVar6 = DAT_007c24dc;
              } while (uVar13 < 4);
            }
            local_5c = (float *)((int)local_5c + 1);
          } while ((int)local_5c < (int)puVar6);
        }
        local_54 = (undefined4 *)((int)local_54 + 1);
      } while ((int)local_54 < (int)DAT_007c24e0);
    }
  }
  if (((DAT_007c5eca != '\0') && (DAT_007852e4 != 0)) && (uVar13 = 0, DAT_007852e0 != 0)) {
    do {
      FUN_0044f340();
      uVar13 = uVar13 + 1;
      puVar6 = DAT_007c24dc;
    } while (uVar13 < DAT_007852e0);
  }
  fVar16 = DAT_006dae60;
  local_58 = (float *)0x0;
  puVar7 = DAT_007c24dc;
  pfVar12 = DAT_007c24e0;
  if (-1 < (int)DAT_007c24e0) {
    do {
      iVar14 = 0;
      if (-1 < (int)puVar7) {
        do {
          iVar11 = ((int)puVar7 + 1) * (int)local_58 + iVar14;
          uVar13 = (uint)*(byte *)(iVar11 + DAT_007b53f8);
          local_54 = (undefined4 *)(uint)*(byte *)(iVar11 + DAT_007b53fc);
          if ((undefined4 *)uVar13 != local_54) {
            uVar8 = (int)(DAT_007c3900 * fVar16) & 0xff;
            if (local_54 < uVar13) {
              uVar13 = uVar13 - uVar8;
              if ((int)uVar13 < (int)local_54) {
                uVar13 = (uint)local_54;
              }
              bVar9 = (byte)uVar13;
            }
            else {
              uVar13 = uVar13 + uVar8;
              bVar9 = (byte)uVar13;
              if (local_54 < uVar13) {
                bVar9 = *(byte *)(iVar11 + DAT_007b53fc);
              }
            }
            *(byte *)(iVar11 + DAT_007b53f8) = bVar9;
          }
          iVar14 = iVar14 + 1;
          puVar7 = DAT_007c24dc;
          pfVar12 = DAT_007c24e0;
        } while (iVar14 <= (int)DAT_007c24dc);
      }
      local_58 = (float *)((int)local_58 + 1);
      puVar6 = DAT_007c24dc;
    } while ((int)local_58 <= (int)pfVar12);
  }
  if (DAT_007c4e60 != (undefined4 *)0x0) {
    pfVar12 = (float *)*DAT_007c4e60;
    local_48 = (undefined4 *)DAT_007c4e60[1];
    local_44 = pfVar12;
    if (((puVar6 == (undefined4 *)0x0) || (DAT_007c24e0 == (float *)0x0)) ||
       ((pfVar12 == (float *)0x0 || (local_48 == (undefined4 *)0x0)))) goto LAB_00446828;
    local_58 = (float *)((float)(int)puVar6 / (float)(int)pfVar12);
    local_4c = (undefined4 *)((float)(int)DAT_007c24e0 / (float)(int)local_48);
    if ((DAT_007c4e60 == (undefined4 *)0x0) ||
       (iVar14 = (**(code **)(*(int *)DAT_007c4e60[0x110] + 0x4c))
                           ((int *)DAT_007c4e60[0x110],0,&local_20,0,0x800), puVar6 = local_4c,
       pfVar15 = local_58, iVar14 != 0)) goto LAB_00446828;
    iVar14 = (int)(float *)local_20;
    lVar5 = local_20;
    if (DAT_007c4e60[0x108] == 5) {
      local_54 = (undefined4 *)0x0;
      if (0 < (int)local_48) {
        local_40 = CONCAT44(local_40._4_4_,(float *)local_20);
        do {
          fVar16 = (float)(int)local_54;
          local_38 = CONCAT44(local_38._4_4_,(uint)in_FPUControlWord) | 0xc00;
          local_20._0_4_ = (float *)(longlong)ROUND(fVar16 * (float)local_4c);
          local_58 = (float *)local_20;
          local_5c = (float *)0x0;
          piVar10 = local_20._4_4_;
          if (0 < (int)pfVar12) {
            do {
              fVar1 = (float)(int)local_5c;
              local_5c = (float *)((int)local_5c + 1);
              local_38 = (ulonglong)ROUND(fVar1 * (float)pfVar15);
              *(ushort *)piVar10 =
                   (-(ushort)*(byte *)(((int)DAT_007c24dc + 1) * (int)(float *)local_20 +
                                       (int)local_38 + DAT_007b53fc) - 1 & 0xfff0) << 8;
              pfVar12 = local_44;
              piVar10 = (int *)((int)piVar10 + 2);
            } while ((int)local_5c < (int)local_44);
          }
          local_20._4_4_ = (int *)((int)local_20._4_4_ + iVar14);
          local_54 = (undefined4 *)((int)local_54 + 1);
          local_50 = local_20._4_4_;
          lVar5 = (longlong)ROUND(fVar16 * (float)local_4c);
        } while ((int)local_54 < (int)local_48);
      }
    }
    else if ((DAT_007c4e60[0x108] == 8) && (local_54 = (undefined4 *)0x0, 0 < (int)local_48)) {
      local_38 = CONCAT44(local_38._4_4_,(float *)local_20);
      do {
        fVar16 = (float)(int)local_54;
        local_20._0_4_ = (float *)(longlong)ROUND(fVar16 * (float)puVar6);
        local_4c = (float *)local_20;
        local_5c = (float *)0x0;
        piVar10 = local_20._4_4_;
        if (0 < (int)pfVar12) {
          do {
            fVar1 = (float)(int)local_5c;
            local_5c = (float *)((int)local_5c + 1);
            local_40 = (longlong)ROUND(fVar1 * (float)pfVar15);
            *piVar10 = (-1 - (uint)*(byte *)(((int)DAT_007c24dc + 1) * (int)(float *)local_20 +
                                             (int)(float)local_40 + DAT_007b53fc)) * 0x1000000;
            pfVar12 = local_44;
            piVar10 = piVar10 + 1;
          } while ((int)local_5c < (int)local_44);
        }
        local_58 = (float *)(in_FPUControlWord | 0xc00);
        local_20._4_4_ = (int *)((int)local_20._4_4_ + iVar14);
        local_54 = (undefined4 *)((int)local_54 + 1);
        local_50 = local_20._4_4_;
        lVar5 = (longlong)ROUND(fVar16 * (float)puVar6);
      } while ((int)local_54 < (int)local_48);
    }
    local_20 = lVar5;
    if (DAT_007c4e60 != (undefined4 *)0x0) {
      (**(code **)(*(int *)DAT_007c4e60[0x110] + 0x50))((int *)DAT_007c4e60[0x110],0);
    }
  }
  FUN_00449520();
  local_58 = DAT_007c24a4;
  pfVar12 = (float *)*DAT_007c24a4;
  pfVar15 = DAT_007c24a4;
  fVar16 = DAT_006da944;
  local_44 = pfVar12;
  if (pfVar12 != DAT_007c24a4) {
    do {
      local_38 = CONCAT44(local_38._4_4_,pfVar12[2]);
      local_48 = *(undefined4 **)((int)pfVar12[2] + 0x30);
      local_4c = (undefined4 *)local_48[0x25];
      if (local_4c != (undefined4 *)0x0) {
        local_44 = pfVar12;
        uVar18 = FUN_00456ae0();
        iVar14 = (int)((ulonglong)uVar18 >> 0x20);
        local_50 = (int *)uVar18;
        fStack_30 = *(float *)(iVar14 + 0x10);
        fStack_28 = *(float *)(iVar14 + 0x18);
        iVar11 = (int)(fStack_30 * fVar16);
        iVar14 = (int)(fStack_28 * fVar16);
        if ((((iVar11 < (int)DAT_007c24dc) && (iVar14 < (int)DAT_007c24e0)) && (-1 < iVar11)) &&
           (((-1 < iVar14 && (DAT_007c24e4 + -3 <= iVar11)) &&
            ((iVar11 <= (int)DAT_007c24ec + 3 &&
             ((DAT_007c24e8 + -3 <= iVar14 && (iVar14 <= (int)DAT_007c24f0 + 3)))))))) {
          if ((((((int)DAT_007c24dc <= iVar11) || ((int)DAT_007c24e0 <= iVar14)) || (iVar11 < 0)) ||
              ((iVar14 < 0 ||
               (*(char *)(iVar14 * (int)DAT_007c24dc + iVar11 + (int)DAT_007c2490) == '\0')))) ||
             (iVar14 = FUN_00456920(), fVar16 = DAT_006da944, iVar14 != 0)) {
            local_20 = CONCAT44((DAT_007c390c - DAT_007c3914) - (uint)(DAT_007c3908 < DAT_007c3910),
                                DAT_007c3908 - DAT_007c3910);
            local_5c = (float *)CONCAT22(local_5c._2_2_,in_FPUControlWord);
            local_40 = (longlong)ROUND((float)local_20 * _DAT_007641f4 * _DAT_006dad48);
            if (local_50 != (int *)0x0) {
              piVar10 = (int *)((uint)(*(int *)((int)local_38 + 0x14c) + (int)(float)local_40) %
                               (uint)local_50);
              local_4c = (undefined4 *)local_48[0x25];
              iVar14 = local_4c[0x17];
              local_40._4_4_ = (float)((ulonglong)local_40 >> 0x20);
              local_40 = CONCAT44(local_40._4_4_,iVar14);
              local_50 = piVar10;
              for (; iVar14 != 0; iVar14 = *(int *)(iVar14 + 100)) {
                if (*(int *)(iVar14 + 0x44) == -1) {
                  FUN_004553d0(piVar10,1);
                }
                pfVar12 = local_44;
                pfVar15 = local_58;
              }
              if ((uint *)local_4c[0x16] != (uint *)0x0) {
                *(uint *)local_4c[0x16] = (uint)local_50;
              }
              if ((*(byte *)(local_4c + 0x10) & 4) != 0) {
                puVar4 = (uint *)local_4c[0x13];
                uVar13 = puVar4[1];
                local_38._4_4_ = (undefined4)(local_38 >> 0x20);
                local_38 = CONCAT44(local_38._4_4_,uVar13);
                if (uVar13 != 0) {
                  uVar8 = puVar4[4];
                  local_40._4_4_ = (float)((ulonglong)local_40 >> 0x20);
                  local_40 = CONCAT44(local_40._4_4_,uVar8);
                  pfVar12 = local_44;
                  if (uVar8 != 0) {
                    piVar10 = local_50;
                    if ((int *)*puVar4 <= local_50) {
                      piVar10 = (int *)((uint)local_50 % *puVar4);
                    }
                    puVar6 = (undefined4 *)
                             ((uint)*(ushort *)(uVar8 + (int)piVar10 * 2) * 0x40 + uVar13);
                    puVar7 = local_4c;
                    for (iVar14 = 0x10; iVar14 != 0; iVar14 = iVar14 + -1) {
                      *puVar7 = *puVar6;
                      puVar6 = puVar6 + 1;
                      puVar7 = puVar7 + 1;
                    }
                  }
                }
                local_4c[0x10] = local_4c[0x10] | 2;
                pfVar15 = local_58;
              }
            }
            iVar14 = local_48[0x25];
            if ((iVar14 != 0) && ((local_48[0x15] & 0x1000) == 0)) {
              *(uint *)(iVar14 + 0x40) = *(uint *)(iVar14 + 0x40) & 0xffffff3f | 0x30;
              iVar14 = *(int *)(iVar14 + 0x5c);
              while ((iVar14 != 0 && (iVar14 != -1))) {
                FUN_00456c20(0x30);
                iVar14 = *(int *)(extraout_EDX + 100);
              }
              local_48[0x15] = local_48[0x15] | 1;
            }
            FUN_0045e060();
            fVar16 = DAT_006da944;
          }
        }
        else if (local_4c != (undefined4 *)0x0) {
          local_4c[0x10] = local_4c[0x10] & 0xffffff0f;
          iVar14 = local_4c[0x17];
          while ((iVar14 != 0 && (iVar14 != -1))) {
            FUN_00456c20(0);
            iVar14 = *(int *)(extraout_EDX_00 + 100);
          }
          local_48[0x15] = local_48[0x15] & 0xfffffffe;
        }
      }
      pfVar12 = (float *)*pfVar12;
      local_44 = pfVar12;
    } while (pfVar12 != pfVar15);
  }
LAB_00446828:
  __security_check_cookie(local_14 ^ (uint)auStack_68);
  return;
}


```

