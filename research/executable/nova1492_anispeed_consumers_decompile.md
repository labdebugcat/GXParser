# Selected Nova1492 Decompilation

## `0045b790`

- Function: `FUN_0045b6c0`
- Entry: `0045b6c0`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void __thiscall FUN_0045b6c0(int *param_1,uint param_2,int param_3,undefined *param_4,float param_5)

{
  undefined *puVar1;
  undefined1 *puVar2;
  uint uVar3;
  int iVar4;
  int iVar5;
  float fVar6;
  int *piVar7;
  undefined4 uVar8;
  undefined4 extraout_ECX;
  undefined4 extraout_ECX_00;
  undefined4 *puVar9;
  undefined4 extraout_ECX_01;
  undefined4 extraout_ECX_02;
  undefined4 extraout_ECX_03;
  undefined4 extraout_ECX_04;
  undefined4 extraout_ECX_05;
  float10 fVar10;
  unkbyte10 Var11;
  float10 fVar12;
  float10 extraout_ST1;
  undefined4 in_stack_fffffa50;
  undefined4 in_stack_fffffa54;
  undefined4 uVar13;
  float fVar14;
  float fVar15;
  undefined4 uVar16;
  undefined4 uVar17;
  undefined4 uVar18;
  undefined4 uVar19;
  undefined1 local_580 [16];
  undefined4 local_570;
  undefined4 local_56c;
  undefined1 local_530 [16];
  undefined4 local_520;
  undefined4 local_51c;
  undefined4 local_4fc;
  undefined4 local_4f0;
  undefined4 uStack_4ec;
  undefined4 uStack_4e8;
  undefined4 uStack_4e4;
  undefined4 local_4e0;
  undefined4 uStack_4dc;
  undefined4 uStack_4d8;
  undefined4 uStack_4d4;
  undefined4 local_4d0;
  undefined4 uStack_4cc;
  undefined4 uStack_4c8;
  undefined4 uStack_4c4;
  undefined4 local_4c0;
  undefined4 uStack_4bc;
  undefined4 uStack_4b8;
  undefined4 uStack_4b4;
  undefined4 local_4b0;
  undefined4 uStack_4ac;
  undefined4 uStack_4a8;
  undefined4 uStack_4a4;
  undefined4 local_4a0;
  undefined4 uStack_49c;
  undefined4 uStack_498;
  undefined4 uStack_494;
  undefined4 local_490;
  undefined4 uStack_48c;
  undefined4 uStack_488;
  undefined4 uStack_484;
  undefined4 local_480;
  undefined4 uStack_47c;
  undefined4 uStack_478;
  undefined4 uStack_474;
  undefined4 local_470;
  undefined4 uStack_46c;
  undefined4 uStack_468;
  undefined4 uStack_464;
  undefined4 local_460;
  undefined4 uStack_45c;
  undefined4 uStack_458;
  undefined4 uStack_454;
  undefined4 local_450;
  undefined4 uStack_44c;
  undefined4 uStack_448;
  undefined4 uStack_444;
  undefined4 local_440;
  undefined4 uStack_43c;
  undefined4 uStack_438;
  undefined4 uStack_434;
  undefined4 local_430;
  undefined4 uStack_42c;
  undefined4 uStack_428;
  undefined4 uStack_424;
  undefined4 local_418;
  float local_414;
  undefined4 local_410;
  undefined4 local_40c;
  undefined4 local_408;
  undefined4 local_404;
  undefined4 local_3fc;
  float local_3e4;
  undefined4 local_3d8;
  float local_3d4;
  undefined4 local_3d0;
  undefined4 local_3cc;
  undefined4 local_3c8;
  undefined4 local_3c4;
  undefined4 local_3bc;
  float local_3a4;
  undefined1 local_398 [12];
  undefined4 local_38c;
  undefined4 local_388;
  undefined4 local_384;
  undefined4 local_37c;
  undefined4 local_364;
  float local_358;
  float local_354;
  float local_350;
  undefined4 local_34c;
  undefined4 local_348;
  undefined4 local_344;
  undefined4 local_340;
  undefined4 local_33c;
  undefined4 local_334;
  undefined4 local_324;
  undefined4 local_318;
  float local_314;
  undefined4 local_310;
  undefined4 local_308;
  undefined4 local_304;
  undefined4 local_300;
  undefined4 local_2fc;
  undefined4 local_2f4;
  undefined4 local_2e8;
  float local_2e4;
  undefined4 local_2e0;
  undefined4 local_2dc;
  undefined4 local_2d8;
  float local_2d4;
  undefined4 local_2d0;
  undefined4 local_2cc;
  undefined4 local_2c8;
  undefined4 local_2c4;
  undefined4 local_2c0;
  undefined4 local_2bc;
  undefined4 local_2b4;
  undefined4 local_2a8;
  float local_2a4;
  undefined4 local_2a0;
  undefined4 local_29c;
  undefined4 local_298;
  float local_294;
  undefined4 local_290;
  undefined4 local_28c;
  undefined4 local_288;
  undefined4 local_284;
  undefined4 local_280;
  undefined4 local_27c;
  undefined4 local_274;
  undefined4 local_268;
  float local_264;
  undefined4 local_260;
  undefined4 local_25c;
  undefined4 local_258;
  float local_254;
  undefined4 local_250;
  undefined4 local_24c;
  undefined4 local_248;
  undefined4 local_244;
  undefined4 local_240;
  undefined4 local_23c;
  undefined4 local_234;
  undefined4 local_228;
  float local_224;
  undefined4 local_220;
  undefined4 local_21c;
  undefined4 local_218;
  undefined4 local_214;
  undefined4 local_210;
  undefined4 local_20c;
  undefined4 local_208;
  undefined4 local_204;
  undefined4 local_200;
  undefined4 local_1fc;
  undefined4 local_1f8;
  undefined4 local_1f4;
  undefined4 local_1f0;
  undefined4 local_1ec;
  undefined4 local_1e8;
  undefined4 local_1e4;
  undefined4 local_1e0;
  undefined4 local_1dc;
  undefined4 local_1d8;
  undefined4 local_1d4;
  undefined4 local_1d0;
  undefined4 local_1cc;
  undefined4 local_1c8;
  undefined4 local_1c4;
  undefined4 local_1c0;
  undefined4 local_1bc;
  undefined4 local_1b8;
  undefined4 local_1b4;
  undefined4 local_1b0;
  undefined4 local_1ac;
  undefined4 local_1a8;
  undefined4 local_1a4;
  undefined4 local_1a0;
  undefined4 local_19c;
  undefined4 local_198;
  undefined4 local_194;
  undefined4 local_190;
  undefined4 local_18c;
  undefined4 local_188;
  undefined4 local_184;
  undefined4 local_180;
  undefined4 local_17c;
  undefined4 local_178;
  undefined4 local_174;
  int local_170;
  float local_16c;
  int local_168;
  int local_164;
  int local_160;
  float local_15c;
  int local_158;
  int local_154;
  int local_150;
  float local_14c;
  int local_148;
  int local_144;
  undefined4 local_138;
  float local_134;
  undefined4 local_130;
  float local_12c;
  undefined4 local_128;
  float local_124;
  undefined4 local_120;
  float local_11c;
  undefined4 local_118;
  undefined4 local_114;
  float local_110;
  undefined4 local_10c;
  undefined4 local_108;
  float local_104;
  undefined4 local_100;
  float local_fc;
  undefined4 local_f8;
  float local_f4;
  float local_f0;
  float local_ec;
  float local_e8;
  undefined4 local_e4;
  float local_e0;
  undefined4 local_dc;
  undefined4 local_d8;
  float local_d4;
  undefined4 local_d0;
  undefined4 local_cc;
  undefined4 local_c8;
  undefined4 local_c4;
  undefined4 local_c0;
  undefined4 local_bc;
  undefined4 local_b8;
  undefined4 local_b4;
  undefined4 local_b0;
  undefined4 local_ac;
  undefined4 local_a8;
  undefined4 local_a4;
  undefined4 local_a0;
  undefined4 local_9c;
  undefined4 local_98;
  undefined4 local_94;
  undefined4 local_90;
  undefined4 local_8c;
  undefined4 local_88;
  int *local_84;
  uint local_80;
  float local_7c;
  undefined *local_78;
  int local_74;
  int *local_70;
  float local_6c;
  int *local_68;
  int *local_64;
  float local_60;
  float fStack_5c;
  float fStack_58;
  undefined4 uStack_54;
  float local_50;
  float fStack_4c;
  float fStack_48;
  undefined4 uStack_44;
  undefined1 local_40 [28];
  uint local_24;
  undefined1 *puStack_20;
  void *local_1c;
  undefined1 *puStack_18;
  undefined4 local_14;
  
  puStack_20 = &stack0xfffffffc;
  local_14 = 0xffffffff;
  puStack_18 = &LAB_0065fd3d;
  local_1c = ExceptionList;
  uVar3 = DAT_007360c8 ^ (uint)&stack0xfffffff0;
  ExceptionList = &local_1c;
  local_74 = param_3;
  local_78 = param_4;
  local_80 = param_2;
  local_6c = param_5;
  local_84 = param_1;
  local_24 = uVar3;
  puVar2 = &stack0xfffffffc;
  if (0x707 < param_2) goto LAB_0045d1b8;
  if (param_2 < 0x2b5) {
    iVar4 = (&DAT_0076442c)[param_2];
    puVar2 = &stack0xfffffffc;
    if (iVar4 == 0) {
      FUN_00431920(param_2,0);
      iVar4 = (&DAT_0076442c)[param_2];
      puVar2 = puStack_20;
    }
  }
  else {
    iVar4 = 0;
    puVar2 = &stack0xfffffffc;
  }
  puStack_20 = puVar2;
  uVar13 = 0x45b76a;
  iVar5 = (**(code **)(*param_1 + 0x10))(iVar4,local_74,local_78,local_6c,uVar3);
  puVar2 = puStack_20;
  if (iVar5 == 0) goto LAB_0045d1b8;
  local_74 = 0;
  if (param_2 < 0x2b5) {
    local_78 = &DAT_0076604c + param_2 * 0x44;
    if ((local_78 != (undefined *)0x0) &&
       (local_74 = (&DAT_00766060)[param_2 * 0x11], local_74 != 0)) {
      param_1[0x23] = *(int *)(local_74 + 8);
    }
  }
  else {
    local_78 = (undefined *)0x0;
  }
  uVar16 = extraout_ECX;
  if (DAT_0078443c == '\0') goto LAB_0045d172;
  if (0x134 < param_2) goto switchD_0045b7e8_caseD_7;
  if (param_2 == 0x134) {
    uVar13 = 0x10;
    local_68 = (int *)FUN_00640b15(0x5f0,0x10);
    local_14 = 0;
    local_64 = local_68;
    if (local_68 == (int *)0x0) goto LAB_0045cef7;
    iVar4 = FUN_00438b10(param_1[0x25],5,0x1e,0x1e,0x3f800000,DAT_006da9bc,DAT_006da9d4,uVar13);
    goto LAB_0045cef9;
  }
  switch(param_2) {
  case 5:
    FUN_004446a0();
    fVar10 = (float10)FUN_00471060(DAT_006dac84,_DAT_006dacbc);
    local_314 = (float)fVar10;
    local_138 = 0;
    local_318 = 0;
    local_130 = 0;
    local_310 = 0;
    local_308 = 0x3f800000;
    local_2fc = 0x3f333333;
    local_300 = 0x40000000;
    local_2e8 = 0;
    local_2e0 = 0;
    local_2f4 = 0x3f800000;
    local_134 = local_314;
    fVar10 = (float10)FUN_00471060(_DAT_006daf60,DAT_006dad1c);
    local_2e4 = (float)fVar10;
    local_304 = 0x3cf5c28f;
    local_2dc = 1;
    local_64 = (int *)FUN_00640b15(0xc0,0x10);
    local_14 = 0x17;
    if (local_64 != (int *)0x0) {
      piVar7 = param_1 + 4;
      puVar9 = &local_318;
      goto LAB_0045c26a;
    }
LAB_0045c28d:
    iVar4 = 0;
    _DAT_00000004 = 0xffffffff;
    local_68 = local_64;
    goto LAB_0045cf03;
  case 6:
  case 0x13:
    uVar16 = 0xa0;
    local_194 = 0x3dcccccd;
    local_190 = 0;
    local_18c = 0;
    local_188 = 0xbdcccccd;
    local_184 = 0;
    local_180 = 0;
    uVar13 = 0x45b837;
    local_68 = (int *)FUN_00640b15(0xa0,0x10);
    local_14 = 1;
    local_64 = local_68;
    if (local_68 == (int *)0x0) {
LAB_0045cef7:
      iVar4 = 0;
      local_68 = local_64;
    }
    else {
      local_90 = 0;
      local_8c = 0;
      local_88 = 0;
      local_4c0 = _DAT_006db240;
      uStack_4bc = _UNK_006db244;
      uStack_4b8 = _UNK_006db248;
      uStack_4b4 = _UNK_006db24c;
      iVar4 = FUN_0043a820(DAT_007c4e64,&local_194,2,DAT_006da9d4,DAT_006da9bc,&local_4c0,10,
                           0x3f800000,0x3f800000,0,0,0,uVar13,uVar16,1);
    }
    break;
  default:
    goto switchD_0045b7e8_caseD_7;
  case 0x16:
    uVar13 = 0x10;
    local_68 = (int *)FUN_00640b15(0x5f0,0x10);
    local_14 = 3;
    local_64 = local_68;
    if (local_68 == (int *)0x0) goto LAB_0045cef7;
    iVar4 = FUN_00438b10(param_1[0x25],8,0,0,_DAT_006da9fc,0x3f800000,DAT_006da9d4,uVar13);
    break;
  case 0x17:
  case 0x75:
    FUN_004446a0();
    local_570 = 0x3f000000;
    local_56c = 0x3c23d70a;
    local_68 = (int *)FUN_00640b15(0xc0,0x10);
    local_14 = 5;
    local_64 = local_68;
    if (local_68 == (int *)0x0) goto LAB_0045cef7;
    local_490 = 0;
    uStack_48c = 0;
    uStack_488 = 0;
    uStack_484 = 0;
    iVar4 = FUN_00435f50(DAT_007c5df4,8,local_580,&local_490,0,0);
    break;
  case 0x18:
    uVar16 = 0xa0;
    local_1ac = 0x3dcccccd;
    local_1a8 = 0;
    local_1a4 = 0;
    local_1a0 = 0xbdcccccd;
    local_19c = 0;
    local_198 = 0;
    uVar13 = 0x45bbcb;
    local_68 = (int *)FUN_00640b15(0xa0,0x10);
    local_14 = 7;
    local_64 = local_68;
    if (local_68 == (int *)0x0) goto LAB_0045cef7;
    local_a8 = 0;
    local_a4 = 0;
    local_a0 = 0;
    local_440 = _DAT_006db240;
    uStack_43c = _UNK_006db244;
    uStack_438 = _UNK_006db248;
    uStack_434 = _UNK_006db24c;
    iVar4 = FUN_0043a820(DAT_007c4e70,&local_1ac,2,DAT_006da9ec,DAT_006da9bc,&local_440,10,
                         DAT_006da974,0x3f800000,0,0,0,uVar13,uVar16,1);
    break;
  case 0x1e:
    uVar13 = 0x10;
    local_68 = (int *)FUN_00640b15(0x5f0,0x10);
    local_14 = 4;
    local_64 = local_68;
    if (local_68 == (int *)0x0) goto LAB_0045cef7;
    iVar4 = FUN_00438b10(param_1[0x25],2,10,0,0x3f800000,0x3f800000,0x3f800000,uVar13);
    break;
  case 0x1f:
    uVar16 = 0xa0;
    local_1f4 = 0x3dcccccd;
    local_1f0 = 0;
    local_1ec = 0;
    local_1e8 = 0xbdcccccd;
    local_1e4 = 0;
    local_1e0 = 0;
    uVar13 = 0x45bebb;
    local_68 = (int *)FUN_00640b15(0xa0,0x10);
    local_14 = 10;
    local_64 = local_68;
    if (local_68 == (int *)0x0) {
LAB_0045bd6c:
      uVar13 = 0;
      local_68 = local_64;
    }
    else {
      local_cc = 0;
      local_c8 = 0;
      local_c4 = 0;
      local_470 = _DAT_006db240;
      uStack_46c = _UNK_006db244;
      uStack_468 = _UNK_006db248;
      uStack_464 = _UNK_006db24c;
      uVar13 = FUN_0043a820(DAT_007c4e74,&local_1f4,2,DAT_006da9d4,DAT_006da9bc,&local_470,10,
                            DAT_006da974,0x3f800000,0,0,0,uVar13,uVar16,1);
    }
    goto LAB_0045bd6e;
  case 0x2a:
  case 0x2b:
  case 0x33:
    local_150 = param_1[4];
    local_68 = param_1 + 4;
    local_148 = param_1[6];
    local_14c = (float)param_1[5] + DAT_006daa00;
    local_144 = param_1[7];
    uVar3 = FUN_00635d42();
    uVar3 = uVar3 & 0x80000001;
    if ((int)uVar3 < 0) {
      uVar3 = (uVar3 - 1 | 0xfffffffe) + 1;
    }
    piVar7 = (int *)(uVar3 + 1);
    local_64 = piVar7;
    if (0 < (int)piVar7) {
      do {
        fVar10 = (float10)FUN_00471060(_DAT_006daf48,DAT_006dac70);
        local_7c = (float)fVar10;
        fVar10 = (float10)FUN_00471060(DAT_006dabf0,DAT_006dac84);
        local_70 = (int *)(float)fVar10;
        fVar10 = (float10)FUN_00471060(_DAT_006daf48,DAT_006dac70);
        fStack_58 = (float)fVar10;
        local_64 = (int *)local_7c;
        uVar17 = 0x50;
        local_60 = local_7c;
        fStack_5c = (float)local_70;
        uStack_54 = 0;
        uVar16 = 0x45c3a7;
        local_70 = (int *)FUN_00640b15(0x50,0x10);
        local_14 = 0xe;
        local_64 = local_70;
        if (local_70 == (int *)0x0) {
          iVar5 = 0;
        }
        else {
          local_6c = DAT_00764454;
          if (DAT_00764454 == 0.0) {
            uVar17 = 10;
            uVar16 = 0x45c3d6;
            FUN_00431920(10,0);
          }
          uVar18 = 0x3f800000;
          local_6c = DAT_00764454;
          fVar10 = (float10)FUN_00471060(DAT_006da974,DAT_006daa24);
          iVar5 = FUN_00439630(local_6c,local_68,&local_60,(float)fVar10,in_stack_fffffa50,
                               in_stack_fffffa54,uVar13,iVar4,uVar16,uVar17,uVar18);
        }
        local_14 = 0xffffffff;
        *(undefined4 *)(iVar5 + 4) = 0xffffffff;
        FUN_00438760(iVar5,300);
        piVar7 = (int *)((int)piVar7 + -1);
        param_1 = local_84;
      } while (piVar7 != (int *)0x0);
    }
    FUN_004446a0();
    fVar10 = (float10)FUN_00471060(DAT_006dacc8,DAT_006dacf0);
    local_294 = (float)fVar10;
    local_e4 = 0;
    local_298 = 0;
    local_dc = 0;
    local_290 = 0;
    local_288 = 0x3fc00000;
    local_27c = 0x3f333333;
    local_280 = 0x40000000;
    local_268 = 0;
    local_260 = 0;
    local_274 = 0x3f800000;
    local_e0 = local_294;
    fVar10 = (float10)FUN_00471060(_DAT_006daf60,DAT_006dad1c);
    local_264 = (float)fVar10;
    local_28c = 0x3fc00000;
    local_284 = 0x3ba3d70a;
    local_25c = 1;
    local_68 = (int *)FUN_00640b15(0xc0,0x10);
    local_14 = 0xf;
    local_64 = local_68;
    if (local_68 == (int *)0x0) {
      iVar4 = 0;
    }
    else {
      iVar4 = FUN_00435f50(DAT_007c5e04,0x10,&local_298,&local_150,0,DAT_006da974);
    }
    local_14 = 0xffffffff;
    *(undefined4 *)(iVar4 + 4) = 0xffffffff;
    FUN_00438760(iVar4,100);
    iVar4 = FUN_00635d42();
    iVar4 = iVar4 % 3 + 4;
    if (0 < iVar4) {
      do {
        FUN_004446a0();
        local_344 = 0x3e99999a;
        fVar10 = (float10)FUN_00471060(_DAT_006daf48,DAT_006dac70);
        local_68 = (int *)(float)fVar10;
        fVar10 = (float10)FUN_00471060(DAT_006dac78,DAT_006dacb8);
        local_64 = (int *)(float)fVar10;
        fVar10 = (float10)FUN_00471060(_DAT_006daf48,DAT_006dac70);
        local_f0 = (float)local_68;
        local_ec = (float)local_64;
        local_358 = (float)local_68;
        local_354 = (float)local_64;
        local_350 = (float)fVar10;
        local_348 = 0x40400000;
        local_33c = 0x3d4ccccd;
        local_340 = 0x3e99999a;
        local_34c = 0x3fc00000;
        local_324 = 0x3f800000;
        local_334 = 0x3dcccccd;
        local_e8 = local_350;
        local_68 = (int *)FUN_00640b15(0xc0,0x10);
        local_14 = 0x10;
        local_64 = local_68;
        if (local_68 == (int *)0x0) {
          iVar5 = 0;
        }
        else {
          iVar5 = FUN_00435f50(DAT_007c5e14,0x10,&local_358,&local_150,0,0x3f800000);
        }
        local_14 = 0xffffffff;
        *(undefined4 *)(iVar5 + 4) = 0xffffffff;
        FUN_00438760(iVar5,700);
        iVar4 = iVar4 + -1;
      } while (iVar4 != 0);
    }
    Var11 = FUN_00471060(0,_DAT_006dac90);
    local_f8 = 0;
    fVar10 = (float10)fsin(Var11);
    fVar12 = (float10)fcos(Var11);
    local_fc = (float)fVar12;
    local_f4 = (float)fVar10;
    local_68 = (int *)FUN_00640b15(0x30,0x10);
    local_14 = 0x11;
    local_64 = local_68;
    if (local_68 == (int *)0x0) {
      iVar4 = 0;
    }
    else {
      iVar4 = FUN_00635d42();
      iVar4 = iVar4 % 5000 + 20000;
      fVar10 = (float10)FUN_00471060(DAT_006dab58,DAT_006dac70);
      iVar4 = FUN_00442f20(param_1 + 4,local_fc,local_f8,local_f4,(float)fVar10,iVar4);
    }
    local_14 = 0xffffffff;
    *(undefined4 *)(iVar4 + 4) = 0xffffffff;
    FUN_00438760(iVar4,300);
    local_4a0 = _DAT_006dafc0;
    uStack_49c = _UNK_006dafc4;
    uStack_498 = _UNK_006dafc8;
    uStack_494 = _UNK_006dafcc;
    fVar10 = (float10)FUN_00471060(DAT_006daba0,_DAT_006dac48);
    local_108 = 0;
    local_104 = (float)fVar10;
    local_100 = 0;
    FUN_004446a0();
    local_3d8 = local_108;
    local_3d4 = local_104;
    local_3d0 = local_100;
    local_3c8 = 0x3fc00000;
    local_3bc = 0x3e4ccccd;
    local_3cc = 0x3fc00000;
    fVar10 = (float10)FUN_00471060(_DAT_006daf60,DAT_006dad1c);
    local_3a4 = (float)fVar10;
    local_3c4 = 0x3d4ccccd;
    local_68 = (int *)FUN_00640b15(0xc0,0x10);
    local_14 = 0x12;
    local_64 = local_68;
    if (local_68 == (int *)0x0) {
      uVar13 = 0;
    }
    else {
      uVar13 = FUN_00435f50(DAT_007c5e0c,8,&local_3d8,&local_4a0,0,0);
    }
    local_14 = 0xffffffff;
    FUN_0045d290(uVar13,1000);
    uVar16 = extraout_ECX_01;
    goto switchD_0045b7e8_caseD_7;
  case 0x2c:
  case 0x2d:
  case 0x35:
    local_160 = param_1[4];
    local_64 = param_1 + 4;
    local_158 = param_1[6];
    local_15c = (float)param_1[5] + DAT_006daa00;
    local_154 = param_1[7];
    uVar3 = FUN_00635d42();
    uVar3 = uVar3 & 0x80000001;
    if ((int)uVar3 < 0) {
      uVar3 = (uVar3 - 1 | 0xfffffffe) + 1;
    }
    fVar6 = (float)(uVar3 + 1);
    local_6c = fVar6;
    if (0 < (int)fVar6) {
      do {
        fVar10 = (float10)FUN_00471060(DAT_006daf34,DAT_006dab58);
        local_70 = (int *)(float)fVar10;
        fVar10 = (float10)FUN_00471060(DAT_006dab58,DAT_006dac84);
        local_7c = (float)fVar10;
        fVar10 = (float10)FUN_00471060(DAT_006daf34,DAT_006dab58);
        local_6c = (float)fVar10;
        uVar17 = 0x50;
        local_50 = (float)local_70;
        fStack_4c = local_7c;
        uStack_44 = 0;
        uVar16 = 0x45c0b2;
        fStack_48 = local_6c;
        local_70 = (int *)FUN_00640b15(0x50,0x10);
        local_14 = 0xc;
        local_68 = local_70;
        if (local_70 == (int *)0x0) {
          iVar5 = 0;
        }
        else {
          local_6c = DAT_00764454;
          if (DAT_00764454 == 0.0) {
            uVar17 = 10;
            uVar16 = 0x45c0e1;
            FUN_00431920(10,0);
          }
          uVar18 = 0x3f800000;
          local_6c = DAT_00764454;
          fVar10 = (float10)FUN_00471060(DAT_006da9bc,0x3f800000);
          iVar5 = FUN_00439630(local_6c,local_64,&local_50,(float)fVar10,in_stack_fffffa50,
                               in_stack_fffffa54,uVar13,iVar4,uVar16,uVar17,uVar18);
        }
        local_14 = 0xffffffff;
        *(undefined4 *)(iVar5 + 4) = 0xffffffff;
        FUN_00438760(iVar5,300);
        fVar6 = (float)((int)fVar6 + -1);
        param_1 = local_84;
      } while (fVar6 != 0.0);
    }
    FUN_004446a0();
    fVar10 = (float10)FUN_00471060(DAT_006dac84,_DAT_006dacbc);
    local_254 = (float)fVar10;
    local_d8 = 0;
    local_258 = 0;
    local_d0 = 0;
    local_250 = 0;
    local_248 = 0x3f800000;
    local_23c = 0x3f333333;
    local_240 = 0x40000000;
    local_228 = 0;
    local_220 = 0;
    local_234 = 0x3f800000;
    local_24c = 0x3fc00000;
    local_d4 = local_254;
    fVar10 = (float10)FUN_00471060(_DAT_006daf60,DAT_006dad1c);
    local_224 = (float)fVar10;
    local_244 = 0x3ca3d70a;
    local_21c = 1;
    local_64 = (int *)FUN_00640b15(0xc0,0x10);
    local_14 = 0xd;
    if (local_64 == (int *)0x0) goto LAB_0045c28d;
    piVar7 = &local_160;
    puVar9 = &local_258;
LAB_0045c26a:
    local_68 = local_64;
    iVar4 = FUN_00435f50(DAT_007c5e04,0x10,puVar9,piVar7,0,DAT_006da974);
    *(undefined4 *)(iVar4 + 4) = 0xffffffff;
    goto LAB_0045cf03;
  case 0x34:
    local_4b0 = _DAT_006dafc0;
    uStack_4ac = _UNK_006dafc4;
    uStack_4a8 = _UNK_006dafc8;
    uStack_4a4 = _UNK_006dafcc;
    fVar10 = (float10)FUN_00471060(DAT_006dac78,DAT_006dac98);
    local_114 = 0;
    local_110 = (float)fVar10;
    local_10c = 0;
    FUN_004446a0();
    local_418 = local_114;
    local_414 = local_110;
    local_410 = local_10c;
    local_408 = 0x40400000;
    local_3fc = 0x3e4ccccd;
    local_40c = 0x40000000;
    fVar10 = (float10)FUN_00471060(_DAT_006daf60,DAT_006dad1c);
    local_3e4 = (float)fVar10;
    local_404 = 0x3c23d70a;
    local_68 = (int *)FUN_00640b15(0xc0,0x10);
    local_14 = 0x13;
    local_64 = local_68;
    if (local_68 == (int *)0x0) {
      uVar13 = 0;
    }
    else {
      in_stack_fffffa50 = 0x45c9da;
      uVar13 = FUN_00435f50(DAT_007c5e0c,8,&local_418,&local_4b0,0,0);
    }
    local_14 = 0xffffffff;
    FUN_0045d290(uVar13,1000);
    local_170 = param_1[4];
    local_64 = param_1 + 4;
    local_16c = (float)param_1[5] + DAT_006daa00;
    local_168 = param_1[6];
    local_164 = param_1[7];
    uVar3 = FUN_00635d42();
    uVar3 = uVar3 & 0x80000003;
    if ((int)uVar3 < 0) {
      uVar3 = (uVar3 - 1 | 0xfffffffc) + 1;
    }
    piVar7 = (int *)(uVar3 + 1);
    local_68 = piVar7;
    if (0 < (int)piVar7) {
      do {
        uVar17 = 0;
        fVar10 = (float10)FUN_00471060(DAT_006daf4c,DAT_006dac78);
        fVar6 = (float)fVar10;
        fVar10 = (float10)FUN_00471060(DAT_006dacc8,DAT_006dad00);
        fVar15 = (float)fVar10;
        uVar13 = 0x45cab2;
        fVar10 = (float10)FUN_00471060(DAT_006daf4c,DAT_006dac78);
        fVar14 = (float)fVar10;
        uVar16 = 0x45cabe;
        FUN_004359b0(fVar14,fVar15,fVar6,uVar17);
        uVar18 = 0x50;
        uVar17 = 0x45cac7;
        local_70 = (int *)FUN_00640b15(0x50,0x10);
        local_14 = 0x14;
        local_68 = local_70;
        if (local_70 == (int *)0x0) {
          iVar4 = 0;
        }
        else {
          local_6c = DAT_00764454;
          if (DAT_00764454 == 0.0) {
            uVar18 = 10;
            uVar17 = 0x45caf6;
            FUN_00431920(10,0);
          }
          uVar8 = 0x3f800000;
          local_6c = DAT_00764454;
          fVar10 = (float10)FUN_00471060(_DAT_006daa60,DAT_006daba0);
          iVar4 = FUN_00439630(local_6c,local_64,local_40,(float)fVar10,in_stack_fffffa50,uVar13,
                               uVar16,fVar14,uVar17,uVar18,uVar8);
        }
        local_14 = 0xffffffff;
        *(undefined4 *)(iVar4 + 4) = 0xffffffff;
        FUN_00438760(iVar4,300);
        piVar7 = (int *)((int)piVar7 + -1);
      } while (piVar7 != (int *)0x0);
    }
    iVar4 = 4;
    local_118 = 0;
    local_120 = 0;
    do {
      fVar10 = (float10)FUN_004446a0();
      fVar10 = (float10)FUN_00471060((float)extraout_ST1,(float)fVar10);
      local_2d4 = (float)fVar10;
      local_2d8 = local_120;
      local_2d0 = 0;
      local_2c8 = 0x3f800000;
      local_2bc = 0x3f333333;
      local_2c0 = 0x40000000;
      local_2a8 = 0;
      local_2a0 = 0;
      local_2b4 = 0x3f800000;
      local_11c = local_2d4;
      fVar10 = (float10)FUN_00471060(_DAT_006daf60,DAT_006dad1c);
      local_2a4 = (float)fVar10;
      local_2c4 = 0x3c23d70a;
      local_29c = 1;
      local_2cc = 0x40000000;
      local_68 = (int *)FUN_00640b15(0xc0,0x10);
      local_14 = 0x15;
      local_64 = local_68;
      if (local_68 == (int *)0x0) {
        iVar5 = 0;
      }
      else {
        iVar5 = FUN_00435f50(DAT_007c5e04,0x10,&local_2d8,&local_170,0,DAT_006da974);
      }
      local_14 = 0xffffffff;
      *(undefined4 *)(iVar5 + 4) = 0xffffffff;
      FUN_00438760(iVar5,0);
      iVar4 = iVar4 + -1;
    } while (iVar4 != 0);
    Var11 = FUN_00471060(0,_DAT_006dac90);
    local_128 = 0;
    fVar10 = (float10)fsin(Var11);
    fVar12 = (float10)fcos(Var11);
    local_12c = (float)fVar12;
    local_124 = (float)fVar10;
    local_68 = (int *)FUN_00640b15(0x30,0x10);
    param_1 = local_84;
    local_14 = 0x16;
    local_64 = local_68;
    if (local_68 == (int *)0x0) {
      iVar4 = 0;
    }
    else {
      iVar4 = FUN_00635d42();
      iVar4 = iVar4 % 5000 + 20000;
      fVar10 = (float10)FUN_00471060(DAT_006dac84,DAT_006dacb8);
      iVar4 = FUN_00442f20(param_1 + 4,local_12c,local_128,local_124,(float)fVar10,iVar4);
    }
    *(undefined4 *)(iVar4 + 4) = 0xffffffff;
    uVar13 = 300;
    goto LAB_0045cf05;
  case 0x3b:
    uVar16 = 0xa0;
    local_1dc = 0x3dcccccd;
    local_1d8 = 0;
    local_1d4 = 0;
    local_1d0 = 0xbdcccccd;
    local_1cc = 0;
    local_1c8 = 0;
    uVar13 = 0x45bdcc;
    local_68 = (int *)FUN_00640b15(0xa0,0x10);
    local_14 = 9;
    local_64 = local_68;
    if (local_68 == (int *)0x0) goto LAB_0045bd6c;
    local_c0 = 0;
    local_bc = 0;
    local_b8 = 0;
    local_460 = _DAT_006db240;
    uStack_45c = _UNK_006db244;
    uStack_458 = _UNK_006db248;
    uStack_454 = _UNK_006db24c;
    uVar13 = FUN_0043a820(DAT_007c4e68,&local_1dc,2,DAT_006da9ec,DAT_006da974,&local_460,10,
                          0x3f800000,0x3f800000,0,0,0,uVar13,uVar16,1);
    goto LAB_0045bd6e;
  case 0x3c:
    uVar16 = 0xa0;
    local_1c4 = 0x3dcccccd;
    local_1c0 = 0;
    local_1bc = 0;
    local_1b8 = 0xbdcccccd;
    local_1b4 = 0;
    local_1b0 = 0;
    uVar13 = 0x45bcc4;
    local_68 = (int *)FUN_00640b15(0xa0,0x10);
    local_14 = 8;
    local_64 = local_68;
    if (local_68 == (int *)0x0) goto LAB_0045bd6c;
    local_b4 = 0;
    local_b0 = 0;
    local_ac = 0;
    local_450 = _DAT_006db240;
    uStack_44c = _UNK_006db244;
    uStack_448 = _UNK_006db248;
    uStack_444 = _UNK_006db24c;
    uVar13 = FUN_0043a820(DAT_007c4e6c,&local_1c4,2,DAT_006da9ec,DAT_006da974,&local_450,10,
                          0x3f800000,0x3f800000,0,0,0,uVar13,uVar16,1);
    goto LAB_0045bd6e;
  case 0x45:
    uVar13 = 0x10;
    local_68 = (int *)FUN_00640b15(0x5f0,0x10);
    local_14 = 0xb;
    local_64 = local_68;
    if (local_68 == (int *)0x0) goto LAB_0045bd6c;
    uVar13 = FUN_00438b10(param_1[0x25],4,0x1e,0,0x3f800000,0x3f800000,DAT_006da994,uVar13);
LAB_0045bd6e:
    local_14 = 0xffffffff;
    FUN_0045d290(uVar13,0);
    uVar16 = extraout_ECX_00;
    goto switchD_0045b7e8_caseD_7;
  case 0x69:
    FUN_004446a0();
    local_520 = 0x3e99999a;
    local_4fc = 0x3dcccccd;
    local_51c = 0x3c23d70a;
    local_68 = (int *)FUN_00640b15(0xc0,0x10);
    local_14 = 6;
    local_64 = local_68;
    if (local_68 == (int *)0x0) goto LAB_0045cef7;
    local_430 = 0;
    uStack_42c = 0;
    uStack_428 = 0;
    uStack_424 = 0;
    iVar4 = FUN_00435f50(DAT_007c5df8,8,local_530,&local_430,0,0);
    break;
  case 0x6c:
    uVar16 = 0xa0;
    local_218 = 0x3fc00000;
    local_214 = 0;
    local_210 = 0;
    local_20c = 0;
    local_208 = 0;
    local_204 = 0x3f800000;
    local_200 = 0xbfc00000;
    local_1fc = 0;
    local_1f8 = 0;
    uVar13 = 0x45b936;
    local_68 = (int *)FUN_00640b15(0xa0,0x10);
    local_14 = 2;
    local_64 = local_68;
    if (local_68 == (int *)0x0) goto LAB_0045cef7;
    local_9c = 0;
    local_98 = 0;
    local_94 = 0;
    local_480 = _DAT_006db240;
    uStack_47c = _UNK_006db244;
    uStack_478 = _UNK_006db248;
    uStack_474 = _UNK_006db24c;
    iVar4 = FUN_0043a820(DAT_007c4e78,&local_218,3,DAT_006da9ec,DAT_006da9bc,&local_480,7,0x3f800000
                         ,DAT_006dac70,0,0,0,uVar13,uVar16,0);
  }
LAB_0045cef9:
  *(int **)(iVar4 + 4) = param_1;
LAB_0045cf03:
  uVar13 = 0;
LAB_0045cf05:
  local_14 = 0xffffffff;
  FUN_00438760(iVar4,uVar13);
  uVar16 = extraout_ECX_02;
switchD_0045b7e8_caseD_7:
  param_2 = local_80;
  if (local_78 != (undefined *)0x0) {
    if (local_74 != 0) {
      local_68 = (int *)FUN_00640b15(0x40,0x10);
      local_14 = 0x18;
      local_64 = local_68;
      if (local_68 == (int *)0x0) {
        uVar13 = 0;
      }
      else {
        puVar9 = &local_17c;
        uVar19 = 1;
        local_17c = 0xbf800000;
        local_178 = 0xbf800000;
        uVar13 = *(undefined4 *)(local_74 + 0x14);
        local_174 = 0xbf800000;
        uVar16 = *(undefined4 *)(local_74 + 0x10);
        uVar17 = *(undefined4 *)(local_74 + 0xc);
        uVar3 = (uint)*(byte *)(local_74 + 4);
        uVar18 = *(undefined4 *)(local_74 + 8);
        uVar8 = FUN_00443ca0(local_74);
        uVar13 = FUN_00437a30(uVar8,uVar3,uVar18,uVar17,puVar9,uVar16,uVar13,uVar19);
      }
      local_14 = 0xffffffff;
      FUN_0045d290(uVar13,0);
    }
    puVar1 = local_78;
    FUN_004446a0();
    uVar3 = *(uint *)(puVar1 + 0x20);
    local_388 = 0x3ecccccd;
    local_37c = 0x3e4ccccd;
    local_384 = 0x3d4ccccd;
    local_364 = 0x3f800000;
    if ((uVar3 & 1) == 0) {
      if ((uVar3 & 2) != 0) {
        local_38c = 0x3f800000;
        local_68 = (int *)FUN_00640b15(0xc0,0x10);
        local_14 = 0x1a;
        local_64 = local_68;
        if (local_68 == (int *)0x0) goto LAB_0045d118;
        local_4e0 = 0;
        uStack_4dc = 0;
        uStack_4d8 = 0;
        uStack_4d4 = 0;
        uVar13 = FUN_00435f50(DAT_007c5e14,0x10,local_398,&local_4e0,0,0);
        goto LAB_0045d11a;
      }
      uVar16 = extraout_ECX_03;
      if ((uVar3 & 4) != 0) {
        local_38c = 0x3fc00000;
        local_68 = (int *)FUN_00640b15(0xc0,0x10);
        local_14 = 0x1b;
        local_64 = local_68;
        if (local_68 == (int *)0x0) goto LAB_0045d118;
        local_4f0 = 0;
        uStack_4ec = 0;
        uStack_4e8 = 0;
        uStack_4e4 = 0;
        uVar13 = FUN_00435f50(DAT_007c5e14,0x10,local_398,&local_4f0,0,0);
        goto LAB_0045d11a;
      }
    }
    else {
      local_38c = 0x3f000000;
      local_68 = (int *)FUN_00640b15(0xc0,0x10);
      local_14 = 0x19;
      local_64 = local_68;
      if (local_68 == (int *)0x0) {
LAB_0045d118:
        uVar13 = 0;
        local_68 = local_64;
      }
      else {
        local_4d0 = 0;
        uStack_4cc = 0;
        uStack_4c8 = 0;
        uStack_4c4 = 0;
        uVar13 = FUN_00435f50(DAT_007c5e14,0x10,local_398,&local_4d0,0,0);
      }
LAB_0045d11a:
      local_14 = 0xffffffff;
      FUN_0045d290(uVar13,0);
      uVar16 = extraout_ECX_04;
    }
    param_2 = local_80;
    if ((puVar1[0x20] & 8) != 0) {
      local_68 = (int *)FUN_00640b15(0x30,0x10);
      local_14 = 0x1c;
      local_64 = local_68;
      if (local_68 == (int *)0x0) {
        uVar13 = 0;
      }
      else {
        uVar13 = FUN_004431e0(3,0,puVar1);
      }
      local_14 = 0xffffffff;
      FUN_0045d290(uVar13,0);
      uVar16 = extraout_ECX_05;
      param_2 = local_80;
    }
  }
LAB_0045d172:
  if (((param_2 == 0x33) || (param_2 == 0x2a)) || (param_2 == 0x2b)) {
    uVar13 = 0x24;
  }
  else if (param_2 == 0x34) {
    uVar13 = 0x25;
  }
  else {
    if (((param_2 != 0x35) && (param_2 != 0x2c)) && (puVar2 = puStack_20, param_2 != 0x2d))
    goto LAB_0045d1b8;
    uVar13 = 0x26;
  }
  FUN_005929b0(uVar13,param_1 + 4,uVar16);
  puVar2 = puStack_20;
LAB_0045d1b8:
  puStack_20 = puVar2;
  ExceptionList = local_1c;
  __security_check_cookie(local_24 ^ (uint)&stack0xfffffff0);
  return;
}


