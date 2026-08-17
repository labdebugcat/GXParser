# Selected Nova1492 Decompilation

## `00432c60`

- Function: `FUN_00432c60`
- Entry: `00432c60`

```c

undefined4 FUN_00432c60(undefined4 param_1)

{
  undefined4 uVar1;
  undefined4 local_28;
  undefined4 local_24;
  undefined4 local_20;
  undefined4 local_1c;
  undefined4 local_18;
  undefined4 local_14;
  undefined4 local_10;
  undefined4 local_c;
  undefined4 local_8;
  undefined4 local_4;
  
  switch(param_1) {
  case 0:
  case 8:
  case 0xb:
  case 0xc:
    local_28 = 8;
    local_24 = 5;
    goto LAB_00432d34;
  default:
    return 0xffffffff;
  case 2:
    local_1c = 2;
    local_18 = 3;
    break;
  case 3:
    local_1c = 3;
    local_18 = 2;
    break;
  case 4:
    local_28 = 4;
    local_24 = 5;
    local_20 = 8;
    uVar1 = FUN_00432e00(&local_28,&local_1c);
    return uVar1;
  case 5:
    local_28 = 5;
    local_24 = 8;
LAB_00432d34:
    local_20 = 4;
    uVar1 = FUN_00432e00(&local_28,&local_1c);
    return uVar1;
  case 6:
  case 9:
    local_1c = 6;
    local_18 = 7;
    goto LAB_00432d69;
  case 7:
  case 10:
    local_1c = 7;
    local_18 = 6;
LAB_00432d69:
    local_14 = 8;
    local_10 = 2;
    local_c = 3;
    local_8 = 4;
    local_4 = 5;
    goto LAB_00432cc1;
  case 0xffffffff:
    uVar1 = FUN_005a5400();
    return uVar1;
  }
  local_14 = 4;
  local_10 = 5;
  local_c = 6;
  local_8 = 7;
  local_4 = 8;
LAB_00432cc1:
  uVar1 = FUN_00432e00(&local_1c,&stack0x00000000);
  return uVar1;
}


```

## `0046ccf0`

- Function: `FUN_0046ccf0`
- Entry: `0046ccf0`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void __fastcall FUN_0046ccf0(int param_1)

{
  if ((DAT_007848d8 != 0) && (*(int *)(param_1 + 0x440) != 0)) {
    _DAT_00784458 = _DAT_00784458 - *(int *)(param_1 + 0x434);
    (**(code **)(**(int **)(param_1 + 0x440) + 8))(*(int **)(param_1 + 0x440));
    *(undefined4 *)(param_1 + 0x440) = 0;
    FID_conflict__free(*(void **)(param_1 + 0x428));
    *(undefined4 *)(param_1 + 0x428) = 0;
  }
  return;
}


```

