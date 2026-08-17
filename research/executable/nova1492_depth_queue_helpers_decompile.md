# Selected Nova1492 Decompilation

## `00446870`

- Function: `FUN_00446870`
- Entry: `00446870`

```c

void FUN_00446870(void)

{
  int iVar1;
  uint uVar2;
  uint uVar3;
  int iVar4;
  
  if (DAT_00784570 != 2) {
    DAT_00784570 = 2;
    (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x13,5);
    (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x14,6);
  }
  if ((DAT_007c5eca != '\0') && (DAT_007852e4 != 0)) {
    uVar3 = 0;
    if (DAT_007852e0 != 0) {
      iVar4 = 0;
      iVar1 = DAT_007852e4;
      uVar2 = DAT_007852e0;
      do {
        if (*(int *)(iVar4 + 4 + iVar1) == 0) {
          FUN_0044f410();
          iVar1 = DAT_007852e4;
          uVar2 = DAT_007852e0;
        }
        uVar3 = uVar3 + 1;
        iVar4 = iVar4 + 0x68;
      } while (uVar3 < uVar2);
    }
  }
  if (DAT_00784570 != 1) {
    DAT_00784570 = 1;
    (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x13,5);
    (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x14,6);
  }
  return;
}


```

## `00431bf0`

- Function: `FUN_00431bf0`
- Entry: `00431bf0`

```c

void __thiscall FUN_00431bf0(int param_1,int param_2,char param_3)

{
  int *piVar1;
  
  if (*(int *)(param_1 + 0x205ac) != 0) {
    if (param_3 != '\0') {
                    /* WARNING: Could not recover jumptable at 0x00431c2f. Too many branches */
                    /* WARNING: Treating indirect jump as call */
      (*(code *)(&PTR_LAB_00432654)[param_2])();
      return;
    }
    if (*(int *)(param_1 + 0x20d6c) != param_2) {
      *(int *)(param_1 + 0x20d6c) = param_2;
      piVar1 = *(int **)(param_1 + 0x206e4 + param_2 * 4);
      (**(code **)(*piVar1 + 0x14))(piVar1);
      return;
    }
  }
  return;
}


```

## `0042cf70`

- Function: `FUN_0042cf70`
- Entry: `0042cf70`