```

## `0045d430`

- Function: `FUN_0045d410`
- Entry: `0045d410`

```c

void __thiscall FUN_0045d410(int param_1,undefined4 param_2,undefined4 param_3,undefined4 param_4)

{
  uint uVar1;
  undefined4 uVar2;
  undefined4 uVar3;
  
  if (((*(int *)(param_1 + 0x94) != 0) &&
      (uVar1 = *(uint *)(*(int *)(param_1 + 0x94) + 0x44), uVar1 < 0x2b5)) &&
     (uVar1 * 0x44 != -0x76604c)) {
    uVar3 = 0;
    uVar2 = FUN_00469b50(param_4,param_2);
    FUN_004553d0(uVar2,uVar3);
  }
  return;
}


```

## `0045d70c`

- Function: `FUN_0045d690`
- Entry: `0045d690`

```c

void __thiscall FUN_0045d690(int param_1,uint param_2)

{
  undefined1 *puVar1;
  int iVar2;
  int iVar3;
  float local_50;
  float local_4c;
  float local_48;
  float local_44;
  undefined4 local_38;
  undefined4 local_34;
  undefined4 local_30;
  int local_2c;
  int local_28;
  byte *local_24;
  undefined1 *puStack_20;
  void *local_1c;
  undefined1 *puStack_18;
  undefined4 local_14;
  
  puStack_20 = &stack0xfffffffc;
  local_14 = 0xffffffff;
  puStack_18 = &LAB_0065fd81;
  local_1c = ExceptionList;
  if (*(int *)(param_1 + 0x98) == 0) {
    return;
  }
  if (0x707 < param_2) {
    return;
  }
  ExceptionList = &local_1c;
  puVar1 = &stack0xfffffffc;
  if (DAT_0078443c == '\0') {
LAB_0045d7de:
    puStack_20 = puVar1;
    puVar1 = puStack_20;
    if (param_2 < 0x2b5) {
      iVar2 = (&DAT_0076442c)[param_2];
      if (iVar2 == 0) {
        FUN_00431920(param_2,0);
        iVar2 = (&DAT_0076442c)[param_2];
      }
      goto LAB_0045d808;
    }
  }
  else {
    puVar1 = &stack0xfffffffc;
    if (param_2 < 0x2b5) {
      puVar1 = &stack0xfffffffc;
      if ((param_2 * 0x44 != -0x76604c) &&
         (local_24 = (byte *)(&DAT_00766060)[param_2 * 0x11], puVar1 = &stack0xfffffffc,
         local_24 != (byte *)0x0)) {
        local_2c = FUN_00640b15(0x40,0x10,DAT_007360c8 ^ (uint)&stack0xfffffff0);
        local_14 = 0;
        local_28 = local_2c;
        if (local_2c == 0) {
          iVar2 = 0;
        }
        else {
          local_38 = 0xbf800000;
          local_34 = 0xbf800000;
          local_48 = (float)*local_24;
          local_30 = 0xbf800000;
          local_4c = (float)local_24[1];
          local_50 = (float)local_24[2];
          local_44 = (float)local_24[3];
          iVar2 = FUN_00437a30(&local_50,local_24[4],*(undefined4 *)(local_24 + 8),
                               *(undefined4 *)(local_24 + 0xc),&local_38,
                               *(undefined4 *)(local_24 + 0x10),*(undefined4 *)(local_24 + 0x14),1);
        }
        local_14 = 0xffffffff;
        *(int *)(iVar2 + 4) = param_1;
        FUN_00438760(iVar2,0);
        puVar1 = puStack_20;
      }
      goto LAB_0045d7de;
    }
  }
  puStack_20 = puVar1;
  iVar2 = 0;
LAB_0045d808:
  iVar3 = FUN_00431650(iVar2);
  iVar2 = *(int *)(param_1 + 0x98);
  if (iVar3 != 0) {
    if (*(int *)(iVar2 + 0x5c) == 0) {
      *(int *)(iVar2 + 0x5c) = iVar3;
      *(int *)(iVar3 + 0x60) = iVar2;
    }
    else {
      FUN_00455350(iVar3,iVar2);
    }
  }
  ExceptionList = local_1c;
  return;
}


