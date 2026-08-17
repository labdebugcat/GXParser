# Selected Nova1492 Decompilation

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

## `0042eac0`

- Function: `FUN_0042eac0`
- Entry: `0042eac0`

```c

void __fastcall FUN_0042eac0(int param_1)

{
  int *piVar1;
  int iVar2;
  undefined4 *puVar3;
  undefined4 *puVar4;
  undefined4 uVar5;
  undefined4 local_c0 [4];
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
  undefined4 local_84;
  int local_74;
  undefined4 local_70 [19];
  uint local_24;
  undefined1 *puStack_20;
  void *local_1c;
  undefined1 *puStack_18;
  undefined4 uStack_14;
  
  uStack_14 = 0xffffffff;
  puStack_18 = &LAB_0065b150;
  local_1c = ExceptionList;
  puStack_20 = &stack0xfffffffc;
  local_24 = DAT_007360c8 ^ (uint)&stack0xfffffff0;
  ExceptionList = &local_1c;
  local_74 = param_1;
  local_c0[0] = DAT_008b22e0;
  local_c0[1] = DAT_008b22e4;
  local_c0[2] = DAT_008b22e8;
  local_c0[3] = DAT_008b22ec;
  local_b0 = DAT_008b22f0;
  local_ac = DAT_008b22f4;
  local_a8 = DAT_008b22f8;
  local_a4 = DAT_008b22fc;
  local_a0 = DAT_008b2300;
  local_9c = DAT_008b2304;
  local_98 = DAT_008b2308;
  local_94 = DAT_008b230c;
  local_90 = DAT_008b2310;
  local_8c = DAT_008b2314;
  local_88 = DAT_008b2318;
  local_84 = DAT_008b231c;
  puVar3 = local_c0;
  puVar4 = local_70;
  for (iVar2 = 0x10; iVar2 != 0; iVar2 = iVar2 + -1) {
    *puVar4 = *puVar3;
    puVar3 = puVar3 + 1;
    puVar4 = puVar4 + 1;
  }
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xb0))
            (*(int **)(param_1 + 0x205ac),0x100,local_70,DAT_007360c8 ^ (uint)&stack0xfffffff0);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xb0))(*(int **)(param_1 + 0x205ac),2,local_70);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xb0))(*(int **)(param_1 + 0x205ac),3,local_70);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),7,1);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),8,3);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),9,2);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0xe,1);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0xf,1);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0x10,1);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0x13,5);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0x14,6);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0x17,4);
  piVar1 = *(int **)(param_1 + 0x205ac);
  if (*(char *)(param_1 + 0x2010d) == '\0') {
    (**(code **)(*piVar1 + 0xe4))(piVar1,0x18,0);
    uVar5 = 6;
  }
  else {
    (**(code **)(*piVar1 + 0xe4))(piVar1,0x18,10);
    uVar5 = 5;
  }
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0x19,uVar5);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0x1a,0);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0x1b,0);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0x1c,0);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0x1d,0);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0x22,0xffffffff);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0x23,0);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0xc3,0);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0x30,0);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0x34,0);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0x35,1);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0x36,1);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0x37,1);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0x38,1);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0x39,0);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0x3a,0xffffffff);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0x3b,0xffffffff);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0x3c,0xffffffff);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0x16,2);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0x88,1);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0x89,0);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0x8b,0xffffffff);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0x8c,0);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0x8d,1);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0x8e,1);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0x8f,0);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0x91,1);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0x92,1);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0x93,2);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0x94,0);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0x97,0);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0x98,0);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0x10c))(*(int **)(param_1 + 0x205ac),0,0xb,0);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0x10c))(*(int **)(param_1 + 0x205ac),0,2,2);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0x10c))(*(int **)(param_1 + 0x205ac),0,3,0);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0x10c))(*(int **)(param_1 + 0x205ac),0,1,4);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0x10c))(*(int **)(param_1 + 0x205ac),0,4,4);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0x10c))(*(int **)(param_1 + 0x205ac),0,5,2);
  (**(code **)(**(int **)(param_1 + 0x205ac) + 0x10c))(*(int **)(param_1 + 0x205ac),0,6,0);
  if (*(int *)(param_1 + 0x201ac) != 1) {
    *(undefined4 *)(param_1 + 0x201ac) = 1;
    (**(code **)(**(int **)(param_1 + 0x205ac) + 0x114))(*(int **)(param_1 + 0x205ac),0,6,1);
  }
  if (*(int *)(param_1 + 0x201cc) != 1) {
    *(undefined4 *)(param_1 + 0x201cc) = 1;
    (**(code **)(**(int **)(param_1 + 0x205ac) + 0x114))(*(int **)(param_1 + 0x205ac),0,5,1);
  }
  if (*(int *)(param_1 + 0x2016c) != 3) {
    *(undefined4 *)(param_1 + 0x2016c) = 3;
    (**(code **)(**(int **)(param_1 + 0x205ac) + 0x114))(*(int **)(param_1 + 0x205ac),0,1,3);
  }
  if (*(int *)(param_1 + 0x2018c) != 3) {
    *(undefined4 *)(param_1 + 0x2018c) = 3;
    (**(code **)(**(int **)(param_1 + 0x205ac) + 0x114))(*(int **)(param_1 + 0x205ac),0,2,3);
  }
  ExceptionList = local_1c;
  __security_check_cookie(local_24 ^ (uint)&stack0xfffffff0);
  return;
}


```

## `00431fdc`

- No function found.

## `0043230f`

- No function found.

## `00432473`

- No function found.

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

## `00447250`

- Function: `FUN_00447250`
- Entry: `00447250`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void __thiscall FUN_00447250(int param_1,int param_2,int param_3,int param_4)

{
  float fVar1;
  int *piVar2;
  int iVar3;
  int iVar4;
  int iVar5;
  int iVar6;
  undefined4 *puVar7;
  int iVar8;
  int extraout_ECX;
  int extraout_ECX_00;
  int extraout_ECX_01;
  int iVar9;
  int extraout_ECX_02;
  int iVar10;
  uint uVar11;
  int iVar12;
  uint uVar13;
  undefined4 *puVar14;
  float10 fVar15;
  float fVar16;
  float fVar17;
  float fVar18;
  float fVar19;
  float fVar20;
  undefined4 uVar21;
  undefined4 uVar22;
  undefined4 *local_6c;
  uint local_60;
  int local_54;
  uint local_38;
  undefined4 uStack_30;
  float fStack_2c;
  int iStack_28;
  undefined4 uStack_24;
  undefined1 auStack_20 [28];
  
  if (param_2 == 0) {
    return;
  }
  if (*(int **)(DAT_007b5320 + 0x48) == (int *)0x0) {
    return;
  }
  if (**(int **)(DAT_007b5320 + 0x48) == 0) {
    return;
  }
  iVar5 = FUN_0046bc40(0);
  uVar22 = 0;
  iVar6 = FUN_0046bd80(0);
  switch(param_3) {
  case 0:
    if ((param_4 != 0) || (param_4 = DAT_007c4e50, DAT_007c4e50 != 0)) {
      FUN_0046cd50(param_4);
    }
    if (DAT_00784570 != 4) {
      DAT_00784570 = 4;
      (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x13,2);
      (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x14,2);
    }
    FUN_0042b9e5(1);
    FUN_0042b98b(0);
    FUN_0042ba38(0);
    goto LAB_00447636;
  case 1:
    iVar9 = DAT_007c4e58;
    goto LAB_00447307;
  case 2:
    if (DAT_007c4e3c != 0) {
      FUN_0046cd50(DAT_007c4e3c);
    }
    if (DAT_00784570 != 2) {
      DAT_00784570 = 2;
      (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x13,5);
      (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x14,6);
    }
    FUN_0042ba38(1);
    break;
  default:
    goto switchD_004472aa_caseD_3;
  case 4:
    if ((DAT_007c4ea4 != 0) && (uVar13 = *(uint *)(DAT_007c4ea4 + 8), uVar13 != 0)) {
      fVar15 = (float10)FUN_00480070();
      local_38 = (uint)(longlong)ROUND(fVar15 * (float10)DAT_006dacc8);
      local_38 = local_38 % uVar13;
      uVar21 = 1;
LAB_00447614:
      FUN_00461850(uVar21,local_38,uVar22);
    }
    break;
  case 5:
    if ((DAT_007c4ea8 != 0) && (uVar13 = *(uint *)(DAT_007c4ea8 + 8), uVar13 != 0)) {
      fVar15 = (float10)FUN_00480070();
      local_38 = (uint)(longlong)ROUND(fVar15 * (float10)DAT_006dacc8);
      local_38 = local_38 % uVar13;
      uVar21 = 1;
      goto LAB_00447614;
    }
    break;
  case 6:
    if ((DAT_007c4eac != 0) && (uVar13 = *(uint *)(DAT_007c4eac + 8), uVar13 != 0)) {
      fVar15 = (float10)FUN_00480070();
      local_38 = (uint)(longlong)ROUND(fVar15 * (float10)DAT_006dacc8);
      local_38 = local_38 % uVar13;
      uVar21 = 1;
      goto LAB_00447614;
    }
    break;
  case 7:
    iVar9 = DAT_007c4e40;
LAB_00447307:
    if (iVar9 != 0) {
      FUN_0046cd50(iVar9);
    }
    if (DAT_00784570 != 2) {
      DAT_00784570 = 2;
      (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x13,5);
      (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x14,6);
    }
    break;
  case 8:
    if (DAT_007c4e44 != 0) {
      FUN_0046cd50(DAT_007c4e44);
    }
    if (DAT_00784570 != 3) {
      DAT_00784570 = 3;
      (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x13,5);
      (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x14,2);
    }
    break;
  case 0xb:
    if ((DAT_007c4eb0 != 0) && (uVar13 = *(uint *)(DAT_007c4eb0 + 8), uVar13 != 0)) {
      fVar15 = (float10)FUN_00480070();
      local_38 = (uint)(longlong)ROUND(fVar15 * (float10)DAT_006dacc8);
LAB_0044760a:
      local_38 = local_38 % uVar13;
      uVar21 = 4;
      goto LAB_00447614;
    }
    break;
  case 0xc:
    if ((DAT_007c4eb4 != 0) && (uVar13 = *(uint *)(DAT_007c4eb4 + 8), uVar13 != 0)) {
      fVar15 = (float10)FUN_00480070();
      local_38 = (uint)(longlong)ROUND(fVar15 * (float10)DAT_006dacc8);
      goto LAB_0044760a;
    }
    break;
  case 0xd:
    if ((DAT_007c4eb8 != 0) && (uVar13 = *(uint *)(DAT_007c4eb8 + 8), uVar13 != 0)) {
      fVar15 = (float10)FUN_00480070();
      local_38 = (uint)(longlong)ROUND(fVar15 * (float10)DAT_006dacc8);
      goto LAB_0044760a;
    }
  }
  FUN_0042b9e5(1);
  FUN_0042b98b(0);
LAB_00447636:
  uVar13 = *(uint *)(DAT_007c2478 + 0x10);
  local_6c = (undefined4 *)FUN_00428860(uVar13,&DAT_007c2480);
  if (local_6c != (undefined4 *)0x0) {
    uVar11 = 0;
    local_60 = 0;
    iVar9 = extraout_ECX;
    if (DAT_0078449c != 3) {
      DAT_0078449c = 3;
      (**(code **)(*DAT_007848dc + 0x114))(DAT_007848dc,0,1,3);
      iVar9 = extraout_ECX_00;
    }
    if (DAT_007844bc != 3) {
      DAT_007844bc = 3;
      (**(code **)(*DAT_007848dc + 0x114))(DAT_007848dc,0,2,3);
      iVar9 = extraout_ECX_01;
    }
    if (param_1 != 0) {
      puVar14 = (undefined4 *)(param_2 + 0x10);
      fVar20 = DAT_006da944;
      local_54 = param_1;
      do {
        if (param_3 == 0) {
          uStack_30 = puVar14[-4];
          fStack_2c = (float)puVar14[-3];
          iStack_28 = puVar14[-2];
          uStack_24 = 0x3f800000;
          if (fStack_2c == _DAT_006daf7c) goto LAB_00447776;
          puVar7 = (undefined4 *)FUN_004457c0(auStack_20,&uStack_30,0);
          fVar18 = (float)puVar14[-1];
          uStack_30 = *puVar7;
          fStack_2c = (float)puVar7[1];
          fVar17 = (float)puVar14[-3] - fStack_2c;
          iVar9 = puVar7[2];
          uStack_24 = puVar7[3];
          fVar20 = DAT_006da944;
          iStack_28 = iVar9;
          if (fVar17 < fVar18) {
            fVar18 = SQRT(fVar18 * fVar18 - fVar17 * fVar17);
            goto LAB_0044777b;
          }
        }
        else {
LAB_00447776:
          fVar18 = (float)puVar14[-1];
LAB_0044777b:
          fVar17 = (float)puVar14[-4];
          fVar16 = fVar18 * DAT_006dab58;
          fVar1 = (float)puVar14[-2];
          iVar10 = (int)((fVar17 - fVar18) * fVar20);
          if (iVar10 <= DAT_007c24e4) {
            iVar10 = DAT_007c24e4;
          }
          iVar8 = (int)(fVar17 * fVar20 + fVar18 * fVar20);
          if (DAT_007c24ec <= iVar8) {
            iVar8 = DAT_007c24ec;
          }
          iVar9 = (int)((fVar1 - fVar18) * fVar20);
          if (iVar9 <= DAT_007c24e8) {
            iVar9 = DAT_007c24e8;
          }
          iVar12 = (int)(fVar1 * fVar20 + fVar18 * fVar20);
          fVar18 = DAT_006da974;
          uVar11 = local_60;
          if (DAT_007c24f0 <= iVar12) {
            iVar12 = DAT_007c24f0;
          }
          for (; iVar3 = iVar10, iVar4 = DAT_007c2478, iVar9 <= iVar12; iVar9 = iVar9 + 1) {
            for (; DAT_007c2478 = iVar4, iVar3 <= iVar8; iVar3 = iVar3 + 1) {
              if (*(char *)(DAT_007c24dc * iVar9 + DAT_007c2490 + iVar3) != '\0') {
                if (uVar13 < uVar11 + 4) {
                  if (((*(char *)(iVar4 + 0x34) != '\0') && (*(char *)(iVar4 + 0x35) != '\0')) &&
                     (piVar2 = *(int **)(iVar4 + 0xc), piVar2 != (int *)0x0)) {
                    (**(code **)(*piVar2 + 0x30))(piVar2);
                    *(undefined1 *)(iVar4 + 0x35) = 0;
                  }
                  FUN_00428ab0(local_60,DAT_007c2480,local_60,DAT_007c2484,local_60,
                               (local_60 >> 2) * 6);
                  local_6c = (undefined4 *)FUN_00428860(uVar13,&DAT_007c2480);
                  local_60 = 0;
                  fVar18 = DAT_006da974;
                }
                iVar4 = DAT_007b53ec;
                fVar19 = DAT_006daa00 / fVar16;
                uVar11 = (uint)*(ushort *)(iVar6 + (DAT_007c24dc * iVar9 + iVar3) * 8);
                *local_6c = *(undefined4 *)(DAT_007b53ec + uVar11 * 0xc);
                local_6c[1] = *(undefined4 *)(iVar4 + 4 + uVar11 * 0xc);
                local_6c[2] = *(undefined4 *)(iVar4 + 8 + uVar11 * 0xc);
                local_6c[3] = 0x3f800000;
                local_6c[4] = *puVar14;
                fVar20 = *(float *)(iVar5 + 8 + uVar11 * 0xc);
                local_6c[5] = (*(float *)(iVar5 + uVar11 * 0xc) - fVar17) * fVar19 + fVar18;
                local_6c[6] = fVar19 * (fVar20 - fVar1) + fVar18;
                iVar4 = DAT_007b53ec;
                uVar11 = (uint)*(ushort *)(iVar6 + 2 + (DAT_007c24dc * iVar9 + iVar3) * 8);
                local_6c[7] = *(undefined4 *)(DAT_007b53ec + uVar11 * 0xc);
                local_6c[8] = *(undefined4 *)(iVar4 + 4 + uVar11 * 0xc);
                local_6c[9] = *(undefined4 *)(iVar4 + 8 + uVar11 * 0xc);
                local_6c[10] = 0x3f800000;
                local_6c[0xb] = *puVar14;
                fVar20 = *(float *)(iVar5 + 8 + uVar11 * 0xc);
                local_6c[0xc] = (*(float *)(iVar5 + uVar11 * 0xc) - fVar17) * fVar19 + fVar18;
                local_6c[0xd] = fVar19 * (fVar20 - fVar1) + fVar18;
                iVar4 = DAT_007b53ec;
                uVar11 = (uint)*(ushort *)(iVar6 + 4 + (DAT_007c24dc * iVar9 + iVar3) * 8);
                local_6c[0xe] = *(undefined4 *)(DAT_007b53ec + uVar11 * 0xc);
                local_6c[0xf] = *(undefined4 *)(iVar4 + 4 + uVar11 * 0xc);
                local_6c[0x10] = *(undefined4 *)(iVar4 + 8 + uVar11 * 0xc);
                local_6c[0x11] = 0x3f800000;
                local_6c[0x12] = *puVar14;
                fVar20 = *(float *)(iVar5 + 8 + uVar11 * 0xc);
                local_6c[0x13] = (*(float *)(iVar5 + uVar11 * 0xc) - fVar17) * fVar19 + fVar18;
                local_6c[0x14] = fVar19 * (fVar20 - fVar1) + fVar18;
                iVar4 = DAT_007b53ec;
                uVar11 = (uint)*(ushort *)(iVar6 + 6 + (DAT_007c24dc * iVar9 + iVar3) * 8);
                local_6c[0x15] = *(undefined4 *)(DAT_007b53ec + uVar11 * 0xc);
                local_6c[0x16] = *(undefined4 *)(iVar4 + 4 + uVar11 * 0xc);
                local_6c[0x17] = *(undefined4 *)(iVar4 + 8 + uVar11 * 0xc);
                local_6c[0x18] = 0x3f800000;
                local_6c[0x19] = *puVar14;
                fVar20 = *(float *)(iVar5 + 8 + uVar11 * 0xc);
                local_6c[0x1a] = fVar19 * (*(float *)(iVar5 + uVar11 * 0xc) - fVar17) + fVar18;
                local_6c[0x1b] = fVar19 * (fVar20 - fVar1) + fVar18;
                local_6c = local_6c + 0x1c;
                uVar11 = local_60 + 4;
                local_60 = uVar11;
              }
              iVar4 = DAT_007c2478;
            }
            fVar20 = DAT_006da944;
          }
        }
        puVar14 = puVar14 + 5;
        local_54 = local_54 + -1;
      } while (local_54 != 0);
    }
    iVar5 = DAT_007c2478;
    if ((*(char *)(DAT_007c2478 + 0x34) != '\0') && (*(char *)(DAT_007c2478 + 0x35) != '\0')) {
      piVar2 = *(int **)(DAT_007c2478 + 0xc);
      iVar9 = 0;
      if (piVar2 != (int *)0x0) {
        (**(code **)(*piVar2 + 0x30))(piVar2);
        *(undefined1 *)(iVar5 + 0x35) = 0;
        iVar9 = extraout_ECX_02;
      }
    }
    if (uVar11 != 0) {
      FUN_00428ab0(iVar9,DAT_007c2480,uVar11,DAT_007c2484,iVar9,(uVar11 >> 2) * 6);
    }
    if (DAT_00784570 != 1) {
      DAT_00784570 = 1;
      (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x13,5);
      (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x14,6);
    }
  }
switchD_004472aa_caseD_3:
  return;
}


