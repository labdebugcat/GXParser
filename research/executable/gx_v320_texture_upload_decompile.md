# Selected Nova1492 Decompilation

## `0046ed60`

- Function: `FUN_0046ed60`
- Entry: `0046ed60`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void __thiscall
FUN_0046ed60(int *param_1,undefined4 param_2,void **param_3,int param_4,undefined4 param_5,
            int param_6,undefined4 param_7,undefined4 param_8,undefined4 param_9)

{
  undefined4 uVar1;
  int *piVar2;
  void *pvVar3;
  int iVar4;
  char cVar5;
  uint uVar6;
  int iVar7;
  short *psVar8;
  int iVar10;
  void *pvVar11;
  void *local_3c;
  void *local_34;
  int local_30;
  void *local_2c [5];
  bool local_15;
  uint local_14;
  void *local_10;
  undefined1 *puStack_c;
  undefined4 local_8;
  short *psVar9;
  
  local_8 = 0xffffffff;
  puStack_c = &LAB_00663e88;
  local_10 = ExceptionList;
  uVar6 = DAT_007360c8 ^ (uint)&stack0xfffffffc;
  ExceptionList = &local_10;
  pvVar11 = param_3[1];
  if (param_4 != 0) {
    switch(pvVar11) {
    case (void *)0x0:
    case (void *)0x6:
    case (void *)0x7:
    case (void *)0x9:
    case (void *)0xa:
      pvVar11 = (void *)0x8;
      break;
    case (void *)0x2:
    case (void *)0x3:
      pvVar11 = (void *)0x5;
    }
  }
  local_14 = uVar6;
  FUN_0046fa00(0x200000,pvVar11,param_3[3],param_3[4],param_5,param_8,param_9,pvVar11);
  if (param_3[1] == (void *)0x0) {
    for (iVar7 = param_6; iVar7 != param_6 + 0x400; iVar7 = iVar7 + 4) {
      *(undefined1 *)(iVar7 + 3) = 0xff;
    }
    *(undefined1 *)(param_6 + 3) = 0;
  }
  psVar8 = (short *)&DAT_006bf8d0;
  do {
    psVar9 = psVar8;
    psVar8 = psVar9 + 1;
  } while (*psVar8 != 0);
  if ((param_1[2] == ((int)(psVar9 + -0x35fc67) >> 1 & 0x7fffffffU)) &&
     (cVar5 = FUN_0059c5c0(param_1[2]), cVar5 != '\0')) {
    param_1[0x111] = param_1[0x111] & 0xffff0fff;
  }
  if (DAT_0078443b == '\0') {
    param_1[0x111] = param_1[0x111] & 0xffff0fff;
  }
  iVar7 = (&DAT_006b9e50)[param_1[0x108] * 0x16];
  uVar1 = (&DAT_006b9e54)[param_1[0x108] * 0x16];
  piVar2 = (int *)param_1[0x110];
  if (piVar2 != (int *)0x0) {
    (**(code **)(*piVar2 + 8))(piVar2,uVar6);
    param_1[0x110] = 0;
  }
  (**(code **)(*DAT_007848dc + 0x5c))
            (DAT_007848dc,*param_1,param_1[1],0,0,uVar1,1,param_1 + 0x110,0);
  pvVar11 = (void *)param_1[0x108];
  local_15 = pvVar11 != param_3[1];
  if (pvVar11 != param_3[1]) {
    *(int *)(*(int *)ThreadLocalStoragePointer + 8) = param_6;
    FUN_005a4b90(param_3,pvVar11);
    param_3 = local_2c;
  }
  if (param_4 != 0) {
    (*(code *)(&PTR_LAB_006b9e98)[(int)param_3[1] * 0x16])();
  }
  local_8 = 0;
  pvVar11 = *param_3;
  pvVar3 = param_3[2];
  iVar4 = *param_1;
  iVar10 = (**(code **)(*(int *)param_1[0x110] + 0x4c))((int *)param_1[0x110],0,&local_34,0,0x800);
  local_3c = pvVar3;
  if (iVar10 == 0) {
    uVar6 = 0;
    local_3c = local_34;
    iVar10 = local_30;
    if (param_1[1] != 0) {
      do {
        FUN_0062cfd0(iVar10,pvVar11,iVar4 * iVar7);
        uVar6 = uVar6 + 1;
        pvVar11 = (void *)((int)pvVar11 + (int)pvVar3);
        iVar10 = iVar10 + (int)local_34;
      } while (uVar6 < (uint)param_1[1]);
    }
    (**(code **)(*(int *)param_1[0x110] + 0x50))((int *)param_1[0x110],0);
  }
  uVar6 = (uint)(param_1[1] * (int)local_3c * 3) >> 1;
  param_1[0x10d] = uVar6;
  _DAT_00784458 = _DAT_00784458 + uVar6;
  local_8 = 0xffffffff;
  if (local_15 != false) {
    FID_conflict__free(local_2c[0]);
  }
  ExceptionList = local_10;
  __security_check_cookie(local_14 ^ (uint)&stack0xfffffffc);
  return;
}


```

