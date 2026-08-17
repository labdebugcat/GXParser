# Selected Nova1492 Decompilation

## `004589c0`

- Function: `FUN_004589c0`
- Entry: `004589c0`

```c

void __fastcall FUN_004589c0(float param_1)

{
  undefined4 *puVar1;
  uint uVar2;
  float *pfVar3;
  int iVar4;
  float *extraout_EDX;
  float *extraout_EDX_00;
  float *extraout_EDX_01;
  undefined4 *puVar5;
  float *pfVar6;
  float fVar7;
  undefined1 auStack_108 [12];
  float local_fc;
  float local_f8;
  float local_f4;
  float local_f0;
  float local_ec;
  float local_e8;
  float local_e4;
  float local_e0 [4];
  float local_d0;
  float local_cc;
  float local_c8;
  undefined4 local_c4;
  float local_c0;
  float local_bc;
  float local_b8;
  undefined4 local_b4;
  undefined4 local_b0;
  undefined4 local_ac;
  undefined4 local_a8;
  undefined4 local_a4;
  float local_a0 [5];
  float local_8c;
  float local_88;
  undefined4 local_84;
  float local_80;
  float local_7c;
  float local_78;
  undefined4 local_74;
  undefined4 local_70;
  undefined4 local_6c;
  undefined4 local_68;
  undefined4 local_64;
  float local_60 [5];
  float local_4c;
  float local_48;
  undefined4 local_44;
  float local_40;
  float local_3c;
  float local_38;
  undefined4 local_34;
  undefined4 local_30;
  undefined4 local_2c;
  undefined4 local_28;
  undefined4 local_24;
  uint local_14;
  
  local_14 = DAT_007360c8 ^ (uint)auStack_108;
  local_fc = param_1;
  if ((*(uint *)((int)param_1 + 0x40) & 0xf000) == 0) {
    puVar1 = (undefined4 *)FUN_00435620(local_e0,param_1);
    puVar5 = &DAT_00736d90;
    for (iVar4 = 0x10; iVar4 != 0; iVar4 = iVar4 + -1) {
      *puVar5 = *puVar1;
      puVar1 = puVar1 + 1;
      puVar5 = puVar5 + 1;
    }
    puVar1 = (undefined4 *)FUN_004d4960(&DAT_00736d90);
    puVar5 = &DAT_00736d10;
    for (iVar4 = 0x10; iVar4 != 0; iVar4 = iVar4 + -1) {
      *puVar5 = *puVar1;
      puVar1 = puVar1 + 1;
      puVar5 = puVar5 + 1;
    }
    __security_check_cookie(local_14 ^ (uint)auStack_108);
    return;
  }
  puVar1 = (undefined4 *)FUN_00435620(local_e0,param_1);
  puVar5 = &DAT_00736d90;
  for (iVar4 = 0x10; iVar4 != 0; iVar4 = iVar4 + -1) {
    *puVar5 = *puVar1;
    puVar1 = puVar1 + 1;
    puVar5 = puVar5 + 1;
  }
  puVar1 = (undefined4 *)FUN_004d4960(&DAT_00736d90);
  local_78 = DAT_008b2308;
  local_a0[1] = DAT_008b22e4;
  local_a0[0] = DAT_008b22e0;
  puVar5 = &DAT_00736d10;
  for (iVar4 = 0x10; iVar4 != 0; iVar4 = iVar4 + -1) {
    *puVar5 = *puVar1;
    puVar1 = puVar1 + 1;
    puVar5 = puVar5 + 1;
  }
  local_a0[2] = DAT_008b22e8;
  local_70 = DAT_008b2310;
  local_a0[3] = (float)DAT_008b22ec;
  local_6c = DAT_008b2314;
  local_a0[4] = DAT_008b22f0;
  local_68 = DAT_008b2318;
  local_8c = DAT_008b22f4;
  local_64 = DAT_008b231c;
  local_88 = DAT_008b22f8;
  local_84 = DAT_008b22fc;
  local_80 = DAT_008b2300;
  local_7c = DAT_008b2304;
  local_74 = DAT_008b230c;
  pfVar3 = local_a0;
  pfVar6 = local_60;
  for (iVar4 = 0x10; iVar4 != 0; iVar4 = iVar4 + -1) {
    *pfVar6 = *pfVar3;
    pfVar3 = pfVar3 + 1;
    pfVar6 = pfVar6 + 1;
  }
  local_28 = DAT_008b2318;
  local_24 = DAT_008b231c;
  local_e0[0] = DAT_008b22e0;
  local_e0[1] = DAT_008b22e4;
  local_e0[2] = DAT_008b22e8;
  local_e0[3] = (float)DAT_008b22ec;
  local_d0 = DAT_008b22f0;
  local_cc = DAT_008b22f4;
  local_c8 = DAT_008b22f8;
  local_c4 = DAT_008b22fc;
  local_c0 = DAT_008b2300;
  DAT_0078442f = 0;
  local_30 = DAT_008b2310;
  local_2c = DAT_008b2314;
  local_60[3] = 0.0;
  local_44 = 0;
  local_34 = 0;
  local_bc = DAT_008b2304;
  local_b4 = DAT_008b230c;
  local_b8 = local_78;
  local_b0 = DAT_008b2310;
  local_ac = DAT_008b2314;
  local_a4 = DAT_008b231c;
  local_a8 = DAT_008b2318;
  pfVar3 = local_e0;
  pfVar6 = local_a0;
  for (iVar4 = 0x10; iVar4 != 0; iVar4 = iVar4 + -1) {
    *pfVar6 = *pfVar3;
    pfVar3 = pfVar3 + 1;
    pfVar6 = pfVar6 + 1;
  }
  uVar2 = *(uint *)((int)local_fc + 0x40) & 0xf000;
  local_a0[3] = 0.0;
  local_84 = 0;
  local_74 = 0;
  if (uVar2 == 0x1000) {
    local_f4 = DAT_006daa00 /
               SQRT(DAT_00736da0 * DAT_00736da0 + DAT_00736d90 * DAT_00736d90 +
                    DAT_00736db0 * DAT_00736db0);
    local_f8 = local_f4 * DAT_00736d90;
    local_fc = local_f4 * DAT_00736db0;
    local_f4 = local_f4 * DAT_00736da0;
    local_4c = DAT_006daa00 /
               SQRT(DAT_00736da4 * DAT_00736da4 + DAT_00736d94 * DAT_00736d94 +
                    DAT_00736db4 * DAT_00736db4);
    local_e4 = local_4c * DAT_00736db4;
    local_60[1] = local_4c * DAT_00736d94;
    local_4c = local_4c * DAT_00736da4;
    local_38 = DAT_006daa00 /
               SQRT(DAT_00736da8 * DAT_00736da8 + DAT_00736d98 * DAT_00736d98 +
                    DAT_00736db8 * DAT_00736db8);
    local_60[2] = DAT_00736d98 * local_38;
    local_48 = DAT_00736da8 * local_38;
    local_38 = DAT_00736db8 * local_38;
    local_60[0] = local_f8;
    local_60[4] = local_f4;
    local_40 = local_fc;
    local_3c = local_e4;
    FUN_00444400();
    local_a0[2] = DAT_007388a0;
    pfVar3 = local_e0;
    pfVar6 = extraout_EDX;
    for (iVar4 = 0x10; iVar4 != 0; iVar4 = iVar4 + -1) {
      *pfVar6 = *pfVar3;
      pfVar3 = pfVar3 + 1;
      pfVar6 = pfVar6 + 1;
    }
    local_a0[1] = local_fc * DAT_007388a4 - local_f4 * DAT_007388a8;
    local_8c = local_f8 * DAT_007388a8 - local_fc * local_a0[2];
    local_7c = local_f4 * local_a0[2] - local_f8 * DAT_007388a4;
    fVar7 = DAT_006daa00 /
            SQRT(local_a0[1] * local_a0[1] + local_8c * local_8c + local_7c * local_7c);
    local_a0[0] = local_f8;
    local_a0[4] = local_f4;
    local_a0[1] = local_a0[1] * fVar7;
    local_80 = local_fc;
    local_8c = local_8c * fVar7;
    local_7c = local_7c * fVar7;
    local_88 = DAT_007388a4;
    local_78 = DAT_007388a8;
  }
  else if (uVar2 == 0x2000) {
    local_60[4] = DAT_006daa00 /
                  SQRT(DAT_00736d90 * DAT_00736d90 + DAT_00736da0 * DAT_00736da0 +
                       DAT_00736db0 * DAT_00736db0);
    local_e4 = DAT_00736db0 * local_60[4];
    local_60[0] = DAT_00736d90 * local_60[4];
    local_60[4] = DAT_00736da0 * local_60[4];
    local_f4 = DAT_006daa00 /
               SQRT(DAT_00736d94 * DAT_00736d94 + DAT_00736da4 * DAT_00736da4 +
                    DAT_00736db4 * DAT_00736db4);
    local_fc = local_f4 * DAT_00736d94;
    local_f8 = local_f4 * DAT_00736db4;
    local_f4 = local_f4 * DAT_00736da4;
    local_38 = DAT_006daa00 /
               SQRT(DAT_00736d98 * DAT_00736d98 + DAT_00736da8 * DAT_00736da8 +
                    DAT_00736db8 * DAT_00736db8);
    local_60[2] = local_38 * DAT_00736d98;
    local_48 = local_38 * DAT_00736da8;
    local_38 = local_38 * DAT_00736db8;
    local_60[1] = local_fc;
    local_4c = local_f4;
    local_40 = local_e4;
    local_3c = local_f8;
    FUN_00444400();
    local_a0[2] = DAT_007388a0;
    pfVar3 = local_e0;
    pfVar6 = extraout_EDX_00;
    for (iVar4 = 0x10; iVar4 != 0; iVar4 = iVar4 + -1) {
      *pfVar6 = *pfVar3;
      pfVar3 = pfVar3 + 1;
      pfVar6 = pfVar6 + 1;
    }
    fVar7 = local_f4 * DAT_007388a8 - local_f8 * DAT_007388a4;
    local_88 = DAT_007388a4;
    local_a0[4] = local_f8 * local_a0[2] - local_fc * DAT_007388a8;
    local_80 = local_fc * DAT_007388a4 - local_f4 * local_a0[2];
    local_a0[0] = DAT_006daa00 /
                  SQRT(fVar7 * fVar7 + local_a0[4] * local_a0[4] + local_80 * local_80);
    local_80 = local_a0[0] * local_80;
    local_a0[4] = local_a0[0] * local_a0[4];
    local_a0[0] = local_a0[0] * fVar7;
    local_a0[1] = local_fc;
    local_8c = local_f4;
    local_78 = DAT_007388a8;
    local_7c = local_f8;
  }
  else {
    if (uVar2 != 0x7000) goto LAB_00459508;
    local_fc = DAT_006daa00 /
               SQRT(DAT_00736d90 * DAT_00736d90 + DAT_00736da0 * DAT_00736da0 +
                    DAT_00736db0 * DAT_00736db0);
    local_e4 = local_fc * DAT_00736d90;
    local_f4 = local_fc * DAT_00736db0;
    local_fc = local_fc * DAT_00736da0;
    local_4c = DAT_006daa00 /
               SQRT(DAT_00736d94 * DAT_00736d94 + DAT_00736da4 * DAT_00736da4 +
                    DAT_00736db4 * DAT_00736db4);
    local_f8 = DAT_00736db4 * local_4c;
    local_60[1] = DAT_00736d94 * local_4c;
    local_4c = DAT_00736da4 * local_4c;
    local_38 = DAT_006daa00 /
               SQRT(DAT_00736d98 * DAT_00736d98 + DAT_00736da8 * DAT_00736da8 +
                    DAT_00736db8 * DAT_00736db8);
    local_60[2] = DAT_00736d98 * local_38;
    local_48 = DAT_00736da8 * local_38;
    local_38 = DAT_00736db8 * local_38;
    local_60[0] = local_e4;
    local_60[4] = local_fc;
    local_40 = local_f4;
    local_3c = local_f8;
    FUN_00444400();
    local_88 = DAT_007388a4;
    local_a0[2] = DAT_007388a0;
    pfVar3 = local_e0;
    pfVar6 = extraout_EDX_01;
    for (iVar4 = 0x10; iVar4 != 0; iVar4 = iVar4 + -1) {
      *pfVar6 = *pfVar3;
      pfVar3 = pfVar3 + 1;
      pfVar6 = pfVar6 + 1;
    }
    local_a0[0] = DAT_007388a8 - local_88 * 0.0;
    local_e4 = local_88 * 0.0 - local_a0[2];
    local_a0[4] = local_a0[2] * 0.0 - DAT_007388a8 * 0.0;
    fVar7 = DAT_006daa00 /
            SQRT(local_a0[0] * local_a0[0] + local_a0[4] * local_a0[4] + local_e4 * local_e4);
    local_e4 = local_e4 * fVar7;
    local_a0[4] = local_a0[4] * fVar7;
    local_a0[0] = local_a0[0] * fVar7;
    local_a0[1] = local_e4 * local_88 - local_a0[4] * DAT_007388a8;
    local_8c = local_a0[0] * DAT_007388a8 - local_e4 * local_a0[2];
    local_7c = local_a0[4] * local_a0[2] - local_a0[0] * local_88;
    fVar7 = DAT_006daa00 /
            SQRT(local_a0[1] * local_a0[1] + local_8c * local_8c + local_7c * local_7c);
    local_a0[1] = local_a0[1] * fVar7;
    local_8c = local_8c * fVar7;
    local_7c = local_7c * fVar7;
    local_80 = local_e4;
    local_78 = DAT_007388a8;
  }
  DAT_007388a8 = local_78;
  local_f0 = local_a0[2];
  local_ec = local_88;
  local_e8 = local_78;
  pfVar3 = (float *)FUN_00435620(local_e0,local_a0);
  pfVar6 = local_a0;
  for (iVar4 = 0x10; iVar4 != 0; iVar4 = iVar4 + -1) {
    *pfVar6 = *pfVar3;
    pfVar3 = pfVar3 + 1;
    pfVar6 = pfVar6 + 1;
  }
LAB_00459508:
  FUN_004808b0(local_a0);
  __security_check_cookie(local_14 ^ (uint)auStack_108);
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

## `004599d0`

- Function: `FUN_004599d0`
- Entry: `004599d0`

```c