```

## `00447c00`

- Function: `FUN_00447c00`
- Entry: `00447c00`

```c

void FUN_00447c00(int param_1,int param_2,undefined4 param_3,int param_4)

{
  float fVar1;
  float fVar2;
  int *piVar3;
  bool bVar4;
  uint uVar5;
  undefined4 *puVar6;
  int iVar7;
  int iVar8;
  float *pfVar9;
  uint uVar10;
  uint uVar11;
  int extraout_ECX;
  int extraout_ECX_00;
  int extraout_ECX_01;
  int iVar12;
  int extraout_ECX_02;
  int iVar13;
  uint uVar14;
  int iVar15;
  uint uVar16;
  uint uVar17;
  uint uVar18;
  float10 fVar19;
  float fVar20;
  float fVar21;
  float fVar22;
  float fVar23;
  float fVar24;
  float fVar25;
  float fVar26;
  undefined4 uVar27;
  undefined4 *local_48;
  uint local_44;
  uint local_10;
  
  if (param_1 == 0) {
    return;
  }
  if (param_2 == 0) {
    return;
  }
  if (*(int **)(DAT_007b5320 + 0x48) == (int *)0x0) {
    return;
  }
  if (**(int **)(DAT_007b5320 + 0x48) == 0) {
    return;
  }
  iVar7 = FUN_0046bc40(0);
  uVar27 = 0;
  iVar8 = FUN_0046bd80(0);
  switch(param_3) {
  case 0:
    if (DAT_007c4e50 != 0) {
      FUN_0046cd50(DAT_007c4e50);
    }
    if (DAT_00784570 == 4) break;
    DAT_00784570 = 4;
    uVar27 = 2;
LAB_00447cea:
    (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x13,uVar27);
    uVar27 = 2;
    goto LAB_00447ca4;
  case 1:
    iVar12 = DAT_007c4e58;
    goto LAB_00447c6f;
  case 2:
    if (DAT_007c4e3c != 0) {
      FUN_0046cd50(DAT_007c4e3c);
    }
    if (DAT_00784570 != 2) {
      DAT_00784570 = 2;
      (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x13,5);
      (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x14,6);
    }
    FUN_0042ba38(1);
    break;
  default:
    goto switchD_00447c62_caseD_3;
  case 4:
    if ((DAT_007c4ea4 != 0) && (uVar18 = *(uint *)(DAT_007c4ea4 + 8), uVar18 != 0)) {
      fVar19 = (float10)FUN_00480070();
      local_10 = (uint)(longlong)ROUND(fVar19 * (float10)DAT_006dacc8);
LAB_00447f5e:
      FUN_00461850(1,local_10 % uVar18,uVar27);
    }
    break;
  case 5:
    if ((DAT_007c4ea8 != 0) && (uVar18 = *(uint *)(DAT_007c4ea8 + 8), uVar18 != 0)) {
      fVar19 = (float10)FUN_00480070();
      local_10 = (uint)(longlong)ROUND(fVar19 * (float10)DAT_006dacc8);
      goto LAB_00447f5e;
    }
    break;
  case 6:
    if ((DAT_007c4eac != 0) && (uVar18 = *(uint *)(DAT_007c4eac + 8), uVar18 != 0)) {
      fVar19 = (float10)FUN_00480070();
      local_10 = (uint)(longlong)ROUND(fVar19 * (float10)DAT_006dacc8);
      goto LAB_00447f5e;
    }
    break;
  case 7:
    iVar12 = DAT_007c4e40;
    goto LAB_00447c6f;
  case 8:
    if (DAT_007c4e44 != 0) {
      FUN_0046cd50(DAT_007c4e44);
    }
    if (DAT_00784570 != 3) {
      DAT_00784570 = 3;
      uVar27 = 5;
      goto LAB_00447cea;
    }
    break;
  case 9:
    iVar12 = DAT_007c4e48;
    goto LAB_00447c6f;
  case 10:
    iVar12 = DAT_007c4e4c;
LAB_00447c6f:
    if (iVar12 != 0) {
      FUN_0046cd50(iVar12);
    }
    if (DAT_00784570 != 2) {
      DAT_00784570 = 2;
      (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x13,5);
      uVar27 = 6;
LAB_00447ca4:
      (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x14,uVar27);
    }
    break;
  case 0xb:
    if ((DAT_007c4eb0 != 0) && (uVar18 = *(uint *)(DAT_007c4eb0 + 8), uVar18 != 0)) {
      fVar19 = (float10)FUN_00480070();
      local_10 = (uint)(longlong)ROUND(fVar19 * (float10)DAT_006dacc8);
      goto LAB_00447f5e;
    }
    break;
  case 0xc:
    if ((DAT_007c4eb4 != 0) && (uVar18 = *(uint *)(DAT_007c4eb4 + 8), uVar18 != 0)) {
      fVar19 = (float10)FUN_00480070();
      local_10 = (uint)(longlong)ROUND(fVar19 * (float10)DAT_006dacc8);
      goto LAB_00447f5e;
    }
    break;
  case 0xd:
    if ((DAT_007c4eb8 != 0) && (uVar18 = *(uint *)(DAT_007c4eb8 + 8), uVar18 != 0)) {
      fVar19 = (float10)FUN_00480070();
      local_10 = (uint)(longlong)ROUND(fVar19 * (float10)DAT_006dacc8);
      goto LAB_00447f5e;
    }
  }
  FUN_0042b9e5(1);
  FUN_0042b98b(0);
  uVar18 = DAT_007c2478[4];
  local_48 = (undefined4 *)FUN_00428860(uVar18,&DAT_007c2480);
  if (local_48 != (undefined4 *)0x0) {
    uVar16 = 0;
    local_44 = 0;
    iVar12 = extraout_ECX;
    if (DAT_0078449c != 3) {
      DAT_0078449c = 3;
      (**(code **)(*DAT_007848dc + 0x114))(DAT_007848dc,0,1,3);
      iVar12 = extraout_ECX_00;
    }
    if (DAT_007844bc != 3) {
      DAT_007844bc = 3;
      (**(code **)(*DAT_007848dc + 0x114))(DAT_007848dc,0,2,3);
      iVar12 = extraout_ECX_01;
    }
    if (param_1 != 0) {
      pfVar9 = (float *)(param_2 + 0x10);
      uVar11 = DAT_007c24dc;
      fVar21 = DAT_006da944;
      fVar26 = DAT_006daa00;
      do {
        fVar22 = pfVar9[-2];
        fVar1 = pfVar9[-4];
        fVar20 = fVar22 * DAT_006dab58;
        fVar2 = pfVar9[-3];
        uVar14 = (uint)((fVar1 - fVar22) * fVar21);
        if ((int)uVar14 <= (int)DAT_007c24e4) {
          uVar14 = DAT_007c24e4;
        }
        iVar12 = (int)(fVar1 * fVar21 + fVar22 * fVar21);
        if (DAT_007c24ec <= iVar12) {
          iVar12 = DAT_007c24ec;
        }
        uVar10 = (uint)((fVar2 - fVar22) * fVar21);
        if ((int)uVar10 <= (int)DAT_007c24e8) {
          uVar10 = DAT_007c24e8;
        }
        iVar13 = (int)(fVar2 * fVar21 + fVar22 * fVar21);
        if (DAT_007c24f0 <= iVar13) {
          iVar13 = DAT_007c24f0;
        }
        bVar4 = false;
        if ((int)uVar10 <= iVar13) {
          iVar15 = uVar11 * uVar10 + DAT_007c2490;
          uVar5 = uVar14;
          uVar17 = uVar10;
          do {
            for (; (int)uVar5 <= iVar12; uVar5 = uVar5 + 1) {
              if ((((uVar5 < uVar11) && (uVar17 < DAT_007c24e0)) &&
                  (*(char *)((DAT_007c2494 - DAT_007c2490) + iVar15 + uVar5) != '\0')) &&
                 (*(char *)(iVar15 + uVar5) != '\0')) {
                bVar4 = true;
              }
            }
            uVar17 = uVar17 + 1;
            iVar15 = iVar15 + uVar11;
            uVar16 = local_44;
            uVar5 = uVar14;
          } while ((int)uVar17 <= iVar13);
        }
        if ((param_4 == 0) || (bVar4)) {
          for (; uVar5 = uVar14, puVar6 = DAT_007c2478, (int)uVar10 <= iVar13; uVar10 = uVar10 + 1)
          {
            for (; DAT_007c2478 = puVar6, (int)uVar5 <= iVar12; uVar5 = uVar5 + 1) {
              if (*(char *)(uVar11 * uVar10 + DAT_007c2490 + uVar5) != '\0') {
                if (uVar18 < uVar16 + 4) {
                  if (((*(char *)(puVar6 + 0xd) != '\0') && (*(char *)((int)puVar6 + 0x35) != '\0'))
                     && (piVar3 = (int *)puVar6[3], piVar3 != (int *)0x0)) {
                    (**(code **)(*piVar3 + 0x30))(piVar3);
                    *(undefined1 *)((int)puVar6 + 0x35) = 0;
                  }
                  iVar15 = DAT_007c2480;
                  piVar3 = DAT_007848dc;
                  uVar11 = (uVar16 >> 2) * 6;
                  uVar17 = uVar11 / 3;
                  if (*(char *)(DAT_007c2478 + 0xd) == '\0') {
                    FUN_00432690(4,*DAT_007c2478,DAT_007c2478[2] * DAT_007c2480 + DAT_007c2478[0xc],
                                 uVar16,uVar17,*(undefined4 *)(DAT_007c2484 + 0x18),DAT_007c2478[2])
                    ;
                  }
                  else {
                    FUN_0042f270(DAT_007c2478,DAT_007c2484,uVar11);
                    (**(code **)(*piVar3 + 0x148))(piVar3,4,iVar15,0,local_44,0,uVar17);
                  }
                  local_48 = (undefined4 *)FUN_00428860(uVar18,&DAT_007c2480);
                  local_44 = 0;
                  uVar11 = DAT_007c24dc;
                  fVar26 = DAT_006daa00;
                }
                iVar15 = DAT_007b53ec;
                fVar25 = fVar26 / fVar20;
                uVar16 = (uint)*(ushort *)(iVar8 + (uVar11 * uVar10 + uVar5) * 8);
                *local_48 = *(undefined4 *)(DAT_007b53ec + uVar16 * 0xc);
                local_48[1] = *(undefined4 *)(iVar15 + 4 + uVar16 * 0xc);
                local_48[2] = *(undefined4 *)(iVar15 + 8 + uVar16 * 0xc);
                local_48[3] = 0x3f800000;
                local_48[4] = pfVar9[-1];
                fVar21 = (*(float *)(iVar7 + 8 + uVar16 * 0xc) - fVar2) * fVar25;
                fVar23 = (*(float *)(iVar7 + uVar16 * 0xc) - fVar1) * fVar25;
                fVar22 = fVar21 * pfVar9[1] + fVar23 * *pfVar9 + DAT_006da974;
                local_48[5] = (fVar23 * pfVar9[1] - fVar21 * *pfVar9) + DAT_006da974;
                local_48[6] = fVar22;
                iVar15 = DAT_007b53ec;
                uVar16 = (uint)*(ushort *)(iVar8 + 2 + (DAT_007c24dc * uVar10 + uVar5) * 8);
                local_48[7] = *(undefined4 *)(DAT_007b53ec + uVar16 * 0xc);
                local_48[8] = *(undefined4 *)(iVar15 + 4 + uVar16 * 0xc);
                local_48[9] = *(undefined4 *)(iVar15 + 8 + uVar16 * 0xc);
                local_48[10] = 0x3f800000;
                local_48[0xb] = pfVar9[-1];
                fVar21 = (*(float *)(iVar7 + 8 + uVar16 * 0xc) - fVar2) * fVar25;
                fVar23 = (*(float *)(iVar7 + uVar16 * 0xc) - fVar1) * fVar25;
                fVar22 = fVar21 * pfVar9[1] + fVar23 * *pfVar9 + DAT_006da974;
                local_48[0xc] = (fVar23 * pfVar9[1] - fVar21 * *pfVar9) + DAT_006da974;
                local_48[0xd] = fVar22;
                iVar15 = DAT_007b53ec;
                uVar16 = (uint)*(ushort *)(iVar8 + 4 + (DAT_007c24dc * uVar10 + uVar5) * 8);
                local_48[0xe] = *(undefined4 *)(DAT_007b53ec + uVar16 * 0xc);
                local_48[0xf] = *(undefined4 *)(iVar15 + 4 + uVar16 * 0xc);
                local_48[0x10] = *(undefined4 *)(iVar15 + 8 + uVar16 * 0xc);
                local_48[0x11] = 0x3f800000;
                local_48[0x12] = pfVar9[-1];
                fVar23 = DAT_006da974;
                fVar21 = (*(float *)(iVar7 + 8 + uVar16 * 0xc) - fVar2) * fVar25;
                fVar24 = (*(float *)(iVar7 + uVar16 * 0xc) - fVar1) * fVar25;
                fVar22 = fVar21 * pfVar9[1] + fVar24 * *pfVar9 + DAT_006da974;
                local_48[0x13] = (fVar24 * pfVar9[1] - fVar21 * *pfVar9) + DAT_006da974;
                local_48[0x14] = fVar22;
                iVar15 = DAT_007b53ec;
                uVar11 = (uint)*(ushort *)(iVar8 + 6 + (DAT_007c24dc * uVar10 + uVar5) * 8);
                local_48[0x15] = *(undefined4 *)(DAT_007b53ec + uVar11 * 0xc);
                local_48[0x16] = *(undefined4 *)(iVar15 + 4 + uVar11 * 0xc);
                local_48[0x17] = *(undefined4 *)(iVar15 + 8 + uVar11 * 0xc);
                local_48[0x18] = 0x3f800000;
                local_48[0x19] = pfVar9[-1];
                fVar21 = *pfVar9;
                fVar22 = pfVar9[1];
                uVar16 = local_44 + 4;
                fVar24 = fVar25 * (*(float *)(iVar7 + 8 + uVar11 * 0xc) - fVar2);
                fVar25 = fVar25 * (*(float *)(iVar7 + uVar11 * 0xc) - fVar1);
                local_48[0x1a] = (fVar25 * fVar22 - fVar24 * fVar21) + fVar23;
                local_48[0x1b] = fVar24 * fVar22 + fVar25 * fVar21 + fVar23;
                local_48 = local_48 + 0x1c;
                uVar11 = DAT_007c24dc;
                local_44 = uVar16;
              }
              puVar6 = DAT_007c2478;
            }
            fVar21 = DAT_006da944;
          }
        }
        pfVar9 = pfVar9 + 6;
        param_1 = param_1 + -1;
      } while (param_1 != 0);
    }
    puVar6 = DAT_007c2478;
    if ((*(char *)(DAT_007c2478 + 0xd) != '\0') && (*(char *)((int)DAT_007c2478 + 0x35) != '\0')) {
      piVar3 = (int *)DAT_007c2478[3];
      iVar12 = 0;
      if (piVar3 != (int *)0x0) {
        (**(code **)(*piVar3 + 0x30))(piVar3);
        *(undefined1 *)((int)puVar6 + 0x35) = 0;
        iVar12 = extraout_ECX_02;
      }
    }
    if (uVar16 != 0) {
      FUN_00428ab0(iVar12,DAT_007c2480,uVar16,DAT_007c2484,iVar12,(uVar16 >> 2) * 6);
    }
    if (DAT_00784570 != 1) {
      DAT_00784570 = 1;
      (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x13,5);
      (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x14,6);
    }
  }
switchD_00447c62_caseD_3:
  return;
}