```c

void __fastcall FUN_0042cf70(int param_1)

{
  int *piVar1;
  undefined4 uVar2;
  int iVar3;
  undefined4 *unaff_ESI;
  undefined4 *puVar4;
  undefined4 *puVar5;
  undefined1 auStack_b8 [8];
  int local_b0;
  undefined4 local_a0 [4];
  undefined4 local_90;
  undefined4 local_8c;
  undefined4 local_88;
  undefined4 local_84;
  undefined4 local_80;
  undefined4 local_7c;
  undefined4 local_78;
  undefined4 local_74;
  undefined4 local_70;
  undefined4 local_6c;
  undefined4 local_68;
  undefined4 local_64;
  undefined4 local_60 [19];
  uint local_14;
  
  local_14 = DAT_007360c8 ^ (uint)auStack_b8;
  piVar1 = *(int **)(param_1 + 0x205ac);
  local_b0 = param_1;
  if (((piVar1 != (int *)0x0) && (*(int *)(param_1 + 0x20104) == 5)) &&
     (*(int *)(param_1 + 0x20dc8) != 0)) {
    local_a0[0] = DAT_008b22e0;
    local_a0[1] = DAT_008b22e4;
    local_a0[2] = DAT_008b22e8;
    local_a0[3] = DAT_008b22ec;
    local_90 = DAT_008b22f0;
    local_8c = DAT_008b22f4;
    local_88 = DAT_008b22f8;
    local_84 = DAT_008b22fc;
    local_80 = DAT_008b2300;
    local_7c = DAT_008b2304;
    local_78 = DAT_008b2308;
    local_74 = DAT_008b230c;
    local_70 = DAT_008b2310;
    local_6c = DAT_008b2314;
    local_68 = DAT_008b2318;
    local_64 = DAT_008b231c;
    puVar4 = local_a0;
    puVar5 = local_60;
    for (iVar3 = 0x10; iVar3 != 0; iVar3 = iVar3 + -1) {
      *puVar5 = *puVar4;
      puVar4 = puVar4 + 1;
      puVar5 = puVar5 + 1;
    }
    (**(code **)(*piVar1 + 0xb0))(piVar1,0x100,local_60);
    if (*(char *)(unaff_ESI + 0x8091) != '\0') {
      *(undefined1 *)(unaff_ESI + 0x8091) = 0;
      (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0xe,0);
    }
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x34,1);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],9,1);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x38,8);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x36,1);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x35,1);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x39,1);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x3a,0xffffffff);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x3b,0xffffffff);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x19,8);
    if (*(char *)((int)unaff_ESI + 0x20246) != '\x01') {
      *(undefined1 *)((int)unaff_ESI + 0x20246) = 1;
      (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x1b,1);
    }
    if (unaff_ESI[0x8090] != 0xb) {
      unaff_ESI[0x8090] = 0xb;
      (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x13,1);
      (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x14,2);
    }
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x16,2);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x37,7);
    iVar3 = unaff_ESI[0x8372];
    uVar2 = FUN_00428940(*(undefined4 *)(iVar3 + 8),iVar3 + 0x10);
    *(undefined4 *)(iVar3 + 0x1c) = uVar2;
    FUN_004549a0();
    FUN_00433030(0);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x16,3);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x37,8);
    FUN_00433030(1);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],9,2);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0xe,1);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x34,0);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x16,2);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x34,1);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x39,1);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x38,4);
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x37,1);
    *unaff_ESI = 0x8c000000;
    FUN_00429d5b(1,0,0,0,(float)DAT_007c3920,(float)DAT_007c3924);
    if (*(char *)(unaff_ESI + 0x8091) != '\x01') {
      *(undefined1 *)(unaff_ESI + 0x8091) = 1;
      (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0xe,1);
    }
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x34,0);
    if (*(char *)((int)unaff_ESI + 0x20246) != '\0') {
      *(undefined1 *)((int)unaff_ESI + 0x20246) = 0;
      (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x1b,0);
    }
    (**(code **)(*(int *)unaff_ESI[0x816b] + 0xe4))((int *)unaff_ESI[0x816b],0x19,6);
  }
  __security_check_cookie(local_14 ^ (uint)auStack_b8);
  return;
}


```

## `00459580`

- Function: `FUN_00459580`
- Entry: `00459580`

