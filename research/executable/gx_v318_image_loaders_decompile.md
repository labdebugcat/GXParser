# Selected Nova1492 Decompilation

## `0046cf10`

- Function: `FUN_0046cf10`
- Entry: `0046cf10`

```c

void __thiscall
FUN_0046cf10(undefined2 *param_1,undefined4 param_2,undefined4 **param_3,undefined4 **param_4,
            undefined4 **param_5,undefined4 **param_6)

{
  undefined2 *puVar1;
  LPARAM dwInitParam;
  undefined4 *puVar2;
  undefined4 *puVar3;
  char cVar4;
  uint uVar5;
  undefined4 *puVar6;
  undefined4 **ppuVar7;
  uint uVar8;
  int *piVar9;
  undefined4 **ppuVar10;
  uint uVar11;
  undefined4 extraout_ECX;
  uint uVar12;
  int iVar13;
  undefined *puVar14;
  undefined4 *local_54;
  undefined4 *local_50;
  int local_4c [5];
  undefined2 *local_38;
  undefined4 local_34;
  undefined4 local_30;
  int local_2c;
  uint local_28;
  uint local_24;
  undefined4 **local_20;
  undefined4 **local_1c;
  uint local_18;
  void *local_10;
  undefined1 *puStack_c;
  undefined4 local_8;
  
  local_8 = 0xffffffff;
  puStack_c = &LAB_00663906;
  local_10 = ExceptionList;
  uVar5 = DAT_007360c8 ^ (uint)&stack0xfffffffc;
  ExceptionList = &local_10;
  local_50 = (undefined4 *)0x0;
  local_54 = (undefined4 *)0x0;
  iVar13 = 0;
  local_18 = uVar5;
  do {
    puVar6 = (undefined4 *)FUN_0063ea48(0x24,uVar5);
    if (puVar6 == (undefined4 *)0x0) {
      puVar6 = (undefined4 *)0x0;
    }
    else {
      *puVar6 = 0;
      puVar6[1] = 0;
      puVar6[2] = 0;
      puVar6[3] = 0;
      puVar6[4] = 0;
      puVar6[5] = 0;
      puVar6[6] = 0;
      puVar6[7] = 0;
      puVar6[8] = 0;
      puVar6[5] = &DAT_006b9e28;
      *puVar6 = 0;
      puVar6[1] = 0;
      puVar6[2] = 0;
      puVar6[3] = 0;
      *(undefined2 *)(puVar6 + 4) = 0;
      puVar6[6] = 0;
      puVar6[7] = 0;
      puVar6[8] = 0;
    }
    local_8 = 0xffffffff;
    ppuVar7 = param_3;
    ppuVar10 = param_4;
    puVar2 = local_54;
    puVar3 = puVar6;
    if ((iVar13 != 0) &&
       (ppuVar7 = param_5, ppuVar10 = param_6, puVar2 = puVar6, puVar3 = local_50,
       param_5 == (undefined4 **)0x0)) {
      if (puVar6 != (undefined4 *)0x0) {
        local_8 = 0x13;
        FUN_00427090();
        local_8 = 0xffffffff;
        if ((undefined2 *)puVar6[5] != &DAT_006b9e28) {
          thunk_FUN_00640afb((undefined2 *)puVar6[5] + -2);
        }
        FUN_0062a696(puVar6,0x24);
      }
      break;
    }
    local_50 = puVar3;
    local_54 = puVar2;
    local_20 = ppuVar7;
    local_1c = ppuVar10;
    cVar4 = FUN_00427300(ppuVar7,ppuVar10);
    puVar2 = local_50;
    if (cVar4 == '\0') {
      if (local_50 != (undefined4 *)0x0) {
        local_8 = 0x25;
        FUN_00427090();
        local_8 = 0xffffffff;
        if ((undefined2 *)puVar2[5] != &DAT_006b9e28) {
          thunk_FUN_00640afb((undefined2 *)puVar2[5] + -2);
        }
        FUN_0062a696(puVar2,0x24);
      }
      puVar6 = local_54;
      if (local_54 != (undefined4 *)0x0) {
        local_8 = 0x37;
        FUN_00427090();
        local_8 = 0xffffffff;
        puVar1 = (undefined2 *)puVar6[5];
        if (puVar1 != &DAT_006b9e28) {
          thunk_FUN_00640afb(puVar1 + -2);
        }
        FUN_0062a696(puVar6,0x24);
      }
      piVar9 = (int *)FUN_00453320(DAT_00887d08,DAT_00887d0c);
      local_8 = 0x49;
      FUN_00434ab0(*(int *)(*piVar9 + -4),*(int *)(*piVar9 + -4) + 1);
      iVar13 = *piVar9;
      *(undefined2 *)(iVar13 + *(int *)(iVar13 + -4) * 2) = 0;
      dwInitParam = *piVar9;
      if (DAT_0088ca90 != '\0') {
        DAT_0088ca90 = '\0';
        FUN_0056f4d0(iVar13);
        SetWindowPos(DAT_007642c4,(HWND)0xfffffffe,0,0,0,0,3);
        if (DAT_007c8c94 != (int *)0x0) {
          (**(code **)(*DAT_007c8c94 + 0xc))(DAT_007c8c94);
        }
      }
      DialogBoxParamW(DAT_008afcc4,(LPCWSTR)0x98,DAT_007642c4,(DLGPROC)&LAB_004d8220,dwInitParam);
LAB_0046d334:
      local_8 = 0xffffffff;
      if (param_1 != &DAT_006b9e28) {
        FUN_0059c360(param_1 + -2);
      }
      goto LAB_0046d4b0;
    }
    uVar11 = (uint)*(ushort *)(puVar6 + 3);
    if (((uVar11 & uVar11 - 1) != 0) ||
       (uVar12 = (uint)*(ushort *)((int)puVar6 + 0xe), (uVar12 & uVar12 - 1) != 0)) {
      if (local_50 != (undefined4 *)0x0) {
        local_8 = 0x5c;
        FUN_00427090();
        local_8 = 0xffffffff;
        if ((undefined2 *)puVar2[5] != &DAT_006b9e28) {
          thunk_FUN_00640afb((undefined2 *)puVar2[5] + -2);
        }
        FUN_0062a696(puVar2,0x24);
      }
      if (local_54 != (undefined4 *)0x0) {
        FUN_0046d5e0(local_54);
      }
      piVar9 = (int *)FUN_00453320(DAT_00887dd0,DAT_00887dd4);
      local_8 = 0x6e;
      FUN_00434ab0(*(int *)(*piVar9 + -4),*(int *)(*piVar9 + -4) + 1);
      *(undefined2 *)(*piVar9 + *(int *)(*piVar9 + -4) * 2) = 0;
      FUN_004d7ec0();
      goto LAB_0046d334;
    }
    cVar4 = *(char *)(puVar6 + 4);
    if ((((cVar4 != '\b') && (cVar4 != '\x10')) && (cVar4 != '\x18')) && (cVar4 != ' ')) {
      if (local_50 != (undefined4 *)0x0) {
        FUN_0046d5e0(local_50);
      }
      if (local_54 != (undefined4 *)0x0) {
        FUN_0046d5e0(local_54);
      }
      FUN_00453320(DAT_00887dd8,DAT_00887ddc);
      local_8 = 0x81;
      FUN_00433820();
      FUN_004d7ec0();
      goto LAB_0046d334;
    }
    if (((DAT_00784468 < uVar11) || (DAT_00784468 < uVar12)) || (DAT_00764401 != '\0')) {
      uVar8 = *(ushort *)((int)puVar6 + 0xe) / DAT_00784468;
      uVar12 = uVar11 / DAT_00784468;
      if (uVar11 / DAT_00784468 < uVar8) {
        uVar12 = uVar8;
      }
      if (uVar12 < 2) {
        uVar12 = 2;
      }
      *(char *)(param_1 + 0x224) = (char)uVar12;
      *(char *)((int)param_1 + 0x449) = (char)uVar12;
      cVar4 = FUN_00426ce0(*(ushort *)(puVar6 + 3) / uVar12,*(ushort *)((int)puVar6 + 0xe) / uVar12)
      ;
      if (cVar4 == '\0') {
        if (local_50 != (undefined4 *)0x0) {
          FUN_0046d5e0(local_50);
        }
        if (local_54 != (undefined4 *)0x0) {
          FUN_0046d5e0(local_54);
        }
        local_50 = (undefined4 *)0x0;
        local_54 = (undefined4 *)0x0;
        FUN_00433880();
        local_8 = 0x94;
        FUN_00470740(extraout_ECX);
        puVar14 = &DAT_006be948;
        FUN_0044cfc0(&local_20);
        piVar9 = (int *)FUN_00433e10(puVar14);
        FUN_00434ab0(*(int *)(*piVar9 + -4),*(int *)(*piVar9 + -4) + 1);
        *(undefined2 *)(*piVar9 + *(int *)(*piVar9 + -4) * 2) = 0;
        goto LAB_0046d334;
      }
    }
    iVar13 = iVar13 + 1;
  } while (iVar13 < 2);
  FUN_0046c990(local_54);
  local_8 = 0xa7;
  if (local_50[7] != 0) {
    FUN_00426640();
  }
  local_20 = &local_50;
  local_1c = &local_54;
  local_8 = CONCAT31(local_8._1_3_,0xa8);
  switch((uint)*(byte *)(local_50 + 4)) {
  case 8:
    local_30 = 0;
    break;
  default:
    goto switchD_0046d3f2_caseD_9;
  case 0x10:
    local_30 = 3;
    break;
  case 0x18:
    local_30 = 6;
    break;
  case 0x20:
    local_30 = 8;
  }
  local_34 = local_50[6];
  local_24 = (uint)*(ushort *)((int)local_50 + 0xe);
  local_28 = (uint)*(ushort *)(local_50 + 3);
  local_2c = (int)(local_28 * *(byte *)(local_50 + 4)) >> 3;
  piVar9 = local_4c;
  if (local_4c[0] == 0) {
    piVar9 = (int *)0x0;
  }
  cVar4 = FUN_0046ed60(0,&local_34,piVar9,param_2,local_50[8],0,param_3,param_4);
  if (cVar4 == '\0') {
switchD_0046d3f2_caseD_9:
  }
  local_8 = CONCAT31(local_8._1_3_,0xa7);
  FUN_0046d500();
  local_8 = 0xffffffff;
  if (local_38 != &DAT_006b9e28) {
    FUN_0059c360(local_38 + -2);
  }
LAB_0046d4b0:
  ExceptionList = local_10;
  __security_check_cookie(local_18 ^ (uint)&stack0xfffffffc);
  return;
}


```

