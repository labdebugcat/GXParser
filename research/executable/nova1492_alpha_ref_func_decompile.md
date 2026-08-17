# Selected Nova1492 Decompilation

## `0042ecbb`

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

## `0042ecca`

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

## `0042d131`

- Function: `FUN_0042cf70`
- Entry: `0042cf70`

```c

void __fastcall FUN_0042cf70(int param_1)

{
  int *piVar1;
  undefined4 uVar2;
  int iVar3;
  undefined4 *unaff_ESI;
  undefined4 *puVar4;
  undefined4 *puVar5;
  undefined1 auStack_b8 [8];
  int local_b0;
  undefined4 local_a0 [4];
  undefined4 local_90;
  undefined4 local_8c;
  undefined4 local_88;
  undefined4 local_84;
  undefined4 local_80;
  undefined4 local_7c;
  undefined4 local_78;
  undefined4 local_74;
  undefined4 local_70;
  undefined4 local_6c;
  undefined4 local_68;
  undefined4 local_64;
  undefined4 local_60 [19];
  uint local_14;
  
  local_14 = DAT_007360c8 ^ (uint)auStack_b8;
  piVar1 = *(int **)(param_1 + 0x205ac);
  local_b0 = param_1;
  if (((piVar1 != (int *)0x0) && (*(int *)(param_1 + 0x20104) == 5)) &&
     (*(int *)(param_1 + 0x20dc8) != 0)) {
    local_a0[0] = DAT_008b22e0;
    local_a0[1] = DAT_008b22e4;
    local_a0[2] = DAT_008b22e8;
    local_a0[3] = DAT_008b22ec;
    local_90 = DAT_008b22f0;
    local_8c = DAT_008b22f4;
    local_88 = DAT_008b22f8;
    local_84 = DAT_008b22fc;
    local_80 = DAT_008b2300;
    local_7c = DAT_008b2304;
    local_78 = DAT_008b2308;
    local_74 = DAT_008b230c;
    local_70 = DAT_008b2310;
    local_6c = DAT_008b2314;
    local_68 = DAT_008b2318;
    local_64 = DAT_008b231c;
    puVar4 = local_a0;
    puVar5 = local_60;
    for (iVar3 = 0x10; iVar3 != 0; iVar3 = iVar3 + -1) {
      *puVar5 = *puVar4;
      puVar4 = puVar4 + 1;
      puVar5 = puVar5 + 1;
    }
    (**(code **)(*piVar1 + 0xb0))(piVar1,0x100,local_60);
    if (*(char *)(unaff_ESI + 0x8091) != '\0') {
      *(undefined1 *)(unaff_ESI + 0x8091) = 0;
      (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0xe,0);
    }
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x34,1);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],9,1);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x38,8);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x36,1);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x35,1);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x39,1);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x3a,0xffffffff);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x3b,0xffffffff);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x19,8);
    if (*(char *)((int)unaff_ESI + 0x20246) != '\x01') {
      *(undefined1 *)((int)unaff_ESI + 0x20246) = 1;
      (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x1b,1);
    }
    if (unaff_ESI[0x8090] != 0xb) {
      unaff_ESI[0x8090] = 0xb;
      (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x13,1);
      (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x14,2);
    }
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x16,2);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x37,7);
    iVar3 = unaff_ESI[0x8372];
    uVar2 = FUN_00428940(*(undefined4 *)(iVar3 + 8),iVar3 + 0x10);
    *(undefined4 *)(iVar3 + 0x1c) = uVar2;
    FUN_004549a0();
    FUN_00433030(0);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x16,3);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x37,8);
    FUN_00433030(1);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],9,2);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0xe,1);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x34,0);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x16,2);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x34,1);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x39,1);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x38,4);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x37,1);
    *unaff_ESI = 0x8c000000;
    FUN_00429d5b(1,0,0,0,(float)DAT_007c3920,(float)DAT_007c3924);
    if (*(char *)(unaff_ESI + 0x8091) != '\x01') {
      *(undefined1 *)(unaff_ESI + 0x8091) = 1;
      (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0xe,1);
    }
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x34,0);
    if (*(char *)((int)unaff_ESI + 0x20246) != '\0') {
      *(undefined1 *)((int)unaff_ESI + 0x20246) = 0;
      (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x1b,0);
    }
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x19,6);
  }
  __security_check_cookie(local_14 ^ (uint)auStack_b8);
  return;
}


```