```

## `0044bf60`

- Function: `FUN_0044bf60`
- Entry: `0044bf60`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_0044bf60(void)

{
  undefined4 uVar1;
  ushort uVar2;
  ushort uVar3;
  int *piVar4;
  float *pfVar5;
  undefined4 extraout_ECX;
  undefined4 extraout_ECX_00;
  int iVar6;
  int extraout_ECX_01;
  int iVar7;
  uint uVar8;
  ushort *puVar9;
  uint uVar10;
  int iVar11;
  float fVar12;
  float fVar13;
  float fVar14;
  float fVar15;
  float fVar16;
  float fVar17;
  float fVar18;
  undefined8 uVar19;
  undefined1 auStack_138 [4];
  int iStack_134;
  float fStack_130;
  float fStack_12c;
  int local_11c;
  int iStack_118;
  uint uStack_114;
  ushort *puStack_110;
  float *pfStack_10c;
  int iStack_108;
  uint uStack_104;
  int iStack_100;
  uint uStack_fc;
  int iStack_f8;
  int iStack_f4;
  float fStack_f0;
  float fStack_ec;
  float fStack_e8;
  float fStack_e4;
  float fStack_e0;
  float fStack_dc;
  float fStack_d8;
  undefined4 uStack_d4;
  float fStack_d0;
  float fStack_cc;
  float fStack_c8;
  undefined4 uStack_c4;
  float fStack_c0;
  float fStack_bc;
  float fStack_b8;
  undefined4 uStack_b4;
  float fStack_b0;
  float fStack_ac;
  float fStack_a8;
  undefined4 uStack_a4;
  undefined1 auStack_a0 [16];
  undefined1 auStack_90 [16];
  undefined1 auStack_80 [16];
  undefined1 auStack_70 [16];
  float fStack_60;
  undefined4 uStack_5c;
  undefined4 uStack_58;
  undefined4 uStack_54;
  undefined4 uStack_50;
  undefined4 uStack_4c;
  undefined4 uStack_48;
  undefined4 uStack_44;
  undefined4 uStack_40;
  undefined4 uStack_3c;
  undefined4 uStack_38;
  undefined4 uStack_34;
  undefined4 uStack_30;
  undefined4 uStack_2c;
  undefined4 uStack_28;
  undefined4 uStack_24;
  uint local_14;
  
  local_14 = DAT_007360c8 ^ (uint)auStack_138;
  if ((((DAT_007b5320 != 0) && (DAT_007850e4 != 0)) && (DAT_00784440 != '\0')) &&
     ((*(int **)(DAT_007b5320 + 0x48) != (int *)0x0 && (**(int **)(DAT_007b5320 + 0x48) != 0)))) {
    local_11c = FUN_0046bc40(0);
    FUN_0046cd50(extraout_ECX);
    FUN_0042b9e5(1);
    if (DAT_00784570 != 8) {
      DAT_00784570 = 8;
      (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x13,1);
      (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x14,3);
    }
    FUN_0042b98b(0);
    iStack_100 = FUN_0046bd80(0);
    if (DAT_0078449c != 3) {
      DAT_0078449c = 3;
      (**(code **)(*DAT_007848dc + 0x114))(DAT_007848dc,0,1,3);
    }
    if (DAT_007844bc != 3) {
      DAT_007844bc = 3;
      (**(code **)(*DAT_007848dc + 0x114))(DAT_007848dc,0,2,3);
    }
    uVar8 = 0;
    uStack_114 = 0;
    iStack_134 = FUN_00428860(300,&DAT_007c2480);
    if (iStack_134 != 0) {
      pfStack_10c = &fStack_60;
      fStack_60 = _DAT_006db080;
      uStack_5c = _UNK_006db084;
      uStack_58 = _UNK_006db088;
      uStack_54 = _UNK_006db08c;
      uStack_50 = _DAT_006db090;
      uStack_4c = _UNK_006db094;
      uStack_48 = _UNK_006db098;
      uStack_44 = _UNK_006db09c;
      uStack_40 = _DAT_006db100;
      uStack_3c = _UNK_006db104;
      uStack_38 = _UNK_006db108;
      uStack_34 = _UNK_006db10c;
      uStack_30 = _DAT_006db110;
      uStack_2c = _UNK_006db114;
      uStack_28 = _UNK_006db118;
      uStack_24 = _UNK_006db11c;
      uStack_104 = 0;
      iVar7 = DAT_007c24dc;
      iVar11 = DAT_007c24e0;
      fVar16 = DAT_006daa00;
      fVar17 = DAT_006da974;
      fVar18 = DAT_006daf0c;
      do {
        iStack_108 = 0;
        if (0 < iVar7 * iVar11) {
          puVar9 = (ushort *)(iStack_100 + 4);
          iVar6 = DAT_007c24e0;
          do {
            iVar7 = iStack_108;
            if (*(char *)(DAT_007c2490 + iStack_108) != '\0') {
              puStack_110 = puVar9;
              uVar19 = FUN_0044cdf0(iStack_108);
              iVar6 = DAT_007c24e0;
              iVar7 = (int)((ulonglong)uVar19 >> 0x20);
              if ((int)uVar19 != 0) {
                if (300 < uVar8 + 4) {
                  FUN_00428a00();
                  FUN_00428ab0(extraout_ECX_00,DAT_007c2480,uVar8,DAT_007c2484,extraout_ECX_00,
                               (uVar8 >> 2) * 6);
                  uVar8 = 0;
                  uStack_114 = 0;
                  iStack_134 = FUN_00428860(300,&DAT_007c2480);
                  fVar16 = DAT_006daa00;
                  fVar17 = DAT_006da974;
                  fVar18 = DAT_006daf0c;
                  if (iStack_134 == 0) goto LAB_0044c667;
                }
                uVar2 = puVar9[-2];
                iStack_118 = uVar8 * 7;
                uVar3 = puVar9[-1];
                uVar10 = (uint)*puVar9;
                uStack_fc = (uint)puStack_110[1];
                uStack_d4 = 0x3f800000;
                *(undefined4 *)(iStack_134 + 0x10 + uVar8 * 0x1c) = 0xffffffff;
                *(undefined4 *)(iStack_134 + 0x2c + uVar8 * 0x1c) = 0xffffffff;
                *(undefined4 *)(iStack_134 + 0x48 + uVar8 * 0x1c) = 0xffffffff;
                *(undefined4 *)(iStack_134 + 100 + uVar8 * 0x1c) = 0xffffffff;
                iStack_f8 = (uint)uVar2 * 0xc;
                fStack_e0 = *(float *)(iStack_f8 + local_11c);
                fStack_dc = *(float *)(iStack_f8 + 4 + local_11c);
                fStack_d8 = *(float *)(iStack_f8 + 8 + local_11c);
                fVar12 = *pfStack_10c;
                fVar13 = pfStack_10c[1];
                fVar14 = pfStack_10c[2];
                fVar15 = pfStack_10c[3];
                fStack_f0 = fVar12 + fStack_e0;
                fStack_ec = fVar13 + fStack_dc;
                fStack_e8 = fVar14 + fStack_d8;
                fStack_e4 = fVar15 + 1.0;
                pfVar5 = (float *)FUN_00435730(auStack_a0,&fStack_f0);
                uStack_c4 = 0x3f800000;
                fStack_130 = *pfVar5;
                fStack_12c = pfVar5[1];
                *(float *)(iStack_134 + 0x14 + iStack_118 * 4) = (fStack_130 + fVar16) * fVar17;
                *(float *)(iStack_134 + 0x18 + iStack_118 * 4) = (fStack_12c - fVar16) * fVar18;
                iStack_f4 = (uint)uVar3 * 0xc;
                fStack_d0 = *(float *)(iStack_f4 + local_11c);
                fStack_cc = *(float *)(iStack_f4 + 4 + local_11c);
                fStack_c8 = *(float *)(iStack_f4 + 8 + local_11c);
                fStack_f0 = fVar12 + fStack_d0;
                fStack_ec = fVar13 + fStack_cc;
                fStack_e8 = fVar14 + fStack_c8;
                fStack_e4 = fVar15 + 1.0;
                pfVar5 = (float *)FUN_00435730(auStack_90,&fStack_f0);
                iVar7 = iStack_118;
                fStack_130 = *pfVar5;
                fStack_12c = pfVar5[1];
                *(float *)(iStack_134 + 0x30 + iStack_118 * 4) = (fStack_130 + fVar16) * fVar17;
                uStack_b4 = 0x3f800000;
                *(float *)(iStack_134 + 0x34 + iStack_118 * 4) = (fStack_12c - fVar16) * fVar18;
                fStack_c0 = *(float *)(local_11c + uVar10 * 0xc);
                fStack_bc = *(float *)(local_11c + 4 + uVar10 * 0xc);
                fStack_b8 = *(float *)(local_11c + 8 + uVar10 * 0xc);
                fStack_f0 = fVar12 + fStack_c0;
                fStack_ec = fVar13 + fStack_bc;
                fStack_e8 = fVar14 + fStack_b8;
                fStack_e4 = fVar15 + 1.0;
                pfVar5 = (float *)FUN_00435730(auStack_80,&fStack_f0);
                uVar8 = uStack_fc;
                uStack_a4 = 0x3f800000;
                fStack_130 = *pfVar5;
                fStack_12c = pfVar5[1];
                *(float *)(iStack_134 + 0x4c + iVar7 * 4) = (fStack_130 + fVar16) * fVar17;
                *(float *)(iStack_134 + 0x50 + iVar7 * 4) = (fStack_12c - fVar16) * fVar18;
                fStack_b0 = *(float *)(local_11c + uStack_fc * 0xc);
                fStack_ac = *(float *)(local_11c + 4 + uStack_fc * 0xc);
                fStack_a8 = *(float *)(local_11c + 8 + uStack_fc * 0xc);
                fStack_f0 = fVar12 + fStack_b0;
                fStack_ec = fVar13 + fStack_ac;
                fStack_e8 = fVar14 + fStack_a8;
                fStack_e4 = fVar15 + 1.0;
                pfVar5 = (float *)FUN_00435730(auStack_70,&fStack_f0);
                fStack_130 = *pfVar5;
                fStack_12c = pfVar5[1];
                *(float *)(iStack_134 + 0x68 + iStack_118 * 4) = (fStack_130 + fVar16) * fVar17;
                *(float *)(iStack_134 + 0x6c + iStack_118 * 4) = (fStack_12c - fVar16) * fVar18;
                *(undefined4 *)(iStack_134 + iStack_118 * 4) =
                     *(undefined4 *)(iStack_f8 + DAT_007b53ec);
                *(undefined4 *)(iStack_134 + 4 + iStack_118 * 4) =
                     *(undefined4 *)(iStack_f8 + 4 + DAT_007b53ec);
                *(undefined4 *)(iStack_134 + 8 + iStack_118 * 4) =
                     *(undefined4 *)(iStack_f8 + 8 + DAT_007b53ec);
                *(undefined4 *)(iStack_134 + 0xc + iStack_118 * 4) = 0x3f800000;
                *(undefined4 *)(iStack_134 + 0x1c + iStack_118 * 4) =
                     *(undefined4 *)(iStack_f4 + DAT_007b53ec);
                *(undefined4 *)(iStack_134 + 0x20 + iStack_118 * 4) =
                     *(undefined4 *)(iStack_f4 + 4 + DAT_007b53ec);
                *(undefined4 *)(iStack_134 + 0x24 + iStack_118 * 4) =
                     *(undefined4 *)(iStack_f4 + 8 + DAT_007b53ec);
                *(undefined4 *)(iStack_134 + 0x28 + iStack_118 * 4) = 0x3f800000;
                *(undefined4 *)(iStack_134 + 0x38 + iStack_118 * 4) =
                     *(undefined4 *)(DAT_007b53ec + uVar10 * 0xc);
                *(undefined4 *)(iStack_134 + 0x3c + iStack_118 * 4) =
                     *(undefined4 *)(DAT_007b53ec + 4 + uVar10 * 0xc);
                *(undefined4 *)(iStack_134 + 0x40 + iStack_118 * 4) =
                     *(undefined4 *)(DAT_007b53ec + 8 + uVar10 * 0xc);
                *(undefined4 *)(iStack_134 + 0x44 + iStack_118 * 4) = 0x3f800000;
                *(undefined4 *)(iStack_134 + 0x54 + iStack_118 * 4) =
                     *(undefined4 *)(DAT_007b53ec + uVar8 * 0xc);
                *(undefined4 *)(iStack_134 + 0x58 + iStack_118 * 4) =
                     *(undefined4 *)(DAT_007b53ec + 4 + uVar8 * 0xc);
                uVar1 = *(undefined4 *)(DAT_007b53ec + 8 + uVar8 * 0xc);
                uVar8 = uStack_114 + 4;
                *(undefined4 *)(iStack_134 + 0x60 + iStack_118 * 4) = 0x3f800000;
                *(undefined4 *)(iStack_134 + 0x5c + iStack_118 * 4) = uVar1;
                iVar6 = DAT_007c24e0;
                iVar7 = iStack_108;
                puVar9 = puStack_110;
                uStack_114 = uVar8;
              }
            }
            iStack_108 = iVar7 + 1;
            puVar9 = puVar9 + 4;
            iVar7 = DAT_007c24dc;
            iVar11 = DAT_007c24e0;
            puStack_110 = puVar9;
          } while (iStack_108 < DAT_007c24dc * iVar6);
        }
        iVar6 = DAT_007c2478;
        pfStack_10c = pfStack_10c + 4;
        uStack_104 = uStack_104 + 1;
      } while (uStack_104 < 4);
      if ((*(char *)(DAT_007c2478 + 0x34) != '\0') && (*(char *)(DAT_007c2478 + 0x35) != '\0')) {
        piVar4 = *(int **)(DAT_007c2478 + 0xc);
        iVar7 = 0;
        if (piVar4 != (int *)0x0) {
          (**(code **)(*piVar4 + 0x30))(piVar4);
          *(undefined1 *)(iVar6 + 0x35) = 0;
          iVar7 = extraout_ECX_01;
        }
      }
      if (uVar8 != 0) {
        FUN_00428ab0(iVar7,DAT_007c2480,uVar8,DAT_007c2484,iVar7,(uVar8 >> 2) * 6);
      }
      if (DAT_00784570 != 1) {
        DAT_00784570 = 1;
        (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x13,5);
        (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x14,6);
      }
      if (DAT_00784576 != '\0') {
        DAT_00784576 = '\0';
        (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x1b,0);
      }
      if (DAT_00784574 != '\x01') {
        DAT_00784574 = '\x01';
        (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0xe,1);
      }
    }
  }
LAB_0044c667:
  __security_check_cookie(local_14 ^ (uint)auStack_138);
  return;
}


```

