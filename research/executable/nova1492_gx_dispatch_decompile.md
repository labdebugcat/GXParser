# Selected Nova1492 Decompilation

## `00435ad0`

- Function: `FUN_00435ad0`
- Entry: `00435ad0`

```c

bool __thiscall FUN_00435ad0(int param_1,int *param_2)

{
  uint *puVar1;
  undefined4 uVar2;
  int iVar3;
  int local_4;
  
  local_4 = param_1;
  FUN_0046c6d0(&DAT_006bec3c,&local_4);
  if (local_4 != -0x10000) {
    return false;
  }
  FUN_0046c6d0(&DAT_006bec44,param_1);
  FUN_0046c6d0(&DAT_006bec44,param_1 + 0xc);
  puVar1 = (uint *)(param_1 + 4);
  FUN_0046c6d0(&DAT_006bec44,puVar1);
  FID_conflict__free(*(void **)(param_1 + 8));
  *(undefined4 *)(param_1 + 8) = 0;
  uVar2 = FUN_0063ea48(-(uint)((int)((ulonglong)*puVar1 * 0x14 >> 0x20) != 0) |
                       (uint)((ulonglong)*puVar1 * 0x14));
  *(undefined4 *)(param_1 + 8) = uVar2;
  iVar3 = *puVar1 * 0x14;
  if ((iVar3 != 0) && ((uint)(*param_2 + iVar3) <= (uint)param_2[1])) {
    FUN_0062cfd0(uVar2,param_2[2] + *param_2,iVar3);
    *param_2 = *param_2 + iVar3;
  }
  FUN_0046c6d0(&DAT_006bec44,&local_4);
  return local_4 == -0xfffa;
}


```

## `00435c80`

- Function: `FUN_00435c80`
- Entry: `00435c80`

