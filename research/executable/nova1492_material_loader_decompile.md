# Selected Nova1492 Decompilation

## `00460c80`

- Function: `FUN_00460c80`
- Entry: `00460c80`

```c

void __thiscall FUN_00460c80(uint *param_1,uint *param_2)

{
  longlong lVar1;
  undefined4 *puVar2;
  uint uVar3;
  int iVar4;
  void *pvVar5;
  undefined4 uVar6;
  uint uVar7;
  undefined4 *puVar8;
  undefined2 *puVar9;
  uint *puVar10;
  undefined4 local_13c;
  uint local_138;
  uint local_134;
  void *local_130;
  undefined4 *local_12c;
  undefined2 *local_128;
  undefined2 *local_124;
  undefined2 *local_120;
  undefined1 local_11c [264];
  uint local_14;
  void *local_10;
  undefined1 *puStack_c;
  undefined4 local_8;
  
  local_8 = 0xffffffff;
  puStack_c = &LAB_006601c6;
  local_10 = ExceptionList;
  uVar3 = DAT_007360c8 ^ (uint)&stack0xfffffffc;
  ExceptionList = &local_10;
  local_14 = uVar3;
  FUN_0046c6d0(&DAT_006bec3c,&local_134);
  uVar7 = local_134;
  if ((((local_134 == 0xffff0003) || (local_134 == 0xffff0007)) || (local_134 == 0xffff000e)) ||
     (local_134 == 0xffff0017)) {
    pvVar5 = (void *)param_1[1];
    if (pvVar5 != (void *)0x0) {
      _eh_vector_destructor_iterator_(pvVar5,0x1c,*(uint *)((int)pvVar5 + -4),guard_check_icall);
      FUN_0062a696((int *)((int)pvVar5 + -4),*(int *)((int)pvVar5 + -4) * 0x1c + 4,uVar3);
    }
    param_1[1] = 0;
    FID_conflict__free((void *)param_1[3]);
    param_1[3] = 0;
    *param_1 = 1;
    param_1[2] = 0;
    if (0xffff000d < uVar7) {
      if (*param_2 + 4 <= param_2[1]) {
        *param_1 = *(uint *)(param_2[2] + *param_2);
        *param_2 = *param_2 + 4;
      }
      if (*param_2 + 4 <= param_2[1]) {
        param_1[2] = *(uint *)(param_2[2] + *param_2);
        *param_2 = *param_2 + 4;
      }
      if (param_1[2] != 0) {
        lVar1 = (ulonglong)param_1[2] * 4;
        local_130 = (void *)FUN_0063ea48(-(uint)((int)((ulonglong)lVar1 >> 0x20) != 0) | (uint)lVar1
                                        );
        param_1[3] = (uint)local_130;
        iVar4 = param_1[2] * 4;
        if ((iVar4 != 0) && (*param_2 + iVar4 <= param_2[1])) {
          FUN_0062cfd0(local_130,param_2[2] + *param_2,iVar4);
          *param_2 = *param_2 + iVar4;
        }
      }
    }
    local_130 = (void *)*param_1;
    uVar3 = -(uint)((int)(ZEXT48(local_130) * 0x1c >> 0x20) != 0) | (uint)(ZEXT48(local_130) * 0x1c)
    ;
    local_12c = (undefined4 *)FUN_0063ea48(-(uint)(0xfffffffb < uVar3) | uVar3 + 4);
    pvVar5 = local_130;
    local_8 = 0;
    if (local_12c == (undefined4 *)0x0) {
      pvVar5 = (void *)0x0;
    }
    else {
      *local_12c = local_130;
      local_130 = local_12c + 1;
      _eh_vector_constructor_iterator_
                (local_130,0x1c,(uint)pvVar5,(_func_void_void_ptr *)&LAB_0045a940,guard_check_icall)
      ;
      pvVar5 = local_130;
    }
    local_8 = 0xffffffff;
    param_1[1] = (uint)pvVar5;
    local_138 = 0;
    if (*param_1 != 0) {
      local_130 = (void *)0x0;
      do {
        puVar8 = (undefined4 *)(param_1[1] + (int)local_130);
        if (*param_2 + 4 <= param_2[1]) {
          puVar8[2] = *(undefined4 *)(param_2[2] + *param_2);
          *param_2 = *param_2 + 4;
        }
        if (*param_2 + 4 <= param_2[1]) {
          puVar8[6] = *(undefined4 *)(param_2[2] + *param_2);
          *param_2 = *param_2 + 4;
        }
        if (*param_2 + 4 <= param_2[1]) {
          puVar8[4] = *(undefined4 *)(param_2[2] + *param_2);
          *param_2 = *param_2 + 4;
        }
        if (uVar7 < 0xffff000e) {
          FUN_0046c6d0(&DAT_006bf018,puVar8 + 5);
        }
        else if (*param_2 + 4 <= param_2[1]) {
          puVar8[5] = *(undefined4 *)(param_2[2] + *param_2);
          *param_2 = *param_2 + 4;
        }
        if (*param_2 + 4 <= param_2[1]) {
          puVar8[3] = *(undefined4 *)(param_2[2] + *param_2);
          *param_2 = *param_2 + 4;
        }
        if (0xffff0006 < uVar7) {
          if (*param_2 + 4 <= param_2[1]) {
            puVar8[1] = *(undefined4 *)(param_2[2] + *param_2);
            *param_2 = *param_2 + 4;
          }
          if (uVar7 == 0xffff000e) {
            if ((puVar8[1] & 0x10000) != 0) {
              puVar8[1] = puVar8[1] | 0x40000;
            }
            if ((puVar8[1] & 0x20000) != 0) {
              puVar8[1] = puVar8[1] | 0x80000;
            }
          }
        }
        FUN_0046c6d0(&DAT_006bec3c,&local_134);
        uVar7 = local_134;
        if (local_134 == 0xffff0004) {
          _memset(local_11c,0,0x104);
          local_12c = (undefined4 *)0x0;
          FUN_0046c6d0(&DAT_006bec44,&local_12c);
          puVar2 = local_12c;
          if (0 < (int)local_12c) {
            local_12c = (undefined4 *)(*param_2 + (int)local_12c);
            if (local_12c <= (undefined4 *)param_2[1]) {
              FUN_0062cfd0(local_11c,param_2[2] + *param_2,puVar2);
              *param_2 = (uint)local_12c;
            }
            uVar6 = FUN_0042a5cd(local_11c,0,0x3000);
            *puVar8 = uVar6;
          }
        }
        else {
          if (local_134 == 0xffff000f) {
            local_124 = (undefined2 *)0x0;
            puVar10 = param_2;
            FUN_004629f0(&local_124,param_2);
            local_8 = 1;
            puVar9 = local_124;
            if (*(int *)(local_124 + -2) != 0) {
              uVar6 = FUN_0042aaf5(0x3000,local_124,local_124 + *(int *)(local_124 + -2),0,puVar10);
              *puVar8 = uVar6;
              puVar9 = local_124;
            }
          }
          else {
            if (local_134 != 0xffff0013) {
              if (local_134 != 0xffff0006) goto LAB_0046118e;
              goto LAB_004611fc;
            }
            local_120 = (undefined2 *)0x0;
            FUN_004629f0(&local_120,param_2);
            local_8 = 0x14;
            local_128 = (undefined2 *)0x0;
            puVar10 = param_2;
            FUN_004629f0(&local_128,param_2);
            local_8._0_1_ = 0x15;
            if (*(int *)(local_120 + -2) != 0) {
              if (*(int *)(local_128 + -2) == 0) {
                puVar9 = (undefined2 *)0x0;
              }
              else {
                puVar10 = (uint *)(local_128 + *(int *)(local_128 + -2));
                puVar9 = local_128;
              }
              uVar6 = FUN_0042aaf5(0x3000,local_120,local_120 + *(int *)(local_120 + -2),puVar9,
                                   puVar10);
              *puVar8 = uVar6;
            }
            local_8 = CONCAT31(local_8._1_3_,0x14);
            puVar9 = local_120;
            if (local_128 != &DAT_006b9e28) {
              FUN_0059c360(local_128 + -2);
              puVar9 = local_120;
            }
          }
          local_8 = 0xffffffff;
          if (puVar9 != &DAT_006b9e28) {
            FUN_0059c360(puVar9 + -2);
          }
        }
LAB_0046118e:
        local_138 = local_138 + 1;
        local_13c = CONCAT13(*(undefined1 *)((int)puVar8 + 0x1b),0xffff00);
        local_13c = CONCAT31(local_13c._1_3_,0xff);
        puVar8[6] = local_13c;
        local_130 = (void *)((int)local_130 + 0x1c);
      } while (local_138 < *param_1);
    }
    FUN_0046c6d0(&DAT_006bec44,&local_134);
  }
LAB_004611fc:
  ExceptionList = local_10;
  __security_check_cookie(local_14 ^ (uint)&stack0xfffffffc);
  return;
}


```