## `0044c680`

- Function: `FUN_0044c680`
- Entry: `0044c680`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_0044c680(void)

{
  char cVar1;
  int iVar2;
  int iVar3;
  uint uVar4;
  uint uVar5;
  uint uVar6;
  undefined4 extraout_ECX;
  undefined4 extraout_ECX_00;
  ushort *puVar7;
  int iVar8;
  ushort *puVar9;
  int iVar10;
  uint uVar11;
  int iVar12;
  float fVar13;
  float fVar14;
  float fVar15;
  float fVar16;
  undefined8 uVar17;
  uint uStack_20;
  int iStack_18;
  
  if ((((DAT_007848dc != (int *)0x0) && (DAT_007b5320 != 0)) && (DAT_007850d8 != 0)) &&
     ((DAT_00784440 != '\0' && (DAT_007c24cc != 0)))) {
    FUN_0046cd50(DAT_007850d8);
    FUN_00431bf0(5,0);
    if ((*(int **)(DAT_007b5320 + 0x48) != (int *)0x0) && (**(int **)(DAT_007b5320 + 0x48) != 0)) {
      FUN_0042b9e5(1);
      if (DAT_00784570 != 8) {
        DAT_00784570 = 8;
        (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x13,1);
        (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x14,3);
      }
      FUN_0042b98b(0);
      iVar2 = FUN_0046bd80(0);
      if (DAT_0078449c != 3) {
        DAT_0078449c = 3;
        (**(code **)(*DAT_007848dc + 0x114))(DAT_007848dc,0,1,3);
      }
      if (DAT_007844bc != 3) {
        DAT_007844bc = 3;
        (**(code **)(*DAT_007848dc + 0x114))(DAT_007848dc,0,2,3);
      }
      uVar11 = 0;
      uStack_20 = 0;
      iVar3 = FUN_00428860(300,&DAT_007c2480);
      if (iVar3 != 0) {
        iVar10 = 0;
        if (0 < DAT_007c24e0 * DAT_007c24dc) {
          puVar7 = (ushort *)(iVar2 + 4);
          iStack_18 = 0;
          iVar2 = DAT_007c24dc;
          do {
            puVar9 = puVar7;
            if (*(char *)(DAT_007c2490 + iVar10) != '\0') {
              uVar17 = FUN_0044cdf0(iVar10);
              iVar2 = DAT_007c24dc;
              puVar9 = (ushort *)((ulonglong)uVar17 >> 0x20);
              if ((int)uVar17 != 0) {
                if (300 < uVar11 + 4) {
                  FUN_00428a00();
                  FUN_00428ab0(extraout_ECX,DAT_007c2480,uVar11,DAT_007c2484,extraout_ECX,
                               (uVar11 >> 2) * 6);
                  uVar11 = 0;
                  uStack_20 = 0;
                  iVar3 = FUN_00428860(300,&DAT_007c2480);
                  if (iVar3 == 0) {
                    return;
                  }
                }
                iVar2 = iVar10 / DAT_007c24dc;
                iVar8 = iVar10 % DAT_007c24dc;
                iVar12 = uVar11 * 8 - uStack_20;
                uVar11 = (uint)puVar7[-2];
                uVar4 = (uint)puVar7[-1];
                uVar5 = (uint)*puVar7;
                uVar6 = (uint)puVar7[1];
                *(undefined4 *)(iVar3 + 0x10 + iVar12 * 4) = 0xffffffff;
                *(undefined4 *)(iVar3 + 0x2c + iVar12 * 4) = 0xffffffff;
                *(undefined4 *)(iVar3 + 0x48 + iVar12 * 4) = 0xffffffff;
                *(undefined4 *)(iVar3 + 100 + iVar12 * 4) = 0xffffffff;
                fVar15 = DAT_007c24bc;
                cVar1 = *(char *)(iStack_18 + 0xc + DAT_007b540c);
                fVar14 = (float)iVar2 * DAT_007c24c0 + _DAT_007c24c8;
                fVar13 = (float)iVar8 * DAT_007c24bc + _DAT_007c24c4;
                fVar16 = DAT_007c24c0 + fVar14;
                *(float *)(iVar3 + 0x18 + iVar12 * 4) = fVar14;
                fVar15 = fVar15 + fVar13;
                *(float *)(iVar3 + 0x30 + iVar12 * 4) = fVar13;
                *(float *)(iVar3 + 0x6c + iVar12 * 4) = fVar16;
                *(float *)(iVar3 + 0x4c + iVar12 * 4) = fVar15;
                if (cVar1 == -0x10) {
                  *(float *)(iVar3 + 0x14 + iVar12 * 4) = fVar15;
                  *(float *)(iVar3 + 0x34 + iVar12 * 4) = fVar14;
                  *(float *)(iVar3 + 0x50 + iVar12 * 4) = fVar16;
                  *(float *)(iVar3 + 0x68 + iVar12 * 4) = fVar13;
                }
                else {
                  *(float *)(iVar3 + 0x14 + iVar12 * 4) = fVar13;
                  *(float *)(iVar3 + 0x34 + iVar12 * 4) = fVar16;
                  *(float *)(iVar3 + 0x50 + iVar12 * 4) = fVar14;
                  *(float *)(iVar3 + 0x68 + iVar12 * 4) = fVar15;
                }
                *(undefined4 *)(iVar3 + iVar12 * 4) = *(undefined4 *)(DAT_007b53ec + uVar11 * 0xc);
                *(undefined4 *)(iVar3 + 4 + iVar12 * 4) =
                     *(undefined4 *)(DAT_007b53ec + 4 + uVar11 * 0xc);
                *(undefined4 *)(iVar3 + 8 + iVar12 * 4) =
                     *(undefined4 *)(DAT_007b53ec + 8 + uVar11 * 0xc);
                *(undefined4 *)(iVar3 + 0xc + iVar12 * 4) = 0x3f800000;
                *(undefined4 *)(iVar3 + 0x1c + iVar12 * 4) =
                     *(undefined4 *)(DAT_007b53ec + uVar4 * 0xc);
                *(undefined4 *)(iVar3 + 0x20 + iVar12 * 4) =
                     *(undefined4 *)(DAT_007b53ec + 4 + uVar4 * 0xc);
                *(undefined4 *)(iVar3 + 0x24 + iVar12 * 4) =
                     *(undefined4 *)(DAT_007b53ec + 8 + uVar4 * 0xc);
                *(undefined4 *)(iVar3 + 0x28 + iVar12 * 4) = 0x3f800000;
                *(undefined4 *)(iVar3 + 0x38 + iVar12 * 4) =
                     *(undefined4 *)(DAT_007b53ec + uVar5 * 0xc);
                *(undefined4 *)(iVar3 + 0x3c + iVar12 * 4) =
                     *(undefined4 *)(DAT_007b53ec + 4 + uVar5 * 0xc);
                *(undefined4 *)(iVar3 + 0x40 + iVar12 * 4) =
                     *(undefined4 *)(DAT_007b53ec + 8 + uVar5 * 0xc);
                *(undefined4 *)(iVar3 + 0x44 + iVar12 * 4) = 0x3f800000;
                *(undefined4 *)(iVar3 + 0x54 + iVar12 * 4) =
                     *(undefined4 *)(DAT_007b53ec + uVar6 * 0xc);
                *(undefined4 *)(iVar3 + 0x58 + iVar12 * 4) =
                     *(undefined4 *)(DAT_007b53ec + 4 + uVar6 * 0xc);
                *(undefined4 *)(iVar3 + 0x5c + iVar12 * 4) =
                     *(undefined4 *)(DAT_007b53ec + 8 + uVar6 * 0xc);
                *(undefined4 *)(iVar3 + 0x60 + iVar12 * 4) = 0x3f800000;
                uVar11 = uStack_20 + 4;
                iVar2 = DAT_007c24dc;
                puVar9 = puVar7;
                uStack_20 = uVar11;
              }
            }
            iVar10 = iVar10 + 1;
            iStack_18 = iStack_18 + 0x10;
            puVar7 = puVar9 + 4;
          } while (iVar10 < DAT_007c24e0 * iVar2);
        }
        FUN_00428a00();
        if (uVar11 != 0) {
          FUN_00428ab0(extraout_ECX_00,DAT_007c2480,uVar11,DAT_007c2484,extraout_ECX_00,
                       (uVar11 >> 2) * 6);
        }
        FUN_0042b9e5(0);
        FUN_0042b98b(1);
      }
    }
  }
  return;
}


