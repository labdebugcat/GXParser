# Selected Nova1492 Decompilation

## `00431920`

- Function: `FUN_00431920`
- Entry: `00431920`

```c

uint __thiscall FUN_00431920(int param_1,int param_2,undefined4 *param_3)

{
  int iVar1;
  char cVar2;
  undefined4 uVar3;
  undefined4 *puVar4;
  int *piVar5;
  int iVar6;
  undefined4 extraout_ECX;
  undefined8 uVar7;
  void *local_10;
  undefined1 *puStack_c;
  undefined4 local_8;
  
  iVar1 = param_2;
  local_8 = 0xffffffff;
  puStack_c = &LAB_0065b548;
  local_10 = ExceptionList;
  ExceptionList = &local_10;
  puVar4 = *(undefined4 **)(param_1 + 0xfc + param_2 * 4);
  if (puVar4 == (undefined4 *)0x0) {
    iVar6 = 0;
    if ((char)param_3 != '\0') goto LAB_00431aff;
  }
  else {
    if ((char)param_3 == '\0') goto LAB_00431aa0;
    FUN_004315b0(puVar4);
    *(undefined4 *)(param_1 + 0xfc + iVar1 * 4) = 0;
  }
  iVar6 = (&DAT_007c2548)[iVar1];
  uVar3 = FUN_00431850(iVar6,*(int *)(iVar6 + -4) + iVar6,iVar1);
  *(undefined4 *)(param_1 + 0xfc + iVar1 * 4) = uVar3;
  iVar6 = (&DAT_007c2548)[iVar1];
  cVar2 = FUN_00463490(iVar6,*(int *)(iVar6 + -4) + iVar6);
  if (cVar2 != '\0') {
    FUN_004553d0(0,0);
    iVar6 = *(int *)(param_1 + 0xfc + iVar1 * 4);
    if (*(int *)(iVar6 + 0x5c) != 0) {
      do {
        uVar3 = *(undefined4 *)(param_1 + (iVar1 + 0x6e) * 0x44);
        uVar7 = FUN_004599d0(uVar3,uVar3,uVar3);
        iVar6 = (int)uVar7;
      } while (*(int *)((int)((ulonglong)uVar7 >> 0x20) + 100) != 0);
    }
LAB_00431aff:
    ExceptionList = local_10;
    return CONCAT31((int3)((uint)iVar6 >> 8),1);
  }
  puVar4 = (undefined4 *)FUN_0059c260(&param_2,0x800,2,*(int *)ThreadLocalStoragePointer + 0xc);
  param_3 = (undefined4 *)*puVar4 + 1;
  *(undefined4 *)*puVar4 = 0;
  local_8 = 0x12;
  iVar1 = (&DAT_007c2548)[iVar1];
  uVar3 = FUN_004278e0(iVar1,*(int *)(iVar1 + -4) + iVar1);
  iVar6 = param_3[-1];
  iVar1 = iVar6 + 1;
  FUN_00434ab0(iVar1,iVar1);
  *(undefined2 *)((int)param_3 + iVar6 * 2) = 0x5b;
  piVar5 = (int *)FUN_00433d50(uVar3);
  FUN_00434960(extraout_ECX);
  FUN_00434ab0(*(int *)(*piVar5 + -4),*(int *)(*piVar5 + -4) + 1);
  *(undefined2 *)(*piVar5 + *(int *)(*piVar5 + -4) * 2) = 0;
  FUN_004d7ec0();
  local_8 = 0xffffffff;
  puVar4 = param_3;
  if (param_3 != (undefined4 *)&DAT_006b9e28) {
    puVar4 = (undefined4 *)FUN_0059c360(param_3 + -1);
  }
LAB_00431aa0:
  ExceptionList = local_10;
  return (uint)puVar4 & 0xffffff00;
}


```

## `00431650`

- Function: `FUN_00431650`
- Entry: `00431650`

```c

int __thiscall FUN_00431650(undefined4 param_1,int param_2)

{
  int iVar1;
  int iVar2;
  int iVar3;
  int iVar4;
  
  if (param_2 == 0) {
    return 0;
  }
  iVar3 = FUN_00431780(0,param_1);
  FUN_00457e10(iVar3);
  iVar1 = *(int *)(param_2 + 0x5c);
  do {
    if (iVar1 == 0) {
      return iVar3;
    }
    iVar4 = FUN_00431650(iVar1);
    if (iVar4 != 0) {
      iVar2 = *(int *)(iVar3 + 0x5c);
      if (iVar2 == 0) {
        *(int *)(iVar3 + 0x5c) = iVar4;
      }
      else {
        if (*(int *)(iVar2 + 100) != 0) {
          FUN_00455350(iVar4,iVar3);
          goto LAB_004316b8;
        }
        *(int *)(iVar4 + 0x68) = iVar2;
        *(int *)(iVar2 + 100) = iVar4;
      }
      *(int *)(iVar4 + 0x60) = iVar3;
    }
LAB_004316b8:
    iVar1 = *(int *)(iVar1 + 100);
  } while( true );
}


```

## `00431900`

- Function: `FUN_00431850`
- Entry: `00431850`

```c

int __thiscall FUN_00431850(int param_1,undefined4 param_2,undefined4 param_3,undefined4 param_4)

{
  int iVar1;
  int iVar2;
  int iVar3;
  int local_14;
  void *local_10;
  undefined1 *puStack_c;
  undefined4 local_8;
  
  local_8 = 0xffffffff;
  puStack_c = &LAB_0065b3f8;
  local_10 = ExceptionList;
  ExceptionList = &local_10;
  local_14 = param_1;
  iVar2 = FUN_00640b15(0x70,0x10,DAT_007360c8 ^ (uint)&stack0xfffffffc);
  if (iVar2 == 0) {
    iVar2 = 0;
  }
  else {
    local_14 = iVar2;
    FUN_00453720();
    local_8 = 0;
    FUN_00456080(param_2,param_3);
    *(undefined4 *)(iVar2 + 0x44) = param_4;
    local_8 = 0xffffffff;
  }
  iVar1 = *(int *)(param_1 + 0xf4);
  local_14 = iVar2;
  iVar3 = FUN_00434330(iVar1,*(undefined4 *)(iVar1 + 4),&local_14);
  if (*(int *)(param_1 + 0xf8) == 0x15555554) {
                    /* WARNING: Subroutine does not return */
    FUN_00627726("list<T> too long");
  }
  *(int *)(param_1 + 0xf8) = *(int *)(param_1 + 0xf8) + 1;
  *(int *)(iVar1 + 4) = iVar3;
  **(int **)(iVar3 + 4) = iVar3;
  ExceptionList = local_10;
  return iVar2;
}


```

