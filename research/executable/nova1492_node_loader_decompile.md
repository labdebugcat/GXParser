# Selected Nova1492 Decompilation

## `004539c0`

- Function: `FUN_004539c0`
- Entry: `004539c0`

```c

void __thiscall FUN_004539c0(undefined4 *param_1,uint *param_2)

{
  uint uVar1;
  int *piVar2;
  undefined4 *puVar3;
  int *piVar4;
  int iVar5;
  int *piVar6;
  int *piVar7;
  int *piVar8;
  undefined4 *puVar9;
  undefined1 local_200 [64];
  undefined1 local_1c0 [76];
  undefined4 *local_174;
  undefined4 local_170;
  uint local_16c;
  int *local_168;
  uint *local_164;
  undefined4 *local_160;
  int *local_15c;
  int local_158 [12];
  undefined1 local_128 [260];
  uint local_24;
  undefined1 *puStack_20;
  void *local_1c;
  undefined1 *puStack_18;
  uint local_14;
  
  puStack_20 = &stack0xfffffffc;
  local_14 = 0xffffffff;
  puStack_18 = &LAB_0065e778;
  local_1c = ExceptionList;
  local_24 = DAT_007360c8 ^ (uint)&stack0xfffffff0;
  ExceptionList = &local_1c;
  local_164 = param_2;
  local_160 = param_1;
  if ((param_1[0x17] != 0) || (param_1[0x12] != 0)) {
    FUN_004d8000(local_24);
    goto LAB_00453ee0;
  }
  local_16c = 0;
  puStack_20 = &stack0xfffffffc;
  FUN_0046c6d0(&DAT_006bec3c,&local_16c);
  if (((local_16c == 0xffff0001) || (local_16c == 0xffff000a)) || (local_16c == 0xffff000b)) {
LAB_00453a70:
    if (0xffff000f < local_16c) goto LAB_00453a77;
    FUN_0046c6d0(&DAT_006bec44,&local_15c);
  }
  else {
    if (local_16c != 0xffff0010) {
      if (local_16c != 0xffff0012) goto LAB_00453ee0;
      goto LAB_00453a70;
    }
LAB_00453a77:
    uVar1 = *param_2 + 4;
    if (uVar1 <= param_2[1]) {
      local_15c = *(int **)(param_2[2] + *param_2);
      *param_2 = uVar1;
    }
  }
  if (local_15c < (int *)0x100) {
    _memset(local_128,0,0xff);
    if (local_15c != (int *)0x0) {
      local_168 = (int *)(*param_2 + (int)local_15c);
      if (local_168 <= (int *)param_2[1]) {
        FUN_0062cfd0(local_128,param_2[2] + *param_2,local_15c);
        *param_2 = (uint)local_168;
      }
    }
    FUN_00455e50(local_128);
    uVar1 = *param_2;
    if (local_16c < 0xffff0012) {
      piVar6 = (int *)(uVar1 + 0x40);
      if (local_16c < 0xffff0010) {
        local_168 = piVar6;
        if (piVar6 <= (int *)param_2[1]) {
          FUN_0062cfd0(local_1c0,param_2[2] + uVar1,0x40);
          *param_2 = (uint)local_168;
        }
        puVar3 = (undefined4 *)FUN_0045aa00(local_200);
        puVar9 = param_1;
        for (iVar5 = 0x10; param_2 = local_164, param_1 = local_160, iVar5 != 0; iVar5 = iVar5 + -1)
        {
          *puVar9 = *puVar3;
          puVar3 = puVar3 + 1;
          puVar9 = puVar9 + 1;
        }
      }
      else if (piVar6 <= (int *)param_2[1]) {
        FUN_0062cfd0(param_1,param_2[2] + uVar1,0x40);
        *param_2 = *param_2 + 0x40;
      }
      if (*param_2 + 0x40 <= param_2[1]) {
        *param_2 = *param_2 + 0x40;
      }
    }
    else if (uVar1 + 0x40 <= param_2[1]) {
      FUN_0062cfd0(param_1,param_2[2] + uVar1,0x40);
      *param_2 = *param_2 + 0x40;
    }
    if ((0xffff000a < local_16c) && (*param_2 + 4 <= param_2[1])) {
      param_1[0x10] = *(undefined4 *)(param_2[2] + *param_2);
      *param_2 = *param_2 + 4;
    }
    _eh_vector_constructor_iterator_
              (local_158,0x10,3,(_func_void_void_ptr *)&LAB_004359e0,FUN_00435a80);
    local_14 = 0;
    local_168 = local_158;
    local_164 = (uint *)0x0;
    puVar3 = local_160;
LAB_00453c2a:
    local_15c = (int *)*param_2;
    FUN_0046c6d0(&DAT_006bec3c,&local_170);
    switch(local_170) {
    case 0xffff0000:
      *param_2 = (uint)local_15c;
      if ((int *)param_2[1] <= local_15c) {
        *param_2 = (int)param_2[1] - 1;
      }
      local_164 = (uint *)((int)local_164 + 1);
      local_168 = local_168 + 4;
      iVar5 = FUN_00435ad0(param_2);
      if (iVar5 == 0) {
        FUN_004d8000();
      }
      goto LAB_00453c2a;
    case 0xffff0001:
    case 0xffff000a:
    case 0xffff000b:
    case 0xffff0010:
    case 0xffff0012:
      piVar6 = (int *)param_2[1];
      *param_2 = (uint)local_15c;
      if (piVar6 <= local_15c) {
        *param_2 = (int)piVar6 - 1;
      }
      local_15c = (int *)FUN_00431780(0,piVar6);
      iVar5 = FUN_004539c0(param_2);
      if (iVar5 == 0) goto LAB_00453ead;
      if (local_15c != (int *)0x0) {
        if (puVar3[0x17] == 0) {
          puVar3[0x17] = local_15c;
          local_15c[0x18] = (int)puVar3;
        }
        else {
          FUN_00455350(local_15c,puVar3);
        }
      }
      goto LAB_00453c2a;
    default:
LAB_00453ead:
      FUN_004d8000();
LAB_00453eb4:
      local_14 = 0xffffffff;
      _eh_vector_destructor_iterator_(local_158,0x10,3,FUN_00435a80);
      break;
    case 0xffff0006:
      if (local_16c < 0xffff000a) {
        piVar6 = (int *)0x0;
        piVar7 = (int *)0x0;
        local_15c = (int *)0x0;
        if (local_164 != (uint *)0x0) {
          piVar4 = local_158;
          piVar8 = piVar7;
          do {
            iVar5 = *piVar4;
            piVar7 = piVar8;
            piVar2 = piVar4;
            if (((iVar5 != 0) && (piVar7 = piVar4, piVar2 = local_15c, iVar5 != 1)) &&
               (piVar7 = piVar8, iVar5 == 2)) {
              piVar6 = piVar4;
            }
            local_15c = piVar2;
            piVar4 = piVar4 + 4;
            local_164 = (uint *)((int)local_164 + -1);
            piVar8 = piVar7;
          } while (local_164 != (uint *)0x0);
        }
        FUN_00455500(piVar6,piVar7,local_15c);
      }
      goto LAB_00453eb4;
    case 0xffff0007:
    case 0xffff000d:
      local_174 = (undefined4 *)FUN_0063ea48(0x14);
      if (local_174 == (undefined4 *)0x0) {
        puVar9 = (undefined4 *)0x0;
      }
      else {
        local_174[2] = 0;
        local_174[1] = 0;
        local_174[3] = 0;
        *local_174 = 0;
        local_174[4] = 0;
        puVar9 = local_174;
      }
      local_14 = local_14 & 0xffffff00;
      *param_2 = (uint)local_15c;
      if ((int *)param_2[1] <= local_15c) {
        *param_2 = (int)param_2[1] - 1;
      }
      iVar5 = FUN_00471c40(param_2);
      if (iVar5 == 0) {
        FUN_004d8000();
      }
      iVar5 = local_160[0x12];
      puVar3 = local_160;
      if (iVar5 == 0) {
        local_160[0x12] = puVar9;
        if (puVar9 != (undefined4 *)0x0) {
          puVar9[4] = puVar9[4] + 1;
        }
      }
      else if (puVar9 != (undefined4 *)0x0) {
        if (*(int *)(iVar5 + 8) == 0) {
          *(undefined4 **)(iVar5 + 8) = puVar9;
          puVar9[4] = puVar9[4] + 1;
        }
        else {
          FUN_00471c20(puVar9);
          puVar3 = local_160;
        }
      }
      goto LAB_00453c2a;
    case 0xffff0009:
    case 0xffff0011:
    case 0xffff0016:
      *param_2 = (uint)local_15c;
      if ((int *)param_2[1] <= local_15c) {
        *param_2 = (int)param_2[1] - 1;
      }
      if (puVar3[0x13] != 0) {
        FUN_00431540(puVar3[0x13]);
        puVar3[0x13] = 0;
      }
      local_15c = (int *)FUN_004316d0();
      iVar5 = FUN_00435c80(param_2);
      if (iVar5 == 0) {
        FUN_004d8000();
      }
      if (puVar3[0x13] != 0) {
        FUN_00431540(puVar3[0x13]);
      }
      puVar3[0x13] = local_15c;
      if (local_15c == (int *)0x0) {
        puVar3[0x10] = puVar3[0x10] & 0xfffffffb;
      }
      else {
        local_15c[2] = local_15c[2] + 1;
        puVar3[0x10] = puVar3[0x10] | 4;
      }
      goto LAB_00453c2a;
    }
  }
LAB_00453ee0:
  ExceptionList = local_1c;
  __security_check_cookie(local_24 ^ (uint)&stack0xfffffff0);
  return;
}


```