```

## `0044f410`

- Function: `FUN_0044f410`
- Entry: `0044f410`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void __fastcall FUN_0044f410(int *param_1)

{
  float *pfVar1;
  ushort uVar2;
  undefined1 uVar3;
  uint uVar4;
  float *pfVar5;
  undefined4 *puVar6;
  int extraout_ECX;
  int extraout_ECX_00;
  uint extraout_ECX_01;
  uint extraout_ECX_02;
  int iVar7;
  undefined4 *extraout_ECX_03;
  undefined4 *extraout_ECX_04;
  undefined4 *extraout_ECX_05;
  float *pfVar8;
  undefined4 *puVar9;
  float fVar10;
  int *piVar11;
  float *pfVar12;
  undefined4 **ppuVar13;
  uint uVar14;
  float fVar15;
  float fVar16;
  float fVar17;
  float fVar18;
  float fVar19;
  undefined1 auStack_1c8 [4];
  float *pfStack_1c4;
  undefined4 *puStack_1c0;
  float *local_1bc;
  int *local_1b8;
  int iStack_1b4;
  uint local_1b0;
  float *pfStack_1ac;
  undefined4 *puStack_1a8;
  float *pfStack_1a4;
  float fStack_1a0;
  float fStack_19c;
  undefined4 *puStack_198;
  undefined4 *puStack_194;
  float fStack_190;
  uint uStack_18c;
  uint uStack_188;
  uint uStack_184;
  undefined4 *puStack_180;
  undefined4 uStack_17c;
  undefined4 *puStack_178;
  undefined4 uStack_174;
  float fStack_170;
  float fStack_16c;
  float fStack_168;
  float fStack_164;
  undefined4 *apuStack_160 [3];
  float fStack_154;
  undefined4 uStack_150;
  undefined4 uStack_14c;
  undefined4 uStack_148;
  float fStack_144;
  float fStack_140;
  float fStack_13c;
  float fStack_138;
  float fStack_134;
  undefined4 uStack_130;
  undefined4 uStack_12c;
  undefined4 uStack_128;
  undefined4 uStack_124;
  float afStack_120 [4];
  float fStack_110;
  float fStack_10c;
  float fStack_108;
  float fStack_104;
  float fStack_100;
  float fStack_fc;
  undefined4 uStack_f8;
  float fStack_f4;
  float fStack_f0;
  undefined4 uStack_ec;
  undefined4 uStack_e8;
  float fStack_e4;
  float afStack_e0 [4];
  float fStack_d0;
  float fStack_cc;
  float fStack_c8;
  float fStack_c4;
  float fStack_c0;
  float fStack_bc;
  float fStack_b8;
  float fStack_b4;
  float fStack_b0;
  float fStack_ac;
  float fStack_a8;
  float fStack_a4;
  undefined4 auStack_a0 [16];
  undefined4 auStack_60 [19];
  uint local_14;
  
  local_14 = DAT_007360c8 ^ (uint)auStack_1c8;
  local_1b8 = param_1;
  if ((param_1[2] != 0) && (param_1[0x13] != 0)) {
    FUN_0044ed30();
    uVar14 = 0;
    local_1b0 = 0;
    if (param_1[2] != 0) {
      local_1bc = (float *)0x0;
      do {
        if (*(char *)(local_1b0 + param_1[0xe]) != '\0') {
          puVar9 = (undefined4 *)(param_1[0x15] + (int)local_1bc);
          iVar7 = param_1[0x16];
          *(undefined4 *)(iVar7 + uVar14 * 2) = *puVar9;
          *(undefined4 *)(iVar7 + 4 + uVar14 * 2) = puVar9[1];
          *(undefined4 *)(iVar7 + 8 + uVar14 * 2) = puVar9[2];
          uVar14 = uVar14 + 6;
        }
        local_1b0 = local_1b0 + 1;
        local_1bc = local_1bc + 3;
      } while (local_1b0 < (uint)param_1[2]);
      if (uVar14 != 0) {
        if (*(int *)(param_1[0x13] + 4) != 0) {
          FUN_004618a0(1,*(undefined4 *)(param_1[0x13] + 0xc));
        }
        DAT_00764330 = DAT_0073ae68;
        FUN_00431bf0(5,0);
        if (DAT_0078449c != 2) {
          DAT_0078449c = 2;
          (**(code **)(*DAT_007848dc + 0x114))(DAT_007848dc,0,1,2);
        }
        if (DAT_007844bc != 2) {
          DAT_007844bc = 2;
          (**(code **)(*DAT_007848dc + 0x114))(DAT_007848dc,0,2,2);
        }
        FUN_00432690(4,0x144,param_1[0xc],param_1[0x14],uVar14 / 3,param_1[0x16],0x1c);
        if (DAT_0078449c != 3) {
          DAT_0078449c = 3;
          (**(code **)(*DAT_007848dc + 0x114))(DAT_007848dc,0,1,3);
        }
        if (DAT_007844bc != 3) {
          DAT_007844bc = 3;
          (**(code **)(*DAT_007848dc + 0x114))(DAT_007848dc,0,2,3);
        }
        FUN_00431bf0(5,0);
        if (param_1[1] == 0) {
          iStack_1b4 = 0;
          pfStack_1a4 = (float *)DAT_007c2478[4];
          if ((DAT_007b9324 != 0) && (*param_1 != 0)) {
            if (DAT_007c4e5c != 0) {
              FUN_0046cd50(DAT_007c4e5c);
            }
            if (DAT_00784570 != 4) {
              DAT_00784570 = 4;
              (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x13,2);
              (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x14,2);
            }
            if (DAT_00784576 != '\x01') {
              DAT_00784576 = '\x01';
              (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x1b,1);
            }
            if (DAT_00784574 != '\0') {
              DAT_00784574 = '\0';
              (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0xe,0);
            }
            fVar15 = 0.0;
            fStack_1a0 = 0.0;
            puStack_1c0 = (undefined4 *)FUN_00428860(pfStack_1a4,&iStack_1b4);
            if (puStack_1c0 != (undefined4 *)0x0) {
              uStack_184 = 0;
              iVar7 = extraout_ECX;
              if (DAT_007b9324 != 0) {
                pfStack_1c4 = (float *)&DAT_007b8614;
                iVar7 = DAT_007c24dc;
                fVar16 = DAT_006da944;
                fVar10 = DAT_006daa00;
                do {
                  fVar17 = pfStack_1c4[-1];
                  fVar18 = pfStack_1c4[-4];
                  puStack_194 = (undefined4 *)(fVar17 * DAT_006dab58);
                  puVar9 = (undefined4 *)pfStack_1c4[-2];
                  uVar14 = (uint)((fVar18 - fVar17) * fVar16);
                  local_1b0 = 0;
                  if (0 < (int)uVar14) {
                    local_1b0 = uVar14;
                  }
                  pfStack_1ac = (float *)(int)(fVar18 * fVar16 + fVar17 * fVar16);
                  if (iVar7 <= (int)pfStack_1ac) {
                    pfStack_1ac = (float *)(iVar7 + -1);
                  }
                  uVar4 = (uint)(((float)puVar9 - fVar17) * fVar16);
                  uVar14 = 0;
                  if (0 < (int)uVar4) {
                    uVar14 = uVar4;
                  }
                  fStack_19c = (float)(int)((float)puVar9 * fVar16 + fVar17 * fVar16);
                  if (DAT_007c24e0 <= (int)fStack_19c) {
                    fStack_19c = (float)(DAT_007c24e0 + -1);
                  }
                  puStack_1a8 = puVar9;
                  fStack_190 = fVar18;
                  uStack_188 = uVar14;
                  if ((int)uVar14 <= (int)fStack_19c) {
                    do {
                      uStack_18c = local_1b0;
                      param_1 = local_1b8;
                      uStack_188 = uVar14;
                      if ((int)local_1b0 <= (int)pfStack_1ac) {
                        do {
                          puVar6 = DAT_007c2478;
                          uVar2 = *(ushort *)(*param_1 + (iVar7 * uVar14 + uStack_18c) * 2);
                          pfVar5 = (float *)(uint)uVar2;
                          if ((uVar2 != 0xffff) &&
                             (local_1bc = pfVar5, *(char *)((int)pfVar5 + param_1[0xe]) != '\0')) {
                            if (pfStack_1a4 < (float *)((int)fVar15 + 4)) {
                              if (((*(char *)(DAT_007c2478 + 0xd) != '\0') &&
                                  (*(char *)((int)DAT_007c2478 + 0x35) != '\0')) &&
                                 (piVar11 = (int *)DAT_007c2478[3], piVar11 != (int *)0x0)) {
                                (**(code **)(*piVar11 + 0x30))(piVar11);
                                *(undefined1 *)((int)puVar6 + 0x35) = 0;
                              }
                              FUN_00428ab0(fStack_1a0,iStack_1b4,fStack_1a0,DAT_007c2484,fStack_1a0,
                                           ((uint)fStack_1a0 >> 2) * 6);
                              puStack_1c0 = (undefined4 *)FUN_00428860(pfStack_1a4,&iStack_1b4);
                              fStack_1a0 = 0.0;
                              fVar18 = fStack_190;
                              puVar9 = puStack_1a8;
                              fVar10 = DAT_006daa00;
                            }
                            fVar17 = fVar10 / (float)puStack_194;
                            uVar14 = (uint)*(ushort *)(param_1[0x15] + (int)local_1bc * 0xc);
                            iVar7 = local_1b8[0xc];
                            *puStack_1c0 = *(undefined4 *)(iVar7 + uVar14 * 0x1c);
                            puStack_1c0[1] = *(undefined4 *)(iVar7 + 4 + uVar14 * 0x1c);
                            puStack_1c0[2] = *(undefined4 *)(iVar7 + 8 + uVar14 * 0x1c);
                            puStack_1c0[3] = 0x3f800000;
                            puStack_1c0[4] = *pfStack_1c4;
                            fVar16 = DAT_006da974;
                            fVar15 = *(float *)(local_1b8[0xd] + 8 + uVar14 * 0x10);
                            puStack_1c0[5] =
                                 (*(float *)(local_1b8[0xd] + uVar14 * 0x10) - fVar18) * fVar17 +
                                 DAT_006da974;
                            puStack_1c0[6] = fVar17 * (fVar15 - (float)puVar9) + fVar16;
                            iVar7 = local_1b8[0xc];
                            uVar14 = (uint)*(ushort *)(local_1b8[0x15] + 2 + (int)local_1bc * 0xc);
                            puStack_1c0[7] = *(undefined4 *)(iVar7 + uVar14 * 0x1c);
                            puStack_1c0[8] = *(undefined4 *)(iVar7 + 4 + uVar14 * 0x1c);
                            puStack_1c0[9] = *(undefined4 *)(iVar7 + 8 + uVar14 * 0x1c);
                            puStack_1c0[10] = 0x3f800000;
                            puStack_1c0[0xb] = *pfStack_1c4;
                            fVar15 = *(float *)(local_1b8[0xd] + 8 + uVar14 * 0x10);
                            puStack_1c0[0xc] =
                                 (*(float *)(local_1b8[0xd] + uVar14 * 0x10) - fVar18) * fVar17 +
                                 fVar16;
                            puStack_1c0[0xd] = fVar17 * (fVar15 - (float)puVar9) + fVar16;
                            iVar7 = local_1b8[0xc];
                            uVar14 = (uint)*(ushort *)(local_1b8[0x15] + 4 + (int)local_1bc * 0xc);
                            puStack_1c0[0xe] = *(undefined4 *)(iVar7 + uVar14 * 0x1c);
                            puStack_1c0[0xf] = *(undefined4 *)(iVar7 + 4 + uVar14 * 0x1c);
                            puStack_1c0[0x10] = *(undefined4 *)(iVar7 + 8 + uVar14 * 0x1c);
                            puStack_1c0[0x11] = 0x3f800000;
                            puStack_1c0[0x12] = *pfStack_1c4;
                            fVar15 = *(float *)(local_1b8[0xd] + 8 + uVar14 * 0x10);
                            puStack_1c0[0x13] =
                                 (*(float *)(local_1b8[0xd] + uVar14 * 0x10) - fVar18) * fVar17 +
                                 fVar16;
                            puStack_1c0[0x14] = fVar17 * (fVar15 - (float)puVar9) + fVar16;
                            iVar7 = local_1b8[0xc];
                            uVar14 = (uint)*(ushort *)(local_1b8[0x15] + 10 + (int)local_1bc * 0xc);
                            puStack_1c0[0x15] = *(undefined4 *)(iVar7 + uVar14 * 0x1c);
                            puStack_1c0[0x16] = *(undefined4 *)(iVar7 + 4 + uVar14 * 0x1c);
                            puStack_1c0[0x17] = *(undefined4 *)(iVar7 + 8 + uVar14 * 0x1c);
                            puStack_1c0[0x18] = 0x3f800000;
                            puStack_1c0[0x19] = *pfStack_1c4;
                            fVar15 = *(float *)(local_1b8[0xd] + 8 + uVar14 * 0x10);
                            puStack_1c0[0x1a] =
                                 fVar17 * (*(float *)(local_1b8[0xd] + uVar14 * 0x10) - fVar18) +
                                 fVar16;
                            puStack_1c0[0x1b] = fVar17 * (fVar15 - (float)puVar9) + fVar16;
                            puStack_1c0 = puStack_1c0 + 0x1c;
                            fVar15 = (float)((int)fStack_1a0 + 4);
                            uVar14 = uStack_188;
                            param_1 = local_1b8;
                            fVar18 = fStack_190;
                            local_1bc = (float *)((int)local_1bc * 6);
                            fStack_1a0 = fVar15;
                          }
                          uStack_18c = uStack_18c + 1;
                          iVar7 = DAT_007c24dc;
                        } while ((int)uStack_18c <= (int)pfStack_1ac);
                      }
                      uVar14 = uVar14 + 1;
                      fVar16 = DAT_006da944;
                      uStack_188 = uVar14;
                    } while ((int)uVar14 <= (int)fStack_19c);
                  }
                  uStack_184 = uStack_184 + 1;
                  pfStack_1c4 = pfStack_1c4 + 5;
                } while (uStack_184 < DAT_007b9324);
              }
              puStack_194 = DAT_007c2478;
              if ((*(char *)(DAT_007c2478 + 0xd) != '\0') &&
                 (*(char *)((int)DAT_007c2478 + 0x35) != '\0')) {
                piVar11 = (int *)DAT_007c2478[3];
                iVar7 = 0;
                if (piVar11 != (int *)0x0) {
                  (**(code **)(*piVar11 + 0x30))(piVar11);
                  *(undefined1 *)((int)puStack_194 + 0x35) = 0;
                  iVar7 = extraout_ECX_00;
                }
              }
              if (fVar15 != 0.0) {
                FUN_00428ab0(iVar7,iStack_1b4,fVar15,DAT_007c2484,iVar7,((uint)fVar15 >> 2) * 6);
              }
            }
          }
          DAT_007b9324 = 0;
          if ((DAT_007bf1c0 != (undefined4 *)0x0) && (*param_1 != 0)) {
            if (DAT_007c4e34 != 0) {
              FUN_0046cd50(DAT_007c4e34);
            }
            if (DAT_00784570 != 4) {
              DAT_00784570 = 4;
              (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x13,2);
              (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x14,2);
            }
            if (DAT_00784576 != '\x01') {
              DAT_00784576 = '\x01';
              (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x1b,1);
            }
            if (DAT_00784574 != '\0') {
              DAT_00784574 = '\0';
              (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0xe,0);
            }
            pfVar5 = (float *)0x0;
            pfStack_1ac = (float *)0x0;
            puStack_1c0 = (undefined4 *)FUN_00428860(pfStack_1a4,&iStack_1b4);
            if (puStack_1c0 != (undefined4 *)0x0) {
              puStack_1a8 = (undefined4 *)0x0;
              uVar14 = extraout_ECX_01;
              if (DAT_007bf1c0 != (undefined4 *)0x0) {
                pfStack_1c4 = (float *)&DAT_007be210;
                fVar15 = DAT_006da944;
                do {
                  fVar16 = pfStack_1c4[-2];
                  fStack_19c = pfStack_1c4[-4];
                  puStack_198 = (undefined4 *)(fVar16 * DAT_006dab58);
                  fStack_1a0 = pfStack_1c4[-3];
                  uVar14 = (uint)((fStack_19c - fVar16) * fVar15);
                  uStack_184 = 0;
                  if (0 < (int)uVar14) {
                    uStack_184 = uVar14;
                  }
                  uVar14 = (uint)(fStack_19c * fVar15 + fVar16 * fVar15);
                  if (DAT_007c24dc <= (int)uVar14) {
                    uVar14 = DAT_007c24dc - 1;
                  }
                  fVar17 = (float)(int)((fStack_1a0 - fVar16) * fVar15);
                  fVar10 = 0.0;
                  if (0 < (int)fVar17) {
                    fVar10 = fVar17;
                  }
                  local_1bc = (float *)(int)(fStack_1a0 * fVar15 + fVar16 * fVar15);
                  if (DAT_007c24e0 <= (int)local_1bc) {
                    local_1bc = (float *)(DAT_007c24e0 + -1);
                  }
                  fStack_190 = fVar10;
                  uStack_18c = uVar14;
                  if ((int)fVar10 <= (int)local_1bc) {
                    do {
                      uStack_188 = uStack_184;
                      fStack_190 = fVar10;
                      if ((int)uStack_184 <= (int)uVar14) {
                        do {
                          puVar9 = DAT_007c2478;
                          uVar2 = *(ushort *)
                                   (*param_1 + ((int)fVar10 * DAT_007c24dc + uStack_188) * 2);
                          puVar6 = (undefined4 *)(uint)uVar2;
                          if ((uVar2 != 0xffff) &&
                             (puStack_194 = puVar6, *(char *)((int)puVar6 + param_1[0xe]) != '\0'))
                          {
                            if (pfStack_1a4 < pfVar5 + 1) {
                              if (((*(char *)(DAT_007c2478 + 0xd) != '\0') &&
                                  (*(char *)((int)DAT_007c2478 + 0x35) != '\0')) &&
                                 (piVar11 = (int *)DAT_007c2478[3], piVar11 != (int *)0x0)) {
                                (**(code **)(*piVar11 + 0x30))(piVar11);
                                *(undefined1 *)((int)puVar9 + 0x35) = 0;
                              }
                              FUN_00428ab0(pfStack_1ac,iStack_1b4,pfStack_1ac,DAT_007c2484,
                                           pfStack_1ac,((uint)pfStack_1ac >> 2) * 6);
                              puStack_1c0 = (undefined4 *)FUN_00428860(pfStack_1a4,&iStack_1b4);
                              pfStack_1ac = (float *)0x0;
                            }
                            local_1b0 = (int)puStack_194 * 6;
                            fVar19 = DAT_006daa00 / (float)puStack_198;
                            uVar14 = (uint)*(ushort *)(param_1[0x15] + (int)puStack_194 * 0xc);
                            iVar7 = local_1b8[0xc];
                            *puStack_1c0 = *(undefined4 *)(iVar7 + uVar14 * 0x1c);
                            puStack_1c0[1] = *(undefined4 *)(iVar7 + 4 + uVar14 * 0x1c);
                            puStack_1c0[2] = *(undefined4 *)(iVar7 + 8 + uVar14 * 0x1c);
                            puStack_1c0[3] = 0x3f800000;
                            puStack_1c0[4] = pfStack_1c4[-1];
                            fVar10 = DAT_006da974;
                            fVar15 = (*(float *)(local_1b8[0xd] + 8 + uVar14 * 0x10) - fStack_1a0) *
                                     fVar19;
                            fVar17 = (*(float *)(local_1b8[0xd] + uVar14 * 0x10) - fStack_19c) *
                                     fVar19;
                            fVar16 = fVar15 * pfStack_1c4[1] + fVar17 * *pfStack_1c4 + DAT_006da974;
                            puStack_1c0[5] =
                                 (fVar17 * pfStack_1c4[1] - fVar15 * *pfStack_1c4) + DAT_006da974;
                            puStack_1c0[6] = fVar16;
                            iVar7 = local_1b8[0xc];
                            uVar14 = (uint)*(ushort *)(local_1b8[0x15] + 2 + (int)puStack_194 * 0xc)
                            ;
                            puStack_1c0[7] = *(undefined4 *)(iVar7 + uVar14 * 0x1c);
                            puStack_1c0[8] = *(undefined4 *)(iVar7 + 4 + uVar14 * 0x1c);
                            puStack_1c0[9] = *(undefined4 *)(iVar7 + 8 + uVar14 * 0x1c);
                            puStack_1c0[10] = 0x3f800000;
                            puStack_1c0[0xb] = pfStack_1c4[-1];
                            fVar15 = *pfStack_1c4;
                            fVar16 = pfStack_1c4[1];
                            fVar18 = (*(float *)(local_1b8[0xd] + uVar14 * 0x10) - fStack_19c) *
                                     fVar19;
                            fVar17 = (*(float *)(local_1b8[0xd] + 8 + uVar14 * 0x10) - fStack_1a0) *
                                     fVar19;
                            puStack_1c0[0xc] = (fVar18 * fVar16 - fVar17 * fVar15) + fVar10;
                            puStack_1c0[0xd] = fVar17 * fVar16 + fVar18 * fVar15 + fVar10;
                            iVar7 = local_1b8[0xc];
                            uVar14 = (uint)*(ushort *)(local_1b8[0x15] + 4 + (int)puStack_194 * 0xc)
                            ;
                            puStack_1c0[0xe] = *(undefined4 *)(iVar7 + uVar14 * 0x1c);
                            puStack_1c0[0xf] = *(undefined4 *)(iVar7 + 4 + uVar14 * 0x1c);
                            puStack_1c0[0x10] = *(undefined4 *)(iVar7 + 8 + uVar14 * 0x1c);
                            puStack_1c0[0x11] = 0x3f800000;
                            puStack_1c0[0x12] = pfStack_1c4[-1];
                            fVar15 = pfStack_1c4[1];
                            fVar16 = *pfStack_1c4;
                            fVar17 = (*(float *)(local_1b8[0xd] + 8 + uVar14 * 0x10) - fStack_1a0) *
                                     fVar19;
                            fVar18 = (*(float *)(local_1b8[0xd] + uVar14 * 0x10) - fStack_19c) *
                                     fVar19;
                            puStack_1c0[0x13] = (fVar18 * fVar15 - fVar17 * fVar16) + fVar10;
                            puStack_1c0[0x14] = fVar17 * fVar15 + fVar18 * fVar16 + fVar10;
                            iVar7 = local_1b8[0xc];
                            uVar14 = (uint)*(ushort *)
                                            (local_1b8[0x15] + 10 + (int)puStack_194 * 0xc);
                            puStack_1c0[0x15] = *(undefined4 *)(iVar7 + uVar14 * 0x1c);
                            puStack_1c0[0x16] = *(undefined4 *)(iVar7 + 4 + uVar14 * 0x1c);
                            puStack_1c0[0x17] = *(undefined4 *)(iVar7 + 8 + uVar14 * 0x1c);
                            puStack_1c0[0x18] = 0x3f800000;
                            puStack_1c0[0x19] = pfStack_1c4[-1];
                            fVar15 = *pfStack_1c4;
                            fVar16 = pfStack_1c4[1];
                            fVar17 = fVar19 * (*(float *)(local_1b8[0xd] + uVar14 * 0x10) -
                                              fStack_19c);
                            fVar19 = fVar19 * (*(float *)(local_1b8[0xd] + 8 + uVar14 * 0x10) -
                                              fStack_1a0);
                            puStack_1c0[0x1a] = (fVar17 * fVar16 - fVar19 * fVar15) + fVar10;
                            puStack_1c0[0x1b] = fVar19 * fVar16 + fVar17 * fVar15 + fVar10;
                            puStack_1c0 = puStack_1c0 + 0x1c;
                            pfVar5 = pfStack_1ac + 1;
                            fVar10 = fStack_190;
                            param_1 = local_1b8;
                            pfStack_1ac = pfVar5;
                          }
                          uStack_188 = uStack_188 + 1;
                          uVar14 = uStack_18c;
                        } while ((int)uStack_188 <= (int)uStack_18c);
                      }
                      fVar10 = (float)((int)fVar10 + 1);
                      fVar15 = DAT_006da944;
                      fStack_190 = fVar10;
                    } while ((int)fVar10 <= (int)local_1bc);
                  }
                  puStack_1a8 = (undefined4 *)((int)puStack_1a8 + 1);
                  pfStack_1c4 = pfStack_1c4 + 6;
                } while (puStack_1a8 < DAT_007bf1c0);
              }
              puStack_198 = DAT_007c2478;
              if ((*(char *)(DAT_007c2478 + 0xd) != '\0') &&
                 (*(char *)((int)DAT_007c2478 + 0x35) != '\0')) {
                piVar11 = (int *)DAT_007c2478[3];
                uVar14 = 0;
                if (piVar11 != (int *)0x0) {
                  (**(code **)(*piVar11 + 0x30))(piVar11);
                  *(undefined1 *)((int)puStack_198 + 0x35) = 0;
                  uVar14 = extraout_ECX_02;
                }
              }
              if (pfVar5 != (float *)0x0) {
                FUN_00428ab0(uVar14,iStack_1b4,pfVar5,DAT_007c2484,uVar14,((uint)pfVar5 >> 2) * 6);
              }
            }
          }
          DAT_007bf1c0 = (undefined4 *)0x0;
          if ((DAT_007c0ea8 != (undefined4 *)0x0) && (*param_1 != 0)) {
            if (DAT_007c4e30 != 0) {
              FUN_0046cd50(DAT_007c4e30);
            }
            if (DAT_00784570 != 4) {
              DAT_00784570 = 4;
              (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x13,2);
              (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x14,2);
            }
            if (DAT_00784576 != '\x01') {
              DAT_00784576 = '\x01';
              (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x1b,1);
            }
            if (DAT_00784574 != '\0') {
              DAT_00784574 = '\0';
              (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0xe,0);
            }
            FUN_00481730(apuStack_160);
            pfVar5 = pfStack_1a4;
            pfVar12 = (float *)&DAT_00736d50;
            pfVar8 = afStack_e0;
            for (iVar7 = 0x10; iVar7 != 0; iVar7 = iVar7 + -1) {
              *pfVar8 = *pfVar12;
              pfVar12 = pfVar12 + 1;
              pfVar8 = pfVar8 + 1;
            }
            pfStack_1c4 = (float *)0x0;
            local_1b0 = FUN_00428860(pfStack_1a4,&iStack_1b4);
            if (local_1b0 != 0) {
              puStack_1a8 = (undefined4 *)0x0;
              puVar9 = extraout_ECX_03;
              pfVar12 = (float *)0x0;
              if (DAT_007c0ea8 != (undefined4 *)0x0) {
                local_1bc = (float *)&DAT_007c0188;
                piVar11 = local_1b8;
                fVar15 = DAT_006da944;
                fVar16 = DAT_006daa00;
                do {
                  uVar2 = *(ushort *)
                           (*piVar11 +
                           ((int)(local_1bc[2] * fVar15) * DAT_007c24dc + (int)(*local_1bc * fVar15)
                           ) * 2);
                  puVar6 = (undefined4 *)(uint)uVar2;
                  puVar9 = (undefined4 *)0xffff;
                  if ((uVar2 != 0xffff) &&
                     (puVar9 = puVar6, puStack_198 = puVar6,
                     *(char *)((int)puVar6 + piVar11[0xe]) != '\0')) {
                    if (pfVar5 < pfStack_1c4 + 1) {
                      FUN_00428a00();
                      FUN_00428ab0(pfStack_1c4,iStack_1b4,pfStack_1c4,DAT_007c2484,pfStack_1c4,
                                   ((uint)pfStack_1c4 >> 2) * 6);
                      local_1b0 = FUN_00428860(pfVar5,&iStack_1b4);
                      pfStack_1c4 = (float *)0x0;
                      fVar16 = DAT_006daa00;
                    }
                    fStack_fc = local_1bc[3];
                    fStack_100 = fStack_fc * DAT_006da974;
                    fStack_154 = *local_1bc;
                    fStack_134 = local_1bc[2];
                    afStack_120[0] = _DAT_008b23d0 * fStack_100;
                    afStack_120[1] = fRam008b23d4 * fStack_fc;
                    afStack_120[2] = fRam008b23d8 * 0.0;
                    afStack_120[3] = fRam008b23dc * fVar16;
                    fStack_110 = _DAT_008b23d0 * fStack_100;
                    fStack_10c = fRam008b23d4 * 0.0;
                    fStack_108 = fRam008b23d8 * 0.0;
                    fStack_104 = fRam008b23dc * fVar16;
                    uStack_f8 = 0;
                    fStack_144 = *(float *)(piVar11[0xb] + 0xc + (int)puStack_198 * 0x10) -
                                 fStack_fc * DAT_006da920;
                    uStack_ec = 0;
                    uStack_e8 = 0;
                    fStack_f4 = fVar16;
                    fStack_f0 = fStack_100;
                    fStack_e4 = fVar16;
                    puVar9 = (undefined4 *)FUN_00435620(auStack_60,apuStack_160);
                    uVar14 = local_1b0;
                    puVar6 = auStack_a0;
                    for (iVar7 = 0x10; iVar7 != 0; iVar7 = iVar7 + -1) {
                      *puVar6 = *puVar9;
                      puVar9 = puVar9 + 1;
                      puVar6 = puVar6 + 1;
                    }
                    FUN_00450c70(afStack_120,0);
                    fVar15 = DAT_006da944;
                    *(float *)(uVar14 + 0x10) = local_1bc[4];
                    *(float *)(uVar14 + 0x2c) = local_1bc[4];
                    *(float *)(uVar14 + 0x48) = local_1bc[4];
                    *(float *)(uVar14 + 100) = local_1bc[4];
                    *(undefined4 *)(uVar14 + 0x14) = 0;
                    *(undefined4 *)(uVar14 + 0x18) = 0;
                    *(undefined4 *)(uVar14 + 0x30) = 0;
                    *(undefined4 *)(uVar14 + 0x34) = 0x3f800000;
                    *(undefined4 *)(uVar14 + 0x4c) = 0x3f800000;
                    *(undefined4 *)(uVar14 + 0x50) = 0;
                    *(undefined4 *)(uVar14 + 0x68) = 0x3f800000;
                    *(undefined4 *)(uVar14 + 0x6c) = 0x3f800000;
                    local_1b0 = uVar14 + 0x70;
                    pfStack_1c4 = pfStack_1c4 + 1;
                    puVar9 = extraout_ECX_04;
                    piVar11 = local_1b8;
                    pfVar5 = pfStack_1a4;
                  }
                  local_1bc = local_1bc + 5;
                  puStack_1a8 = (undefined4 *)((int)puStack_1a8 + 1);
                  pfVar12 = pfStack_1c4;
                } while (puStack_1a8 < DAT_007c0ea8);
              }
              puVar6 = DAT_007c2478;
              if ((*(char *)(DAT_007c2478 + 0xd) != '\0') &&
                 (*(char *)((int)DAT_007c2478 + 0x35) != '\0')) {
                piVar11 = (int *)DAT_007c2478[3];
                puVar9 = (undefined4 *)0x0;
                if (piVar11 != (int *)0x0) {
                  (**(code **)(*piVar11 + 0x30))(piVar11);
                  *(undefined1 *)((int)puVar6 + 0x35) = 0;
                  puVar9 = extraout_ECX_05;
                }
              }
              if (pfVar12 != (float *)0x0) {
                FUN_00428ab0(puVar9,iStack_1b4,pfVar12,DAT_007c2484,puVar9,((uint)pfVar12 >> 2) * 6)
                ;
              }
            }
          }
          DAT_007c0ea8 = (undefined4 *)0x0;
          if (DAT_007c4e38 != 0) {
            FUN_0046cd50(DAT_007c4e38);
          }
          if (DAT_00784570 != 4) {
            DAT_00784570 = 4;
            (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x13,2);
            (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x14,2);
          }
          if (DAT_00784576 != '\x01') {
            DAT_00784576 = '\x01';
            (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x1b,1);
          }
          if (DAT_00784574 != '\0') {
            DAT_00784574 = '\0';
            (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0xe,0);
          }
          pfVar5 = pfStack_1a4;
          puVar9 = &DAT_00736d50;
          puVar6 = auStack_a0;
          for (iVar7 = 0x10; iVar7 != 0; iVar7 = iVar7 + -1) {
            *puVar6 = *puVar9;
            puVar9 = puVar9 + 1;
            puVar6 = puVar6 + 1;
          }
          puStack_1c0 = (undefined4 *)0x0;
          local_1b0 = FUN_00428860(pfStack_1a4,&iStack_1b4);
          if (local_1b0 != 0) {
            pfVar12 = (float *)local_1b8[0x19];
            pfVar8 = pfVar12 + (int)pfVar12[-1] * 0xb;
            puVar9 = (undefined4 *)0x0;
            pfStack_1c4 = pfVar8;
            if (pfVar12 != pfVar8) {
              pfVar12 = pfVar12 + 1;
              piVar11 = local_1b8;
              fVar15 = DAT_006daa00;
              do {
                pfStack_1ac = pfVar12;
                if (*pfVar12 < fVar15) {
                  puStack_1a8 = (undefined4 *)(int)(pfVar12[7] * DAT_006da944);
                  pfVar8 = pfStack_1c4;
                  if (((((int)puStack_1a8 < DAT_007c24dc) &&
                       ((int)(pfVar12[9] * DAT_006da944) < DAT_007c24e0)) &&
                      (uVar2 = *(ushort *)
                                (*piVar11 +
                                ((int)(pfVar12[9] * DAT_006da944) * DAT_007c24dc + (int)puStack_1a8)
                                * 2), uVar2 != 0xffff)) &&
                     (*(char *)((uint)uVar2 + piVar11[0xe]) != '\0')) {
                    if (pfVar5 < puStack_1c0 + 1) {
                      FUN_00428a00();
                      FUN_00428ab0(puStack_1c0,iStack_1b4,puStack_1c0,DAT_007c2484,puStack_1c0,
                                   ((uint)puStack_1c0 >> 2) * 6);
                      local_1b0 = FUN_00428860(pfVar5,&iStack_1b4);
                      puStack_1c0 = (undefined4 *)0x0;
                      fVar15 = DAT_006daa00;
                    }
                    fStack_a8 = *pfVar12 * DAT_006dab58 + DAT_006da974;
                    fStack_ac = _DAT_006dafe0;
                    fStack_a4 = _UNK_006dafe4;
                    afStack_e0[0] = fVar15 * _DAT_008b2430;
                    afStack_e0[1] = _DAT_006dafe0 * fRam008b2434;
                    afStack_e0[2] = fStack_a8 * fRam008b2438;
                    afStack_e0[3] = _UNK_006dafe4 * fRam008b243c;
                    fStack_c0 = fVar15 * _DAT_008b2440;
                    fStack_bc = _DAT_006dafe0 * fRam008b2444;
                    fStack_b8 = fStack_a8 * fRam008b2448;
                    fStack_b4 = _UNK_006dafe4 * fRam008b244c;
                    fStack_d0 = fVar15 * _DAT_008b23d0;
                    fStack_cc = _DAT_006dafe0 * fRam008b23d4;
                    fStack_c8 = fStack_a8 * fRam008b23d8;
                    fStack_c4 = _UNK_006dafe4 * fRam008b23dc;
                    fVar16 = _DAT_008b23d0;
                    fVar10 = fRam008b23d4;
                    fVar17 = fRam008b23d8;
                    fVar18 = fRam008b23dc;
                    fVar19 = DAT_006da974;
                    fStack_b0 = fVar15;
                    FUN_0059c793(pfVar12[-1] * DAT_006daf40 * _DAT_006da8b0);
                    puStack_180 = puStack_194;
                    uStack_17c = 0;
                    puStack_178 = puStack_198;
                    uStack_174 = 0;
                    apuStack_160[0] = puStack_194;
                    apuStack_160[1] = (undefined4 *)0x0;
                    apuStack_160[2] = puStack_198;
                    fStack_154 = 0.0;
                    uStack_150 = DAT_008b22f0;
                    uStack_14c = DAT_008b22f4;
                    uStack_148 = DAT_008b22f8;
                    fStack_144 = DAT_008b22fc;
                    fStack_170 = fVar16 * (float)puStack_198;
                    fStack_16c = fVar10 * 0.0;
                    fStack_168 = fVar17 * (float)puStack_194;
                    fStack_164 = fVar18 * 0.0;
                    fStack_140 = fStack_170;
                    fStack_13c = fStack_16c;
                    fStack_138 = fStack_168;
                    fStack_134 = fStack_164;
                    uStack_130 = DAT_008b2310;
                    uStack_12c = DAT_008b2314;
                    uStack_128 = DAT_008b2318;
                    uStack_124 = DAT_008b231c;
                    ppuVar13 = apuStack_160;
                    pfVar5 = afStack_120;
                    for (iVar7 = 0x10; iVar7 != 0; iVar7 = iVar7 + -1) {
                      *pfVar5 = (float)*ppuVar13;
                      ppuVar13 = ppuVar13 + 1;
                      pfVar5 = pfVar5 + 1;
                    }
                    afStack_120[3] = pfStack_1ac[7];
                    fStack_104 = pfStack_1ac[8];
                    fStack_f4 = pfStack_1ac[9];
                    puVar9 = (undefined4 *)FUN_00435620(apuStack_160,afStack_120);
                    uVar14 = local_1b0;
                    puVar6 = auStack_60;
                    for (iVar7 = 0x10; iVar7 != 0; iVar7 = iVar7 + -1) {
                      *puVar6 = *puVar9;
                      puVar9 = puVar9 + 1;
                      puVar6 = puVar6 + 1;
                    }
                    FUN_00450c70(afStack_e0,0);
                    fVar15 = DAT_006daa00;
                    fVar10 = 0.0;
                    fVar16 = *pfStack_1ac;
                    if ((fVar19 <= fVar16) || (fVar16 < 0.0)) {
                      if (fVar16 < DAT_006daa00) {
                        fVar10 = DAT_006dae64 - (fVar16 - fVar19) * DAT_006dae64 * DAT_006dab58;
                      }
                    }
                    else {
                      fVar10 = fVar16 * DAT_006dae64 * DAT_006dab58;
                    }
                    uVar3 = (undefined1)(int)fVar10;
                    local_1bc = (float *)CONCAT31(CONCAT21(CONCAT11(0xff,uVar3),uVar3),uVar3);
                    *(float **)(uVar14 + 0x10) = local_1bc;
                    *(float **)(uVar14 + 0x2c) = local_1bc;
                    *(float **)(uVar14 + 0x48) = local_1bc;
                    *(float **)(uVar14 + 100) = local_1bc;
                    *(undefined4 *)(uVar14 + 0x14) = 0;
                    *(undefined4 *)(uVar14 + 0x18) = 0x3f800000;
                    *(undefined4 *)(uVar14 + 0x30) = 0x3f800000;
                    *(undefined4 *)(uVar14 + 0x34) = 0x3f800000;
                    *(undefined4 *)(uVar14 + 0x4c) = 0;
                    *(undefined4 *)(uVar14 + 0x50) = 0;
                    *(undefined4 *)(uVar14 + 0x68) = 0x3f800000;
                    *(undefined4 *)(uVar14 + 0x6c) = 0;
                    local_1b0 = uVar14 + 0x70;
                    puStack_1c0 = puStack_1c0 + 1;
                    pfVar8 = pfStack_1c4;
                    piVar11 = local_1b8;
                    pfVar5 = pfStack_1a4;
                  }
                }
                pfVar12 = pfStack_1ac + 0xb;
                pfVar1 = pfStack_1ac + 10;
                puVar9 = puStack_1c0;
                pfStack_1ac = pfVar12;
              } while (pfVar1 != pfVar8);
            }
            puVar6 = DAT_007c2478;
            puStack_1a8 = DAT_007c2478;
            if (((*(char *)(DAT_007c2478 + 0xd) != '\0') &&
                (*(char *)((int)DAT_007c2478 + 0x35) != '\0')) &&
               (piVar11 = (int *)DAT_007c2478[3], piVar11 != (int *)0x0)) {
              (**(code **)(*piVar11 + 0x30))(piVar11);
              *(undefined1 *)((int)puVar6 + 0x35) = 0;
              puStack_1a8 = DAT_007c2478;
            }
            piVar11 = DAT_007848dc;
            DAT_007c2478 = puStack_1a8;
            if (puVar9 != (undefined4 *)0x0) {
              uVar14 = ((uint)puVar9 >> 2) * 6;
              puStack_198 = (undefined4 *)(uVar14 / 3);
              if (*(char *)(puStack_1a8 + 0xd) == '\0') {
                FUN_00432690(4,*puStack_1a8,puStack_1a8[2] * iStack_1b4 + puStack_1a8[0xc],puVar9,
                             puStack_198,*(undefined4 *)(DAT_007c2484 + 0x18),puStack_1a8[2]);
              }
              else {
                FUN_0042f270(puStack_1a8,DAT_007c2484,uVar14);
                (**(code **)(*piVar11 + 0x148))(piVar11,4,iStack_1b4,0,puVar9,0,puStack_198);
              }
            }
          }
          if (DAT_00784570 != 1) {
            DAT_00784570 = 1;
            (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x13,5);
            (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x14,6);
          }
        }
      }
    }
  }
  __security_check_cookie(local_14 ^ (uint)auStack_1c8);
  return;
}


```

