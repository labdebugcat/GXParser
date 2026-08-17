# Selected Nova1492 Decompilation

## `0042c720`

- Function: `FUN_0042c720`
- Entry: `0042c720`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void __fastcall FUN_0042c720(int param_1)

{
  undefined4 uVar1;
  undefined1 *puVar2;
  uint uVar3;
  float *pfVar4;
  int iVar5;
  undefined4 extraout_ECX;
  undefined4 extraout_ECX_00;
  undefined4 *puVar6;
  undefined4 *puVar7;
  float *pfVar8;
  undefined1 auVar9 [16];
  undefined1 auVar10 [16];
  float fVar11;
  float fVar14;
  float fVar15;
  float fVar16;
  float fVar17;
  undefined1 auVar12 [16];
  float fVar18;
  undefined1 auVar13 [16];
  float fVar19;
  float fVar20;
  float fVar22;
  float fVar23;
  undefined1 auVar21 [16];
  float fVar24;
  float fVar25;
  float fVar26;
  float fVar28;
  float fVar29;
  undefined1 auVar27 [16];
  float fVar30;
  float fVar31;
  float fVar32;
  float fVar33;
  float fVar34;
  undefined4 uVar35;
  undefined4 uVar36;
  undefined1 local_310 [64];
  undefined1 local_2d0 [64];
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
  float local_1f0;
  float fStack_1ec;
  float fStack_1e8;
  float fStack_1e4;
  float local_1e0;
  float fStack_1dc;
  float fStack_1d8;
  float fStack_1d4;
  float local_1d0 [4];
  undefined1 local_1c0 [16];
  undefined4 local_1b0;
  float fStack_1ac;
  undefined4 uStack_1a8;
  undefined4 uStack_1a4;
  undefined4 local_1a0;
  undefined4 local_19c;
  undefined4 local_198;
  undefined4 local_194;
  float local_190;
  float fStack_18c;
  float fStack_188;
  float fStack_184;
  float local_180;
  float fStack_17c;
  float fStack_178;
  float fStack_174;
  float local_170;
  float fStack_16c;
  float fStack_168;
  float fStack_164;
  float local_160;
  float fStack_15c;
  float fStack_158;
  float fStack_154;
  float local_150;
  float fStack_14c;
  float fStack_148;
  float fStack_144;
  float local_140;
  float fStack_13c;
  float fStack_138;
  float fStack_134;
  float local_130;
  float fStack_12c;
  float fStack_128;
  float fStack_124;
  float local_120;
  float fStack_11c;
  float fStack_118;
  float fStack_114;
  undefined1 local_110 [16];
  float local_100;
  float fStack_fc;
  float fStack_f8;
  float fStack_f4;
  float local_f0;
  float fStack_ec;
  float fStack_e8;
  float fStack_e4;
  undefined4 local_d4;
  undefined4 local_d0;
  undefined4 local_cc;
  undefined4 local_c8;
  int local_c4;
  float *local_c0;
  float local_bc;
  float local_b8;
  float local_b4;
  undefined1 local_b0 [64];
  float local_70;
  float local_64;
  float local_5c;
  float local_54;
  uint local_24;
  undefined1 *puStack_20;
  void *local_1c;
  undefined1 *puStack_18;
  undefined4 local_14;
  
  puStack_20 = &stack0xfffffffc;
  local_14 = 0xffffffff;
  puStack_18 = &LAB_0065ae10;
  local_1c = ExceptionList;
  uVar3 = DAT_007360c8 ^ (uint)&stack0xfffffff0;
  ExceptionList = &local_1c;
  local_c4 = param_1;
  local_24 = uVar3;
  puVar2 = &stack0xfffffffc;
  if ((*(int *)(param_1 + 0x205ac) == 0) ||
     ((((*(int *)(param_1 + 0x20104) != 3 &&
        (puVar2 = &stack0xfffffffc, *(int *)(param_1 + 0x20104) != 4)) ||
       (puVar2 = &stack0xfffffffc, *(int *)(param_1 + 0x20db4) == 0)) ||
      (puVar2 = &stack0xfffffffc, *(int *)(param_1 + 0x20dc4) == 0)))) goto LAB_0042cf42;
  local_d4 = 0;
  local_d0 = 0;
  local_cc = 0;
  local_c8 = 0;
  FUN_0042d3a0(*(int *)(param_1 + 0x20db4),&local_d4);
  puVar6 = &DAT_00736d50;
  puVar7 = &DAT_00736de0;
  for (iVar5 = 0x10; iVar5 != 0; iVar5 = iVar5 + -1) {
    *puVar7 = *puVar6;
    puVar6 = puVar6 + 1;
    puVar7 = puVar7 + 1;
  }
  FUN_00480830(uVar3);
  auVar12 = divps(_DAT_008b2360,_DAT_006db520);
  local_1a0 = DAT_008b2310;
  local_19c = DAT_008b2314;
  local_198 = DAT_008b2318;
  local_194 = DAT_008b231c;
  local_c0 = (float *)(local_c4 + 0x90);
  local_1d0[0] = _UNK_006db1f8 + auVar12._0_4_;
  local_1d0[1] = _UNK_006db1f8;
  local_1d0[2] = _UNK_006db1f8;
  local_1d0[3] = (float)_DAT_006db1f0;
  local_1c0._4_4_ = auVar12._4_4_;
  local_1c0._0_4_ = auVar12._8_4_;
  local_1c0._8_4_ = _UNK_006db1f8;
  local_1c0._12_4_ = _UNK_006db1f4;
  local_1b0 = auVar12._8_4_;
  fStack_1ac = _UNK_006db1f8;
  uStack_1a8 = auVar12._12_4_;
  uStack_1a4 = _UNK_006db1fc;
  pfVar4 = local_1d0;
  pfVar8 = (float *)(local_c4 + 0x90);
  for (iVar5 = 0x10; iVar5 != 0; iVar5 = iVar5 + -1) {
    *pfVar8 = *pfVar4;
    pfVar4 = pfVar4 + 1;
    pfVar8 = pfVar8 + 1;
  }
  fVar25 = (float)(DAT_007c24e4 + DAT_007c24ec + 1) * DAT_006daa38;
  auVar9._4_12_ = local_1c0._4_12_;
  auVar9._0_4_ = (float)(DAT_007c24e8 + DAT_007c24f0 + 1) * DAT_006daa38;
  fVar31 = fVar25 + DAT_00785120;
  fVar32 = _DAT_006dafe0 + DAT_00785124;
  fVar33 = auVar9._0_4_ + DAT_00785128;
  fVar34 = _UNK_006dafe4 + fRam0078512c;
  auVar27._0_4_ = fVar25 - fVar31;
  auVar27._4_4_ = _DAT_006dafe0 - fVar32;
  auVar27._8_4_ = auVar9._0_4_ - fVar33;
  auVar27._12_4_ = _UNK_006dafe4 - fVar34;
  fVar11 = auVar27._0_4_ * auVar27._0_4_;
  fVar14 = auVar27._4_4_ * auVar27._4_4_;
  fVar16 = auVar27._8_4_ * auVar27._8_4_;
  fVar18 = auVar27._12_4_ * auVar27._12_4_;
  fVar25 = _DAT_006db290;
  fVar15 = _UNK_006db294;
  fVar17 = _UNK_006db298;
  fVar19 = _UNK_006db29c;
  local_1e0 = fVar11;
  fStack_1dc = fVar14;
  fStack_1d8 = fVar16;
  fStack_1d4 = fVar18;
  pfVar4 = (float *)FUN_004356f0(local_270);
  fVar11 = fVar11 + *pfVar4;
  fVar14 = fVar14 + pfVar4[1];
  fVar16 = fVar16 + pfVar4[2];
  fVar18 = fVar18 + pfVar4[3];
  local_1f0 = fVar11;
  fStack_1ec = fVar14;
  fStack_1e8 = fVar16;
  fStack_1e4 = fVar18;
  pfVar4 = (float *)FUN_00435710(local_280);
  auVar13._0_4_ = fVar11 + *pfVar4;
  auVar13._4_4_ = fVar14 + pfVar4[1];
  auVar13._8_4_ = fVar16 + pfVar4[2];
  auVar13._12_4_ = fVar18 + pfVar4[3];
  auVar12 = sqrtps(auVar9,auVar13);
  auVar12 = divps(auVar27,auVar12);
  fVar26 = (float)(auVar12._0_4_ ^ _DAT_008b2370);
  fVar28 = (float)(auVar12._4_4_ ^ uRam008b2374);
  fVar29 = (float)(auVar12._8_4_ ^ uRam008b2378);
  fVar30 = (float)(auVar12._12_4_ ^ uRam008b237c);
  auVar10._0_4_ = fVar26 * fVar15;
  auVar10._4_4_ = fVar28 * fVar17;
  auVar10._8_4_ = fVar29 * fVar25;
  auVar10._12_4_ = fVar30 * fVar19;
  fVar16 = fVar28 * fVar25 - auVar10._0_4_;
  fVar11 = fVar29 * fVar15 - auVar10._4_4_;
  fVar14 = fVar26 * fVar17 - auVar10._8_4_;
  auVar21._12_4_ = fVar30 * fVar19 - auVar10._12_4_;
  auVar21._4_4_ = fVar14;
  auVar21._0_4_ = fVar11;
  auVar21._8_4_ = fVar16;
  fVar11 = fVar11 * fVar11;
  fVar14 = fVar14 * fVar14;
  fVar16 = fVar16 * fVar16;
  fVar18 = auVar21._12_4_ * auVar21._12_4_;
  fVar25 = fVar26;
  fVar15 = fVar28;
  fVar17 = fVar29;
  fVar19 = fVar30;
  local_120 = fVar11;
  fStack_11c = fVar14;
  fStack_118 = fVar16;
  fStack_114 = fVar18;
  local_f0 = fVar26;
  fStack_ec = fVar28;
  fStack_e8 = fVar29;
  fStack_e4 = fVar30;
  pfVar4 = (float *)FUN_004356f0(local_290);
  fVar11 = *pfVar4 + fVar11;
  fVar14 = pfVar4[1] + fVar14;
  fVar16 = pfVar4[2] + fVar16;
  fVar18 = pfVar4[3] + fVar18;
  local_130 = fVar11;
  fStack_12c = fVar14;
  fStack_128 = fVar16;
  fStack_124 = fVar18;
  pfVar4 = (float *)FUN_00435710(local_200);
  auVar12._4_4_ = fVar14 + pfVar4[1];
  auVar12._0_4_ = fVar11 + *pfVar4;
  auVar12._8_4_ = fVar16 + pfVar4[2];
  auVar12._12_4_ = fVar18 + pfVar4[3];
  auVar12 = sqrtps(auVar10,auVar12);
  local_110 = divps(auVar21,auVar12);
  fVar20 = local_110._0_4_;
  fVar22 = local_110._4_4_;
  fVar23 = local_110._8_4_;
  fVar24 = local_110._12_4_;
  fVar11 = fVar31 * fVar20;
  fVar14 = fVar32 * fVar22;
  fVar16 = fVar33 * fVar23;
  fVar18 = fVar34 * fVar24;
  fStack_f8 = fVar25 * fVar22 - fVar28 * fVar20;
  local_100 = fVar15 * fVar23 - fVar29 * fVar22;
  fStack_fc = fVar17 * fVar20 - fVar26 * fVar23;
  fStack_f4 = fVar19 * fVar24 - fVar30 * fVar24;
  local_140 = fVar11;
  fStack_13c = fVar14;
  fStack_138 = fVar16;
  fStack_134 = fVar18;
  pfVar4 = (float *)FUN_004356f0(local_210);
  fVar11 = fVar11 + *pfVar4;
  fStack_14c = fVar14 + pfVar4[1];
  fStack_148 = fVar16 + pfVar4[2];
  fStack_144 = fVar18 + pfVar4[3];
  local_150 = fVar11;
  pfVar4 = (float *)FUN_00435710(local_220);
  local_b4 = *pfVar4 + fVar11;
  fVar25 = local_100 * fVar31;
  fVar15 = fStack_fc * fVar32;
  fVar17 = fStack_f8 * fVar33;
  fVar19 = fStack_f4 * fVar34;
  local_110._12_4_ = -local_b4;
  local_160 = fVar25;
  fStack_15c = fVar15;
  fStack_158 = fVar17;
  fStack_154 = fVar19;
  pfVar4 = (float *)FUN_004356f0(local_230);
  fVar25 = fVar25 + *pfVar4;
  fStack_16c = fVar15 + pfVar4[1];
  fStack_168 = fVar17 + pfVar4[2];
  fStack_164 = fVar19 + pfVar4[3];
  local_170 = fVar25;
  pfVar4 = (float *)FUN_00435710(local_240);
  local_b4 = fVar25 + *pfVar4;
  fStack_f4 = -local_b4;
  fVar31 = local_f0 * fVar31;
  fVar32 = fStack_ec * fVar32;
  fVar33 = fStack_e8 * fVar33;
  fVar34 = fStack_e4 * fVar34;
  local_180 = fVar31;
  fStack_17c = fVar32;
  fStack_178 = fVar33;
  fStack_174 = fVar34;
  pfVar4 = (float *)FUN_004356f0(local_250);
  fVar31 = *pfVar4 + fVar31;
  fStack_18c = pfVar4[1] + fVar32;
  fStack_188 = pfVar4[2] + fVar33;
  fStack_184 = pfVar4[3] + fVar34;
  local_190 = fVar31;
  pfVar4 = (float *)FUN_00435710(local_260);
  local_b4 = fVar31 + *pfVar4;
  fStack_e4 = -local_b4;
  FUN_004358f0(local_110,&local_100,&local_f0,&DAT_008b2310);
  pfVar4 = (float *)FUN_00435620(local_2d0,local_b0);
  pfVar8 = local_c0;
  for (iVar5 = 0x10; iVar5 != 0; iVar5 = iVar5 + -1) {
    *pfVar8 = *pfVar4;
    pfVar4 = pfVar4 + 1;
    pfVar8 = pfVar8 + 1;
  }
  FUN_00480910(local_c0);
  iVar5 = local_c4;
  (**(code **)(**(int **)(local_c4 + 0x205ac) + 0xac))
            (*(int **)(local_c4 + 0x205ac),0,0,1,0xffffffff,0x3f800000,0);
  FUN_0042b98b(0);
  FUN_0042b9b5(0);
  FUN_0042ba38(0);
  FUN_0042b9e5(0);
  FUN_0042b17a(extraout_ECX);
  uVar1 = _UNK_006db3dc;
  uVar36 = _UNK_006db3d8;
  uVar35 = _UNK_006db3d4;
  pfVar4 = (float *)(iVar5 + 0x20590);
  *(undefined4 *)(iVar5 + 0x20580) = _DAT_006db3d0;
  *(undefined4 *)(iVar5 + 0x20584) = uVar35;
  *(undefined4 *)(iVar5 + 0x20588) = uVar36;
  *(undefined4 *)(iVar5 + 0x2058c) = uVar1;
  uVar1 = _UNK_006db3ac;
  uVar36 = _UNK_006db3a8;
  uVar35 = _UNK_006db3a4;
  *pfVar4 = _DAT_006db3a0;
  *(undefined4 *)(iVar5 + 0x20594) = uVar35;
  *(undefined4 *)(iVar5 + 0x20598) = uVar36;
  *(undefined4 *)(iVar5 + 0x2059c) = uVar1;
  FUN_00454320((undefined4 *)(iVar5 + 0x20580),pfVar4);
  if ((*(int *)(*(int *)ThreadLocalStoragePointer + 0x70) < DAT_008b2380) &&
     (FUN_0062a7d8(&DAT_008b2380), DAT_008b2380 == -1)) {
    DAT_008b2384 = *pfVar4;
    local_14 = 0xffffffff;
    FUN_0062a799(&DAT_008b2380);
  }
  if ((*(int *)(*(int *)ThreadLocalStoragePointer + 0x70) < DAT_008b2388) &&
     (FUN_0062a7d8(&DAT_008b2388), DAT_008b2388 == -1)) {
    DAT_008b238c = *(float *)(iVar5 + 0x20594);
    local_14 = 0xffffffff;
    FUN_0062a799(&DAT_008b2388);
  }
  if ((*(int *)(*(int *)ThreadLocalStoragePointer + 0x70) < DAT_008b2390) &&
     (FUN_0062a7d8(&DAT_008b2390), DAT_008b2390 == -1)) {
    DAT_008b2394 = *(float *)(iVar5 + 0x20580);
    local_14 = 0xffffffff;
    FUN_0062a799(&DAT_008b2390);
  }
  if ((*(int *)(*(int *)ThreadLocalStoragePointer + 0x70) < DAT_008b2398) &&
     (FUN_0062a7d8(&DAT_008b2398), DAT_008b2398 == -1)) {
    DAT_008b239c = *(float *)(iVar5 + 0x20584);
    local_14 = 0xffffffff;
    FUN_0062a799(&DAT_008b2398);
  }
  fVar25 = *pfVar4;
  if (DAT_008b2384 <= fVar25) {
    if (DAT_008b2384 < fVar25 - DAT_006dad54) goto LAB_0042cd01;
  }
  else {
    fVar25 = fVar25 - DAT_006dad54;
LAB_0042cd01:
    DAT_008b2384 = fVar25;
  }
  fVar25 = *(float *)(iVar5 + 0x20594);
  if (DAT_008b238c <= fVar25) {
    if (DAT_008b238c < fVar25 - DAT_006dad54) goto LAB_0042cd43;
  }
  else {
    fVar25 = fVar25 - DAT_006dad54;
LAB_0042cd43:
    DAT_008b238c = fVar25;
  }
  fVar25 = *(float *)(iVar5 + 0x20580);
  if (fVar25 <= DAT_008b2394) {
    if (fVar25 + DAT_006dad54 < DAT_008b2394) goto LAB_0042cd80;
  }
  else {
    fVar25 = fVar25 + DAT_006dad54;
LAB_0042cd80:
    DAT_008b2394 = fVar25;
  }
  fVar25 = *(float *)(iVar5 + 0x20584);
  if (fVar25 <= DAT_008b239c) {
    if (fVar25 + DAT_006dad54 < DAT_008b239c) goto LAB_0042cdb5;
  }
  else {
    fVar25 = fVar25 + DAT_006dad54;
LAB_0042cdb5:
    DAT_008b239c = fVar25;
  }
  fVar25 = (float)*(int *)(iVar5 + 0x20dbc);
  if (*(int *)(iVar5 + 0x20dbc) < 0) {
    fVar25 = fVar25 + _DAT_006daed8;
  }
  fVar15 = (float)*(int *)(iVar5 + 0x20dc0);
  fVar17 = (fVar25 / (DAT_008b2394 - DAT_008b2384)) * DAT_006da9ec;
  if (*(int *)(iVar5 + 0x20dc0) < 0) {
    fVar15 = fVar15 + _DAT_006daed8;
  }
  fVar31 = (fVar15 / (DAT_008b239c - DAT_008b238c)) * DAT_006da9ec;
  fVar19 = DAT_008b2394;
  fVar11 = DAT_008b239c;
  local_bc = DAT_008b2384;
  local_b8 = fVar15;
  local_b4 = DAT_008b238c;
  FUN_004358f0(&DAT_008b22e0,&DAT_008b22f0,&DAT_008b2300,&DAT_008b2310);
  local_64 = (float)((uint)(((fVar19 + local_bc) - fVar25) / fVar25) ^ DAT_006db4a0) * fVar17;
  local_54 = (((fVar11 + local_b4) - fVar15) / fVar15) * fVar31;
  local_70 = fVar17;
  local_5c = fVar31;
  pfVar4 = (float *)FUN_00435620(local_310,iVar5 + 0x90);
  pfVar8 = local_c0;
  for (iVar5 = 0x10; iVar5 != 0; iVar5 = iVar5 + -1) {
    *pfVar8 = *pfVar4;
    pfVar4 = pfVar4 + 1;
    pfVar8 = pfVar8 + 1;
  }
  uVar35 = 0x42cebd;
  pfVar4 = local_c0;
  FUN_00480910(local_c0);
  iVar5 = local_c4;
  if ((*(int **)(local_c4 + 0x20dc4) != (int *)0x0) && (**(int **)(local_c4 + 0x20dc4) != 0)) {
    FUN_0042ba0f(3,uVar35,pfVar4);
    FUN_004331a0(*(undefined4 *)(*(int *)(iVar5 + 0x20dc4) + 8));
    FUN_004544c0();
    uVar36 = 0x42cf03;
    uVar35 = extraout_ECX_00;
    FUN_004331c0(extraout_ECX_00);
    FUN_0042ba0f(4,uVar36,uVar35);
  }
  FUN_0042d480(&local_d4);
  FUN_00480860();
  FUN_004807e0();
  FUN_0042b98b(1);
  FUN_0042b9b5(1);
  FUN_0042ba38(1);
  puVar2 = puStack_20;
LAB_0042cf42:
  puStack_20 = puVar2;
  ExceptionList = local_1c;
  __security_check_cookie(local_24 ^ (uint)&stack0xfffffff0);
  return;
}