## `0042d377`

- Function: `FUN_0042cf70`
- Entry: `0042cf70`

```c

void __fastcall FUN_0042cf70(int param_1)

{
  int *piVar1;
  undefined4 uVar2;
  int iVar3;
  undefined4 *unaff_ESI;
  undefined4 *puVar4;
  undefined4 *puVar5;
  undefined1 auStack_b8 [8];
  int local_b0;
  undefined4 local_a0 [4];
  undefined4 local_90;
  undefined4 local_8c;
  undefined4 local_88;
  undefined4 local_84;
  undefined4 local_80;
  undefined4 local_7c;
  undefined4 local_78;
  undefined4 local_74;
  undefined4 local_70;
  undefined4 local_6c;
  undefined4 local_68;
  undefined4 local_64;
  undefined4 local_60 [19];
  uint local_14;
  
  local_14 = DAT_007360c8 ^ (uint)auStack_b8;
  piVar1 = *(int **)(param_1 + 0x205ac);
  local_b0 = param_1;
  if (((piVar1 != (int *)0x0) && (*(int *)(param_1 + 0x20104) == 5)) &&
     (*(int *)(param_1 + 0x20dc8) != 0)) {
    local_a0[0] = DAT_008b22e0;
    local_a0[1] = DAT_008b22e4;
    local_a0[2] = DAT_008b22e8;
    local_a0[3] = DAT_008b22ec;
    local_90 = DAT_008b22f0;
    local_8c = DAT_008b22f4;
    local_88 = DAT_008b22f8;
    local_84 = DAT_008b22fc;
    local_80 = DAT_008b2300;
    local_7c = DAT_008b2304;
    local_78 = DAT_008b2308;
    local_74 = DAT_008b230c;
    local_70 = DAT_008b2310;
    local_6c = DAT_008b2314;
    local_68 = DAT_008b2318;
    local_64 = DAT_008b231c;
    puVar4 = local_a0;
    puVar5 = local_60;
    for (iVar3 = 0x10; iVar3 != 0; iVar3 = iVar3 + -1) {
      *puVar5 = *puVar4;
      puVar4 = puVar4 + 1;
      puVar5 = puVar5 + 1;
    }
    (**(code **)(*piVar1 + 0xb0))(piVar1,0x100,local_60);
    if (*(char *)(unaff_ESI + 0x8091) != '\0') {
      *(undefined1 *)(unaff_ESI + 0x8091) = 0;
      (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0xe,0);
    }
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x34,1);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],9,1);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x38,8);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x36,1);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x35,1);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x39,1);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x3a,0xffffffff);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x3b,0xffffffff);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x19,8);
    if (*(char *)((int)unaff_ESI + 0x20246) != '\x01') {
      *(undefined1 *)((int)unaff_ESI + 0x20246) = 1;
      (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x1b,1);
    }
    if (unaff_ESI[0x8090] != 0xb) {
      unaff_ESI[0x8090] = 0xb;
      (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x13,1);
      (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x14,2);
    }
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x16,2);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x37,7);
    iVar3 = unaff_ESI[0x8372];
    uVar2 = FUN_00428940(*(undefined4 *)(iVar3 + 8),iVar3 + 0x10);
    *(undefined4 *)(iVar3 + 0x1c) = uVar2;
    FUN_004549a0();
    FUN_00433030(0);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x16,3);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x37,8);
    FUN_00433030(1);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],9,2);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0xe,1);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x34,0);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x16,2);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x34,1);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x39,1);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x38,4);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x37,1);
    *unaff_ESI = 0x8c000000;
    FUN_00429d5b(1,0,0,0,(float)DAT_007c3920,(float)DAT_007c3924);
    if (*(char *)(unaff_ESI + 0x8091) != '\x01') {
      *(undefined1 *)(unaff_ESI + 0x8091) = 1;
      (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0xe,1);
    }
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x34,0);
    if (*(char *)((int)unaff_ESI + 0x20246) != '\0') {
      *(undefined1 *)((int)unaff_ESI + 0x20246) = 0;
      (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x1b,0);
    }
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x19,6);
  }
  __security_check_cookie(local_14 ^ (uint)auStack_b8);
  return;
}


```

## `0042ecdb`

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

