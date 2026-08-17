# Selected Nova1492 Decompilation

## `00427300`

- Function: `FUN_00427300`
- Entry: `00427300`

```c

/* WARNING: Removing unreachable block (ram,0x004273b4) */

undefined * __thiscall FUN_00427300(int param_1,int param_2,undefined4 param_3)

{
  undefined2 *puVar1;
  uint uVar2;
  undefined4 uVar3;
  uint uVar4;
  void *local_10;
  undefined1 *puStack_c;
  undefined4 local_8;
  
  local_8 = 0xffffffff;
  puStack_c = &LAB_006591f8;
  local_10 = ExceptionList;
  uVar2 = DAT_007360c8 ^ (uint)&stack0xfffffffc;
  ExceptionList = &local_10;
  uVar4 = 0;
  if (param_2 != 0) {
    uVar3 = FUN_004a4d00(param_2,param_3);
    uVar4 = FUN_00426900(uVar3);
    if ((char)uVar4 != '\0') {
      FUN_00427460(&param_2);
      local_8 = 1;
      puVar1 = *(undefined2 **)(param_1 + 0x14);
      if (puVar1 != &DAT_006b9e28) {
        thunk_FUN_00640afb(puVar1 + -2,uVar2);
      }
      *(undefined **)(param_1 + 0x14) = &DAT_006b78d0;
      ExceptionList = local_10;
      return &DAT_006b9e01;
    }
  }
  ExceptionList = local_10;
  return (undefined *)(uVar4 & 0xffffff00);
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

