# Selected Nova1492 Decompilation

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

