# Selected Nova1492 Decompilation

## `0047f150`

- Function: `FUN_0047f150`
- Entry: `0047f150`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_0047f150(void)

{
  float fVar1;
  int iVar2;
  float10 fVar3;
  float10 fVar4;
  float10 fVar5;
  float10 fVar6;
  float10 fVar7;
  
  fVar3 = (float10)FUN_00641ed0();
  iVar2 = DAT_007c3890;
  fVar1 = (float)fVar3;
  DAT_007c388c = (DAT_007c388c - *(float *)(&PTR_DAT_00736ce0)[DAT_007c3890 * 5]) * fVar1 +
                 *(float *)(&PTR_DAT_00736ce0)[DAT_007c3890 * 5];
  FUN_006562da();
  fVar3 = (float10)FUN_006562da();
  _DAT_007c3870 = (float)(fVar3 - (float10)DAT_006dac00);
  DAT_007c3874 = (DAT_007c3874 - (float)(&DAT_00736cdc)[iVar2 * 5]) * fVar1 +
                 (float)(&DAT_00736cdc)[iVar2 * 5];
  DAT_007388ac = (DAT_007388ac - DAT_007c5e78) * fVar1 + DAT_007c5e78;
  fVar3 = (float10)fsin((float10)DAT_007c3874);
  fVar7 = (float10)fpatan((float10)DAT_007388ac * (float10)DAT_006da974,(float10)1);
  DAT_007c387c = DAT_007c3884 + (DAT_007c387c - DAT_007c3884) * fVar1;
  _DAT_007388b0 = (float)fVar7;
  fVar4 = (float10)fptan((float10)_DAT_006da928);
  fVar4 = (fVar4 / fVar7) * (float10)DAT_007c388c;
  DAT_007c3878 = (DAT_007c3878 - DAT_007c3880) * fVar1 + DAT_007c3880;
  DAT_00738870 = DAT_007c3878;
  DAT_00738874 = _DAT_006dafe0;
  DAT_00738878 = DAT_007c387c;
  DAT_0073887c = _UNK_006dafe4;
  DAT_007388b8 = (float)(fVar4 + fVar4);
  DAT_00738890 = DAT_008b22f0;
  DAT_00738894 = DAT_008b22f4;
  DAT_00738898 = DAT_008b22f8;
  _DAT_0073889c = DAT_008b22fc;
  fVar7 = (float10)fcos((float10)_DAT_007c3870);
  fVar5 = (float10)fcos((float10)DAT_007c3874);
  fVar6 = (float10)fsin((float10)_DAT_007c3870);
  fVar1 = (float)fVar4;
  DAT_00738880 = (float)(fVar6 * fVar3) * fVar1 + DAT_007c3878;
  DAT_00738884 = (float)fVar5 * fVar1 + _DAT_006dafe0;
  DAT_00738888 = (float)(fVar7 * fVar3) * fVar1 + DAT_007c387c;
  DAT_0073888c = fVar1 * 0.0 + _UNK_006dafe4;
  return;
}


```

## `0047f9c0`

- Function: `FUN_0047f990`
- Entry: `0047f990`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_0047f990(void)

{
  float10 fVar1;
  float10 fVar2;
  
  DAT_007c388c = *(float *)(&PTR_DAT_00736ce0)[DAT_007c3890 * 5];
  _DAT_007c3870 = (&DAT_00736cd8)[DAT_007c3890 * 5];
  DAT_007c3874 = (&DAT_00736cdc)[DAT_007c3890 * 5];
  fVar2 = (float10)fpatan((float10)DAT_007c5e78 * (float10)DAT_006da974,(float10)1);
  DAT_007c3878 = DAT_007c3880;
  DAT_007c387c = DAT_007c3884;
  DAT_007388ac = DAT_007c5e78;
  _DAT_007388b0 = (float)fVar2;
  fVar1 = (float10)fptan((float10)_DAT_006da928);
  fVar1 = (fVar1 / fVar2) * (float10)DAT_007c388c;
  DAT_007388b8 = (float)(fVar1 + fVar1);
  FUN_0047f150();
  return;
}


```

## `00594d40`

- Function: `FUN_00594880`
- Entry: `00594880`