## `0046d6d0`

- Function: `FUN_0046d6d0`
- Entry: `0046d6d0`

```c

void __thiscall
FUN_0046d6d0(int param_1,undefined1 *param_2,undefined1 *param_3,undefined4 param_4,
            undefined1 *param_5,undefined1 *param_6)

{
  short sVar1;
  undefined4 uVar2;
  undefined4 uVar3;
  undefined1 *puVar4;
  char cVar5;
  uint uVar6;
  undefined4 uVar7;
  int *piVar8;
  undefined4 uVar9;
  undefined4 extraout_ECX;
  int iVar10;
  undefined4 *puVar11;
  undefined4 *puVar12;
  undefined1 **ppuVar13;
  undefined2 **ppuVar14;
  undefined2 *local_b24 [2];
  undefined1 *local_b1c;
  undefined1 *local_b18;
  undefined4 local_b14 [256];
  int local_714;
  undefined1 local_710 [520];
  int local_508 [6];
  undefined4 local_4f0 [14];
  undefined4 local_4b8 [14];
  undefined4 local_480;
  undefined2 *local_47c;
  uint local_478;
  int local_474;
  undefined4 local_470;
  undefined4 local_46c;
  undefined4 local_468;
  undefined4 local_464;
  undefined4 local_460;
  undefined4 local_45c;
  undefined4 local_458;
  undefined4 local_454;
  uint local_450;
  uint local_44c;
  undefined4 local_448;
  undefined4 local_444;
  undefined4 local_440;
  undefined4 local_43c;
  undefined2 local_438;
  undefined4 local_434;
  int local_430;
  undefined4 local_42c;
  undefined4 local_428;
  undefined4 local_424;
  undefined4 local_420;
  undefined4 local_41c;
  uint local_418;
  uint local_414;
  undefined4 local_410;
  undefined4 local_40c;
  undefined4 local_408;
  undefined4 local_404;
  undefined2 local_400;
  undefined1 local_3fc [480];
  undefined1 local_21c [520];
  uint local_14;
  void *local_10;
  undefined1 *puStack_c;
  int local_8;
  
  local_8 = 0xffffffff;
  puStack_c = &LAB_00663df0;
  local_10 = ExceptionList;
  uVar6 = DAT_007360c8 ^ (uint)&stack0xfffffffc;
  ExceptionList = &local_10;
  local_14 = uVar6;
  _memset(&local_434,0,0x38);
  local_42c = 0;
  local_420 = 0;
  local_434 = 0;
  local_430 = 0;
  local_428 = 0;
  local_424 = 0;
  local_410 = 0;
  local_418 = 0;
  local_414 = 0;
  local_41c = 1;
  local_40c = 0;
  local_408 = 0;
  local_404 = 0;
  local_400 = 0;
  local_8 = 0;
  _memset(&local_46c,0,0x38);
  local_464 = 0;
  local_458 = 0;
  local_46c = 0;
  local_468 = 0;
  local_460 = 0;
  local_45c = 0;
  local_448 = 0;
  local_450 = 0;
  local_44c = 0;
  local_454 = 1;
  local_444 = 0;
  local_440 = 0;
  local_43c = 0;
  local_438 = 0;
  local_8._0_1_ = 1;
  FUN_00428380(uVar6);
  local_b24[0] = (undefined2 *)&DAT_006b78d0;
  uVar7 = FUN_004a4d00(param_2,param_3);
  cVar5 = FUN_00427bc0(uVar7,1);
  if (cVar5 == '\0') {
    piVar8 = (int *)FUN_00453320(DAT_00887d08,DAT_00887d0c);
    local_8 = CONCAT31(local_8._1_3_,2);
    FUN_00434ab0(*(int *)(*piVar8 + -4),*(int *)(*piVar8 + -4) + 1);
    *(undefined2 *)(*piVar8 + *(int *)(*piVar8 + -4) * 2) = 0;
    FUN_004d7ec0();
LAB_0046deec:
    local_8._0_1_ = 1;
    if (local_b24[0] != &DAT_006b9e28) {
      FUN_0059c360(local_b24[0] + -2);
    }
  }
  else {
    if (((local_418 & local_418 - 1) != 0) || ((local_414 & local_414 - 1) != 0)) {
      piVar8 = (int *)FUN_00453320(DAT_00887d10,DAT_00887d14);
      local_8 = CONCAT31(local_8._1_3_,0x15);
      FUN_00434ab0(*(int *)(*piVar8 + -4),*(int *)(*piVar8 + -4) + 1);
      *(undefined2 *)(*piVar8 + *(int *)(*piVar8 + -4) * 2) = 0;
      FUN_004d7ec0();
      goto LAB_0046deec;
    }
    sVar1 = *(short *)(local_430 + 0xe);
    if ((((sVar1 != 8) && (sVar1 != 0x10)) && (sVar1 != 0x18)) && (sVar1 != 0x20)) {
      FUN_00453320(DAT_00887d18,DAT_00887d1c);
      local_8 = CONCAT31(local_8._1_3_,0x28);
      FUN_00433820();
      FUN_004d7ec0();
      goto LAB_0046deec;
    }
    local_b24[0] = (undefined2 *)0x5c;
    local_b1c = (undefined1 *)0x0;
    local_b18 = (undefined1 *)0x0;
    ppuVar14 = local_b24;
    ppuVar13 = &local_b1c;
    FUN_00433710(ppuVar13,ppuVar14);
    if (local_b1c == (undefined1 *)0x0) {
      local_b1c = param_2;
      local_b18 = param_3;
    }
    local_714 = 0;
    if (param_5 == (undefined1 *)0x0) {
      FUN_004278b0(&DAT_006bf8bc);
      cVar5 = FUN_00470430(ppuVar13,ppuVar14);
      if (cVar5 != '\0') {
        local_b24[0] = (undefined2 *)0x2e;
        local_b1c = (undefined1 *)0x0;
        local_b18 = (undefined1 *)0x0;
        FUN_00433710(&local_b1c,local_b24);
        puVar4 = local_b1c;
        if (local_b1c != (undefined1 *)0x0) {
          local_b1c = param_2;
          local_b18 = puVar4;
          FUN_004704d0(&local_b1c);
          FUN_00470620(extraout_ECX);
          param_5 = local_710;
          param_6 = local_710 + local_714 * 2;
        }
      }
      if (param_5 != (undefined1 *)0x0) goto LAB_0046da24;
    }
    else {
LAB_0046da24:
      cVar5 = FUN_00427b20(1,param_5,param_6);
      uVar3 = DAT_00887d2c;
      uVar9 = DAT_00887d28;
      uVar2 = DAT_00887d24;
      uVar7 = DAT_00887d20;
      if (cVar5 == '\0') {
        uVar7 = FUN_00420fd0();
        local_8._0_1_ = 0x3c;
        FUN_0045a980(uVar9,uVar3);
        FUN_0045a8d0(uVar7);
        uVar7 = FUN_00462c90(param_5,param_6);
        FUN_00470520(local_3fc,uVar7);
        local_8._0_1_ = 1;
        FUN_004208e0();
        param_5 = (undefined1 *)0x0;
        param_6 = local_b18;
      }
      else if ((local_450 != local_418) || (local_44c != local_414)) {
        uVar9 = FUN_00420fd0();
        local_8._0_1_ = 0x3b;
        FUN_0045a980(uVar7,uVar2);
        FUN_0045a8d0(uVar9);
        uVar7 = FUN_00462c90(param_5,param_6);
        FUN_00470520(local_3fc,uVar7);
        local_8._0_1_ = 1;
        FUN_004208e0();
        FUN_004d8000();
      }
    }
    puVar12 = &local_434;
    *(undefined2 *)(param_1 + 0x448) = 0x101;
    puVar11 = &local_46c;
    _memset(local_4f0,0,0x38);
    FUN_00427ab0();
    local_8._0_1_ = 0x3d;
    _memset(local_4b8,0,0x38);
    FUN_00427ab0();
    local_8._0_1_ = 0x3e;
    if (DAT_0078446c == 0) {
      if (((local_418 <= DAT_00784468) && (local_414 <= DAT_00784468)) && (DAT_00764401 == '\0'))
      goto LAB_0046dd1d;
      uVar6 = local_418 / DAT_00784468;
      if (local_418 / DAT_00784468 < local_414 / DAT_00784468) {
        uVar6 = local_414 / DAT_00784468;
      }
      if (uVar6 < 2) {
        uVar6 = 2;
      }
      *(char *)(param_1 + 0x448) = (char)uVar6;
      *(char *)(param_1 + 0x449) = (char)uVar6;
      if (uVar6 == 2) {
        FUN_00428150(&local_434,1);
        puVar12 = local_4f0;
        if (param_5 != (undefined1 *)0x0) {
          uVar7 = 1;
LAB_0046dd05:
          puVar12 = local_4f0;
          FUN_00428150(&local_46c,uVar7);
          puVar11 = local_4b8;
          goto LAB_0046dd1d;
        }
        goto LAB_0046dd46;
      }
      if (uVar6 == 4) {
        FUN_00428150(&local_434,2);
        puVar12 = local_4f0;
        if (param_5 != (undefined1 *)0x0) {
          puVar11 = local_4b8;
          FUN_00428150(&local_46c,2);
          goto LAB_0046dd1d;
        }
        goto LAB_0046dd46;
      }
      if (uVar6 == 8) {
        FUN_00428150(&local_434,3);
        puVar12 = local_4f0;
        if (param_5 != (undefined1 *)0x0) {
          uVar7 = 3;
          goto LAB_0046dd05;
        }
        goto LAB_0046dd46;
      }
    }
    else {
      uVar6 = local_418;
      if (local_414 < local_418) {
        uVar6 = local_414;
      }
      if (DAT_00784468 < uVar6) {
        uVar6 = DAT_00784468;
      }
      FUN_00427f70(puVar12,uVar6,uVar6);
      puVar12 = local_4f0;
      if (param_5 != (undefined1 *)0x0) {
        FUN_00427f70(puVar11,uVar6,uVar6);
        puVar11 = local_4b8;
      }
      *(char *)(param_1 + 0x448) = (char)(local_418 / uVar6);
      *(char *)(param_1 + 0x449) = (char)(local_414 / uVar6);
LAB_0046dd1d:
      if (param_5 == (undefined1 *)0x0) {
LAB_0046dd46:
        puVar11 = (undefined4 *)0x0;
      }
      else {
        FUN_00470310(&param_5);
        FUN_004703b0(local_21c);
      }
      FUN_0046ca70(puVar11);
      local_8._0_1_ = 0x3f;
      switch(*(undefined2 *)(puVar12[1] + 0xe)) {
      case 8:
        local_47c = (undefined2 *)0x0;
        break;
      default:
        local_47c = local_b24[0];
        break;
      case 0x10:
        local_47c = (undefined2 *)0x3;
        break;
      case 0x18:
        local_47c = (undefined2 *)0x6;
        break;
      case 0x20:
        local_47c = (undefined2 *)0x8;
      }
      local_474 = puVar12[7];
      uVar6 = (uint)(*(ushort *)(puVar12[1] + 0xe) >> 3);
      if (uVar6 == 0) {
        local_478 = local_474 + 0x1fU >> 3;
      }
      else {
        local_478 = uVar6 * local_474 + 3 & 0xfffffffc;
      }
      local_480 = puVar12[3];
      local_470 = puVar12[8];
      piVar8 = local_508;
      puVar11 = (undefined4 *)puVar12[2];
      puVar12 = local_b14;
      for (iVar10 = 0x100; iVar10 != 0; iVar10 = iVar10 + -1) {
        *puVar12 = *puVar11;
        puVar11 = puVar11 + 1;
        puVar12 = puVar12 + 1;
      }
      if (local_508[0] == 0) {
        piVar8 = (int *)0x0;
      }
      cVar5 = FUN_0046ed60(local_b14,&local_480,piVar8,param_4,local_b14,0,param_2,param_3);
      if (cVar5 != '\0') {
        local_8._0_1_ = 0x3e;
        FUN_0046d660();
        local_8._0_1_ = 0x3d;
        FUN_00428380();
        local_8._0_1_ = 1;
        FUN_00428380();
        local_8 = (uint)local_8._1_3_ << 8;
        FUN_00428380();
        local_8 = 0xffffffff;
        FUN_00428380();
        goto LAB_0046df38;
      }
      local_8._0_1_ = 0x3e;
      FUN_0046d660();
    }
    local_8._0_1_ = 0x3d;
    FUN_00428380();
    local_8._0_1_ = 1;
    FUN_00428380();
  }
  local_8 = (uint)local_8._1_3_ << 8;
  FUN_00428380();
  local_8 = 0xffffffff;
  FUN_00428380();
LAB_0046df38:
  ExceptionList = local_10;
  __security_check_cookie(local_14 ^ (uint)&stack0xfffffffc);
  return;
}


```