## `00471b80`

- Function: `FUN_00471b80`
- Entry: `00471b80`

```c

void __thiscall FUN_00471b80(int param_1,int param_2)

{
  int iVar1;
  int local_4;
  
  iVar1 = *(int *)(param_1 + 4);
  if (((iVar1 != 0) && (DAT_007848d8 != 0)) &&
     (*(int *)(iVar1 + 0x10) = *(int *)(iVar1 + 0x10) + -1, *(int *)(iVar1 + 0x10) == 0)) {
    local_4 = iVar1;
    FUN_00462950();
    FUN_0062a696(iVar1,0x1c);
    FUN_004336a0(&local_4);
  }
  *(int *)(param_1 + 4) = param_2;
  if (param_2 != 0) {
    *(int *)(param_2 + 0x10) = *(int *)(param_2 + 0x10) + 1;
  }
  return;
}


```

## `00471be0`

- Function: `FUN_00471be0`
- Entry: `00471be0`

```c

void __thiscall FUN_00471be0(undefined4 *param_1,int *param_2)

{
  undefined4 extraout_ECX;
  int *local_4;
  
  local_4 = (int *)*param_1;
  if (local_4 != (int *)0x0) {
    *local_4 = *local_4 + -1;
    if (*local_4 < 1) {
      FUN_004336a0(&local_4);
      FUN_00429aa5(extraout_ECX);
    }
  }
  *param_1 = param_2;
  if (param_2 != (int *)0x0) {
    *param_2 = *param_2 + 1;
  }
  return;
}


```

