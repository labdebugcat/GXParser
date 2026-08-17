# Selected Nova1492 Decompilation

## `0046ca70`

- Function: `FUN_0046ca70`
- Entry: `0046ca70`

```c

int * __thiscall FUN_0046ca70(int *param_1,int param_2)

{
  int *piVar1;
  short sVar2;
  uint uVar3;
  uint uVar4;
  int iVar5;
  undefined1 uVar6;
  int iVar7;
  uint uVar8;
  int local_24;
  uint local_14;
  void *local_10;
  undefined1 *puStack_c;
  undefined4 local_8;
  
  puStack_c = &LAB_006631ab;
  local_10 = ExceptionList;
  ExceptionList = &local_10;
  piVar1 = param_1 + 5;
  *piVar1 = (int)&DAT_006b9e28;
  local_8 = 0x10;
  if (param_2 == 0) {
    *param_1 = 0;
  }
  else {
    uVar3 = *(uint *)(param_2 + 0x1c);
    uVar4 = *(uint *)(param_2 + 0x20);
    FUN_00423690(uVar4 * uVar3,uVar4 * uVar3);
    sVar2 = *(short *)(*(int *)(param_2 + 4) + 0xe);
    if ((((sVar2 == 8) || (sVar2 == 0x18)) || (sVar2 == 0x20)) && (local_14 = 0, uVar4 != 0)) {
      local_24 = 0;
      do {
        uVar8 = 0;
        iVar7 = local_24;
        if (uVar3 != 0) {
          do {
            iVar5 = *piVar1;
            uVar6 = FUN_00428480(uVar8,local_14);
            *(undefined1 *)(iVar7 + iVar5) = uVar6;
            uVar8 = uVar8 + 1;
            iVar7 = iVar7 + 1;
          } while (uVar8 < uVar3);
        }
        local_14 = local_14 + 1;
        local_24 = local_24 + uVar3;
      } while (local_14 < uVar4);
    }
    *param_1 = *piVar1;
    param_1[1] = 1;
    param_1[2] = uVar3;
    param_1[3] = uVar3;
    param_1[4] = uVar4;
  }
  ExceptionList = local_10;
  return param_1;
}


```

## `0046c990`

- Function: `FUN_0046c990`
- Entry: `0046c990`

```c

undefined4 * __thiscall FUN_0046c990(undefined4 *param_1,int param_2)

{
  int iVar1;
  undefined1 uVar2;
  uint uVar3;
  int iVar4;
  int iVar5;
  uint uVar6;
  int local_14;
  void *local_10;
  undefined1 *puStack_c;
  undefined4 local_8;
  
  puStack_c = &LAB_006630fb;
  local_10 = ExceptionList;
  ExceptionList = &local_10;
  param_1[5] = &DAT_006b9e28;
  local_8 = 0x10;
  if (param_2 == 0) {
    *param_1 = 0;
  }
  else {
    uVar6 = (uint)*(ushort *)(param_2 + 0xe);
    uVar3 = (uint)*(ushort *)(param_2 + 0xc);
    FUN_00423690(uVar6 * uVar3,uVar6 * uVar3);
    local_14 = 0;
    if (uVar3 != 0) {
      do {
        iVar5 = 0;
        iVar4 = local_14;
        if (uVar6 != 0) {
          do {
            iVar1 = param_1[5];
            uVar2 = FUN_00426860(local_14,iVar5);
            *(undefined1 *)(iVar4 + iVar1) = uVar2;
            iVar5 = iVar5 + 1;
            iVar4 = iVar4 + uVar3;
          } while (iVar5 < (int)uVar6);
        }
        local_14 = local_14 + 1;
      } while (local_14 < (int)uVar3);
    }
    param_1[1] = 1;
    *param_1 = param_1[5];
    param_1[2] = uVar3;
    param_1[3] = uVar3;
    param_1[4] = uVar6;
  }
  ExceptionList = local_10;
  return param_1;
}


```

## `0046d5e0`

- Function: `FUN_0046d5e0`
- Entry: `0046d5e0`

```c

int __fastcall FUN_0046d5e0(int param_1)

{
  void *local_10;
  undefined1 *puStack_c;
  undefined4 local_8;
  
  puStack_c = &LAB_00658bb3;
  local_10 = ExceptionList;
  ExceptionList = &local_10;
  local_8 = 0;
  FUN_00427090(DAT_007360c8 ^ (uint)&stack0xfffffffc);
  local_8 = 0xffffffff;
  if (*(undefined2 **)(param_1 + 0x14) != &DAT_006b9e28) {
    thunk_FUN_00640afb(*(undefined2 **)(param_1 + 0x14) + -2);
  }
  FUN_0062a696(param_1,0x24);
  ExceptionList = local_10;
  return param_1;
}


```