```

## `0042dcc0`

- Function: `FUN_0042dcc0`
- Entry: `0042dcc0`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void __fastcall FUN_0042dcc0(undefined4 *param_1)

{
  int *piVar1;
  int iVar2;
  undefined4 *puVar3;
  int iVar4;
  undefined4 extraout_ECX;
  undefined4 extraout_ECX_00;
  undefined4 uVar5;
  int iVar6;
  float fVar7;
  float fVar8;
  float fVar9;
  float fVar10;
  float fVar11;
  undefined1 uStack_2d;
  float fStack_2c;
  undefined4 uStack_20;
  float fStack_1c;
  float fStack_14;
  float fStack_10;
  undefined4 uStack_c;
  float fStack_8;
  
  for (iVar4 = DAT_007641bc; iVar4 != 0; iVar4 = *(int *)(iVar4 + 0x9c)) {
    piVar1 = *(int **)(iVar4 + 0x14);
    if (((piVar1 != (int *)0x0) && ((piVar1[0x15] & 0x21U) != 0)) && ((piVar1[0x15] & 0x1000U) == 0)
       ) {
      iVar2 = FUN_00583a20();
      (**(code **)(*piVar1 + 0x18))(*(undefined4 *)(iVar4 + 8),iVar2 == 0x23);
    }
  }
  if (*(char *)(param_1 + 0x8094) != '\x01') {
    FUN_00431bf0(0,0);
    *(undefined1 *)(param_1 + 0x8094) = 1;
    *(undefined2 *)(param_1 + 0x8091) = 0;
  }
  if (DAT_00761cd0 != 0) {
    iVar4 = *(int *)(DAT_00761cd0 + 0x5020);
    if (0 < iVar4) {
      if (iVar4 < 0xff) {
        uStack_2d = (undefined1)iVar4;
      }
      else {
        uStack_2d = 0xff;
      }
      if (param_1[0x8090] != 4) {
        param_1[0x8090] = 4;
        (**(code **)(*(int *)param_1[0x816b] + 0xe4))((int *)param_1[0x816b],0x13,2);
        (**(code **)(*(int *)param_1[0x816b] + 0xe4))((int *)param_1[0x816b],0x14,2);
      }
      uStack_20 = CONCAT13(0xff,CONCAT21(CONCAT11(uStack_2d,uStack_2d),uStack_2d));
      *param_1 = uStack_20;
      FUN_00429d5b(1,0,0,0,(float)DAT_007c3920,(float)DAT_007c3924);
      if (param_1[0x8090] != 1) {
        param_1[0x8090] = 1;
        (**(code **)(*(int *)param_1[0x816b] + 0xe4))((int *)param_1[0x816b],0x13,5);
        (**(code **)(*(int *)param_1[0x816b] + 0xe4))((int *)param_1[0x816b],0x14,6);
      }
    }
    if (((*(int *)(DAT_00761cd0 + 0x20) == 6) && (*(int *)(DAT_00761cd0 + 0x5024) != 0)) &&
       (param_1[0x8367] != 0)) {
      FUN_0046cd50(*(int *)(DAT_00761cd0 + 0x5024));
      if (param_1[0x8090] != 2) {
        param_1[0x8090] = 2;
        (**(code **)(*(int *)param_1[0x816b] + 0xe4))((int *)param_1[0x816b],0x13,5);
        (**(code **)(*(int *)param_1[0x816b] + 0xe4))((int *)param_1[0x816b],0x14,6);
      }
      if (*(char *)((int)param_1 + 0x20246) != '\x01') {
        *(undefined1 *)((int)param_1 + 0x20246) = 1;
        (**(code **)(*(int *)param_1[0x816b] + 0xe4))((int *)param_1[0x816b],0x1b,1);
      }
      if (param_1[0x805b] != 1) {
        param_1[0x805b] = 1;
        (**(code **)(*(int *)param_1[0x816b] + 0x114))((int *)param_1[0x816b],0,1,1);
      }
      if (param_1[0x8063] != 1) {
        param_1[0x8063] = 1;
        (**(code **)(*(int *)param_1[0x816b] + 0x114))((int *)param_1[0x816b],0,2,1);
      }
      fStack_14 = 0.0;
      fVar7 = (float)CONCAT44((DAT_007c390c - DAT_007c3914) - (uint)(DAT_007c3908 < DAT_007c3910),
                              DAT_007c3908 - DAT_007c3910) * _DAT_007641f4;
      fVar11 = fVar7 + DAT_006dacc8;
      fStack_8 = fVar7;
      puVar3 = (undefined4 *)FUN_00428860(4,&fStack_14);
      puVar3[6] = fVar7;
      *puVar3 = 0;
      puVar3[1] = 0;
      puVar3[2] = 0;
      puVar3[3] = 0x3f800000;
      puVar3[4] = 0x50ffffff;
      puVar3[5] = 0;
      puVar3[7] = 0;
      fVar7 = (float)DAT_007c3924;
      puVar3[9] = 0;
      puVar3[10] = 0x3f800000;
      puVar3[0xb] = 0x50ffffff;
      puVar3[0xc] = 0;
      puVar3[0xd] = fVar11;
      puVar3[8] = fVar7;
      fVar7 = (float)DAT_007c3920;
      puVar3[0xf] = 0;
      puVar3[0x10] = 0;
      puVar3[0x11] = 0x3f800000;
      puVar3[0x12] = 0x50ffffff;
      puVar3[0x13] = 0x3f800000;
      puVar3[0xe] = fVar7;
      puVar3[0x14] = fStack_8;
      puVar3[0x15] = (float)DAT_007c3920;
      fVar7 = (float)DAT_007c3924;
      puVar3[0x17] = 0;
      puVar3[0x18] = 0x3f800000;
      puVar3[0x19] = 0x50ffffff;
      puVar3[0x1a] = 0x3f800000;
      puVar3[0x1b] = fVar11;
      puVar3[0x16] = fVar7;
      iVar4 = param_1[0x8367];
      uVar5 = extraout_ECX;
      if ((*(char *)(iVar4 + 0x34) != '\0') && (*(char *)(iVar4 + 0x35) != '\0')) {
        piVar1 = *(int **)(iVar4 + 0xc);
        uVar5 = 0;
        if (piVar1 != (int *)0x0) {
          (**(code **)(*piVar1 + 0x30))(piVar1);
          *(undefined1 *)(iVar4 + 0x35) = 0;
          uVar5 = extraout_ECX_00;
        }
      }
      FUN_00428b20(5,fStack_14,4,uVar5);
      if (param_1[0x805b] != 3) {
        param_1[0x805b] = 3;
        (**(code **)(*(int *)param_1[0x816b] + 0x114))((int *)param_1[0x816b],0,1,3);
      }
      if (param_1[0x8063] != 3) {
        param_1[0x8063] = 3;
        (**(code **)(*(int *)param_1[0x816b] + 0x114))((int *)param_1[0x816b],0,2,3);
      }
    }
  }
  FUN_005170b0();
  if (param_1[0x8090] != 0) {
    param_1[0x8090] = 0;
  }
  iVar4 = DAT_00762478;
  if (DAT_007c3948 == (int *)0x0) {
    *param_1 = DAT_0073ae68;
    if (DAT_007c36cc == 1) {
      iVar2 = (*(int *)(iVar4 + 0x10) + -0x400) / 2 + DAT_007c3748;
    }
    else {
      iVar2 = DAT_007c3748;
      if (DAT_007c36cc == 2) {
        iVar2 = DAT_007c3748 + -0x400 + *(int *)(iVar4 + 0x10);
      }
    }
    if (DAT_007c36cc == 1) {
      iVar6 = (*(int *)(iVar4 + 0x10) + -0x400) / 2 + DAT_007c3748;
    }
    else {
      iVar6 = DAT_007c3748;
      if (DAT_007c36cc == 2) {
        iVar6 = *(int *)(iVar4 + 0x10) + -0x400 + DAT_007c3748;
      }
    }
    FUN_00429d5b(1,1,(float)iVar6,(float)(DAT_007c374c + -0x300 + *(int *)(iVar4 + 0x14)),
                 (float)(DAT_007c3750 + iVar2),
                 (float)(DAT_007c3754 + -0x300 + DAT_007c374c + *(int *)(iVar4 + 0x14)));
  }
  else {
    if (DAT_007c36cc == 1) {
      iVar4 = (*(int *)(DAT_00762478 + 0x10) + -0x400) / 2 + DAT_007c3748;
    }
    else {
      iVar4 = DAT_007c3748;
      if (DAT_007c36cc == 2) {
        iVar4 = DAT_007c3748 + -0x400 + *(int *)(DAT_00762478 + 0x10);
      }
    }
    fVar7 = (float)DAT_007c3948[1];
    if (DAT_007c3948[1] < 0) {
      fVar7 = fVar7 + _DAT_006daed8;
    }
    fVar11 = (float)*DAT_007c3948;
    if (*DAT_007c3948 < 0) {
      fVar11 = fVar11 + _DAT_006daed8;
    }
    FUN_0046e240((float)iVar4,(float)(DAT_007c374c + -0x300 + *(int *)(DAT_00762478 + 0x14)),
                 (float)DAT_007c3750,(float)DAT_007c3754,0,0,fVar11,fVar7);
  }
  uVar5 = DAT_0073ae68;
  fStack_2c = (float)DAT_007c3750;
  fStack_1c = (float)DAT_007c3754;
  fVar7 = (float)DAT_007c24dc;
  fVar11 = (float)DAT_007c24e0;
  if (DAT_007c36cc == 1) {
    iVar4 = (*(int *)(DAT_00762478 + 0x10) + -0x400) / 2 + DAT_007c3748;
  }
  else {
    iVar4 = DAT_007c3748;
    if (DAT_007c36cc == 2) {
      iVar4 = DAT_007c3748 + -0x400 + *(int *)(DAT_00762478 + 0x10);
    }
  }
  fStack_8 = (float)iVar4 + DAT_006daa00;
  fStack_14 = (float)(DAT_007c374c + -0x300 + *(int *)(DAT_00762478 + 0x14));
  if (fVar7 <= fVar11) {
    if (fVar7 < fVar11) {
      fStack_2c = (fVar7 / fVar11) * fStack_2c;
      fVar9 = (float)(DAT_006daee8 & (uint)fStack_2c);
      fVar8 = (float)((uint)DAT_006daed4 &
                      -(uint)((float)((uint)fStack_2c ^ (uint)fVar9) < DAT_006daed4) | (uint)fVar9);
      fVar8 = (fStack_2c + fVar8) - fVar8;
      fStack_2c = fVar8 - (float)(-(uint)(fVar9 < fVar8 - fStack_2c) & (uint)DAT_006daa00);
      fVar9 = ((float)DAT_007c3750 - fStack_2c) * DAT_006da974;
      fVar10 = (float)(DAT_006daee8 & (uint)fVar9);
      fVar8 = (float)((uint)DAT_006daed4 &
                      -(uint)((float)((uint)fVar9 ^ (uint)fVar10) < DAT_006daed4) | (uint)fVar10);
      fVar8 = (fVar9 + fVar8) - fVar8;
      fStack_8 = fStack_8 + (fVar8 - (float)(-(uint)(fVar10 < fVar8 - fVar9) & (uint)DAT_006daa00));
    }
  }
  else {
    fStack_1c = (fVar11 / fVar7) * fStack_1c;
    fVar9 = (float)(DAT_006daee8 & (uint)fStack_1c);
    fVar8 = (float)((uint)DAT_006daed4 &
                    -(uint)((float)((uint)fStack_1c ^ (uint)fVar9) < DAT_006daed4) | (uint)fVar9);
    fVar8 = (fStack_1c + fVar8) - fVar8;
    fStack_1c = fVar8 - (float)(-(uint)(fVar9 < fVar8 - fStack_1c) & (uint)DAT_006daa00);
    fVar9 = ((float)DAT_007c3754 - fStack_1c) * DAT_006da974;
    fVar10 = (float)(DAT_006daee8 & (uint)fVar9);
    fVar8 = (float)((uint)DAT_006daed4 & -(uint)((float)((uint)fVar9 ^ (uint)fVar10) < DAT_006daed4)
                   | (uint)fVar10);
    fVar8 = (fVar9 + fVar8) - fVar8;
    fStack_14 = (fVar8 - (float)(-(uint)(fVar10 < fVar8 - fVar9) & (uint)DAT_006daa00)) + fStack_14;
  }
  fVar7 = fStack_2c / (fVar7 - DAT_006da974);
  fStack_10 = fStack_1c / (fVar11 - DAT_006da974);
  if (param_1[0x8090] != 2) {
    param_1[0x8090] = 2;
    (**(code **)(*(int *)param_1[0x816b] + 0xe4))((int *)param_1[0x816b],0x13,5);
    (**(code **)(*(int *)param_1[0x816b] + 0xe4))((int *)param_1[0x816b],0x14,6);
  }
  uStack_c = 0xc8ff0000;
  DAT_00764330 = 0xc8ff0000;
  fVar11 = (float)DAT_007c4e60[1];
  if (DAT_007c4e60[1] < 0) {
    fVar11 = fVar11 + _DAT_006daed8;
  }
  fVar8 = (float)*DAT_007c4e60;
  if (*DAT_007c4e60 < 0) {
    fVar8 = fVar8 + _DAT_006daed8;
  }
  FUN_0046e240(fStack_8,fStack_14,fStack_2c,fStack_1c,0,0,fVar8,fVar11);
  DAT_00764330 = DAT_0073ae68;
  *param_1 = uVar5;
  FUN_00429d5b(0,1,(float)(int)((float)DAT_007c24e4 * fVar7 + fStack_8),
               (float)(int)((float)DAT_007c24e8 * fStack_10 + fStack_14),
               (float)(int)((float)DAT_007c24ec * fVar7 + fStack_8),
               (float)(int)((float)DAT_007c24f0 * fStack_10 + fStack_14));
  iVar4 = DAT_007641bc;
  *param_1 = DAT_0073ae68;
  for (; iVar4 != 0; iVar4 = *(int *)(iVar4 + 0x9c)) {
    if (((*(byte *)(iVar4 + 0x10) & 0xe0) != 0) &&
       ((*(byte *)(*(int *)(iVar4 + 0x14) + 0x54) & 0x18) != 0)) {
      iVar2 = FUN_00583a20();
      FUN_0045e1c0(*(undefined4 *)(iVar4 + 8),iVar2 == 0x23);
    }
  }
  return;
}


```