```

## `0045f883`

- Function: `FUN_0045f630`
- Entry: `0045f630`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

undefined4 __thiscall
FUN_0045f630(int param_1,uint param_2,int param_3,undefined4 param_4,undefined4 param_5)

{
  undefined1 *puVar1;
  uint uVar2;
  int iVar3;
  undefined4 *puVar4;
  undefined1 local_80 [16];
  undefined4 local_70;
  undefined4 local_6c;
  undefined4 local_68;
  undefined4 local_64;
  undefined4 local_60;
  undefined4 local_4c;
  undefined4 local_40;
  undefined4 uStack_3c;
  undefined4 uStack_38;
  undefined4 uStack_34;
  undefined4 *local_28;
  undefined4 *local_24;
  undefined1 *puStack_20;
  void *local_1c;
  undefined1 *puStack_18;
  undefined4 local_14;
  
  puStack_20 = &stack0xfffffffc;
  local_14 = 0xffffffff;
  puStack_18 = &LAB_0065fec9;
  local_1c = ExceptionList;
  uVar2 = DAT_007360c8 ^ (uint)&stack0xfffffff0;
  ExceptionList = &local_1c;
  *(undefined4 *)(param_1 + 0x3c8) = 0;
  *(undefined4 *)(param_1 + 0xa0) = 0xffffffff;
  *(undefined4 *)(param_1 + 0x3cc) = 0;
  *(undefined4 *)(param_1 + 0xa4) = 0xffffffff;
  *(undefined4 *)(param_1 + 0x3d0) = 0;
  *(undefined4 *)(param_1 + 0xa8) = 0xffffffff;
  *(undefined4 *)(param_1 + 0x3d4) = 0;
  *(undefined4 *)(param_1 + 0xac) = 0xffffffff;
  *(undefined4 *)(param_1 + 0x3d8) = 0;
  *(undefined4 *)(param_1 + 0xb0) = 0xffffffff;
  *(undefined4 *)(param_1 + 0x3dc) = 0;
  *(undefined4 *)(param_1 + 0xb4) = 0xffffffff;
  *(undefined4 *)(param_1 + 0x3e0) = 0;
  *(undefined4 *)(param_1 + 0xb8) = 0xffffffff;
  *(undefined4 *)(param_1 + 0x3e4) = 0;
  *(undefined4 *)(param_1 + 0xbc) = 0xffffffff;
  *(undefined4 *)(param_1 + 1000) = 0;
  *(undefined4 *)(param_1 + 0xc0) = 0xffffffff;
  *(undefined4 *)(param_1 + 0x3ec) = 0;
  *(undefined4 *)(param_1 + 0xc4) = 0xffffffff;
  if (param_2 < 0x2b5) {
    iVar3 = (&DAT_0076442c)[param_2];
    puVar1 = &stack0xfffffffc;
    if (iVar3 == 0) {
      FUN_00431920(param_2,0);
      iVar3 = (&DAT_0076442c)[param_2];
      puVar1 = puStack_20;
      if (iVar3 == 0) {
        ExceptionList = local_1c;
        return 0;
      }
    }
    puStack_20 = puVar1;
    iVar3 = FUN_0045b260(iVar3,param_3,param_4,param_5);
    if (iVar3 != 0) {
      if (((param_3 != -1) && (DAT_0078443c != '\0')) && (DAT_007c5e14 != 0)) {
        FUN_004446a0(uVar2);
        local_70 = 0x40000000;
        local_64 = 0x3ecccccd;
        local_60 = 0x3f000000;
        local_68 = 0x3f000000;
        local_4c = 0x3f800000;
        local_6c = 0x3e19999a;
        puVar4 = (undefined4 *)FUN_00640b15(0xd0,0x10);
        local_14 = 0;
        local_28 = puVar4;
        local_24 = puVar4;
        if (puVar4 == (undefined4 *)0x0) {
          puVar4 = (undefined4 *)0x0;
        }
        else {
          local_40 = _DAT_006db050;
          uStack_3c = _UNK_006db054;
          uStack_38 = _UNK_006db058;
          uStack_34 = _UNK_006db05c;
          FUN_00435f50(DAT_007c5e14,0x10,local_80,&local_40,0,0);
          *puVar4 = G3DETrailer::vftable;
          puVar4[0x30] = 1;
        }
        local_14 = 0xffffffff;
        puVar4[1] = param_1;
        FUN_00438760(puVar4,0);
      }
      uVar2 = (uint)(0x10 < param_2 - 0x284);
      *(uint *)(param_1 + 0xa4 + uVar2 * -4) = param_2;
      *(undefined4 *)(param_1 + 0x3cc + uVar2 * -4) = *(undefined4 *)(param_1 + 0x94);
      *(undefined **)(param_1 + 0x3f4 + uVar2 * -4) = &DAT_0076604c + param_2 * 0x44;
      ExceptionList = local_1c;
      return 1;
    }
  }
  ExceptionList = local_1c;
  return 0;
}


```