## `0046df90`

- Function: `FUN_0046df90`
- Entry: `0046df90`

```c

void FUN_0046df90(undefined4 param_1,undefined4 param_2,undefined4 param_3)

{
  uint uVar1;
  int iVar2;
  undefined4 *puVar3;
  void *local_28;
  undefined4 local_24;
  undefined4 local_20;
  undefined4 local_1c;
  undefined4 local_18;
  uint local_14;
  void *local_10;
  undefined1 *puStack_c;
  undefined4 uStack_8;
  
  uStack_8 = 0xffffffff;
  puStack_c = &LAB_00663e20;
  local_10 = ExceptionList;
  uVar1 = DAT_007360c8 ^ (uint)&stack0xfffffffc;
  ExceptionList = &local_10;
  local_14 = uVar1;
  iVar2 = FUN_004a4d00(param_2,param_3);
  if (iVar2 != 0) {
    puVar3 = (undefined4 *)FUN_005b2470(uVar1);
    local_28 = (void *)*puVar3;
    local_24 = puVar3[1];
    local_20 = puVar3[2];
    local_1c = puVar3[3];
    local_18 = puVar3[4];
    FUN_0046ed60(local_1c,&local_28,0,param_1,0,local_1c,param_2,param_3);
    FID_conflict__free(local_28);
  }
  ExceptionList = local_10;
  __security_check_cookie(local_14 ^ (uint)&stack0xfffffffc);
  return;
}


```