## `004618a0`

- Function: `FUN_004618a0`
- Entry: `004618a0`

```c

void __thiscall FUN_004618a0(int *param_1,uint param_2)

{
  bool bVar1;
  undefined4 uVar2;
  
  if (DAT_0078453c == param_1) goto LAB_004619d0;
  DAT_0078453c = param_1;
  if (param_2 == 0) {
    bVar1 = false;
  }
  else {
    bVar1 = param_2 != 1;
    if (!bVar1) {
      param_2 = (uint)*(byte *)(param_1 + 1);
    }
    bVar1 = bVar1 || *(byte *)(param_1 + 1) != 0;
    FUN_0042b89f(param_2);
  }
  if ((param_1[1] & 0x10000U) == 0) {
    if ((param_1[1] & 0x20000U) == 0) {
      if (DAT_0078449c != 3) {
        DAT_0078449c = 3;
        uVar2 = 3;
        goto LAB_00461934;
      }
    }
    else if (DAT_0078449c != 2) {
      DAT_0078449c = 2;
      uVar2 = 2;
LAB_00461934:
      (**(code **)(*DAT_007848dc + 0x114))(DAT_007848dc,0,1,uVar2);
    }
  }
  else if (DAT_0078449c != 1) {
    DAT_0078449c = 1;
    uVar2 = 1;
    goto LAB_00461934;
  }
  if ((param_1[1] & 0x40000U) == 0) {
    if ((param_1[1] & 0x80000U) == 0) {
      if (DAT_007844bc != 3) {
        DAT_007844bc = 3;
        uVar2 = 3;
        goto LAB_0046199a;
      }
    }
    else if (DAT_007844bc != 2) {
      DAT_007844bc = 2;
      uVar2 = 2;
LAB_0046199a:
      (**(code **)(*DAT_007848dc + 0x114))(DAT_007848dc,0,2,uVar2);
    }
  }
  else if (DAT_007844bc != 1) {
    DAT_007844bc = 1;
    uVar2 = 1;
    goto LAB_0046199a;
  }
  if ((bool)DAT_00784576 != bVar1) {
    DAT_00784576 = bVar1;
    (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x1b,bVar1);
  }
LAB_004619d0:
  if ((DAT_0078442e != '\0') && (*param_1 != 0)) {
    FUN_0046cd50(*param_1);
    return;
  }
  DAT_0078451c = 0;
  (**(code **)(*DAT_007848dc + 0x104))(DAT_007848dc,0,0);
  return;
}


```