## `0045f9c0`

- Function: `FUN_0045f9a0`
- Entry: `0045f9a0`

```c

void FUN_0045f9a0(uint param_1)

{
  undefined *puVar1;
  int iVar2;
  undefined4 uVar3;
  
  if (((param_1 != 0xffffffff) && (param_1 < 0x2b5)) &&
     (puVar1 = &DAT_0076604c + param_1 * 0x44, puVar1 != (undefined *)0x0)) {
    if (0x707 < param_1) {
      FUN_0045fa20(0,puVar1);
      return;
    }
    iVar2 = (&DAT_0076442c)[param_1];
    if (iVar2 == 0) {
      FUN_00431920(param_1,0);
      iVar2 = (&DAT_0076442c)[param_1];
    }
    uVar3 = FUN_00431650(iVar2);
    FUN_0045fa20(uVar3,puVar1);
  }
  return;
}


```

## `0045fc2f`

- Function: `FUN_0045fa20`
- Entry: `0045fa20`

```c

void __thiscall FUN_0045fa20(int param_1,undefined4 param_2,int *param_3)

{
  byte *pbVar1;
  uint uVar2;
  int iVar3;
  int iVar4;
  undefined4 uVar5;
  undefined *puVar6;
  float local_50;
  float local_4c;
  float local_48;
  float local_44;
  undefined4 local_38;
  undefined4 local_34;
  undefined4 local_30;
  uint local_2c;
  uint local_28;
  int local_24;
  undefined1 *puStack_20;
  void *local_1c;
  undefined1 *puStack_18;
  undefined4 local_14;
  
  puStack_20 = &stack0xfffffffc;
  local_14 = 0xffffffff;
  puStack_18 = &LAB_0065ff01;
  local_1c = ExceptionList;
  ExceptionList = &local_1c;
  local_28 = *param_3;
  if (local_28 == -1) {
    if (*(int *)(param_1 + 0x98) != 0) {
      uVar2 = 0xffffffff;
      puStack_20 = &stack0xfffffffc;
      if ((DAT_0078443c != '\0') &&
         (pbVar1 = (byte *)param_3[5], puStack_20 = &stack0xfffffffc, pbVar1 != (byte *)0x0)) {
        puStack_20 = &stack0xfffffffc;
        local_2c = FUN_00640b15(0x40,0x10);
        local_14 = 0;
        local_28 = local_2c;
        if (local_2c == 0) {
          iVar3 = 0;
        }
        else {
          local_38 = 0xbf800000;
          local_48 = (float)*pbVar1;
          local_34 = 0xbf800000;
          local_30 = 0xbf800000;
          local_4c = (float)pbVar1[1];
          local_50 = (float)pbVar1[2];
          local_44 = (float)pbVar1[3];
          iVar3 = FUN_00437a30(&local_50,pbVar1[4],*(undefined4 *)(pbVar1 + 8),
                               *(undefined4 *)(pbVar1 + 0xc),&local_38,
                               *(undefined4 *)(pbVar1 + 0x10),*(undefined4 *)(pbVar1 + 0x14),1);
        }
        local_14 = 0xffffffff;
        *(int *)(iVar3 + 4) = param_1;
        FUN_00438760(iVar3,0);
        uVar2 = local_28;
      }
      local_28 = uVar2;
      iVar4 = FUN_00431650(param_2);
      iVar3 = *(int *)(param_1 + 0x98);
      if (iVar4 != 0) {
        if (*(int *)(iVar3 + 0x5c) == 0) {
          *(int *)(iVar3 + 0x5c) = iVar4;
          *(int *)(iVar4 + 0x60) = iVar3;
        }
        else {
          FUN_00455350(iVar4,iVar3);
        }
      }
    }
  }
  else {
    FUN_0045fcd0(DAT_007360c8 ^ (uint)&stack0xfffffff0);
    if (param_3[9] != -1) {
      if (local_28 == 2) {
        local_24 = 3;
      }
      else if (local_28 == 5) {
        local_24 = 6;
      }
      else {
        local_24 = 9;
      }
      FUN_004315b0(*(undefined4 *)(param_1 + 0x3c8 + local_24 * 4));
      local_2c = param_3[9];
      if (local_2c < 0x708) {
        if (local_2c < 0x2b5) {
          iVar3 = (&DAT_0076442c)[local_2c];
          if (iVar3 == 0) {
            FUN_00431920(local_2c,0);
            iVar3 = (&DAT_0076442c)[local_2c];
          }
        }
        else {
          iVar3 = 0;
        }
        uVar5 = FUN_00431650(iVar3);
      }
      else {
        uVar5 = 0;
      }
      *(undefined4 *)(param_1 + 0x3c8 + local_24 * 4) = uVar5;
      if ((uint)param_3[9] < 0x2b5) {
        puVar6 = &DAT_0076604c + param_3[9] * 0x44;
      }
      else {
        puVar6 = (undefined *)0x0;
      }
      *(undefined **)(param_1 + 0x3f0 + local_24 * 4) = puVar6;
    }
    FUN_004315b0(*(undefined4 *)(param_1 + 0x3c8 + local_28 * 4));
    *(undefined4 *)(param_1 + 0x3c8 + local_28 * 4) = param_2;
    *(int **)(param_1 + 0x3f0 + local_28 * 4) = param_3;
    if (local_28 == 0) {
      *(undefined4 *)(param_1 + 0x94) = param_2;
    }
    FUN_0045fd40();
  }
  ExceptionList = local_1c;
  return;
}


```

