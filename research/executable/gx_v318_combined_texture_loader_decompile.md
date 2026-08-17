# Selected Nova1492 Decompilation

## `0042aaf5`

- Function: `FUN_0042aaf5`
- Entry: `0042aaf5`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void __thiscall
FUN_0042aaf5(int param_1,undefined4 param_2,undefined1 *param_3,undefined1 *param_4,
            undefined4 param_5,undefined4 param_6)

{
  char cVar1;
  int iVar2;
  undefined1 *puVar3;
  undefined1 *puVar4;
  undefined4 *puVar5;
  undefined4 *puVar6;
  int iVar7;
  undefined4 local_244;
  undefined1 *local_23c;
  int local_238;
  undefined1 local_234 [524];
  int local_28;
  undefined1 *local_24;
  undefined1 *local_20;
  undefined1 *local_1c;
  uint local_18;
  void *local_10;
  undefined1 *puStack_c;
  undefined4 local_8;
  
  local_8 = 0xffffffff;
  puStack_c = &LAB_0065aa91;
  local_10 = ExceptionList;
  local_18 = DAT_007360c8 ^ (uint)&stack0xfffffffc;
  ExceptionList = &local_10;
  if (param_3 == (undefined1 *)0x0) {
    local_1c = (undefined1 *)FUN_0063ea48(0x44c,local_18);
    local_8 = 2;
    if (local_1c == (undefined1 *)0x0) {
      local_23c = (undefined1 *)0x0;
    }
    else {
      _memset(local_1c,0,0x44c);
      local_23c = (undefined1 *)FUN_0046cc30();
    }
    local_8 = 0xffffffff;
  }
  else {
    puVar4 = (undefined1 *)0x0;
    local_28 = 0;
    local_24 = (undefined1 *)0x0;
    iVar2 = param_1;
    iVar7 = param_1;
    FUN_004278b0(L"maps_custom");
    FUN_00433750(&local_28,iVar2,iVar7);
    local_20 = (undefined1 *)0x0;
    local_1c = (undefined1 *)0x0;
    local_23c = (undefined1 *)0x5c;
    FUN_00433710(&local_20,&local_23c);
    if ((local_28 == 0) && (local_20 != (undefined1 *)0x0)) {
      param_3 = local_20 + 2;
      param_4 = local_1c;
    }
    local_238 = 0;
    iVar2 = FUN_004a0680(param_3,param_4);
    if ((iVar2 == 4) || (iVar2 == 1)) {
      puVar5 = (undefined4 *)&DAT_008b1f08;
      if ((*(int *)(*(int *)ThreadLocalStoragePointer + 0x70) < DAT_008b22d8) &&
         (FUN_0062a7d8(&DAT_008b22d8), DAT_008b22d8 == -1)) {
        local_8 = 0;
        FUN_004278b0(&DAT_006be3f8);
        _DAT_008b1f10 = 2;
        DAT_008b1f14 = 1;
        FUN_004278b0(&DAT_006be400);
        _DAT_008b1f20 = 3;
        DAT_008b1f24 = 0;
        FUN_004278b0(&DAT_006be408);
        _DAT_008b1f30 = 1;
        DAT_008b1f34 = 1;
        local_8 = 0xffffffff;
        FUN_0062a799(&DAT_008b22d8);
      }
      local_20 = param_3;
      local_238 = 0;
      local_1c = param_3 + (((uint)((int)param_4 - (int)param_3) >> 1) - 3) * 2;
      if (param_4 < param_3 + (((uint)((int)param_4 - (int)param_3) >> 1) - 3) * 2) {
        local_1c = param_4;
      }
      FUN_00433dc0(&local_20);
      local_23c = local_234 + local_238 * 2;
      do {
        FUN_00433dc0(puVar5);
        cVar1 = FUN_004a4eb0(local_234,local_234 + local_238 * 2);
        if (cVar1 != '\0') {
          param_3 = local_234;
          param_4 = local_234 + local_238 * 2;
          if (*(char *)(puVar5 + 3) != '\0') {
            param_5 = 0;
            param_6 = local_244;
          }
          break;
        }
        FUN_00433b10(local_23c);
        puVar5 = puVar5 + 4;
      } while (puVar5 != &DAT_008b1f38);
    }
    puVar5 = *(undefined4 **)(param_1 + 0xd4);
    local_24 = param_3;
    puVar6 = (undefined4 *)*puVar5;
    local_23c = param_4;
    for (; puVar6 != puVar5; puVar6 = (undefined4 *)*puVar6) {
      local_1c = (undefined1 *)puVar6[2];
      cVar1 = FUN_004337a0(local_24,local_23c);
      puVar3 = local_1c;
      if (cVar1 != '\0') goto LAB_0042ad62;
    }
    puVar3 = (undefined1 *)0x0;
LAB_0042ad62:
    if (puVar3 != (undefined1 *)0x0) {
      *(int *)(puVar3 + 0x42c) = *(int *)(puVar3 + 0x42c) + 1;
      goto LAB_0042ae23;
    }
    local_1c = (undefined1 *)FUN_0063ea48(0x44c);
    local_8 = 1;
    if (local_1c != (undefined1 *)0x0) {
      _memset(local_1c,0,0x44c);
      puVar4 = (undefined1 *)FUN_0046cc30();
    }
    local_8 = 0xffffffff;
    local_23c = puVar4;
    FUN_0046e110(param_2,param_3,param_4,param_5,param_6);
  }
  FUN_004333a0(&local_23c);
LAB_0042ae23:
  ExceptionList = local_10;
  __security_check_cookie(local_18 ^ (uint)&stack0xfffffffc);
  return;
}


```