```c

/* WARNING: Removing unreachable block (ram,0x005949ff) */
/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void __thiscall FUN_00594880(float param_1)

{
  uint uVar1;
  uint uVar2;
  undefined4 *puVar3;
  int iVar4;
  int iVar5;
  undefined4 *puVar6;
  float10 fVar7;
  float fVar8;
  float fVar9;
  uint in_stack_00000014;
  int in_stack_00000018;
  undefined4 in_stack_0000001c;
  float in_stack_00000020;
  undefined4 in_stack_00000024;
  undefined4 uVar10;
  undefined4 uVar11;
  undefined1 auStack_108 [8];
  float local_100;
  float local_fc;
  undefined4 local_f8;
  int local_f4;
  undefined4 local_f0 [4];
  undefined4 local_e0;
  undefined4 local_dc;
  undefined4 local_d8;
  undefined4 local_d4;
  undefined4 local_d0;
  undefined4 local_cc;
  undefined4 local_c8;
  undefined4 local_c4;
  undefined4 local_c0;
  undefined4 local_bc;
  undefined4 local_b8;
  undefined4 local_b4;
  undefined4 local_64;
  undefined4 local_60 [5];
  undefined4 local_4c;
  undefined4 local_44;
  undefined4 local_38;
  uint local_14;
  
  local_14 = DAT_007360c8 ^ (uint)auStack_108;
  local_f8 = in_stack_00000024;
  local_f4 = in_stack_00000018;
  local_fc = param_1;
  if (3 < in_stack_00000014) goto LAB_00594e71;
  if ((int)in_stack_00000014 < 3) {
    FUN_00480960(_DAT_006daf30,_DAT_006daad0,_DAT_006daf24,_DAT_006dab90,DAT_006daf4c,DAT_006dac78);
LAB_00594902:
    if (in_stack_00000014 == 0) {
      iVar4 = 0;
    }
    else if (in_stack_00000014 == 1) {
      iVar4 = 0x3c;
    }
    else {
      iVar4 = 0x46;
      if (in_stack_00000014 != 2) goto LAB_00594968;
    }
  }
  else {
    if (in_stack_00000014 != 3) goto LAB_00594902;
    FUN_00480960(_DAT_006daf38,DAT_006daba0,_DAT_006daf28,_DAT_006dac48,DAT_006daf4c,DAT_006dac78);
LAB_00594968:
    iVar4 = 0x32;
  }
  if (DAT_00784580 != '\0') {
    FUN_00431bf0(1,0);
    DAT_00784580 = '\0';
    _DAT_00784574 = 0x101;
  }
  DAT_007c3918 = 0x46;
  DAT_007c391c = 0x1c2 - iVar4;
  DAT_007c3920 = 200;
  DAT_007c3924 = 200;
  FUN_004800e0();
  if (in_stack_00000018 != 0) {
    local_64 = 0xff8264f0;
    uVar1 = FUN_004800a0();
    local_100 = (float)(uVar1 % 1000) * DAT_006da884;
    local_100 = local_100 - (float)(int)local_100;
    if (local_100 < 0.0) {
      local_100 = local_100 + DAT_006daa00;
    }
    if (DAT_006da974 <= local_100) {
      local_100 = DAT_006dab58 - local_100 * DAT_006dab58;
    }
    else {
      local_100 = local_100 * DAT_006dab58;
    }
    DAT_00736dd0 = DAT_00736dd0 + 1;
    puVar3 = &DAT_00736d90;
    puVar6 = &DAT_00736e20 + DAT_00736dd0 * 0x10;
    for (iVar4 = 0x10; iVar4 != 0; iVar4 = iVar4 + -1) {
      *puVar6 = *puVar3;
      puVar3 = puVar3 + 1;
      puVar6 = puVar6 + 1;
    }
    FUN_004808b0(local_f8);
    uVar1 = local_64;
    uVar2 = local_64 >> 0x10;
    local_64 = CONCAT13(200,(uint3)(byte)(int)((float)(uVar2 & 0xff) * local_100) << 0x10);
    local_64 = CONCAT31(CONCAT21(local_64._2_2_,(char)(int)((float)(uVar1 >> 8 & 0xff) * local_100))
                        ,(char)(int)((float)(uVar1 & 0xff) * local_100));
    FUN_004541e0(0x80100000,0,local_64,0x3f800000);
    local_64 = 0xc8323296;
    FUN_004541e0(0x80100000,1,0xc8323296,DAT_006daa24);
    if (DAT_006da974 < in_stack_00000020) {
      if (*(char *)((int)local_fc + 0x5f1) == '\0') {
        local_64 = 0x64323232;
        puVar3 = (undefined4 *)FUN_004d50d0(0x64323232,local_100);
        fVar9 = 1.0;
        uVar11 = *puVar3;
        uVar10 = 2;
      }
      else {
        fVar9 = (in_stack_00000020 - DAT_006da974) * DAT_006dac70;
        local_fc = fVar9;
        if ((fVar9 <= _DAT_006da830) || (DAT_006daa00 <= fVar9)) goto LAB_00594c31;
        local_64 = 0x64503c32;
        fVar8 = DAT_006daa00;
        puVar3 = (undefined4 *)FUN_004d50d0(0x64503c32,fVar9);
        fVar9 = fVar9 + fVar8;
        uVar11 = *puVar3;
        uVar10 = 1;
      }
      FUN_004541e0(0x80100000,uVar10,uVar11,fVar9);
    }
LAB_00594c31:
    iVar4 = DAT_00736dd0 * 0x10;
    puVar3 = &DAT_00736e20 + iVar4;
    puVar6 = &DAT_00736d90;
    for (iVar5 = 0x10; iVar5 != 0; iVar5 = iVar5 + -1) {
      *puVar6 = *puVar3;
      puVar3 = puVar3 + 1;
      puVar6 = puVar6 + 1;
    }
    DAT_00736dd0 = DAT_00736dd0 + -1;
    puVar3 = (undefined4 *)FUN_004d4960(&DAT_00736e20 + iVar4);
    iVar4 = DAT_007644c0;
    local_100 = (float)DAT_007644c0;
    puVar6 = &DAT_00736d10;
    for (iVar5 = 0x10; iVar5 != 0; iVar5 = iVar5 + -1) {
      *puVar6 = *puVar3;
      puVar3 = puVar3 + 1;
      puVar6 = puVar6 + 1;
    }
    if (iVar4 == 0) {
      FUN_00431920(0x25,0);
      local_100 = (float)DAT_007644c0;
      if (DAT_007644c0 == 0) goto LAB_00594e42;
    }
    local_f0[0] = DAT_008b22e0;
    local_f0[1] = DAT_008b22e4;
    local_f0[2] = DAT_008b22e8;
    local_f0[3] = DAT_008b22ec;
    local_e0 = DAT_008b22f0;
    local_dc = DAT_008b22f4;
    local_d8 = DAT_008b22f8;
    local_d4 = DAT_008b22fc;
    local_d0 = DAT_008b2300;
    local_cc = DAT_008b2304;
    local_c8 = DAT_008b2308;
    local_c4 = DAT_008b230c;
    local_c0 = DAT_008b2310;
    local_bc = DAT_008b2314;
    local_b8 = DAT_008b2318;
    local_b4 = DAT_008b231c;
    puVar3 = local_f0;
    puVar6 = local_60;
    for (iVar4 = 0x10; iVar4 != 0; iVar4 = iVar4 + -1) {
      *puVar6 = *puVar3;
      puVar3 = puVar3 + 1;
      puVar6 = puVar6 + 1;
    }
    local_60[0] = 0x3f333333;
    local_4c = 0x3f333333;
    local_38 = 0x3f333333;
    local_44 = 0xbf000000;
    FUN_004808b0(local_60);
    fVar7 = (float10)fpatan((float10)_DAT_006da928,(float10)1);
    DAT_007388ac = 0x3f060a92;
    DAT_007388b8 = 0x43c80000;
    DAT_00738880 = _DAT_006db300;
    DAT_00738884 = _UNK_006db304;
    DAT_00738888 = _UNK_006db308;
    DAT_0073888c = _UNK_006db30c;
    _DAT_007388b0 = (float)fVar7;
    DAT_00738870 = _DAT_006db240;
    DAT_00738874 = _UNK_006db244;
    DAT_00738878 = _UNK_006db248;
    DAT_0073887c = _UNK_006db24c;
    uVar11 = 0x594dbb;
    FUN_00480b30();
    FUN_00455420(in_stack_0000001c,uVar11);
    if (DAT_006da920 <= in_stack_00000020) {
      fVar9 = DAT_006dae64;
      if (DAT_006da9d4 <= in_stack_00000020) {
        fVar9 = (DAT_006daa00 - in_stack_00000020) * DAT_006dae64 * DAT_006dac78;
      }
    }
    else {
      fVar9 = in_stack_00000020 * DAT_006dae64 * DAT_006dac78;
    }
    FUN_004541e0(0,1,(int)fVar9 & 0xff,0x3f800000);
  }
LAB_00594e42:
  DAT_007c3920 = *(undefined4 *)(DAT_00762478 + 0x10);
  DAT_007c3924 = *(undefined4 *)(DAT_00762478 + 0x14);
  DAT_007c3918 = 0;
  DAT_007c391c = 0;
  FUN_004800e0();
LAB_00594e71:
  __security_check_cookie(local_14 ^ (uint)auStack_108);
  return;
}


```