## `0042e6c0`

- Function: `FUN_0042e6c0`
- Entry: `0042e6c0`

```c

void FUN_0042e6c0(void)

{
  float fVar1;
  int *piVar2;
  char cVar3;
  float fVar4;
  int iVar5;
  char extraout_DL;
  int iVar6;
  int iVar7;
  float *pfVar8;
  uint uVar9;
  float10 fVar10;
  float10 extraout_ST0;
  float fVar11;
  float fVar12;
  uint local_44;
  
  uVar9 = DAT_007b5e94;
  fVar11 = DAT_006daa38;
  if (DAT_007641bc != 0) {
    fVar10 = (float10)0;
    iVar7 = DAT_007641bc;
    fVar12 = DAT_006da944;
    do {
      piVar2 = *(int **)(iVar7 + 0x14);
      iVar5 = (int)(*(float *)(iVar7 + 0x84) * fVar12);
      iVar6 = (int)(*(float *)(iVar7 + 0x88) * fVar12);
      if (piVar2 != (int *)0x0) {
        if ((*(byte *)(iVar7 + 0x10) & 0xc0) == 0) {
          cVar3 = FUN_0044cad0(iVar5,iVar6,piVar2[0x23]);
        }
        else {
          cVar3 = FUN_0044cad0(iVar5,iVar6,(float)fVar10);
        }
        if ((cVar3 == '\0') || ((*(byte *)(iVar7 + 0x10) & 0xe0) == 0)) {
          piVar2[0x15] = piVar2[0x15] & 0xffffffef;
        }
        else {
          iVar5 = FUN_00583a20();
          if (iVar5 == 0x23) {
            piVar2[0x15] = piVar2[0x15] | 8;
          }
          piVar2[0x15] = piVar2[0x15] | 0x10;
          cVar3 = extraout_DL;
        }
        if ((cVar3 == '\0') && ((*(byte *)(piVar2 + 0x15) & 0x20) == 0)) {
LAB_0042e884:
          if (piVar2[0x25] != 0) {
            FUN_00456c20(0);
            piVar2[0x15] = piVar2[0x15] & 0xfffffffe;
          }
        }
        else {
          iVar5 = (int)((float)piVar2[4] * fVar12);
          iVar6 = (int)((float)piVar2[6] * fVar12);
          if (((((DAT_007c24dc <= iVar5) ||
                ((((DAT_007c24e0 <= iVar6 || (iVar5 < 0)) || (iVar6 < 0)) ||
                 ((iVar5 < DAT_007c24e4 + -3 || (DAT_007c24ec + 3 < iVar5)))))) ||
               (iVar6 < DAT_007c24e8 + -3)) || (DAT_007c24f0 + 3 < iVar6)) ||
             (((*(int *)(iVar7 + 8) != DAT_007df0f0 &&
               (((DAT_007c24dc <= iVar5 || (DAT_007c24e0 <= iVar6)) ||
                ((iVar5 < 0 ||
                 ((iVar6 < 0 || (*(char *)(iVar6 * DAT_007c24dc + iVar5 + DAT_007c2490) == '\0')))))
                ))) && ((piVar2[0x25] == 0 || (iVar5 = FUN_00456920(), iVar5 == 0))))))
          goto LAB_0042e884;
          if ((piVar2[0x25] != 0) && ((piVar2[0x15] & 0x1000U) == 0)) {
            FUN_00456c20(0x30);
            piVar2[0x15] = piVar2[0x15] | 1;
          }
          FUN_0045e060();
        }
        (**(code **)(*piVar2 + 0x1c))();
        fVar10 = (float10)0;
        uVar9 = DAT_007b5e94;
        fVar11 = DAT_006daa38;
        fVar12 = DAT_006da944;
      }
      if ((*(byte *)(iVar7 + 0x10) & 2) == 0) {
        if ((*(int *)(iVar7 + 4) == 509999) && (*(int *)(iVar7 + 8) == DAT_007df0f0)) {
          fVar4 = *(float *)(iVar7 + 0x88);
          if ((DAT_007b5320 != 0) && (uVar9 < 0xa7)) {
            pfVar8 = (float *)(&DAT_007b5414 + uVar9 * 4);
            *pfVar8 = *(float *)(iVar7 + 0x84) + fVar11;
            (&DAT_007b5418)[uVar9 * 4] = fVar4 + fVar11;
            fVar4 = 100.0;
            (&DAT_007b541c)[uVar9 * 4] = 0xd;
            goto LAB_0042e9ce;
          }
        }
      }
      else if (((*(int *)(iVar7 + 8) == DAT_007df0f0) ||
               (iVar5 = FUN_005844f0(), fVar10 = extraout_ST0, iVar5 != 0)) ||
              (((*(byte *)(iVar7 + 0x10) & 0xa0) != 0 && (*(char *)(iVar7 + 0xa0) != '\0')))) {
        iVar5 = *(int *)(iVar7 + 0xc0);
        fVar1 = *(float *)(iVar7 + 0x88);
        fVar4 = *(float *)(iVar7 + 0x8c);
        if ((DAT_007b5320 != 0) && (uVar9 < 0xa7)) {
          pfVar8 = (float *)(&DAT_007b5414 + uVar9 * 4);
          *pfVar8 = *(float *)(iVar7 + 0x84) + fVar11;
          (&DAT_007b5418)[uVar9 * 4] = fVar1 + fVar11;
          (&DAT_007b541c)[uVar9 * 4] = iVar5 + 1;
LAB_0042e9ce:
          pfVar8[3] = fVar4;
          uVar9 = DAT_007b5e94 + 1;
          DAT_007b5e94 = uVar9;
        }
      }
      iVar7 = *(int *)(iVar7 + 0x9c);
    } while (iVar7 != 0);
  }
  if (DAT_007641a0 != '\0') {
    local_44 = 0;
    do {
      if ((DAT_007b5320 != 0) && (uVar9 < 0xa7)) {
        (&DAT_007b5414)[uVar9 * 4] = (float)(int)((local_44 / 6) * 0x1e + 0xf) + fVar11;
        (&DAT_007b5418)[uVar9 * 4] = (float)((local_44 % 6) * 0x1e + 0xf) + fVar11;
        (&DAT_007b541c)[uVar9 * 4] = 0x1e;
        *(undefined4 *)(&DAT_007b5420 + uVar9 * 0x10) = 0x42c80000;
        uVar9 = DAT_007b5e94 + 1;
        DAT_007b5e94 = uVar9;
      }
      local_44 = local_44 + 1;
    } while ((int)local_44 < 0x78);
  }
  return;
}


```