## `0046e050`

- Function: `FUN_0046e050`
- Entry: `0046e050`

```c

void FUN_0046e050(undefined4 param_1,undefined4 param_2,undefined4 param_3)

{
  uint uVar1;
  int iVar2;
  undefined4 *puVar3;
  void *local_28;
  undefined4 local_24;
  undefined4 local_20;
  undefined4 local_1c;
  undefined4 local_18;
  uint local_14;
  void *local_10;
  undefined1 *puStack_c;
  undefined4 uStack_8;
  
  uStack_8 = 0xffffffff;
  puStack_c = &LAB_00663e20;
  local_10 = ExceptionList;
  uVar1 = DAT_007360c8 ^ (uint)&stack0xfffffffc;
  ExceptionList = &local_10;
  local_14 = uVar1;
  iVar2 = FUN_004a4d00(param_2,param_3);
  if (iVar2 != 0) {
    puVar3 = (undefined4 *)FUN_005b28a0(uVar1);
    local_28 = (void *)*puVar3;
    local_24 = puVar3[1];
    local_20 = puVar3[2];
    local_1c = puVar3[3];
    local_18 = puVar3[4];
    FUN_0046ed60(local_1c,&local_28,0,param_1,0,local_1c,param_2,param_3);
    FID_conflict__free(local_28);
  }
  ExceptionList = local_10;
  __security_check_cookie(local_14 ^ (uint)&stack0xfffffffc);
  return;
}


```