## `0046cd50`

- Function: `FUN_0046cd50`
- Entry: `0046cd50`

```c

void __fastcall FUN_0046cd50(int param_1)

{
  int iVar1;
  int iVar2;
  int iVar3;
  undefined4 *puVar4;
  int *piVar5;
  undefined4 extraout_ECX;
  undefined4 uVar6;
  undefined1 local_18 [4];
  undefined4 *local_14;
  void *local_10;
  undefined1 *puStack_c;
  undefined4 local_8;
  
  local_8 = 0xffffffff;
  puStack_c = &LAB_006632f8;
  local_10 = ExceptionList;
  if (DAT_0078451c == param_1) {
    return;
  }
  DAT_0078451c = param_1;
  ExceptionList = &local_10;
  if ((*(uint *)(param_1 + 0x444) & 0x1000) == 0) {
    if (DAT_007844fc != 1) {
      DAT_007844fc = 1;
      uVar6 = 1;
      goto LAB_0046cdc4;
    }
  }
  else if (DAT_007844fc != 2) {
    DAT_007844fc = 2;
    uVar6 = 2;
LAB_0046cdc4:
    (**(code **)(*DAT_007848dc + 0x114))
              (DAT_007848dc,0,5,uVar6,DAT_007360c8 ^ (uint)&stack0xfffffffc);
  }
  if ((*(uint *)(param_1 + 0x444) & 0x2000) == 0) {
    if (DAT_007844dc == 1) goto LAB_0046ce20;
    DAT_007844dc = 1;
    uVar6 = 1;
  }
  else {
    if (DAT_007844dc == 2) goto LAB_0046ce20;
    DAT_007844dc = 2;
    uVar6 = 2;
  }
  (**(code **)(*DAT_007848dc + 0x114))(DAT_007848dc,0,6,uVar6);
LAB_0046ce20:
  iVar3 = (**(code **)(*DAT_007848dc + 0x104))(DAT_007848dc,0,*(undefined4 *)(param_1 + 0x440));
  if (iVar3 < 0) {
    puVar4 = (undefined4 *)FUN_0059c260(local_18,0x800,2,*(int *)ThreadLocalStoragePointer + 0xc);
    local_14 = (undefined4 *)*puVar4 + 1;
    *(undefined4 *)*puVar4 = 0;
    local_8 = 0x12;
    FUN_004706e0(extraout_ECX);
    iVar1 = *(int *)(param_1 + 8);
    iVar2 = local_14[-1];
    iVar3 = iVar2 + iVar1;
    FUN_00434ab0(iVar3,iVar3);
    FUN_0062cfd0((int)local_14 + iVar2 * 2,param_1 + 0xc,iVar1 * 2);
    piVar5 = (int *)FUN_00433e10(&DAT_006bee50);
    FUN_00434ab0(*(int *)(*piVar5 + -4),*(int *)(*piVar5 + -4) + 1);
    *(undefined2 *)(*piVar5 + *(int *)(*piVar5 + -4) * 2) = 0;
    local_8 = 0xffffffff;
    if (local_14 != (undefined4 *)&DAT_006b9e28) {
      FUN_0059c360(local_14 + -1);
    }
  }
  ExceptionList = local_10;
  return;
}


```

## `00509090`

- Function: `FUN_00509090`
- Entry: `00509090`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00509090(void)

{
  if (DAT_00784570 != 1) {
    DAT_00784570 = 1;
    (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x13,5);
    (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x14,6);
  }
  if (DAT_007844fc != 1) {
    DAT_007844fc = 1;
    (**(code **)(*DAT_007848dc + 0x114))(DAT_007848dc,0,5,1);
  }
  if (DAT_007844dc != 1) {
    DAT_007844dc = 1;
    (**(code **)(*DAT_007848dc + 0x114))(DAT_007848dc,0,6,1);
  }
  if (DAT_00784576 != '\x01') {
    DAT_00784576 = '\x01';
    (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x1b,1);
  }
  if (DAT_00784580 != '\x01') {
    FUN_00431bf0(0,0);
    DAT_00784580 = '\x01';
    _DAT_00784574 = 0;
  }
  return;
}


```