```c

bool __thiscall FUN_00435c80(uint *param_1,int *param_2)

{
  uint *puVar1;
  undefined4 uVar2;
  uint *puVar3;
  uint uVar4;
  int iVar5;
  uint uVar6;
  int iVar7;
  uint *local_4;
  
  local_4 = param_1;
  FUN_0046c6d0(&DAT_006bec3c,&local_4);
  puVar3 = local_4;
  if (((local_4 != (uint *)0xffff0009) && (local_4 != (uint *)0xffff0011)) &&
     (local_4 != (uint *)0xffff0016)) {
    return false;
  }
  puVar1 = param_1 + 3;
  FUN_0046c6d0(&DAT_006bec44,puVar1);
  FID_conflict__free((void *)param_1[1]);
  param_1[1] = 0;
  uVar4 = FUN_00640b15(*puVar1 << 6,0x10);
  iVar7 = *puVar1 * 0x40;
  param_1[1] = uVar4;
  if ((iVar7 != 0) && ((uint)(*param_2 + iVar7) <= (uint)param_2[1])) {
    FUN_0062cfd0(uVar4,param_2[2] + *param_2,iVar7);
    *param_2 = *param_2 + iVar7;
  }
  if ((puVar3 < (uint *)0xffff0011) && (uVar4 = 0, *param_1 != 0)) {
    iVar7 = 0;
    do {
      uVar4 = uVar4 + 1;
      iVar5 = param_1[1] + iVar7;
      iVar7 = iVar7 + 0x40;
      uVar2 = *(undefined4 *)(iVar5 + 4);
      *(undefined4 *)(iVar5 + 4) = *(undefined4 *)(iVar5 + 0x10);
      *(undefined4 *)(iVar5 + 0x10) = uVar2;
      uVar2 = *(undefined4 *)(iVar5 + 8);
      *(undefined4 *)(iVar5 + 8) = *(undefined4 *)(iVar5 + 0x20);
      *(undefined4 *)(iVar5 + 0x20) = uVar2;
      uVar2 = *(undefined4 *)(iVar5 + 0xc);
      *(undefined4 *)(iVar5 + 0xc) = *(undefined4 *)(iVar5 + 0x30);
      *(undefined4 *)(iVar5 + 0x30) = uVar2;
      uVar2 = *(undefined4 *)(iVar5 + 0x18);
      *(undefined4 *)(iVar5 + 0x18) = *(undefined4 *)(iVar5 + 0x24);
      *(undefined4 *)(iVar5 + 0x24) = uVar2;
      uVar2 = *(undefined4 *)(iVar5 + 0x1c);
      *(undefined4 *)(iVar5 + 0x1c) = *(undefined4 *)(iVar5 + 0x34);
      *(undefined4 *)(iVar5 + 0x34) = uVar2;
      uVar2 = *(undefined4 *)(iVar5 + 0x2c);
      *(undefined4 *)(iVar5 + 0x2c) = *(undefined4 *)(iVar5 + 0x38);
      *(undefined4 *)(iVar5 + 0x38) = uVar2;
    } while (uVar4 < *param_1);
  }
  if (puVar3 < (uint *)0xffff0016) {
    *param_1 = param_1[3];
    FID_conflict__free((void *)param_1[4]);
    param_1[4] = 0;
    uVar4 = FUN_0063ea48(-(uint)((int)((ulonglong)*param_1 * 2 >> 0x20) != 0) |
                         (uint)((ulonglong)*param_1 * 2));
    uVar6 = 0;
    param_1[4] = uVar4;
    if (*param_1 != 0) {
      do {
        *(short *)(param_1[4] + uVar6 * 2) = (short)uVar6;
        uVar6 = uVar6 + 1;
      } while (uVar6 < *param_1);
    }
  }
  else {
    FUN_0046c6d0(&DAT_006bec44,param_1);
    FID_conflict__free((void *)param_1[4]);
    param_1[4] = 0;
    uVar4 = FUN_0063ea48(-(uint)((int)((ulonglong)*param_1 * 2 >> 0x20) != 0) |
                         (uint)((ulonglong)*param_1 * 2));
    param_1[4] = uVar4;
    iVar7 = *param_1 * 2;
    if ((iVar7 != 0) && ((uint)(*param_2 + iVar7) <= (uint)param_2[1])) {
      FUN_0062cfd0(uVar4,param_2[2] + *param_2,iVar7);
      *param_2 = *param_2 + iVar7;
    }
  }
  FUN_0046c6d0(&DAT_006bec44,&local_4);
  return local_4 == (uint *)0xffff0006;
}


```

## `00471c40`

- Function: `FUN_00471c40`
- Entry: `00471c40`

```c

undefined4 __thiscall FUN_00471c40(int *param_1,uint *param_2)

{
  uint uVar1;
  uint *puVar2;
  uint uVar3;
  undefined4 uVar4;
  int iVar5;
  uint local_4;
  
  puVar2 = param_2;
  local_4 = 0;
  FUN_0046c6d0(&DAT_006bec3c,&local_4);
  if ((((local_4 == 0xffff0007) || (local_4 == 0xffff000d)) && (param_1[1] == 0)) && (*param_1 == 0)
     ) {
    uVar1 = *puVar2;
    FUN_0046c6d0(&DAT_006bec3c,&local_4);
    uVar3 = local_4;
    if (((local_4 == 0xffff0003) || (local_4 == 0xffff0007)) ||
       ((local_4 == 0xffff000e || (local_4 == 0xffff0017)))) {
      param_2 = (uint *)FUN_0042a47f();
      *puVar2 = uVar1;
      if (puVar2[1] <= uVar1) {
        *puVar2 = puVar2[1] - 1;
      }
      FUN_00460c80(puVar2);
      FUN_00471b80(param_2);
    }
    else {
      *puVar2 = uVar1;
      if (puVar2[1] <= uVar1) {
        *puVar2 = puVar2[1] - 1;
      }
    }
    if (uVar3 < 0xffff0008) {
      FUN_0046c6d0(&DAT_006bec44,&param_2);
    }
    uVar4 = FUN_0042a3cc();
    iVar5 = FUN_0046aca0(puVar2);
    if (iVar5 != 0) {
      FUN_00471be0(uVar4);
      return 1;
    }
  }
  return 0;
}


```

