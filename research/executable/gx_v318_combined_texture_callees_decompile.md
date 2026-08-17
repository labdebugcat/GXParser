# Selected Nova1492 Decompilation

## `0046e110`

- Function: `FUN_0046e110`
- Entry: `0046e110`

```c

undefined4
FUN_0046e110(undefined4 param_1,undefined4 param_2,undefined4 param_3,undefined4 param_4,
            undefined4 param_5)

{
  int iVar1;
  undefined4 uVar2;
  void *local_10;
  undefined1 *puStack_c;
  undefined4 uStack_8;
  
  uStack_8 = 0xffffffff;
  puStack_c = &LAB_006577b0;
  local_10 = ExceptionList;
  ExceptionList = &local_10;
  iVar1 = FUN_004a0680(param_2,param_3);
  if (iVar1 == 0) {
    ExceptionList = local_10;
    return 0;
  }
  if (DAT_00784468 != 0) {
    switch(iVar1) {
    case 1:
      uVar2 = FUN_0046cf10(param_1,param_2,param_3,param_4,param_5);
      ExceptionList = local_10;
      return uVar2;
    case 2:
      uVar2 = FUN_0046df90(param_1,param_2,param_3);
      ExceptionList = local_10;
      return uVar2;
    case 3:
      uVar2 = FUN_0046e050(param_1,param_2,param_3);
      ExceptionList = local_10;
      return uVar2;
    case 4:
      uVar2 = FUN_0046d6d0(param_2,param_3,param_1,param_4,param_5);
      ExceptionList = local_10;
      return uVar2;
    default:
                    /* WARNING: Subroutine does not return */
      _abort();
    }
  }
  FUN_0046f530(param_2,param_3);
  ExceptionList = local_10;
  return 1;
}


```

## `0046cc30`

- Function: `FUN_0046cc30`
- Entry: `0046cc30`

```c

undefined4 * __fastcall FUN_0046cc30(undefined4 *param_1)

{
  param_1[2] = 0;
  param_1[0x83] = 0;
  param_1[0x108] = 0xffffffff;
  param_1[1] = 0;
  *param_1 = 0;
  param_1[0x10a] = 0;
  param_1[0x109] = 0;
  param_1[0x111] = 0;
  *(undefined2 *)(param_1 + 0x112) = 0x101;
  param_1[0x10e] = 0;
  param_1[0x10f] = 0;
  param_1[0x110] = 0;
  param_1[2] = 0;
  param_1[0x83] = 0;
  param_1[0x10c] = 0;
  param_1[0x10d] = 0;
  param_1[0x10b] = 1;
  param_1[0x104] = 0;
  param_1[0x105] = 0;
  param_1[0x106] = 0;
  param_1[0x107] = 0;
  return param_1;
}


```