## `00446940`

- Function: `FUN_00446940`
- Entry: `00446940`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00446940(void)

{
  undefined4 uVar1;
  int *piVar2;
  int iVar3;
  int *piVar4;
  int iVar5;
  int iVar6;
  uint uVar7;
  int iVar8;
  undefined4 *puVar9;
  int iVar10;
  uint extraout_ECX;
  uint uVar11;
  uint uVar12;
  uint uVar13;
  uint uVar14;
  int iVar15;
  undefined4 *puVar16;
  bool bVar17;
  undefined8 uVar18;
  uint uStack_98;
  int *piStack_94;
  uint uStack_90;
  uint uStack_8c;
  int iStack_88;
  uint uStack_84;
  uint uStack_80;
  undefined1 auStack_50 [76];
  
  if ((DAT_007b5320 != 0) && (DAT_00784440 != '\0')) {
    if (DAT_007c5eca == '\0') {
      if (DAT_00784577 != '\0') {
        DAT_00784577 = '\0';
        (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0xf,0);
      }
    }
    else if (DAT_00784577 != DAT_007852e8) {
      DAT_00784577 = DAT_007852e8;
      (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0xf,DAT_007852e8);
    }
    DAT_00764330 = DAT_0073ae68;
    if ((*(int **)(DAT_007b5320 + 0x48) != (int *)0x0) && (**(int **)(DAT_007b5320 + 0x48) != 0)) {
      puVar9 = &DAT_00736d50;
      puVar16 = &DAT_00736de0;
      for (iVar10 = 0x10; iVar10 != 0; iVar10 = iVar10 + -1) {
        *puVar16 = *puVar9;
        puVar9 = puVar9 + 1;
        puVar16 = puVar16 + 1;
      }
      FUN_00480830();
      FUN_004804a0();
      iVar10 = FUN_0046bd80(0);
      piVar4 = DAT_007848dc;
      FUN_00431bf0(5,0);
      uStack_90 = 0;
      do {
        uStack_84 = 0;
        if (DAT_007b5398 != 0) {
          piStack_94 = &DAT_007b5370;
          do {
            if ((piStack_94[-10] == uStack_90) && (iVar8 = piStack_94[0x15], iVar8 != 0)) {
              if (*(int *)(*piStack_94 + 4) != 0) {
                FUN_004618a0(1,*(undefined4 *)(*piStack_94 + 0xc));
              }
              uStack_80 = iVar8 * 4;
              uStack_8c = uStack_80;
              if (300 < uStack_80) {
                uStack_8c = 300;
              }
              uStack_98 = 0;
              iVar5 = FUN_00428860(uStack_8c,&DAT_007c2480);
              if (iVar5 == 0) {
                return;
              }
              iVar6 = FUN_004455e0(uStack_90);
              iStack_88 = 0;
              if (0 < iVar8) {
                do {
                  iVar3 = DAT_007c2478;
                  uVar7 = uStack_98 + 4;
                  if (uStack_8c < uVar7) {
                    if ((*(char *)(DAT_007c2478 + 0x34) != '\0') &&
                       (*(char *)(DAT_007c2478 + 0x35) != '\0')) {
                      piVar2 = *(int **)(DAT_007c2478 + 0xc);
                      uVar7 = 0;
                      if (piVar2 != (int *)0x0) {
                        (**(code **)(*piVar2 + 0x30))(piVar2);
                        *(undefined1 *)(iVar3 + 0x35) = 0;
                        uVar7 = extraout_ECX;
                      }
                    }
                    FUN_00428ab0(uVar7,DAT_007c2480,uStack_98,DAT_007c2484,uVar7,
                                 (uStack_98 >> 2) * 6);
                    uStack_8c = uStack_80 - uStack_98;
                    uStack_98 = 0;
                    if (300 < uStack_8c) {
                      uStack_8c = 300;
                    }
                    uStack_80 = uStack_80 - uStack_8c;
                    iVar5 = FUN_00428860(uStack_8c,&DAT_007c2480);
                    if (iVar5 == 0) {
                      return;
                    }
                  }
                  iVar3 = *(int *)(piStack_94[0xb] + iStack_88 * 4);
                  uVar11 = (uint)*(ushort *)(iVar10 + iVar3 * 8);
                  uVar12 = (uint)*(ushort *)(iVar10 + 2 + iVar3 * 8);
                  uVar13 = (uint)*(ushort *)(iVar10 + 4 + iVar3 * 8);
                  uVar7 = (uint)*(ushort *)(iVar10 + 6 + iVar3 * 8);
                  iVar15 = iVar3 * 0x20;
                  if (*(char *)(DAT_007b540c + 0xc + iVar3 * 0x10) == -0x10) {
                    *(undefined4 *)(iVar5 + 0x14 + uStack_98 * 0x1c) =
                         *(undefined4 *)(iVar15 + 0x10 + iVar6);
                    *(undefined4 *)(iVar5 + 0x18 + uStack_98 * 0x1c) =
                         *(undefined4 *)(iVar15 + 0x14 + iVar6);
                    *(undefined4 *)(iVar5 + 0x30 + uStack_98 * 0x1c) =
                         *(undefined4 *)(iVar15 + iVar6);
                    *(undefined4 *)(iVar5 + 0x34 + uStack_98 * 0x1c) =
                         *(undefined4 *)(iVar15 + 4 + iVar6);
                    *(undefined4 *)(iVar5 + 0x4c + uStack_98 * 0x1c) =
                         *(undefined4 *)(iVar15 + 0x18 + iVar6);
                    *(undefined4 *)(iVar5 + 0x50 + uStack_98 * 0x1c) =
                         *(undefined4 *)(iVar15 + 0x1c + iVar6);
                    *(undefined4 *)(iVar5 + 0x68 + uStack_98 * 0x1c) =
                         *(undefined4 *)(iVar15 + 8 + iVar6);
                    uVar1 = *(undefined4 *)(iVar15 + 0xc + iVar6);
                  }
                  else {
                    *(undefined4 *)(iVar5 + 0x14 + uStack_98 * 0x1c) =
                         *(undefined4 *)(iVar15 + iVar6);
                    *(undefined4 *)(iVar5 + 0x18 + uStack_98 * 0x1c) =
                         *(undefined4 *)(iVar15 + 4 + iVar6);
                    *(undefined4 *)(iVar5 + 0x30 + uStack_98 * 0x1c) =
                         *(undefined4 *)(iVar15 + 8 + iVar6);
                    *(undefined4 *)(iVar5 + 0x34 + uStack_98 * 0x1c) =
                         *(undefined4 *)(iVar15 + 0xc + iVar6);
                    *(undefined4 *)(iVar5 + 0x4c + uStack_98 * 0x1c) =
                         *(undefined4 *)(iVar15 + 0x10 + iVar6);
                    *(undefined4 *)(iVar5 + 0x50 + uStack_98 * 0x1c) =
                         *(undefined4 *)(iVar15 + 0x14 + iVar6);
                    *(undefined4 *)(iVar5 + 0x68 + uStack_98 * 0x1c) =
                         *(undefined4 *)(iVar15 + 0x18 + iVar6);
                    uVar1 = *(undefined4 *)(iVar15 + 0x1c + iVar6);
                  }
                  *(undefined4 *)(iVar5 + 0x6c + uStack_98 * 0x1c) = uVar1;
                  uVar14 = (uint)*(byte *)(DAT_007b53f8 + uVar11);
                  *(uint *)(iVar5 + 0x10 + uStack_98 * 0x1c) =
                       ((uVar14 | 0xffffff00) << 8 | uVar14) << 8 | uVar14;
                  uVar14 = (uint)*(byte *)(DAT_007b53f8 + uVar12);
                  *(uint *)(iVar5 + 0x2c + uStack_98 * 0x1c) =
                       ((uVar14 | 0xffffff00) << 8 | uVar14) << 8 | uVar14;
                  uVar14 = (uint)*(byte *)(DAT_007b53f8 + uVar13);
                  *(uint *)(iVar5 + 0x48 + uStack_98 * 0x1c) =
                       ((uVar14 | 0xffffff00) << 8 | uVar14) << 8 | uVar14;
                  uVar14 = (uint)*(byte *)(DAT_007b53f8 + uVar7);
                  *(uint *)(iVar5 + 100 + uStack_98 * 0x1c) =
                       ((uVar14 | 0xffffff00) << 8 | uVar14) << 8 | uVar14;
                  *(undefined4 *)(iVar5 + uStack_98 * 0x1c) =
                       *(undefined4 *)(DAT_007b53ec + uVar11 * 0xc);
                  *(undefined4 *)(iVar5 + 4 + uStack_98 * 0x1c) =
                       *(undefined4 *)(DAT_007b53ec + 4 + uVar11 * 0xc);
                  *(undefined4 *)(iVar5 + 8 + uStack_98 * 0x1c) =
                       *(undefined4 *)(DAT_007b53ec + 8 + uVar11 * 0xc);
                  *(undefined4 *)(iVar5 + 0xc + uStack_98 * 0x1c) = 0x3f800000;
                  *(undefined4 *)(iVar5 + 0x1c + uStack_98 * 0x1c) =
                       *(undefined4 *)(DAT_007b53ec + uVar12 * 0xc);
                  *(undefined4 *)(iVar5 + 0x20 + uStack_98 * 0x1c) =
                       *(undefined4 *)(DAT_007b53ec + 4 + uVar12 * 0xc);
                  *(undefined4 *)(iVar5 + 0x24 + uStack_98 * 0x1c) =
                       *(undefined4 *)(DAT_007b53ec + 8 + uVar12 * 0xc);
                  *(undefined4 *)(iVar5 + 0x28 + uStack_98 * 0x1c) = 0x3f800000;
                  *(undefined4 *)(iVar5 + 0x38 + uStack_98 * 0x1c) =
                       *(undefined4 *)(DAT_007b53ec + uVar13 * 0xc);
                  *(undefined4 *)(iVar5 + 0x3c + uStack_98 * 0x1c) =
                       *(undefined4 *)(DAT_007b53ec + 4 + uVar13 * 0xc);
                  *(undefined4 *)(iVar5 + 0x40 + uStack_98 * 0x1c) =
                       *(undefined4 *)(DAT_007b53ec + 8 + uVar13 * 0xc);
                  *(undefined4 *)(iVar5 + 0x44 + uStack_98 * 0x1c) = 0x3f800000;
                  *(undefined4 *)(iVar5 + 0x54 + uStack_98 * 0x1c) =
                       *(undefined4 *)(DAT_007b53ec + uVar7 * 0xc);
                  uVar11 = uStack_98 + 4;
                  *(undefined4 *)(iVar5 + 0x58 + uStack_98 * 0x1c) =
                       *(undefined4 *)(DAT_007b53ec + 4 + uVar7 * 0xc);
                  uVar1 = *(undefined4 *)(DAT_007b53ec + 8 + uVar7 * 0xc);
                  iStack_88 = iStack_88 + 1;
                  *(undefined4 *)(iVar5 + 0x60 + uStack_98 * 0x1c) = 0x3f800000;
                  *(undefined4 *)(iVar5 + 0x5c + uStack_98 * 0x1c) = uVar1;
                  uStack_98 = uVar11;
                } while (iStack_88 < iVar8);
              }
              iVar8 = DAT_007c2478;
              if (((*(char *)(DAT_007c2478 + 0x34) != '\0') &&
                  (*(char *)(DAT_007c2478 + 0x35) != '\0')) &&
                 (piVar2 = *(int **)(DAT_007c2478 + 0xc), piVar2 != (int *)0x0)) {
                (**(code **)(*piVar2 + 0x30))(piVar2);
                *(undefined1 *)(iVar8 + 0x35) = 0;
              }
              if (uStack_98 != 0) {
                FUN_00428ab0(uStack_98,DAT_007c2480,uStack_98,DAT_007c2484,uStack_98,
                             (uStack_98 >> 2) * 6);
              }
            }
            uStack_84 = uStack_84 + 1;
            piStack_94 = piStack_94 + 1;
          } while (uStack_84 < DAT_007b5398);
        }
        uStack_90 = uStack_90 + 1;
      } while (uStack_90 < 4);
      if (DAT_007850d4 != '\0') {
        (**(code **)(*piVar4 + 0x104))(piVar4,1,0);
        FUN_00431bf0(5,0);
        if (DAT_007844a0 != 3) {
          DAT_007844a0 = 3;
          (**(code **)(*DAT_007848dc + 0x114))(DAT_007848dc,1,1,3);
        }
        if (DAT_007844c0 != 3) {
          DAT_007844c0 = 3;
          (**(code **)(*DAT_007848dc + 0x114))(DAT_007848dc,1,2,3);
        }
      }
      FUN_00447c00(DAT_007c2170,&DAT_007c1e70,9,0);
      FUN_00447c00(DAT_007c2474,&DAT_007c2174,10,0);
      switch(DAT_00784434) {
      case 1:
      case 2:
        if (DAT_007b78dc != 0) {
          FUN_00447250(&DAT_007b6bbc,1,0);
        }
        break;
      case 3:
      case 4:
        if (((DAT_0078443c == '\0') || (DAT_00761cd0 == 0)) || (*(int *)(DAT_00761cd0 + 0x20) != 6))
        {
          FUN_0044bf60();
        }
      }
      if (DAT_007850d4 != '\0') {
        FUN_0044c680();
      }
      FUN_00447c00(DAT_007c1e6c,&DAT_007c0eac,8,0);
      if (DAT_007b8600 != 0) {
        FUN_00447250(&DAT_007b78e0,2,0);
      }
      if ((DAT_0078443c != '\0') &&
         (FUN_00447c00(DAT_007c0184,&DAT_007bf1c4,7,1), DAT_007b6bb8 != 0)) {
        FUN_00447250(&DAT_007b5e98,0,0);
      }
      if (DAT_007ba048 != 0) {
        FUN_00447250(&DAT_007b9328,4,0);
      }
      if (DAT_007bad6c != 0) {
        FUN_00447250(&DAT_007ba04c,5,0);
      }
      if (DAT_007bba90 != 0) {
        FUN_00447250(&DAT_007bad70,6,0);
      }
      if (DAT_007bc7b4 != 0) {
        FUN_00447250(&DAT_007bba94,0xb,0);
      }
      if (DAT_007bd4d8 != 0) {
        FUN_00447250(&DAT_007bc7b8,0xc,0);
      }
      if (DAT_007be1fc != 0) {
        FUN_00447250(&DAT_007bd4dc,0xd,0);
      }
      FUN_004745a0();
      uVar7 = 0;
      if (DAT_007c36a4 != 0) {
        iVar10 = 0;
        uVar11 = DAT_007c36a4;
        do {
          iVar8 = DAT_007c36a0 + iVar10;
          if ((*(int *)(iVar8 + 0x14) != 0) && (*(char *)(iVar8 + 0x24d) != '\0')) {
            FUN_00447250(iVar8,0,*(int *)(iVar8 + 0x14));
            uVar11 = DAT_007c36a4;
          }
          uVar7 = uVar7 + 1;
          iVar10 = iVar10 + 0x2b0;
        } while (uVar7 < uVar11);
      }
      if (DAT_00784574 != '\x01') {
        DAT_00784574 = '\x01';
        (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0xe,1);
      }
      if (((DAT_007c5eca != '\0') && (DAT_007852e4 != 0)) && (uVar7 = 0, DAT_007852e0 != 0)) {
        iVar8 = 0;
        uVar11 = DAT_007852e0;
        iVar10 = DAT_007852e4;
        do {
          if (*(int *)(iVar10 + 4 + iVar8) != 0) {
            FUN_0044f410();
            uVar11 = DAT_007852e0;
            iVar10 = DAT_007852e4;
          }
          uVar7 = uVar7 + 1;
          iVar8 = iVar8 + 0x68;
        } while (uVar7 < uVar11);
      }
      iVar10 = DAT_00736dd0 * 0x10;
      puVar9 = &DAT_00736e20 + iVar10;
      puVar16 = &DAT_00736d90;
      for (iVar8 = 0x10; iVar8 != 0; iVar8 = iVar8 + -1) {
        *puVar16 = *puVar9;
        puVar9 = puVar9 + 1;
        puVar16 = puVar16 + 1;
      }
      DAT_00736dd0 = DAT_00736dd0 + -1;
      uVar18 = FUN_004d4960(&DAT_00736e20 + iVar10);
      puVar9 = (undefined4 *)uVar18;
      puVar16 = &DAT_00736d10;
      for (iVar10 = 0x10; iVar10 != 0; iVar10 = iVar10 + -1) {
        *puVar16 = *puVar9;
        puVar9 = puVar9 + 1;
        puVar16 = puVar16 + 1;
      }
      puVar9 = &DAT_00736de0;
      puVar16 = (undefined4 *)((ulonglong)uVar18 >> 0x20);
      for (iVar10 = 0x10; iVar10 != 0; iVar10 = iVar10 + -1) {
        *puVar16 = *puVar9;
        puVar9 = puVar9 + 1;
        puVar16 = puVar16 + 1;
      }
      puVar9 = (undefined4 *)FUN_00435620(auStack_50,&DAT_00736d90);
      bVar17 = DAT_00784577 != '\x01';
      puVar16 = &DAT_00736d10;
      for (iVar10 = 0x10; iVar10 != 0; iVar10 = iVar10 + -1) {
        *puVar16 = *puVar9;
        puVar9 = puVar9 + 1;
        puVar16 = puVar16 + 1;
      }
      if (bVar17) {
        DAT_00784577 = '\x01';
        (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0xf,1);
      }
      if (DAT_00784570 != 1) {
        DAT_00784570 = 1;
        (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x13,5);
        (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x14,6);
      }
      FUN_00431490();
    }
  }
  return;
}


```