void __thiscall FUN_004599d0(float *param_1,float param_2,float param_3,float param_4)

{
  float fVar1;
  float *pfVar2;
  int iVar3;
  float fVar4;
  
  fVar1 = DAT_006daa00;
  fVar4 = DAT_006daa00 * param_1[3];
  *param_1 = param_2 * *param_1;
  param_1[1] = param_2 * param_1[1];
  param_1[2] = param_2 * param_1[2];
  param_1[3] = fVar4;
  param_1[4] = param_3 * param_1[4];
  param_1[5] = param_3 * param_1[5];
  param_1[6] = param_3 * param_1[6];
  param_1[7] = fVar1 * param_1[7];
  param_1[8] = param_4 * param_1[8];
  param_1[9] = param_4 * param_1[9];
  param_1[10] = param_4 * param_1[10];
  param_1[0xb] = fVar1 * param_1[0xb];
  fVar1 = param_1[0x13];
  if (fVar1 != 0.0) {
    pfVar2 = *(float **)((int)fVar1 + 4);
    for (iVar3 = *(int *)((int)fVar1 + 0xc); iVar3 != 0; iVar3 = iVar3 + -1) {
      *pfVar2 = *pfVar2 * param_2;
      pfVar2[1] = pfVar2[1] * param_2;
      pfVar2[2] = pfVar2[2] * param_2;
      pfVar2[3] = pfVar2[3] * param_2;
      pfVar2[4] = pfVar2[4] * param_3;
      pfVar2[5] = pfVar2[5] * param_3;
      pfVar2[6] = pfVar2[6] * param_3;
      pfVar2[7] = pfVar2[7] * param_3;
      pfVar2[8] = pfVar2[8] * param_4;
      pfVar2[9] = pfVar2[9] * param_4;
      pfVar2[10] = pfVar2[10] * param_4;
      pfVar2[0xb] = pfVar2[0xb] * param_4;
      pfVar2 = pfVar2 + 0x10;
    }
  }
  return;
}


```

