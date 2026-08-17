# Selected Nova1492 Decompilation

## `00480070`

- Function: `FUN_00480070`
- Entry: `00480070`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

float10 FUN_00480070(void)

{
  return (float10)CONCAT44((DAT_007c390c - DAT_007c3914) - (uint)(DAT_007c3908 < DAT_007c3910),
                           DAT_007c3908 - DAT_007c3910) * (float10)_DAT_007641f4;
}


```

## `0045fd40`

- Function: `FUN_0045fd40`
- Entry: `0045fd40`

```c

void __fastcall FUN_0045fd40(int param_1)

{
  int iVar1;
  undefined4 uVar2;
  int extraout_ECX;
  int iVar3;
  void *local_10;
  undefined1 *puStack_c;
  undefined4 uStack_8;
  
  uStack_8 = 0xffffffff;
  puStack_c = &LAB_00657860;
  local_10 = ExceptionList;
  ExceptionList = &local_10;
  *(int *)(param_1 + 0x94) = *(int *)(param_1 + 0x3c8);
  iVar3 = param_1;
  if (*(int *)(param_1 + 0x3c8) == 0) {
    uVar2 = FUN_00431780(0,param_1);
    *(undefined4 *)(param_1 + 0x3c8) = uVar2;
    *(undefined4 *)(param_1 + 0x94) = uVar2;
    iVar3 = extraout_ECX;
  }
  if (*(int *)(param_1 + 0x3cc) == 0) {
    uVar2 = FUN_00431780(0,iVar3);
    *(undefined4 *)(param_1 + 0x3cc) = uVar2;
  }
  FUN_00460bc0(0,1);
  FUN_00460bc0(1,2);
  FUN_00460bc0(1,3);
  FUN_00460bc0(1,4);
  FUN_00460bc0(1,7);
  FUN_00460bc0(1,5);
  FUN_00460bc0(1,6);
  FUN_00460bc0(5,8);
  FUN_00460bc0(6,9);
  iVar3 = *(int *)(param_1 + 0x4c);
  if ((iVar3 != 0) && (iVar1 = *(int *)(param_1 + 0x94), iVar1 != 0)) {
    if (*(int *)(iVar3 + 0x5c) == 0) {
      *(int *)(iVar3 + 0x5c) = iVar1;
      *(int *)(iVar1 + 0x60) = iVar3;
    }
    else {
      FUN_00455350(iVar1,iVar3);
    }
  }
  FUN_0045b3f0(param_1 + 0x10,param_1 + 0x20,param_1 + 0x30,param_1 + 0x40,1);
  ExceptionList = local_10;
  return;
}


```

## `0045fcd0`

- Function: `FUN_0045fcd0`
- Entry: `0045fcd0`

```c

void __fastcall FUN_0045fcd0(int param_1)

{
  int iVar1;
  int *piVar2;
  int iVar3;
  
  piVar2 = (int *)(param_1 + 0x3c8);
  iVar3 = 10;
  do {
    iVar1 = *piVar2;
    if ((iVar1 != 0) && (*(int *)(iVar1 + 0x60) != 0)) {
      if (*(int *)(iVar1 + 100) != 0) {
        *(undefined4 *)(*(int *)(iVar1 + 100) + 0x68) = *(undefined4 *)(iVar1 + 0x68);
      }
      if (*(int *)(iVar1 + 0x68) != 0) {
        *(undefined4 *)(*(int *)(iVar1 + 0x68) + 100) = *(undefined4 *)(iVar1 + 100);
      }
      if (*(int *)(*(int *)(iVar1 + 0x60) + 0x5c) == iVar1) {
        *(undefined4 *)(*(int *)(iVar1 + 0x60) + 0x5c) = *(undefined4 *)(iVar1 + 100);
      }
      *(undefined4 *)(iVar1 + 0x68) = 0;
      *(undefined4 *)(iVar1 + 100) = 0;
      *(undefined4 *)(iVar1 + 0x60) = 0;
    }
    piVar2 = piVar2 + 1;
    iVar3 = iVar3 + -1;
  } while (iVar3 != 0);
  return;
}


```

