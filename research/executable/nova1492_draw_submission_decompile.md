# Selected Nova1492 Decompilation

## `0042ba63`

- Function: `FUN_0042ba63`
- Entry: `0042ba63`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_0042ba63(void)

{
  byte bVar1;
  uint *puVar2;
  int iVar3;
  undefined1 auVar4 [16];
  undefined4 uVar5;
  int iVar6;
  float *pfVar7;
  float *pfVar8;
  undefined4 extraout_ECX;
  undefined2 *puVar9;
  uint uVar10;
  int unaff_EBX;
  int unaff_EBP;
  uint uVar11;
  undefined4 *puVar12;
  undefined4 *puVar13;
  byte *pbVar14;
  float fVar15;
  undefined1 auVar16 [16];
  float fVar17;
  float fVar18;
  float fVar19;
  float fVar20;
  float fVar21;
  float fVar22;
  float fVar23;
  float fVar24;
  undefined1 auVar25 [16];
  float fVar26;
  
  __EH_prolog3_GS_align(0x1a8,0x10);
  pbVar14 = *(byte **)(unaff_EBX + 8);
  *(byte **)(unaff_EBP + -0x80) = pbVar14;
  puVar12 = *(undefined4 **)(pbVar14 + 4);
  *(undefined4 **)(unaff_EBP + -0x90) = puVar12;
  uVar5 = FUN_0046bc00(*puVar12);
  *(undefined4 *)(unaff_EBP + -0x94) = uVar5;
  uVar5 = FUN_0046bbc0(**(undefined4 **)(pbVar14 + 4));
  *(undefined4 *)(unaff_EBP + -0x74) = uVar5;
  uVar5 = FUN_0046bd40(**(undefined4 **)(pbVar14 + 4));
  *(undefined4 *)(unaff_EBP + -0xa0) = uVar5;
  uVar5 = FUN_0046bc40(**(undefined4 **)(pbVar14 + 4));
  *(undefined4 *)(unaff_EBP + -0x9c) = uVar5;
  uVar5 = FUN_0046bd80(**(undefined4 **)(pbVar14 + 4));
  *(undefined4 *)(unaff_EBP + -0x98) = uVar5;
  uVar5 = FUN_0046bcc0(**(undefined4 **)(pbVar14 + 4));
  bVar1 = *pbVar14;
  *(undefined4 *)(unaff_EBP + -0xa4) = uVar5;
  if ((bVar1 & 0x10) == 0) {
    *(undefined4 *)(unaff_EBP + -0x7c) = *(undefined4 *)(pbVar14 + 0x10);
    uVar5 = extraout_ECX;
  }
  else {
    puVar12 = *(undefined4 **)(pbVar14 + 0x10);
    *(undefined4 **)(unaff_EBP + -0x7c) = (undefined4 *)(unaff_EBP + -0x70);
    iVar3 = *(int *)(unaff_EBP + -0x90);
    puVar13 = (undefined4 *)(unaff_EBP + -0x70);
    for (iVar6 = 0x10; iVar6 != 0; iVar6 = iVar6 + -1) {
      *puVar13 = *puVar12;
      puVar12 = puVar12 + 1;
      puVar13 = puVar13 + 1;
    }
    fVar21 = *(float *)(iVar3 + 0x18);
    fVar17 = fVar21 + DAT_008b2310;
    fVar19 = fVar21 + DAT_008b2314;
    fVar21 = fVar21 + DAT_008b2318;
    fVar26 = DAT_008b231c + 0.0;
    *(float *)(unaff_EBP + -0x70) = *(float *)(unaff_EBP + -0x70) * fVar17;
    *(float *)(unaff_EBP + -0x6c) = *(float *)(unaff_EBP + -0x6c) * fVar19;
    *(float *)(unaff_EBP + -0x68) = *(float *)(unaff_EBP + -0x68) * fVar21;
    *(float *)(unaff_EBP + -100) = *(float *)(unaff_EBP + -100) * fVar26;
    *(float *)(unaff_EBP + -0x60) = fVar17 * *(float *)(unaff_EBP + -0x60);
    *(float *)(unaff_EBP + -0x5c) = fVar19 * *(float *)(unaff_EBP + -0x5c);
    *(float *)(unaff_EBP + -0x58) = fVar21 * *(float *)(unaff_EBP + -0x58);
    *(float *)(unaff_EBP + -0x54) = fVar26 * *(float *)(unaff_EBP + -0x54);
    *(float *)(unaff_EBP + -0x50) = fVar17 * *(float *)(unaff_EBP + -0x50);
    *(float *)(unaff_EBP + -0x4c) = fVar19 * *(float *)(unaff_EBP + -0x4c);
    *(float *)(unaff_EBP + -0x48) = fVar21 * *(float *)(unaff_EBP + -0x48);
    *(float *)(unaff_EBP + -0x44) = fVar26 * *(float *)(unaff_EBP + -0x44);
    *(float *)(unaff_EBP + -0x40) = fVar17 * *(float *)(unaff_EBP + -0x40);
    *(float *)(unaff_EBP + -0x3c) = fVar19 * *(float *)(unaff_EBP + -0x3c);
    *(float *)(unaff_EBP + -0x38) = fVar21 * *(float *)(unaff_EBP + -0x38);
    *(float *)(unaff_EBP + -0x34) = fVar26 * *(float *)(unaff_EBP + -0x34);
    uVar5 = 0;
  }
  FUN_00432e90(*(undefined4 *)(unaff_EBP + -0x74),*(undefined4 *)(unaff_EBP + -0x94),uVar5);
  FUN_00481500(unaff_EBP + -0x30);
  iVar3 = DAT_00736c68;
  iVar6 = DAT_00736c64 * 0x18;
  uVar11 = 0;
  *(undefined4 *)(unaff_EBP + -0x8c) = 0;
  *(undefined4 *)(unaff_EBP + -0x18) = 0;
  *(int *)(unaff_EBP + -0x90) = iVar6 + DAT_00736c70;
  *(int *)(unaff_EBP + -0x88) = DAT_00736c58 + iVar3 * 2;
  FUN_0042c01c(*(undefined4 *)(unaff_EBP + -0x74));
  *(undefined4 *)(unaff_EBP + -4) = 0;
  _memset(*(void **)(unaff_EBP + -0x18),0xff,*(int *)(unaff_EBP + -0x74) * 2);
  if (*(int *)(unaff_EBP + -0x94) != 0) {
    fVar26 = 0.0;
    puVar9 = *(undefined2 **)(unaff_EBP + -0x88);
    fVar21 = DAT_006daa00;
    fVar17 = DAT_006da944;
    fVar19 = DAT_006daba0;
    do {
      uVar10 = (uint)*(ushort *)(*(int *)(unaff_EBP + -0x98) + uVar11 * 2);
      *(uint *)(unaff_EBP + -0x84) = uVar10;
      puVar2 = *(uint **)(unaff_EBP + -0x80);
      if (*(short *)(*(int *)(unaff_EBP + -0x18) + uVar10 * 2) == -1) {
        iVar3 = *(int *)(unaff_EBP + -0x9c);
        *(int *)(unaff_EBP + -0x74) = *(int *)(unaff_EBP + -0x90);
        *(int *)(unaff_EBP + -0x90) = *(int *)(unaff_EBP + -0x90) + 0x18;
        *(undefined2 *)(*(int *)(unaff_EBP + -0x18) + uVar10 * 2) = (undefined2)DAT_00736c64;
        DAT_00736c64 = DAT_00736c64 + 1;
        puVar12 = (undefined4 *)(iVar3 + uVar10 * 0xc);
        *(uint *)(unaff_EBP + -0x78) = uVar10 * 0xc;
        if ((*puVar2 & 0x30) == 0) {
          *(undefined4 *)(unaff_EBP + -0xc0) = *puVar12;
          *(undefined4 *)(unaff_EBP + -0xbc) = puVar12[1];
          *(undefined4 *)(unaff_EBP + -0xb8) = puVar12[2];
          *(undefined4 *)(unaff_EBP + -0xb4) = 0x3f800000;
          FUN_00435730(unaff_EBP + -0x110,unaff_EBP + -0xc0);
          pfVar7 = *(float **)(unaff_EBP + -0x74);
          uVar10 = *(uint *)(unaff_EBP + -0x84);
          iVar3 = *(int *)(unaff_EBP + -0xa0);
          fVar18 = *(float *)(unaff_EBP + -0x10c);
          fVar15 = *(float *)(unaff_EBP + -0x108);
          fVar22 = *(float *)(unaff_EBP + -0x104);
          *pfVar7 = *(float *)(unaff_EBP + -0x110);
          pfVar7[1] = fVar18;
          pfVar7[2] = fVar15;
          pfVar7[3] = fVar22;
          pfVar7[4] = *(float *)(iVar3 + uVar10 * 8);
          fVar18 = *(float *)(iVar3 + 4 + uVar10 * 8);
LAB_0042bedb:
          pbVar14 = *(byte **)(unaff_EBP + -0x80);
          pfVar7[5] = fVar18;
        }
        else {
          if ((*puVar2 & 0x10) == 0) {
            *(undefined4 *)(unaff_EBP + -0xe0) = *puVar12;
            *(undefined4 *)(unaff_EBP + -0xdc) = puVar12[1];
            *(undefined4 *)(unaff_EBP + -0xd8) = puVar12[2];
            *(undefined4 *)(unaff_EBP + -0xd4) = 0x3f800000;
            FUN_00435730(unaff_EBP + -0x130,unaff_EBP + -0xe0);
            iVar3 = *(int *)(unaff_EBP + -0xa4);
            iVar6 = *(int *)(unaff_EBP + -0x78);
            auVar16 = *(undefined1 (*) [16])(unaff_EBP + -0x130);
            **(undefined1 (**) [16])(unaff_EBP + -0x74) = auVar16;
            puVar12 = (undefined4 *)(iVar6 + iVar3);
            *(undefined4 *)(unaff_EBP + -0xf0) = *puVar12;
            *(undefined4 *)(unaff_EBP + -0xec) = puVar12[1];
            *(undefined4 *)(unaff_EBP + -0xe8) = puVar12[2];
            *(undefined4 *)(unaff_EBP + -0xe4) = 0;
            FUN_00435730(unaff_EBP + -0x100,unaff_EBP + -0xf0);
            auVar25 = *(undefined1 (*) [16])(unaff_EBP + -0x100);
            fVar18 = auVar25._0_4_ * auVar25._0_4_;
            fVar15 = auVar25._4_4_ * auVar25._4_4_;
            fVar22 = auVar25._8_4_ * auVar25._8_4_;
            fVar24 = auVar25._12_4_ * auVar25._12_4_;
            *(float *)(unaff_EBP + -0x140) = fVar18;
            *(float *)(unaff_EBP + -0x13c) = fVar15;
            *(float *)(unaff_EBP + -0x138) = fVar22;
            *(float *)(unaff_EBP + -0x134) = fVar24;
            pfVar7 = (float *)FUN_004356f0(unaff_EBP + -0x180);
            fVar18 = fVar18 + *pfVar7;
            fVar15 = fVar15 + pfVar7[1];
            fVar22 = fVar22 + pfVar7[2];
            fVar24 = fVar24 + pfVar7[3];
            *(float *)(unaff_EBP + -0x150) = fVar18;
            *(float *)(unaff_EBP + -0x14c) = fVar15;
            *(float *)(unaff_EBP + -0x148) = fVar22;
            *(float *)(unaff_EBP + -0x144) = fVar24;
            pfVar7 = (float *)FUN_00435710(unaff_EBP + -400);
            auVar4._4_4_ = fVar15 + pfVar7[1];
            auVar4._0_4_ = fVar18 + *pfVar7;
            auVar4._8_4_ = fVar22 + pfVar7[2];
            auVar4._12_4_ = fVar24 + pfVar7[3];
            auVar16 = sqrtps(auVar16,auVar4);
            auVar16 = divps(auVar25,auVar16);
            *(undefined1 (*) [16])(unaff_EBP + -0x100) = auVar16;
            fVar15 = auVar16._0_4_ * *(float *)(unaff_EBP + -0x30);
            fVar22 = auVar16._4_4_ * *(float *)(unaff_EBP + -0x2c);
            fVar23 = auVar16._8_4_ * *(float *)(unaff_EBP + -0x28);
            fVar24 = auVar16._12_4_ * *(float *)(unaff_EBP + -0x24);
            *(float *)(unaff_EBP + -0x160) = fVar15;
            *(float *)(unaff_EBP + -0x15c) = fVar22;
            *(float *)(unaff_EBP + -0x158) = fVar23;
            *(float *)(unaff_EBP + -0x154) = fVar24;
            pfVar7 = (float *)FUN_004356f0(unaff_EBP + -0x1a0);
            fVar18 = pfVar7[3];
            fVar15 = *pfVar7 + fVar15;
            fVar22 = pfVar7[1] + fVar22;
            fVar23 = pfVar7[2] + fVar23;
            *(float *)(unaff_EBP + -0x170) = fVar15;
            *(float *)(unaff_EBP + -0x16c) = fVar22;
            *(float *)(unaff_EBP + -0x168) = fVar23;
            *(float *)(unaff_EBP + -0x164) = fVar18 + fVar24;
            pfVar8 = (float *)FUN_00435710(unaff_EBP + -0x1b0);
            pfVar7 = *(float **)(unaff_EBP + -0x74);
            fVar24 = _DAT_006db3f0 * auVar16._0_4_ * (fVar15 + *pfVar8);
            fVar20 = _UNK_006db3f4 * auVar16._4_4_ * (fVar22 + pfVar8[1]);
            fVar15 = *(float *)(unaff_EBP + -0x2c);
            *(float *)(unaff_EBP + -0x78) =
                 _UNK_006db3f8 * auVar16._8_4_ * (fVar23 + pfVar8[2]) -
                 *(float *)(unaff_EBP + -0x28);
            fVar18 = DAT_006da974;
            fVar22 = *(float *)(unaff_EBP + -0x78) * DAT_006da974;
            *(float *)(unaff_EBP + -0x78) = fVar24 - *(float *)(unaff_EBP + -0x30);
            fVar22 = DAT_006da924 / SQRT(fVar18 - fVar22);
            uVar10 = *(uint *)(unaff_EBP + -0x84);
            pfVar7[4] = *(float *)(unaff_EBP + -0x78) * fVar22 + fVar18;
            *(float *)(unaff_EBP + -0x78) = fVar20 - fVar15;
            fVar18 = fVar22 * *(float *)(unaff_EBP + -0x78) + fVar18;
            goto LAB_0042bedb;
          }
          *(undefined4 *)(unaff_EBP + -0xd0) = *puVar12;
          *(undefined4 *)(unaff_EBP + -0xcc) = puVar12[1];
          *(undefined4 *)(unaff_EBP + -200) = puVar12[2];
          iVar3 = *(int *)(unaff_EBP + -0x7c);
          *(undefined4 *)(unaff_EBP + -0xc4) = 0;
          FUN_00435730(unaff_EBP + -0x120,unaff_EBP + -0xd0);
          pfVar7 = *(float **)(unaff_EBP + -0x74);
          fVar18 = *(float *)(unaff_EBP + -0x11c);
          fVar15 = *(float *)(unaff_EBP + -0x118);
          fVar22 = *(float *)(unaff_EBP + -0x114);
          pbVar14 = *(byte **)(unaff_EBP + -0x80);
          *pfVar7 = *(float *)(unaff_EBP + -0x120);
          pfVar7[1] = fVar18;
          pfVar7[2] = fVar15;
          pfVar7[3] = fVar22;
          uVar11 = *(uint *)(*(int *)(pbVar14 + 4) + 0x20) & 0x30000000;
          if (uVar11 == 0x10000000) {
            fVar15 = *pfVar7 * *pfVar7;
            fVar15 = fVar15 / (pfVar7[2] * pfVar7[2] + fVar15);
            fVar18 = pfVar7[1];
LAB_0042bd2f:
            pfVar7[4] = fVar15;
            pfVar7[5] = fVar18 * fVar17 + *(float *)(*(int *)(pbVar14 + 4) + 0x24) * fVar19;
          }
          else if (uVar11 == 0x20000000) {
            fVar15 = *pfVar7 * *pfVar7;
            fVar15 = fVar15 / (pfVar7[1] * pfVar7[1] + fVar15);
            fVar18 = pfVar7[2];
            goto LAB_0042bd2f;
          }
          uVar10 = *(uint *)(unaff_EBP + -0x84);
          *pfVar7 = *(float *)(iVar3 + 0xc) + *pfVar7;
          pfVar7[1] = *(float *)(iVar3 + 0x1c) + pfVar7[1];
          pfVar7[2] = *(float *)(iVar3 + 0x2c) + pfVar7[2];
        }
        if ((*pbVar14 & 0x31) == 0) {
          pfVar8 = *(float **)(*(int *)(pbVar14 + 4) + 0xc);
          fVar18 = fVar26;
          if (pfVar8[1] != _DAT_006daf7c) {
            fVar18 = pfVar8[1] - pfVar7[1];
          }
          fVar18 = (pfVar8[2] - pfVar7[2]) * (pfVar8[2] - pfVar7[2]) +
                   (*pfVar8 - *pfVar7) * (*pfVar8 - *pfVar7) + fVar18 * fVar18;
          if (fVar18 != fVar26) {
            fVar18 = SQRT(fVar18) / pfVar8[3];
            fVar18 = fVar21 - fVar18 * fVar18;
            if (fVar18 < fVar26) {
              fVar18 = fVar26;
            }
            fVar15 = fVar18 * DAT_006dab58;
            if (fVar21 < fVar18 * DAT_006dab58) {
              fVar15 = fVar21;
            }
            *(char *)((int)pfVar7 + 0xe) =
                 (char)(int)((float)*(byte *)((int)pfVar8 + 0x12) * fVar15);
            *(char *)((int)pfVar7 + 0xd) =
                 (char)(int)((float)*(byte *)((int)pfVar8 + 0x11) * fVar15);
            *(char *)(pfVar7 + 3) = (char)(int)((float)*(byte *)(pfVar8 + 4) * fVar15);
            *(undefined1 *)((int)pfVar7 + 0xf) = *(undefined1 *)(unaff_EBX + 0xc);
          }
          uVar10 = *(uint *)(unaff_EBP + -0x84);
        }
        else {
          pfVar7[3] = *(float *)(unaff_EBX + 0xc);
        }
        uVar11 = *(uint *)(unaff_EBP + -0x8c);
        puVar9 = *(undefined2 **)(unaff_EBP + -0x88);
      }
      *puVar9 = *(undefined2 *)(*(int *)(unaff_EBP + -0x18) + uVar10 * 2);
      puVar9 = puVar9 + 1;
      DAT_00736c68 = DAT_00736c68 + 1;
      uVar11 = uVar11 + 1;
      *(undefined2 **)(unaff_EBP + -0x88) = puVar9;
      *(uint *)(unaff_EBP + -0x8c) = uVar11;
    } while (uVar11 < *(uint *)(unaff_EBP + -0x94));
  }
  *(undefined4 *)(unaff_EBP + -4) = 0xffffffff;
  if (*(undefined2 **)(unaff_EBP + -0x18) != &DAT_006b9e28) {
    FUN_0059c360(*(undefined2 **)(unaff_EBP + -0x18) + -2);
  }
  FUN_0065602d();
  return;
}


```

## `0042b98b`

- Function: `FUN_0042b98b`
- Entry: `0042b98b`

```c

void __thiscall FUN_0042b98b(int param_1,char param_2)

{
  if (*(char *)(param_1 + 0x20244) != param_2) {
    *(char *)(param_1 + 0x20244) = param_2;
    (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0xe,param_2);
  }
  return;
}


```