```c

void __thiscall FUN_00459580(int param_1,uint param_2,uint *param_3)

{
  uint3 uVar1;
  char cVar2;
  undefined4 *puVar3;
  int iVar4;
  int iVar5;
  uint uVar6;
  undefined4 uVar7;
  undefined4 *puVar8;
  undefined2 in_FPUControlWord;
  float10 fVar9;
  float10 extraout_ST1;
  uint *puVar10;
  undefined4 uVar11;
  undefined4 local_a8;
  uint *local_a4;
  int local_a0;
  uint local_9c;
  uint local_98;
  uint local_94;
  uint local_90;
  int local_8c;
  undefined4 *local_88;
  undefined4 *local_84;
  undefined8 local_80;
  uint local_78;
  uint local_74;
  uint local_2c;
  uint *local_28;
  uint local_24;
  undefined4 local_20;
  undefined4 *local_1c;
  uint local_14;
  
  local_14 = DAT_007360c8 ^ (uint)&local_a8;
  DAT_00736dd0 = DAT_00736dd0 + 1;
  local_a4 = param_3;
  puVar3 = &DAT_00736d90;
  puVar8 = &DAT_00736e20 + DAT_00736dd0 * 0x10;
  for (iVar4 = 0x10; iVar4 != 0; iVar4 = iVar4 + -1) {
    *puVar8 = *puVar3;
    puVar3 = puVar3 + 1;
    puVar8 = puVar8 + 1;
  }
  local_a0 = param_1;
  FUN_004589c0();
  local_94 = *(uint *)(param_1 + 0x40) | param_2;
  if (*(uint **)(param_1 + 0x58) != (uint *)0x0) {
    local_a4 = *(uint **)(param_1 + 0x58);
  }
  if ((local_94 & 0x10) != 0) {
    iVar4 = *(int *)(param_1 + 0x5c);
    param_1 = local_a0;
    for (; local_a0 = param_1, iVar4 != 0; iVar4 = *(int *)(iVar4 + 100)) {
      FUN_00459580(param_2,local_a4);
      param_1 = local_a0;
    }
  }
  if (((local_94 & 0x20) != 0) && (*(int *)(param_1 + 0x48) != 0)) {
    local_84 = (undefined4 *)(*(int *)(param_1 + 0x50) * 0x40 + local_a4[0xb]);
    puVar3 = &DAT_00736d90;
    puVar8 = local_84;
    for (iVar4 = 0x10; iVar4 != 0; iVar4 = iVar4 + -1) {
      *puVar8 = *puVar3;
      puVar3 = puVar3 + 1;
      puVar8 = puVar8 + 1;
    }
    local_88 = *(undefined4 **)(local_a0 + 0x48);
    if (((param_2 & 0x80000000) == 0) && (local_88 != (undefined4 *)0x0)) {
      local_80 = CONCAT44(local_80._4_4_,local_94) & 0xffffffff40000000;
      local_74 = (local_94 & 0x100 | 0x2000) >> 7;
      uVar6 = local_94 & 0x40000000;
      do {
        local_8c = *local_88;
        iVar4 = local_88[1];
        if (uVar6 == 0) {
          iVar5 = *(int *)(iVar4 + 4);
          local_78 = *local_a4;
          if (iVar5 == 0) {
LAB_004596df:
            local_90 = 0;
          }
          else if ((*(int *)(iVar4 + 0xc) == 0) || (*(uint *)(iVar4 + 8) <= local_78)) {
            if (iVar5 == 0) goto LAB_004596df;
            local_90 = (uint)*(byte *)(iVar5 + 4);
          }
          else {
            local_90 = (uint)*(byte *)(iVar5 + 4 +
                                      *(int *)(*(int *)(iVar4 + 0xc) + local_78 * 4) * 0x1c);
          }
          local_9c = DAT_0073ae68;
          if (iVar5 != 0) {
            if ((*(int *)(iVar4 + 0xc) == 0) || (*(uint *)(iVar4 + 8) <= local_78)) {
              if (iVar5 != 0) {
                local_9c = *(uint *)(iVar5 + 0x18);
              }
            }
            else {
              local_9c = *(uint *)(iVar5 + 0x18 +
                                  *(int *)(*(int *)(iVar4 + 0xc) + local_78 * 4) * 0x1c);
            }
          }
          local_98 = local_9c;
          if (local_90 == 0) {
            iVar5 = FUN_004627c0(local_78);
            uVar7 = 2;
            uVar6 = local_9c;
            if (iVar5 != 0) {
              uVar6 = local_a8 >> 0x10;
              local_a8._0_2_ =
                   CONCAT11((char)(((local_a8 >> 8 & 0xff) * (local_9c >> 8 & 0xff)) / 0xff),
                            (undefined1)local_a8);
              uVar1 = CONCAT12((char)(((uVar6 & 0xff) * (local_98 >> 0x10 & 0xff)) / 0xff),
                               (undefined2)local_a8);
              local_a8 = (uint)uVar1;
              uVar6 = CONCAT31(uVar1 >> 8,(char)(((local_a8 & 0xff) * (local_9c & 0xff)) / 0xff));
            }
          }
          else {
            uVar7 = 3;
            uVar6 = DAT_0073ae68;
          }
          local_a8 = uVar6;
          local_a8 = CONCAT13((char)(((uint)*(byte *)((int)local_a4 + 7) * (local_98 >> 0x18)) /
                                    0xff),(undefined3)local_a8);
        }
        else {
          local_a8 = local_a4[1];
          uVar7 = 2;
        }
        local_20 = local_8c;
        if ((char)(local_a8 >> 0x18) == -1) {
          uVar7 = 3;
        }
        local_1c = local_84;
        local_8c = *(int *)(iVar4 + 4);
        local_2c = local_74;
        iVar5 = local_8c;
        if ((local_8c != 0) && (*(int *)(iVar4 + 0xc) != 0)) {
          iVar5 = local_8c +
                  *(int *)(*(int *)(iVar4 + 0xc) + (*local_a4 % *(uint *)(iVar4 + 8)) * 4) * 0x1c;
        }
        local_28 = local_a4;
        local_24 = local_a8;
        FUN_00470e40(iVar5,&local_2c,uVar7);
        local_88 = (undefined4 *)local_88[2];
        uVar6 = (uint)local_80;
      } while (local_88 != (undefined4 *)0x0);
      local_88 = (undefined4 *)0x0;
    }
    if ((local_94 & 0x300000) == 0x300000) {
      for (puVar3 = *(undefined4 **)(local_a0 + 0x48); puVar3 != (undefined4 *)0x0;
          puVar3 = (undefined4 *)puVar3[2]) {
        iVar4 = puVar3[1];
        iVar5 = *(int *)(iVar4 + 4);
        if (iVar5 == 0) {
LAB_004598ca:
          cVar2 = '\0';
        }
        else if ((*(int **)(iVar4 + 0xc) == (int *)0x0) || (*(int *)(iVar4 + 8) == 0)) {
          if (iVar5 == 0) goto LAB_004598ca;
          cVar2 = *(char *)(iVar5 + 4);
        }
        else {
          cVar2 = *(char *)(iVar5 + 4 + **(int **)(iVar4 + 0xc) * 0x1c);
        }
        if (cVar2 == '\0') {
          local_24 = local_a4[5];
          local_20 = *puVar3;
          local_2c = 0x50;
          local_28 = local_a4;
          local_1c = local_84;
          if ((local_a4[7] < 3) && ((&DAT_007420e4)[local_a4[7]] != 0)) {
            uVar11 = 3;
            puVar10 = &local_2c;
            fVar9 = (float10)FUN_00480070(puVar10,3);
            local_a8 = CONCAT22(local_a8._2_2_,in_FPUControlWord);
            local_80 = (ulonglong)ROUND(fVar9 * extraout_ST1);
            uVar7 = FUN_00462670((uint)local_80);
            FUN_00470e40(uVar7,puVar10,uVar11);
          }
        }
      }
    }
  }
  iVar4 = DAT_00736dd0 * 0x10;
  puVar3 = &DAT_00736e20 + iVar4;
  puVar8 = &DAT_00736d90;
  for (iVar5 = 0x10; iVar5 != 0; iVar5 = iVar5 + -1) {
    *puVar8 = *puVar3;
    puVar3 = puVar3 + 1;
    puVar8 = puVar8 + 1;
  }
  DAT_00736dd0 = DAT_00736dd0 + -1;
  puVar3 = (undefined4 *)FUN_004d4960(&DAT_00736e20 + iVar4);
  puVar8 = &DAT_00736d10;
  for (iVar4 = 0x10; iVar4 != 0; iVar4 = iVar4 + -1) {
    *puVar8 = *puVar3;
    puVar3 = puVar3 + 1;
    puVar8 = puVar8 + 1;
  }
  __security_check_cookie(local_14 ^ (uint)&local_a8);
  return;
}


```

