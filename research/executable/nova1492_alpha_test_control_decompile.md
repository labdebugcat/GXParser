# Selected Nova1492 Decompilation

## `004449b7`

- Function: `FUN_00444730`
- Entry: `00444730`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

undefined4 * FUN_00444730(void)

{
  int iVar1;
  int iVar2;
  uint uVar3;
  int iVar4;
  uint uVar5;
  undefined *puVar6;
  int iVar7;
  float fVar8;
  float fVar9;
  float fVar10;
  undefined4 uVar11;
  undefined *local_20;
  int local_1c;
  uint local_18;
  int local_14;
  void *local_10;
  undefined1 *puStack_c;
  undefined4 local_8;
  
  puStack_c = &LAB_0065d10c;
  local_10 = ExceptionList;
  ExceptionList = &local_10;
  DAT_007852fc = 0;
  _DAT_007b532c = 0;
  DAT_007b5344 = 0;
  DAT_007b5334 = 0;
  DAT_007b5338 = 0;
  _DAT_007b533c = 0;
  _DAT_007b5340 = 0;
  local_8 = 0;
  DAT_007c24a4 = 0;
  DAT_007c24a8 = 0;
  DAT_007c24a4 = FUN_00433c50(0,0);
  local_8 = CONCAT31(local_8._1_3_,3);
  _DAT_007852ec = 0;
  _DAT_007852f0 = 0;
  _DAT_007852f4 = 0;
  _DAT_007852f8 = 0;
  DAT_007852e0 = 0;
  DAT_007852e4 = 0;
  _DAT_007b5318 = DAT_006be290;
  DAT_007b5320 = 0;
  _DAT_007b531c = 0;
  DAT_007c24e0 = 0;
  DAT_007c24dc = 0;
  DAT_007b5324 = 0;
  DAT_007b5328 = 0;
  DAT_007c249c = 0;
  DAT_007c2488 = 0;
  DAT_007c248c = 0;
  DAT_007c2490 = 0;
  DAT_007c2494 = 0;
  DAT_007b53f0 = 0;
  DAT_007b53f8 = 0;
  DAT_007b53fc = 0;
  DAT_007b53f4 = 0;
  DAT_007b5348 = 0;
  DAT_007b534c = 0;
  _DAT_007b5350 = 0;
  _DAT_007b5354 = 0;
  _DAT_007b5358 = 0;
  _DAT_007b535c = 0;
  _DAT_007b5360 = 0;
  _DAT_007b5364 = 0;
  _DAT_007b5368 = 0;
  _DAT_007b536c = 0;
  DAT_007b53ec = 0;
  DAT_007b5400 = 0;
  DAT_007b5404 = 0;
  DAT_007b5408 = 0;
  DAT_007b540c = 0;
  DAT_007b5410 = 0;
  DAT_007b5e94 = 0;
  DAT_007b6bb8 = 0;
  DAT_007b78dc = 0;
  DAT_007b8600 = 0;
  DAT_007b9324 = 0;
  DAT_007c0ea8 = 0;
  DAT_007c1e6c = 0;
  DAT_007c2170 = 0;
  DAT_007c2474 = 0;
  DAT_007ba048 = 0;
  DAT_007bad6c = 0;
  DAT_007bba90 = 0;
  DAT_007bc7b4 = 0;
  DAT_007bd4d8 = 0;
  DAT_007be1fc = 0;
  DAT_007c0184 = 0;
  _DAT_007852e8 = 0x101;
  DAT_007c24a0 = 0;
  uVar11 = 0xffffffff;
  SetRect((LPRECT)&DAT_007c24ac,-1,-1,-1,-1);
  DAT_007c24bc = 0;
  DAT_007c24c0 = 0;
  _DAT_007c24c4 = 0;
  _DAT_007c24c8 = 0;
  DAT_007c24cc = 0;
  DAT_007c24d0 = 0;
  DAT_007c24d4 = 0;
  DAT_007c24d8 = 0;
  DAT_007b5370 = 0;
  DAT_007b539c = 0;
  DAT_007b53c4 = 0;
  DAT_007b5374 = 0;
  DAT_007b53a0 = 0;
  DAT_007b53c8 = 0;
  _DAT_007b5378 = 0;
  _DAT_007b53a4 = 0;
  _DAT_007b53cc = 0;
  _DAT_007b537c = 0;
  _DAT_007b53a8 = 0;
  _DAT_007b53d0 = 0;
  _DAT_007b5380 = 0;
  _DAT_007b53ac = 0;
  _DAT_007b53d4 = 0;
  _DAT_007b5384 = 0;
  _DAT_007b53b0 = 0;
  _DAT_007b53d8 = 0;
  _DAT_007b5388 = 0;
  _DAT_007b53b4 = 0;
  _DAT_007b53dc = 0;
  _DAT_007b538c = 0;
  _DAT_007b53b8 = 0;
  _DAT_007b53e0 = 0;
  _DAT_007b5390 = 0;
  _DAT_007b53bc = 0;
  _DAT_007b53e4 = 0;
  _DAT_007b5394 = 0;
  _DAT_007b53c0 = 0;
  _DAT_007b53e8 = 0;
  DAT_007c2498 = 0;
  DAT_007b5398 = 0;
  DAT_007c2478 = 0;
  DAT_007c247c = 0;
  DAT_007c2484 = 0;
  if (DAT_0073adec != '\0') {
    local_14 = 0;
    DAT_0073adec = '\0';
    local_20 = &DAT_0074b1c0;
    fVar10 = DAT_006da974;
    do {
      local_1c = 0;
      puVar6 = local_20;
      do {
        iVar4 = 0;
        fVar8 = (float)local_1c * fVar10 + DAT_006da924;
        do {
          FUN_00449410(local_14,(float)iVar4 * fVar10 + DAT_006da924,fVar8,uVar11,puVar6);
          iVar4 = iVar4 + 1;
          puVar6 = puVar6 + 0x5ac0;
        } while (iVar4 < 2);
        local_1c = local_1c + 1;
      } while (local_1c < 2);
      local_14 = local_14 + 1;
      local_20 = local_20 + 0x790;
    } while ((int)local_20 < 0x750c80);
    _memset(&DAT_00742100,0,0x90b4);
    local_20 = (undefined *)0xfffffff6;
    local_14 = -0xd2;
    do {
      local_18 = 0xfffffff6;
      do {
        iVar4 = -10;
        do {
          iVar7 = -10;
          do {
            if (iVar7 == 0) {
              if (local_14 < 0) {
                if (iVar4 < (int)local_20) goto LAB_00444d8a;
              }
              else if ((int)local_20 < iVar4) {
LAB_00444d8a:
                if ((0.0 <= (float)(int)local_18 + DAT_006da974) &&
                   ((float)(int)local_18 - DAT_006da974 <= 0.0)) {
                  iVar1 = (local_14 + local_18) * 0x15 + iVar4;
                  *(byte *)(iVar1 * 4 + 0x746959) = *(byte *)(iVar1 * 4 + 0x746959) | 4;
                }
              }
            }
            else {
              iVar1 = (local_18 ^ (int)local_18 >> 0x1f) - ((int)local_18 >> 0x1f);
              iVar2 = ((uint)local_20 ^ (int)local_20 >> 0x1f) - ((int)local_20 >> 0x1f);
              if (iVar1 < iVar2) {
LAB_00444d62:
                if (local_14 < 0) {
                  if (iVar4 < (int)local_20) goto LAB_00444cc2;
                }
                else if ((int)local_20 < iVar4) goto LAB_00444cc2;
              }
              else {
                if ((int)local_18 < 0) {
                  if ((int)local_18 <= iVar7) goto LAB_00444d5e;
                }
                else if (iVar7 <= (int)local_18) {
LAB_00444d5e:
                  if (iVar2 <= iVar1) goto LAB_00444dce;
                  goto LAB_00444d62;
                }
LAB_00444cc2:
                fVar9 = ((float)(int)local_18 + DAT_006da974) * ((float)iVar4 / (float)iVar7);
                fVar8 = ((float)(int)local_18 - DAT_006da974) * ((float)iVar4 / (float)iVar7);
                fVar10 = fVar9;
                if (fVar9 < fVar8) {
                  fVar10 = fVar8;
                  fVar8 = fVar9;
                }
                if ((fVar8 <= (float)(int)local_20 + DAT_006da974) &&
                   ((float)(int)local_20 - DAT_006da974 <= fVar10)) {
                  uVar5 = iVar7 + 10;
                  iVar1 = (local_14 + local_18) * 0x15 + iVar4;
                  uVar3 = uVar5;
                  if ((int)uVar5 < 0) {
                    uVar3 = iVar7 + 0x11;
                  }
                  uVar5 = uVar5 & 0x80000007;
                  if ((int)uVar5 < 0) {
                    uVar5 = (uVar5 - 1 | 0xfffffff8) + 1;
                  }
                  (&DAT_00746958)[iVar1 * 4 + ((int)uVar3 >> 3)] =
                       (&DAT_00746958)[iVar1 * 4 + ((int)uVar3 >> 3)] | (byte)(1 << (uVar5 & 0x1f));
                }
              }
            }
LAB_00444dce:
            iVar7 = iVar7 + 1;
          } while (iVar7 < 0xb);
          iVar4 = iVar4 + 1;
        } while (iVar4 < 0xb);
        local_18 = local_18 + 1;
      } while ((int)local_18 < 0xb);
      local_14 = local_14 + 0x15;
      local_20 = (undefined *)((int)local_20 + 1);
    } while (local_14 < 0xe7);
  }
  DAT_007852fc = 0;
  ExceptionList = local_10;
  return &DAT_007852e0;
}


```

## `0044b76d`

- Function: `FUN_0044aca0`
- Entry: `0044aca0`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_0044aca0(uint *param_1,uint *param_2)

{
  undefined4 *puVar1;
  byte bVar2;
  int *piVar3;
  longlong lVar4;
  short sVar5;
  char cVar6;
  undefined4 uVar7;
  int iVar8;
  void *_Memory;
  undefined4 *puVar9;
  undefined *puVar10;
  short *psVar11;
  undefined4 extraout_ECX;
  undefined4 extraout_ECX_00;
  uint *puVar13;
  uint uVar14;
  float *pfVar15;
  undefined4 extraout_ECX_01;
  int iVar16;
  uint *puVar17;
  float *pfVar18;
  float fVar19;
  float fVar20;
  float fVar21;
  float fVar22;
  float fVar23;
  uint *local_7c;
  uint *local_78;
  char local_71;
  uint *local_70;
  uint *local_6c;
  undefined1 local_68 [56];
  uint local_30;
  uint local_2c;
  void *local_28;
  uint local_24;
  undefined1 *puStack_20;
  void *local_1c;
  undefined1 *puStack_18;
  uint local_14;
  short *psVar12;
  
  puStack_20 = &stack0xfffffffc;
  local_14 = 0xffffffff;
  puStack_18 = &LAB_0065d5ab;
  local_1c = ExceptionList;
  local_24 = DAT_007360c8 ^ (uint)&stack0xfffffff0;
  ExceptionList = &local_1c;
  FUN_00438590(1);
  local_30 = 0;
  local_2c = 0;
  local_28 = (void *)0x0;
  local_14 = 0;
  if ((param_1 == (uint *)0x0) || (param_1 == param_2)) {
LAB_0044bd71:
    puVar9 = (undefined4 *)FUN_0059c260(&local_7c,0x800,2,*(int *)ThreadLocalStoragePointer + 0xc);
    local_6c = (undefined4 *)*puVar9 + 1;
    *(undefined4 *)*puVar9 = 0;
    local_14._0_1_ = 0x13;
    FUN_0044d000(extraout_ECX_01);
    local_7c = param_1;
    uVar14 = (uint)((int)param_2 - (int)param_1) >> 1;
    iVar16 = local_6c[-1];
    iVar8 = iVar16 + uVar14;
    FUN_00434ab0(iVar8,iVar8);
    FUN_0062cfd0((int)local_6c + iVar16 * 2,local_7c,uVar14 * 2);
    psVar11 = (short *)&DAT_006bee50;
    do {
      psVar12 = psVar11;
      psVar11 = psVar12 + 1;
    } while (*psVar11 != 0);
    uVar14 = (int)(psVar12 + -0x35f727) >> 1;
    iVar16 = local_6c[-1];
    iVar8 = iVar16 + (uVar14 & 0x7fffffff);
    FUN_00434ab0(iVar8,iVar8);
    FUN_0062cfd0((int)local_6c + iVar16 * 2,&DAT_006bee50,uVar14 * 2);
    FUN_00434ab0(local_6c[-1],local_6c[-1] + 1);
    *(undefined2 *)((int)local_6c + local_6c[-1] * 2) = 0;
    FUN_004d7ec0();
    local_14 = (uint)local_14._1_3_ << 8;
    if (local_6c != (uint *)&DAT_006b9e28) {
      FUN_0059c360(local_6c + -1);
    }
  }
  else {
    local_70 = (uint *)&DAT_006b78d0;
    uVar7 = FUN_004a4d00(param_1,param_2);
    cVar6 = FUN_0046c600(uVar7);
    if (cVar6 == '\0') goto LAB_0044bd71;
    FUN_004451e0(extraout_ECX);
    if (local_30 + 4 <= local_2c) {
      DAT_007c2498 = *(uint *)(local_30 + (int)local_28);
      local_30 = local_30 + 4;
    }
    if ((((((DAT_007c2498 == 0x20001113) || (DAT_007c2498 == 0x20001114)) ||
          (DAT_007c2498 == 0x20001115)) ||
         ((DAT_007c2498 == 0x20001116 || (DAT_007c2498 == 0x20001117)))) ||
        ((DAT_007c2498 == 0x20001118 ||
         ((DAT_007c2498 == 0x20001119 || (DAT_007c2498 == 0x20001120)))))) ||
       ((DAT_007c2498 == 0x20001121 || (DAT_007c2498 == 0x20001122)))) {
      if (0x20001122 < DAT_007c2498) goto LAB_0044add4;
    }
    else if (DAT_007c2498 == 0x20001123) {
LAB_0044add4:
      if (local_30 + 0x10 <= local_2c) {
        _DAT_007852ec = *(undefined4 *)(local_30 + (int)local_28);
        _DAT_007852f0 = *(undefined4 *)(local_30 + 4 + (int)local_28);
        _DAT_007852f4 = *(undefined4 *)(local_30 + 8 + (int)local_28);
        _DAT_007852f8 = *(undefined4 *)(local_30 + 0xc + (int)local_28);
        local_30 = local_30 + 0x10;
      }
    }
    else {
      DAT_007c2498 = 0;
      local_30 = 0;
      if (local_2c == 0) {
        local_30 = 0xffffffff;
      }
    }
    FUN_0046c6d0(&DAT_006bec44,&DAT_007c24dc);
    FUN_0046c6d0(&DAT_006bec44,&DAT_007c24e0);
    DAT_007b5320 = FUN_00431780("FIELD",extraout_ECX_00);
    iVar8 = FUN_004539c0(&local_30);
    if (iVar8 != 0) {
      DAT_007c2490 = (void *)FUN_0063ea48(DAT_007c24e0 * DAT_007c24dc);
      lVar4 = (ulonglong)(DAT_007c24e0 + 1) * 2;
      DAT_007c2488 = (void *)FUN_0063ea48(-(uint)((int)((ulonglong)lVar4 >> 0x20) != 0) |
                                          (uint)lVar4);
      DAT_007c248c = (void *)FUN_0063ea48(-(uint)((int)((ulonglong)DAT_007c24e0 * 2 >> 0x20) != 0) |
                                          (uint)((ulonglong)DAT_007c24e0 * 2));
      DAT_007c2494 = (void *)FUN_0063ea48(DAT_007c24e0 * DAT_007c24dc);
      lVar4 = (ulonglong)((DAT_007c24e0 + 1) * (DAT_007c24dc + 1)) * 4;
      DAT_007b5328 = FUN_0063ea48(-(uint)((int)((ulonglong)lVar4 >> 0x20) != 0) | (uint)lVar4);
      if (((DAT_007b5320 == 0) || (*(int **)(DAT_007b5320 + 0x48) == (int *)0x0)) ||
         (**(int **)(DAT_007b5320 + 0x48) == 0)) {
        local_6c = (uint *)0x0;
      }
      else {
        local_6c = (uint *)FUN_0046bbc0(0);
      }
      puVar17 = local_6c;
      DAT_007b5324 = FUN_0063ea48(-(uint)((int)(ZEXT48(local_6c) * 4 >> 0x20) != 0) |
                                  (uint)(ZEXT48(local_6c) * 4));
      DAT_007b5408 = FUN_0063ea48(puVar17);
      DAT_007b5404 = FUN_0063ea48(((uint)((int)puVar17 + 0x1f) >> 5) * 4);
      DAT_007b53f0 = FUN_0063ea48(-(uint)((int)(ZEXT48(puVar17) * 4 >> 0x20) != 0) |
                                  (uint)(ZEXT48(puVar17) * 4));
      DAT_007b53f8 = FUN_0063ea48(puVar17);
      DAT_007b53fc = FUN_0063ea48(puVar17);
      DAT_007b53f4 = FUN_0063ea48(puVar17);
      DAT_007b53ec = FUN_0063ea48(-(uint)((int)(ZEXT48(puVar17) * 0xc >> 0x20) != 0) |
                                  (uint)(ZEXT48(puVar17) * 0xc));
      iVar8 = 0;
      iVar16 = **(int **)(DAT_007b5320 + 0x48);
      if ((*(byte *)(iVar16 + 0x10) & 2) == 0) {
        if (*(int *)(iVar16 + 0x14) == 0) {
          iVar8 = 0;
        }
        else {
          iVar8 = *(int *)(*(int *)(iVar16 + 0x14) + 0x10);
        }
      }
      else {
        if (*(int *)(iVar16 + 4) == 0) {
          iVar8 = -1;
        }
        iVar8 = *(int *)(*(int *)(*(int *)(iVar16 + 8) + iVar8 * 4) * 0x94 + 0x10 +
                        *(int *)(iVar16 + 0x14));
      }
      puVar13 = (uint *)0x0;
      if ((uint *)0x3 < puVar17) {
        local_70 = (uint *)((int)puVar17 + -3);
        puVar9 = (undefined4 *)(iVar8 + 0x10);
        do {
          *(undefined4 *)(DAT_007b5324 + (int)puVar13 * 4) = puVar9[-3];
          *(undefined4 *)(DAT_007b5324 + 4 + (int)puVar13 * 4) = *puVar9;
          *(undefined4 *)(DAT_007b5324 + 8 + (int)puVar13 * 4) = puVar9[3];
          puVar1 = puVar9 + 6;
          puVar9 = puVar9 + 0xc;
          *(undefined4 *)(DAT_007b5324 + 0xc + (int)puVar13 * 4) = *puVar1;
          puVar13 = puVar13 + 1;
          puVar17 = local_6c;
        } while (puVar13 < local_70);
      }
      if (puVar13 < puVar17) {
        puVar9 = (undefined4 *)(iVar8 + ((int)puVar13 * 3 + 1) * 4);
        do {
          uVar7 = *puVar9;
          puVar9 = puVar9 + 3;
          *(undefined4 *)(DAT_007b5324 + (int)puVar13 * 4) = uVar7;
          puVar13 = (uint *)((int)puVar13 + 1);
        } while (puVar13 < puVar17);
      }
      _memset(DAT_007c2488,0xff,DAT_007c24e0 * 2 + 2);
      _memset(DAT_007c248c,0xff,DAT_007c24e0 * 2);
      _memset(DAT_007c2490,0,DAT_007c24e0 * DAT_007c24dc);
      _memset(DAT_007c2494,0,DAT_007c24e0 * DAT_007c24dc);
      puVar13 = (uint *)(DAT_007c24e0 * DAT_007c24dc);
      uVar14 = -(uint)((int)(ZEXT48(puVar13) * 0x10 >> 0x20) != 0) | (uint)(ZEXT48(puVar13) * 0x10);
      local_7c = puVar13;
      local_70 = puVar13;
      local_78 = (uint *)FUN_0063ea48(-(uint)(0xfffffffb < uVar14) | uVar14 + 4);
      local_14._0_1_ = 0x26;
      if (local_78 == (uint *)0x0) {
        puVar13 = (uint *)0x0;
      }
      else {
        *local_78 = (uint)puVar13;
        puVar13 = local_78 + 1;
        _eh_vector_constructor_iterator_
                  (puVar13,0x10,(uint)local_70,(_func_void_void_ptr *)&LAB_0044cc30,FUN_0044cc50);
      }
      local_14 = (uint)local_14._1_3_ << 8;
      DAT_007b5410 = 0;
      DAT_007b540c = puVar13;
      if (DAT_007c2498 < 0x20001120) {
        iVar8 = 0;
        puVar17 = local_6c;
        if (0 < (int)(DAT_007c24e0 * DAT_007c24dc)) {
          iVar16 = 0;
          do {
            *(undefined1 *)(iVar16 + (int)DAT_007b540c) = 6;
            sVar5 = (short)iVar8;
            iVar8 = iVar8 + 1;
            *(undefined1 *)(iVar16 + 1 + (int)DAT_007b540c) = 4;
            *(short *)(iVar16 + 2 + (int)DAT_007b540c) = sVar5 * 4;
            *(undefined4 *)(iVar16 + 4 + (int)DAT_007b540c) = 0;
            *(undefined4 *)(iVar16 + 8 + (int)DAT_007b540c) = 0;
            DAT_007b5410 = DAT_007b5410 + (uint)*(byte *)(iVar16 + 1 + (int)DAT_007b540c);
            iVar16 = iVar16 + 0x10;
          } while (iVar8 < (int)(DAT_007c24e0 * DAT_007c24dc));
        }
      }
      else {
        local_70 = (uint *)0x0;
        if (0 < (int)(DAT_007c24e0 * DAT_007c24dc)) {
          iVar8 = 0;
          do {
            puVar17 = DAT_007b540c;
            if (local_30 + 1 <= local_2c) {
              *(undefined1 *)(iVar8 + (int)DAT_007b540c) = *(undefined1 *)(local_30 + (int)local_28)
              ;
              local_30 = local_30 + 1;
            }
            if (local_30 + 2 <= local_2c) {
              *(undefined2 *)(iVar8 + 2 + (int)puVar17) = *(undefined2 *)(local_30 + (int)local_28);
              local_30 = local_30 + 2;
            }
            if (local_30 + 1 <= local_2c) {
              *(undefined1 *)(iVar8 + 0xc + (int)puVar17) =
                   *(undefined1 *)(local_30 + (int)local_28);
              local_30 = local_30 + 1;
            }
            if (local_30 + 1 <= local_2c) {
              *(undefined1 *)(iVar8 + 1 + (int)puVar17) = *(undefined1 *)(local_30 + (int)local_28);
              local_30 = local_30 + 1;
            }
            FID_conflict__free(*(void **)(iVar8 + 4 + (int)puVar17));
            local_70 = (uint *)((int)local_70 + 1);
            *(undefined4 *)(iVar8 + 4 + (int)puVar17) = 0;
            iVar16 = iVar8 + 1;
            iVar8 = iVar8 + 0x10;
            DAT_007b5410 = DAT_007b5410 + (uint)*(byte *)(iVar16 + (int)DAT_007b540c);
            puVar17 = local_6c;
          } while ((int)local_70 < (int)(DAT_007c24e0 * DAT_007c24dc));
        }
      }
      if (DAT_007c2498 < 0x20001122) {
        FUN_0044cd00(1,DAT_007c24e0 * DAT_007c24dc);
        uVar7 = 0;
        if ((_DAT_007b532c & 1) != 0) {
          uVar7 = DAT_007b5334;
        }
        iVar8 = DAT_007b5410 * 8;
        if ((iVar8 != 0) && (iVar8 + local_30 <= local_2c)) {
          FUN_0062cfd0(uVar7,(int)local_28 + local_30,iVar8);
          local_30 = local_30 + iVar8;
        }
      }
      else {
        FUN_0044ce40(&local_30);
      }
      iVar8 = (int)puVar17 * 4;
      if ((iVar8 != 0) && (iVar8 + local_30 <= local_2c)) {
        FUN_0062cfd0(DAT_007b53f0,(int)local_28 + local_30,iVar8);
        local_30 = local_30 + iVar8;
      }
      local_6c = (uint *)0x1;
      local_70 = (uint *)0x0;
      do {
        puVar17 = local_6c;
        if ((_DAT_007b532c & (uint)local_6c) != 0) {
          iVar8 = *(int *)((int)&DAT_007b5334 + (int)local_70);
          local_7c = (uint *)(DAT_007c24e0 * DAT_007c24dc * 4);
          local_78 = (uint *)FUN_0063ea48(-(uint)((int)(ZEXT48(local_7c) * 8 >> 0x20) != 0) |
                                          (uint)(ZEXT48(local_7c) * 8));
          local_14 = local_14 & 0xffffff00;
          FUN_0062cfd0(local_78,iVar8,DAT_007c24e0 * DAT_007c24dc * 0x20);
          iVar16 = 0;
          if (0 < (int)(DAT_007c24e0 * DAT_007c24dc)) {
            pfVar18 = (float *)(iVar8 + 0x1c);
            pfVar15 = (float *)(iVar8 + 8);
            do {
              uVar14 = DAT_006db4a0;
              fVar23 = (pfVar18[-7] + pfVar18[-1]) * DAT_006da974;
              fVar21 = (float)((uint)(pfVar18[-1] - pfVar18[-7]) & DAT_006db490) * _DAT_006da8c4;
              fVar22 = (pfVar18[-6] + *pfVar18) * DAT_006da974;
              fVar20 = (float)((uint)(*pfVar18 - pfVar18[-6]) & DAT_006db490) * _DAT_006da8c4;
              fVar19 = fVar21;
              if (fVar23 <= pfVar15[-2]) {
                fVar19 = (float)((uint)fVar21 ^ DAT_006db4a0);
              }
              pfVar15[-2] = pfVar15[-2] + fVar19;
              fVar19 = fVar20;
              if (fVar22 <= pfVar15[-1]) {
                fVar19 = (float)((uint)fVar20 ^ uVar14);
              }
              pfVar15[-1] = pfVar15[-1] + fVar19;
              fVar19 = fVar21;
              if (fVar23 <= *pfVar15) {
                fVar19 = (float)((uint)fVar21 ^ uVar14);
              }
              *pfVar15 = *pfVar15 + fVar19;
              fVar19 = fVar20;
              if (fVar22 <= pfVar15[1]) {
                fVar19 = (float)((uint)fVar20 ^ uVar14);
              }
              pfVar15[1] = pfVar15[1] + fVar19;
              fVar19 = fVar21;
              if (fVar23 <= pfVar15[2]) {
                fVar19 = (float)((uint)fVar21 ^ uVar14);
              }
              pfVar15[2] = pfVar15[2] + fVar19;
              fVar19 = fVar20;
              if (fVar22 <= pfVar15[3]) {
                fVar19 = (float)((uint)fVar20 ^ uVar14);
              }
              pfVar15[3] = pfVar15[3] + fVar19;
              if (fVar23 <= pfVar15[4]) {
                fVar21 = (float)((uint)fVar21 ^ uVar14);
              }
              pfVar15[4] = pfVar15[4] + fVar21;
              if (fVar22 <= pfVar15[5]) {
                fVar20 = (float)((uint)fVar20 ^ uVar14);
              }
              iVar16 = iVar16 + 1;
              pfVar18 = pfVar18 + 8;
              pfVar15[5] = pfVar15[5] + fVar20;
              pfVar15 = pfVar15 + 8;
              puVar17 = local_6c;
            } while (iVar16 < (int)(DAT_007c24e0 * DAT_007c24dc));
          }
          FID_conflict__free(local_78);
        }
        local_70 = local_70 + 1;
        local_6c = (uint *)((int)puVar17 << 1 | (uint)((int)puVar17 < 0));
      } while (local_70 < (uint *)0x10);
      if (DAT_007c2498 == 0) {
        uVar14 = 0;
        DAT_007b5398 = 10;
        do {
          uVar7 = FUN_0042a47f();
          (&DAT_007b5370)[uVar14] = uVar7;
          FUN_00460c80(&local_30);
          lVar4 = ((longlong)(int)DAT_007c24e0 * (longlong)DAT_007c24dc & 0xffffffffU) * 4;
          uVar7 = FUN_0063ea48(-(uint)((int)((ulonglong)lVar4 >> 0x20) != 0) | (uint)lVar4);
          (&DAT_007b539c)[uVar14] = uVar7;
          uVar14 = uVar14 + 1;
        } while (uVar14 < DAT_007b5398);
      }
      if (0x20001112 < DAT_007c2498) {
        if (local_30 + 4 <= local_2c) {
          DAT_007b5398 = *(uint *)(local_30 + (int)local_28);
          local_30 = local_30 + 4;
        }
        if (DAT_007c2498 < 0x20001122) {
          _Memory = (void *)FUN_0063ea48(DAT_007c24e0 * DAT_007c24dc);
          iVar8 = DAT_007c24e0 * DAT_007c24dc;
          if ((iVar8 != 0) && (local_30 + iVar8 <= local_2c)) {
            FUN_0062cfd0(_Memory,(int)local_28 + local_30,iVar8);
            local_30 = local_30 + iVar8;
          }
          iVar8 = 0;
          if (0 < (int)(DAT_007c24e0 * DAT_007c24dc)) {
            do {
              bVar2 = *(byte *)(iVar8 + (int)_Memory);
              *(undefined1 *)(DAT_007b5344 + iVar8 * 4) = 0;
              puVar17 = (uint *)(DAT_007b5344 + iVar8 * 4);
              *puVar17 = *puVar17 | (uint)bVar2;
              iVar8 = iVar8 + 1;
            } while (iVar8 < (int)(DAT_007c24e0 * DAT_007c24dc));
          }
          FID_conflict__free(_Memory);
          DAT_007b5348 = 0;
          DAT_007b534c = 0;
          _DAT_007b5350 = 0;
          _DAT_007b5354 = 0;
          _DAT_007b5358 = 0;
          _DAT_007b535c = 0;
          _DAT_007b5360 = 0;
          _DAT_007b5364 = 0;
          _DAT_007b5368 = 0;
          _DAT_007b536c = 0;
        }
        else {
          iVar8 = DAT_007b5398 * 4;
          if ((iVar8 != 0) && (uVar14 = iVar8 + local_30, uVar14 <= local_2c)) {
            FUN_0062cfd0(&DAT_007b5348,(int)local_28 + local_30,iVar8);
            local_30 = uVar14;
          }
        }
        uVar14 = 0;
        if (DAT_007b5398 != 0) {
          do {
            uVar7 = FUN_0042a47f();
            (&DAT_007b5370)[uVar14] = uVar7;
            FUN_00460c80(&local_30);
            lVar4 = ((longlong)(int)DAT_007c24e0 * (longlong)DAT_007c24dc & 0xffffffffU) * 4;
            uVar7 = FUN_0063ea48(-(uint)((int)((ulonglong)lVar4 >> 0x20) != 0) | (uint)lVar4);
            (&DAT_007b539c)[uVar14] = uVar7;
            uVar14 = uVar14 + 1;
          } while (uVar14 < DAT_007b5398);
        }
      }
      DAT_007852e8 = 0;
      DAT_007852e0 = (uint *)0x0;
      if (DAT_007852e4 != (uint *)0x0) {
        puVar17 = DAT_007852e4 + -1;
        _eh_vector_destructor_iterator_(DAT_007852e4,0x68,DAT_007852e4[-1],FUN_0044d690);
        FUN_0062a696(puVar17,*puVar17 * 0x68 + 4);
      }
      DAT_007852e4 = (uint *)0x0;
      if (0x20001113 < DAT_007c2498) {
        if (local_30 + 4 <= local_2c) {
          DAT_007852e0 = *(uint **)(local_30 + (int)local_28);
          local_30 = local_30 + 4;
        }
        puVar17 = DAT_007852e0;
        if (DAT_007852e0 != (uint *)0x0) {
          uVar14 = -(uint)((int)(ZEXT48(DAT_007852e0) * 0x68 >> 0x20) != 0) |
                   (uint)(ZEXT48(DAT_007852e0) * 0x68);
          local_7c = DAT_007852e0;
          local_78 = (uint *)FUN_0063ea48(-(uint)(0xfffffffb < uVar14) | uVar14 + 4);
          local_14._0_1_ = 0x4a;
          if (local_78 == (uint *)0x0) {
            puVar13 = (uint *)0x0;
          }
          else {
            puVar13 = local_78 + 1;
            *local_78 = (uint)puVar17;
            _eh_vector_constructor_iterator_(puVar13,0x68,(uint)puVar17,FUN_0044d5b0,FUN_0044d690);
          }
          local_14 = (uint)local_14._1_3_ << 8;
          local_70 = (uint *)0x0;
          DAT_007852e4 = puVar13;
          if (DAT_007852e0 != (uint *)0x0) {
            iVar8 = 0;
            do {
              iVar16 = FUN_0044d830(&local_30,DAT_007c2498);
              if (iVar16 == 0) {
                DAT_007852e0 = (uint *)((int)DAT_007852e0 + -1);
              }
              if (*(int *)((int)DAT_007852e4 + iVar8 + 4) == 1) {
                DAT_007852e8 = 1;
              }
              iVar8 = iVar8 + 0x68;
              local_70 = (uint *)((int)local_70 + 1);
            } while (local_70 < DAT_007852e0);
          }
        }
      }
      DAT_007c24a0 = (uint *)0x0;
      if (0x20001114 < DAT_007c2498) {
        if (local_30 + 4 <= local_2c) {
          DAT_007c24a0 = *(uint **)(local_30 + (int)local_28);
          local_30 = local_30 + 4;
        }
        local_6c = (uint *)0x0;
        local_70 = (uint *)0x0;
        if (DAT_007c24a0 != (uint *)0x0) {
          do {
            puVar17 = local_6c;
            local_7c = (uint *)FUN_00640b15(0x150,0x10);
            local_14._0_1_ = 0x4b;
            if (local_7c == (uint *)0x0) {
              puVar13 = (uint *)0x0;
            }
            else {
              local_78 = local_7c;
              puVar13 = (uint *)FUN_0044d060();
            }
            local_14 = (uint)local_14._1_3_ << 8;
            local_78 = puVar13;
            iVar16 = FUN_0044d430(&local_30);
            iVar8 = DAT_007c24a4;
            if (iVar16 == 0) {
              local_6c = (uint *)((int)puVar17 + 1);
              if (puVar13 != (uint *)0x0) {
                puVar9 = (undefined4 *)puVar13[0xc];
                if (puVar9 != (undefined4 *)0x0) {
                  (**(code **)*puVar9)(0);
                  thunk_FUN_00640afb(puVar9);
                }
                puVar13[0xc] = 0;
                thunk_FUN_00640afb(puVar13);
              }
            }
            else {
              local_78 = (uint *)FUN_00434330(DAT_007c24a4,*(undefined4 *)(DAT_007c24a4 + 4),
                                              &local_78);
              if (DAT_007c24a8 == 0x15555554) {
                    /* WARNING: Subroutine does not return */
                FUN_00627726("list<T> too long");
              }
              DAT_007c24a8 = DAT_007c24a8 + 1;
              *(uint **)(iVar8 + 4) = local_78;
              *(uint **)local_78[1] = local_78;
              iVar8 = *(int *)(puVar13[0xc] + 0x94);
              puVar17 = (uint *)(iVar8 + 0x40);
              *puVar17 = *puVar17 & 0xfffeffff;
              for (iVar8 = *(int *)(iVar8 + 0x5c); iVar8 != 0; iVar8 = *(int *)(iVar8 + 100)) {
                if (*(int *)(iVar8 + 0x44) == -1) {
                  iVar8 = FUN_00456b40(0,1);
                }
              }
            }
            local_70 = (uint *)((int)local_70 + 1);
          } while (local_70 < DAT_007c24a0);
        }
        DAT_007c24a0 = (uint *)((int)DAT_007c24a0 - (int)local_6c);
      }
      if (DAT_007c2498 < 0x20001119) {
LAB_0044ba31:
        FUN_00445610();
      }
      else {
        iVar8 = (DAT_007c24e0 + 1) * (DAT_007c24dc + 1) * 4;
        if ((iVar8 != 0) && (local_30 + iVar8 <= local_2c)) {
          FUN_0062cfd0(DAT_007b5328,(int)local_28 + local_30,iVar8);
          local_30 = local_30 + iVar8;
        }
        if (DAT_007c2498 < 0x20001119) goto LAB_0044ba31;
      }
      puVar17 = DAT_007850d8;
      local_7c = DAT_007850d8;
      if (DAT_007c24cc != (int *)0x0) {
        (**(code **)(*DAT_007c24cc + 8))(DAT_007c24cc);
        DAT_007c24cc = (int *)0x0;
      }
      iVar8 = DAT_007c24d8;
      if (DAT_007c24d8 != 0) {
        FUN_00428380();
        FUN_0062a696(iVar8,0x38);
      }
      DAT_007c24d8 = 0;
      if ((DAT_007850d4 != '\0') && (puVar17 != (uint *)0x0)) {
        DAT_00764330 = DAT_0073ae68;
        if (puVar17[0x110] != 0) {
          FUN_0042f4a0(puVar17[0x110],puVar17[0x108],0,0,*puVar17,puVar17[1]);
        }
        for (puVar17 = param_1;
            puVar17 != (uint *)((int)param_1 + ((int)param_2 - (int)param_1 & 0xfffffffeU));
            puVar17 = (uint *)((int)puVar17 + 2)) {
          if ((short)*puVar17 == 0x2e) goto LAB_0044badf;
        }
        puVar17 = (uint *)0x0;
LAB_0044badf:
        if (puVar17 != (uint *)0x0) {
          _memset(local_68,0,0x38);
          FUN_00427ab0();
          local_14._0_1_ = 0x4c;
          puVar9 = (undefined4 *)
                   FUN_0059c260(&local_78,0x800,2,*(int *)ThreadLocalStoragePointer + 0xc);
          piVar3 = (int *)*puVar9;
          local_6c = (uint *)(piVar3 + 1);
          *piVar3 = 0;
          local_14._0_1_ = 0x5f;
          local_70 = (uint *)((uint)((int)puVar17 - (int)param_1) >> 1);
          iVar8 = *piVar3;
          puVar10 = (undefined *)((int)local_70 + iVar8);
          FUN_00434ab0(puVar10,puVar10);
          FUN_0062cfd0((int)local_6c + iVar8 * 2,param_1,(int)local_70 * 2);
          psVar11 = (short *)&DAT_006bee60;
          do {
            psVar12 = psVar11;
            psVar11 = psVar12 + 1;
          } while (*psVar11 != 0);
          uVar14 = (int)(psVar12 + -0x35f72f) >> 1;
          iVar16 = local_6c[-1];
          iVar8 = iVar16 + (uVar14 & 0x7fffffff);
          FUN_00434ab0(iVar8,iVar8);
          FUN_0062cfd0((int)local_6c + iVar16 * 2,&DAT_006bee60,uVar14 * 2);
          puVar17 = local_6c;
          iVar8 = (int)local_6c + local_6c[-1] * 2;
          FUN_00428380();
          local_78 = (uint *)&DAT_006b78d0;
          uVar7 = FUN_004a4d00(puVar17,iVar8);
          local_71 = FUN_00427bc0(uVar7,0);
          local_14._0_1_ = 0x4c;
          if (local_6c != (uint *)&DAT_006b9e28) {
            FUN_0059c360(local_6c + -1);
          }
          if (local_71 != '\0') {
            local_78 = (uint *)FUN_0063ea48(0x38);
            local_14._0_1_ = 0x72;
            if (local_78 == (uint *)0x0) {
              DAT_007c24d8 = 0;
            }
            else {
              _memset(local_78,0,0x38);
              DAT_007c24d8 = FUN_00427ab0();
            }
            puVar17 = local_7c;
            local_14._0_1_ = 0x4c;
            FUN_00427f70(local_68,*local_7c,local_7c[1]);
            DAT_007c24d0 = *(undefined4 *)(DAT_007c24d8 + 0x1c);
            DAT_007c24d4 = *(undefined4 *)(DAT_007c24d8 + 0x20);
            FUN_0042f710(DAT_007c24d0,DAT_007c24d4,&DAT_007c24cc,DAT_007c24d8,
                         (&DAT_006b9e54)[puVar17[0x108] * 0x16],DAT_007c24d4);
            _DAT_007c24c4 = 0;
            _DAT_007c24c8 = 0;
            DAT_007c24bc = DAT_006daa00 / (float)DAT_007c24dc;
            DAT_007c24c0 = DAT_006daa00 / (float)(int)DAT_007c24e0;
            FUN_0042f370(puVar17[0x110],DAT_007c24cc);
          }
          iVar8 = DAT_007c24d8;
          if (DAT_007c24d8 != 0) {
            FUN_00428380();
            FUN_0062a696(iVar8,0x38);
          }
          DAT_007c24d8 = 0;
          local_14 = (uint)local_14._1_3_ << 8;
          FUN_00428380();
        }
      }
      FUN_004487e0();
      FUN_00444f80();
      DAT_007b5e94 = 0;
      DAT_007852e9 = 1;
      local_71 = 1;
      goto LAB_0044be82;
    }
  }
  local_71 = 0;
LAB_0044be82:
  local_14 = 0xffffffff;
  if (local_28 != (void *)0x0) {
    FID_conflict__free(local_28);
    local_28 = (void *)0x0;
  }
  ExceptionList = local_1c;
  __security_check_cookie(local_24 ^ (uint)&stack0xfffffff0);
  return;
}


```

## `0044b881`

- Function: `FUN_0044aca0`
- Entry: `0044aca0`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_0044aca0(uint *param_1,uint *param_2)

{
  undefined4 *puVar1;
  byte bVar2;
  int *piVar3;
  longlong lVar4;
  short sVar5;
  char cVar6;
  undefined4 uVar7;
  int iVar8;
  void *_Memory;
  undefined4 *puVar9;
  undefined *puVar10;
  short *psVar11;
  undefined4 extraout_ECX;
  undefined4 extraout_ECX_00;
  uint *puVar13;
  uint uVar14;
  float *pfVar15;
  undefined4 extraout_ECX_01;
  int iVar16;
  uint *puVar17;
  float *pfVar18;
  float fVar19;
  float fVar20;
  float fVar21;
  float fVar22;
  float fVar23;
  uint *local_7c;
  uint *local_78;
  char local_71;
  uint *local_70;
  uint *local_6c;
  undefined1 local_68 [56];
  uint local_30;
  uint local_2c;
  void *local_28;
  uint local_24;
  undefined1 *puStack_20;
  void *local_1c;
  undefined1 *puStack_18;
  uint local_14;
  short *psVar12;
  
  puStack_20 = &stack0xfffffffc;
  local_14 = 0xffffffff;
  puStack_18 = &LAB_0065d5ab;
  local_1c = ExceptionList;
  local_24 = DAT_007360c8 ^ (uint)&stack0xfffffff0;
  ExceptionList = &local_1c;
  FUN_00438590(1);
  local_30 = 0;
  local_2c = 0;
  local_28 = (void *)0x0;
  local_14 = 0;
  if ((param_1 == (uint *)0x0) || (param_1 == param_2)) {
LAB_0044bd71:
    puVar9 = (undefined4 *)FUN_0059c260(&local_7c,0x800,2,*(int *)ThreadLocalStoragePointer + 0xc);
    local_6c = (undefined4 *)*puVar9 + 1;
    *(undefined4 *)*puVar9 = 0;
    local_14._0_1_ = 0x13;
    FUN_0044d000(extraout_ECX_01);
    local_7c = param_1;
    uVar14 = (uint)((int)param_2 - (int)param_1) >> 1;
    iVar16 = local_6c[-1];
    iVar8 = iVar16 + uVar14;
    FUN_00434ab0(iVar8,iVar8);
    FUN_0062cfd0((int)local_6c + iVar16 * 2,local_7c,uVar14 * 2);
    psVar11 = (short *)&DAT_006bee50;
    do {
      psVar12 = psVar11;
      psVar11 = psVar12 + 1;
    } while (*psVar11 != 0);
    uVar14 = (int)(psVar12 + -0x35f727) >> 1;
    iVar16 = local_6c[-1];
    iVar8 = iVar16 + (uVar14 & 0x7fffffff);
    FUN_00434ab0(iVar8,iVar8);
    FUN_0062cfd0((int)local_6c + iVar16 * 2,&DAT_006bee50,uVar14 * 2);
    FUN_00434ab0(local_6c[-1],local_6c[-1] + 1);
    *(undefined2 *)((int)local_6c + local_6c[-1] * 2) = 0;
    FUN_004d7ec0();
    local_14 = (uint)local_14._1_3_ << 8;
    if (local_6c != (uint *)&DAT_006b9e28) {
      FUN_0059c360(local_6c + -1);
    }
  }
  else {
    local_70 = (uint *)&DAT_006b78d0;
    uVar7 = FUN_004a4d00(param_1,param_2);
    cVar6 = FUN_0046c600(uVar7);
    if (cVar6 == '\0') goto LAB_0044bd71;
    FUN_004451e0(extraout_ECX);
    if (local_30 + 4 <= local_2c) {
      DAT_007c2498 = *(uint *)(local_30 + (int)local_28);
      local_30 = local_30 + 4;
    }
    if ((((((DAT_007c2498 == 0x20001113) || (DAT_007c2498 == 0x20001114)) ||
          (DAT_007c2498 == 0x20001115)) ||
         ((DAT_007c2498 == 0x20001116 || (DAT_007c2498 == 0x20001117)))) ||
        ((DAT_007c2498 == 0x20001118 ||
         ((DAT_007c2498 == 0x20001119 || (DAT_007c2498 == 0x20001120)))))) ||
       ((DAT_007c2498 == 0x20001121 || (DAT_007c2498 == 0x20001122)))) {
      if (0x20001122 < DAT_007c2498) goto LAB_0044add4;
    }
    else if (DAT_007c2498 == 0x20001123) {
LAB_0044add4:
      if (local_30 + 0x10 <= local_2c) {
        _DAT_007852ec = *(undefined4 *)(local_30 + (int)local_28);
        _DAT_007852f0 = *(undefined4 *)(local_30 + 4 + (int)local_28);
        _DAT_007852f4 = *(undefined4 *)(local_30 + 8 + (int)local_28);
        _DAT_007852f8 = *(undefined4 *)(local_30 + 0xc + (int)local_28);
        local_30 = local_30 + 0x10;
      }
    }
    else {
      DAT_007c2498 = 0;
      local_30 = 0;
      if (local_2c == 0) {
        local_30 = 0xffffffff;
      }
    }
    FUN_0046c6d0(&DAT_006bec44,&DAT_007c24dc);
    FUN_0046c6d0(&DAT_006bec44,&DAT_007c24e0);
    DAT_007b5320 = FUN_00431780("FIELD",extraout_ECX_00);
    iVar8 = FUN_004539c0(&local_30);
    if (iVar8 != 0) {
      DAT_007c2490 = (void *)FUN_0063ea48(DAT_007c24e0 * DAT_007c24dc);
      lVar4 = (ulonglong)(DAT_007c24e0 + 1) * 2;
      DAT_007c2488 = (void *)FUN_0063ea48(-(uint)((int)((ulonglong)lVar4 >> 0x20) != 0) |
                                          (uint)lVar4);
      DAT_007c248c = (void *)FUN_0063ea48(-(uint)((int)((ulonglong)DAT_007c24e0 * 2 >> 0x20) != 0) |
                                          (uint)((ulonglong)DAT_007c24e0 * 2));
      DAT_007c2494 = (void *)FUN_0063ea48(DAT_007c24e0 * DAT_007c24dc);
      lVar4 = (ulonglong)((DAT_007c24e0 + 1) * (DAT_007c24dc + 1)) * 4;
      DAT_007b5328 = FUN_0063ea48(-(uint)((int)((ulonglong)lVar4 >> 0x20) != 0) | (uint)lVar4);
      if (((DAT_007b5320 == 0) || (*(int **)(DAT_007b5320 + 0x48) == (int *)0x0)) ||
         (**(int **)(DAT_007b5320 + 0x48) == 0)) {
        local_6c = (uint *)0x0;
      }
      else {
        local_6c = (uint *)FUN_0046bbc0(0);
      }
      puVar17 = local_6c;
      DAT_007b5324 = FUN_0063ea48(-(uint)((int)(ZEXT48(local_6c) * 4 >> 0x20) != 0) |
                                  (uint)(ZEXT48(local_6c) * 4));
      DAT_007b5408 = FUN_0063ea48(puVar17);
      DAT_007b5404 = FUN_0063ea48(((uint)((int)puVar17 + 0x1f) >> 5) * 4);
      DAT_007b53f0 = FUN_0063ea48(-(uint)((int)(ZEXT48(puVar17) * 4 >> 0x20) != 0) |
                                  (uint)(ZEXT48(puVar17) * 4));
      DAT_007b53f8 = FUN_0063ea48(puVar17);
      DAT_007b53fc = FUN_0063ea48(puVar17);
      DAT_007b53f4 = FUN_0063ea48(puVar17);
      DAT_007b53ec = FUN_0063ea48(-(uint)((int)(ZEXT48(puVar17) * 0xc >> 0x20) != 0) |
                                  (uint)(ZEXT48(puVar17) * 0xc));
      iVar8 = 0;
      iVar16 = **(int **)(DAT_007b5320 + 0x48);
      if ((*(byte *)(iVar16 + 0x10) & 2) == 0) {
        if (*(int *)(iVar16 + 0x14) == 0) {
          iVar8 = 0;
        }
        else {
          iVar8 = *(int *)(*(int *)(iVar16 + 0x14) + 0x10);
        }
      }
      else {
        if (*(int *)(iVar16 + 4) == 0) {
          iVar8 = -1;
        }
        iVar8 = *(int *)(*(int *)(*(int *)(iVar16 + 8) + iVar8 * 4) * 0x94 + 0x10 +
                        *(int *)(iVar16 + 0x14));
      }
      puVar13 = (uint *)0x0;
      if ((uint *)0x3 < puVar17) {
        local_70 = (uint *)((int)puVar17 + -3);
        puVar9 = (undefined4 *)(iVar8 + 0x10);
        do {
          *(undefined4 *)(DAT_007b5324 + (int)puVar13 * 4) = puVar9[-3];
          *(undefined4 *)(DAT_007b5324 + 4 + (int)puVar13 * 4) = *puVar9;
          *(undefined4 *)(DAT_007b5324 + 8 + (int)puVar13 * 4) = puVar9[3];
          puVar1 = puVar9 + 6;
          puVar9 = puVar9 + 0xc;
          *(undefined4 *)(DAT_007b5324 + 0xc + (int)puVar13 * 4) = *puVar1;
          puVar13 = puVar13 + 1;
          puVar17 = local_6c;
        } while (puVar13 < local_70);
      }
      if (puVar13 < puVar17) {
        puVar9 = (undefined4 *)(iVar8 + ((int)puVar13 * 3 + 1) * 4);
        do {
          uVar7 = *puVar9;
          puVar9 = puVar9 + 3;
          *(undefined4 *)(DAT_007b5324 + (int)puVar13 * 4) = uVar7;
          puVar13 = (uint *)((int)puVar13 + 1);
        } while (puVar13 < puVar17);
      }
      _memset(DAT_007c2488,0xff,DAT_007c24e0 * 2 + 2);
      _memset(DAT_007c248c,0xff,DAT_007c24e0 * 2);
      _memset(DAT_007c2490,0,DAT_007c24e0 * DAT_007c24dc);
      _memset(DAT_007c2494,0,DAT_007c24e0 * DAT_007c24dc);
      puVar13 = (uint *)(DAT_007c24e0 * DAT_007c24dc);
      uVar14 = -(uint)((int)(ZEXT48(puVar13) * 0x10 >> 0x20) != 0) | (uint)(ZEXT48(puVar13) * 0x10);
      local_7c = puVar13;
      local_70 = puVar13;
      local_78 = (uint *)FUN_0063ea48(-(uint)(0xfffffffb < uVar14) | uVar14 + 4);
      local_14._0_1_ = 0x26;
      if (local_78 == (uint *)0x0) {
        puVar13 = (uint *)0x0;
      }
      else {
        *local_78 = (uint)puVar13;
        puVar13 = local_78 + 1;
        _eh_vector_constructor_iterator_
                  (puVar13,0x10,(uint)local_70,(_func_void_void_ptr *)&LAB_0044cc30,FUN_0044cc50);
      }
      local_14 = (uint)local_14._1_3_ << 8;
      DAT_007b5410 = 0;
      DAT_007b540c = puVar13;
      if (DAT_007c2498 < 0x20001120) {
        iVar8 = 0;
        puVar17 = local_6c;
        if (0 < (int)(DAT_007c24e0 * DAT_007c24dc)) {
          iVar16 = 0;
          do {
            *(undefined1 *)(iVar16 + (int)DAT_007b540c) = 6;
            sVar5 = (short)iVar8;
            iVar8 = iVar8 + 1;
            *(undefined1 *)(iVar16 + 1 + (int)DAT_007b540c) = 4;
            *(short *)(iVar16 + 2 + (int)DAT_007b540c) = sVar5 * 4;
            *(undefined4 *)(iVar16 + 4 + (int)DAT_007b540c) = 0;
            *(undefined4 *)(iVar16 + 8 + (int)DAT_007b540c) = 0;
            DAT_007b5410 = DAT_007b5410 + (uint)*(byte *)(iVar16 + 1 + (int)DAT_007b540c);
            iVar16 = iVar16 + 0x10;
          } while (iVar8 < (int)(DAT_007c24e0 * DAT_007c24dc));
        }
      }
      else {
        local_70 = (uint *)0x0;
        if (0 < (int)(DAT_007c24e0 * DAT_007c24dc)) {
          iVar8 = 0;
          do {
            puVar17 = DAT_007b540c;
            if (local_30 + 1 <= local_2c) {
              *(undefined1 *)(iVar8 + (int)DAT_007b540c) = *(undefined1 *)(local_30 + (int)local_28)
              ;
              local_30 = local_30 + 1;
            }
            if (local_30 + 2 <= local_2c) {
              *(undefined2 *)(iVar8 + 2 + (int)puVar17) = *(undefined2 *)(local_30 + (int)local_28);
              local_30 = local_30 + 2;
            }
            if (local_30 + 1 <= local_2c) {
              *(undefined1 *)(iVar8 + 0xc + (int)puVar17) =
                   *(undefined1 *)(local_30 + (int)local_28);
              local_30 = local_30 + 1;
            }
            if (local_30 + 1 <= local_2c) {
              *(undefined1 *)(iVar8 + 1 + (int)puVar17) = *(undefined1 *)(local_30 + (int)local_28);
              local_30 = local_30 + 1;
            }
            FID_conflict__free(*(void **)(iVar8 + 4 + (int)puVar17));
            local_70 = (uint *)((int)local_70 + 1);
            *(undefined4 *)(iVar8 + 4 + (int)puVar17) = 0;
            iVar16 = iVar8 + 1;
            iVar8 = iVar8 + 0x10;
            DAT_007b5410 = DAT_007b5410 + (uint)*(byte *)(iVar16 + (int)DAT_007b540c);
            puVar17 = local_6c;
          } while ((int)local_70 < (int)(DAT_007c24e0 * DAT_007c24dc));
        }
      }
      if (DAT_007c2498 < 0x20001122) {
        FUN_0044cd00(1,DAT_007c24e0 * DAT_007c24dc);
        uVar7 = 0;
        if ((_DAT_007b532c & 1) != 0) {
          uVar7 = DAT_007b5334;
        }
        iVar8 = DAT_007b5410 * 8;
        if ((iVar8 != 0) && (iVar8 + local_30 <= local_2c)) {
          FUN_0062cfd0(uVar7,(int)local_28 + local_30,iVar8);
          local_30 = local_30 + iVar8;
        }
      }
      else {
        FUN_0044ce40(&local_30);
      }
      iVar8 = (int)puVar17 * 4;
      if ((iVar8 != 0) && (iVar8 + local_30 <= local_2c)) {
        FUN_0062cfd0(DAT_007b53f0,(int)local_28 + local_30,iVar8);
        local_30 = local_30 + iVar8;
      }
      local_6c = (uint *)0x1;
      local_70 = (uint *)0x0;
      do {
        puVar17 = local_6c;
        if ((_DAT_007b532c & (uint)local_6c) != 0) {
          iVar8 = *(int *)((int)&DAT_007b5334 + (int)local_70);
          local_7c = (uint *)(DAT_007c24e0 * DAT_007c24dc * 4);
          local_78 = (uint *)FUN_0063ea48(-(uint)((int)(ZEXT48(local_7c) * 8 >> 0x20) != 0) |
                                          (uint)(ZEXT48(local_7c) * 8));
          local_14 = local_14 & 0xffffff00;
          FUN_0062cfd0(local_78,iVar8,DAT_007c24e0 * DAT_007c24dc * 0x20);
          iVar16 = 0;
          if (0 < (int)(DAT_007c24e0 * DAT_007c24dc)) {
            pfVar18 = (float *)(iVar8 + 0x1c);
            pfVar15 = (float *)(iVar8 + 8);
            do {
              uVar14 = DAT_006db4a0;
              fVar23 = (pfVar18[-7] + pfVar18[-1]) * DAT_006da974;
              fVar21 = (float)((uint)(pfVar18[-1] - pfVar18[-7]) & DAT_006db490) * _DAT_006da8c4;
              fVar22 = (pfVar18[-6] + *pfVar18) * DAT_006da974;
              fVar20 = (float)((uint)(*pfVar18 - pfVar18[-6]) & DAT_006db490) * _DAT_006da8c4;
              fVar19 = fVar21;
              if (fVar23 <= pfVar15[-2]) {
                fVar19 = (float)((uint)fVar21 ^ DAT_006db4a0);
              }
              pfVar15[-2] = pfVar15[-2] + fVar19;
              fVar19 = fVar20;
              if (fVar22 <= pfVar15[-1]) {
                fVar19 = (float)((uint)fVar20 ^ uVar14);
              }
              pfVar15[-1] = pfVar15[-1] + fVar19;
              fVar19 = fVar21;
              if (fVar23 <= *pfVar15) {
                fVar19 = (float)((uint)fVar21 ^ uVar14);
              }
              *pfVar15 = *pfVar15 + fVar19;
              fVar19 = fVar20;
              if (fVar22 <= pfVar15[1]) {
                fVar19 = (float)((uint)fVar20 ^ uVar14);
              }
              pfVar15[1] = pfVar15[1] + fVar19;
              fVar19 = fVar21;
              if (fVar23 <= pfVar15[2]) {
                fVar19 = (float)((uint)fVar21 ^ uVar14);
              }
              pfVar15[2] = pfVar15[2] + fVar19;
              fVar19 = fVar20;
              if (fVar22 <= pfVar15[3]) {
                fVar19 = (float)((uint)fVar20 ^ uVar14);
              }
              pfVar15[3] = pfVar15[3] + fVar19;
              if (fVar23 <= pfVar15[4]) {
                fVar21 = (float)((uint)fVar21 ^ uVar14);
              }
              pfVar15[4] = pfVar15[4] + fVar21;
              if (fVar22 <= pfVar15[5]) {
                fVar20 = (float)((uint)fVar20 ^ uVar14);
              }
              iVar16 = iVar16 + 1;
              pfVar18 = pfVar18 + 8;
              pfVar15[5] = pfVar15[5] + fVar20;
              pfVar15 = pfVar15 + 8;
              puVar17 = local_6c;
            } while (iVar16 < (int)(DAT_007c24e0 * DAT_007c24dc));
          }
          FID_conflict__free(local_78);
        }
        local_70 = local_70 + 1;
        local_6c = (uint *)((int)puVar17 << 1 | (uint)((int)puVar17 < 0));
      } while (local_70 < (uint *)0x10);
      if (DAT_007c2498 == 0) {
        uVar14 = 0;
        DAT_007b5398 = 10;
        do {
          uVar7 = FUN_0042a47f();
          (&DAT_007b5370)[uVar14] = uVar7;
          FUN_00460c80(&local_30);
          lVar4 = ((longlong)(int)DAT_007c24e0 * (longlong)DAT_007c24dc & 0xffffffffU) * 4;
          uVar7 = FUN_0063ea48(-(uint)((int)((ulonglong)lVar4 >> 0x20) != 0) | (uint)lVar4);
          (&DAT_007b539c)[uVar14] = uVar7;
          uVar14 = uVar14 + 1;
        } while (uVar14 < DAT_007b5398);
      }
      if (0x20001112 < DAT_007c2498) {
        if (local_30 + 4 <= local_2c) {
          DAT_007b5398 = *(uint *)(local_30 + (int)local_28);
          local_30 = local_30 + 4;
        }
        if (DAT_007c2498 < 0x20001122) {
          _Memory = (void *)FUN_0063ea48(DAT_007c24e0 * DAT_007c24dc);
          iVar8 = DAT_007c24e0 * DAT_007c24dc;
          if ((iVar8 != 0) && (local_30 + iVar8 <= local_2c)) {
            FUN_0062cfd0(_Memory,(int)local_28 + local_30,iVar8);
            local_30 = local_30 + iVar8;
          }
          iVar8 = 0;
          if (0 < (int)(DAT_007c24e0 * DAT_007c24dc)) {
            do {
              bVar2 = *(byte *)(iVar8 + (int)_Memory);
              *(undefined1 *)(DAT_007b5344 + iVar8 * 4) = 0;
              puVar17 = (uint *)(DAT_007b5344 + iVar8 * 4);
              *puVar17 = *puVar17 | (uint)bVar2;
              iVar8 = iVar8 + 1;
            } while (iVar8 < (int)(DAT_007c24e0 * DAT_007c24dc));
          }
          FID_conflict__free(_Memory);
          DAT_007b5348 = 0;
          DAT_007b534c = 0;
          _DAT_007b5350 = 0;
          _DAT_007b5354 = 0;
          _DAT_007b5358 = 0;
          _DAT_007b535c = 0;
          _DAT_007b5360 = 0;
          _DAT_007b5364 = 0;
          _DAT_007b5368 = 0;
          _DAT_007b536c = 0;
        }
        else {
          iVar8 = DAT_007b5398 * 4;
          if ((iVar8 != 0) && (uVar14 = iVar8 + local_30, uVar14 <= local_2c)) {
            FUN_0062cfd0(&DAT_007b5348,(int)local_28 + local_30,iVar8);
            local_30 = uVar14;
          }
        }
        uVar14 = 0;
        if (DAT_007b5398 != 0) {
          do {
            uVar7 = FUN_0042a47f();
            (&DAT_007b5370)[uVar14] = uVar7;
            FUN_00460c80(&local_30);
            lVar4 = ((longlong)(int)DAT_007c24e0 * (longlong)DAT_007c24dc & 0xffffffffU) * 4;
            uVar7 = FUN_0063ea48(-(uint)((int)((ulonglong)lVar4 >> 0x20) != 0) | (uint)lVar4);
            (&DAT_007b539c)[uVar14] = uVar7;
            uVar14 = uVar14 + 1;
          } while (uVar14 < DAT_007b5398);
        }
      }
      DAT_007852e8 = 0;
      DAT_007852e0 = (uint *)0x0;
      if (DAT_007852e4 != (uint *)0x0) {
        puVar17 = DAT_007852e4 + -1;
        _eh_vector_destructor_iterator_(DAT_007852e4,0x68,DAT_007852e4[-1],FUN_0044d690);
        FUN_0062a696(puVar17,*puVar17 * 0x68 + 4);
      }
      DAT_007852e4 = (uint *)0x0;
      if (0x20001113 < DAT_007c2498) {
        if (local_30 + 4 <= local_2c) {
          DAT_007852e0 = *(uint **)(local_30 + (int)local_28);
          local_30 = local_30 + 4;
        }
        puVar17 = DAT_007852e0;
        if (DAT_007852e0 != (uint *)0x0) {
          uVar14 = -(uint)((int)(ZEXT48(DAT_007852e0) * 0x68 >> 0x20) != 0) |
                   (uint)(ZEXT48(DAT_007852e0) * 0x68);
          local_7c = DAT_007852e0;
          local_78 = (uint *)FUN_0063ea48(-(uint)(0xfffffffb < uVar14) | uVar14 + 4);
          local_14._0_1_ = 0x4a;
          if (local_78 == (uint *)0x0) {
            puVar13 = (uint *)0x0;
          }
          else {
            puVar13 = local_78 + 1;
            *local_78 = (uint)puVar17;
            _eh_vector_constructor_iterator_(puVar13,0x68,(uint)puVar17,FUN_0044d5b0,FUN_0044d690);
          }
          local_14 = (uint)local_14._1_3_ << 8;
          local_70 = (uint *)0x0;
          DAT_007852e4 = puVar13;
          if (DAT_007852e0 != (uint *)0x0) {
            iVar8 = 0;
            do {
              iVar16 = FUN_0044d830(&local_30,DAT_007c2498);
              if (iVar16 == 0) {
                DAT_007852e0 = (uint *)((int)DAT_007852e0 + -1);
              }
              if (*(int *)((int)DAT_007852e4 + iVar8 + 4) == 1) {
                DAT_007852e8 = 1;
              }
              iVar8 = iVar8 + 0x68;
              local_70 = (uint *)((int)local_70 + 1);
            } while (local_70 < DAT_007852e0);
          }
        }
      }
      DAT_007c24a0 = (uint *)0x0;
      if (0x20001114 < DAT_007c2498) {
        if (local_30 + 4 <= local_2c) {
          DAT_007c24a0 = *(uint **)(local_30 + (int)local_28);
          local_30 = local_30 + 4;
        }
        local_6c = (uint *)0x0;
        local_70 = (uint *)0x0;
        if (DAT_007c24a0 != (uint *)0x0) {
          do {
            puVar17 = local_6c;
            local_7c = (uint *)FUN_00640b15(0x150,0x10);
            local_14._0_1_ = 0x4b;
            if (local_7c == (uint *)0x0) {
              puVar13 = (uint *)0x0;
            }
            else {
              local_78 = local_7c;
              puVar13 = (uint *)FUN_0044d060();
            }
            local_14 = (uint)local_14._1_3_ << 8;
            local_78 = puVar13;
            iVar16 = FUN_0044d430(&local_30);
            iVar8 = DAT_007c24a4;
            if (iVar16 == 0) {
              local_6c = (uint *)((int)puVar17 + 1);
              if (puVar13 != (uint *)0x0) {
                puVar9 = (undefined4 *)puVar13[0xc];
                if (puVar9 != (undefined4 *)0x0) {
                  (**(code **)*puVar9)(0);
                  thunk_FUN_00640afb(puVar9);
                }
                puVar13[0xc] = 0;
                thunk_FUN_00640afb(puVar13);
              }
            }
            else {
              local_78 = (uint *)FUN_00434330(DAT_007c24a4,*(undefined4 *)(DAT_007c24a4 + 4),
                                              &local_78);
              if (DAT_007c24a8 == 0x15555554) {
                    /* WARNING: Subroutine does not return */
                FUN_00627726("list<T> too long");
              }
              DAT_007c24a8 = DAT_007c24a8 + 1;
              *(uint **)(iVar8 + 4) = local_78;
              *(uint **)local_78[1] = local_78;
              iVar8 = *(int *)(puVar13[0xc] + 0x94);
              puVar17 = (uint *)(iVar8 + 0x40);
              *puVar17 = *puVar17 & 0xfffeffff;
              for (iVar8 = *(int *)(iVar8 + 0x5c); iVar8 != 0; iVar8 = *(int *)(iVar8 + 100)) {
                if (*(int *)(iVar8 + 0x44) == -1) {
                  iVar8 = FUN_00456b40(0,1);
                }
              }
            }
            local_70 = (uint *)((int)local_70 + 1);
          } while (local_70 < DAT_007c24a0);
        }
        DAT_007c24a0 = (uint *)((int)DAT_007c24a0 - (int)local_6c);
      }
      if (DAT_007c2498 < 0x20001119) {
LAB_0044ba31:
        FUN_00445610();
      }
      else {
        iVar8 = (DAT_007c24e0 + 1) * (DAT_007c24dc + 1) * 4;
        if ((iVar8 != 0) && (local_30 + iVar8 <= local_2c)) {
          FUN_0062cfd0(DAT_007b5328,(int)local_28 + local_30,iVar8);
          local_30 = local_30 + iVar8;
        }
        if (DAT_007c2498 < 0x20001119) goto LAB_0044ba31;
      }
      puVar17 = DAT_007850d8;
      local_7c = DAT_007850d8;
      if (DAT_007c24cc != (int *)0x0) {
        (**(code **)(*DAT_007c24cc + 8))(DAT_007c24cc);
        DAT_007c24cc = (int *)0x0;
      }
      iVar8 = DAT_007c24d8;
      if (DAT_007c24d8 != 0) {
        FUN_00428380();
        FUN_0062a696(iVar8,0x38);
      }
      DAT_007c24d8 = 0;
      if ((DAT_007850d4 != '\0') && (puVar17 != (uint *)0x0)) {
        DAT_00764330 = DAT_0073ae68;
        if (puVar17[0x110] != 0) {
          FUN_0042f4a0(puVar17[0x110],puVar17[0x108],0,0,*puVar17,puVar17[1]);
        }
        for (puVar17 = param_1;
            puVar17 != (uint *)((int)param_1 + ((int)param_2 - (int)param_1 & 0xfffffffeU));
            puVar17 = (uint *)((int)puVar17 + 2)) {
          if ((short)*puVar17 == 0x2e) goto LAB_0044badf;
        }
        puVar17 = (uint *)0x0;
LAB_0044badf:
        if (puVar17 != (uint *)0x0) {
          _memset(local_68,0,0x38);
          FUN_00427ab0();
          local_14._0_1_ = 0x4c;
          puVar9 = (undefined4 *)
                   FUN_0059c260(&local_78,0x800,2,*(int *)ThreadLocalStoragePointer + 0xc);
          piVar3 = (int *)*puVar9;
          local_6c = (uint *)(piVar3 + 1);
          *piVar3 = 0;
          local_14._0_1_ = 0x5f;
          local_70 = (uint *)((uint)((int)puVar17 - (int)param_1) >> 1);
          iVar8 = *piVar3;
          puVar10 = (undefined *)((int)local_70 + iVar8);
          FUN_00434ab0(puVar10,puVar10);
          FUN_0062cfd0((int)local_6c + iVar8 * 2,param_1,(int)local_70 * 2);
          psVar11 = (short *)&DAT_006bee60;
          do {
            psVar12 = psVar11;
            psVar11 = psVar12 + 1;
          } while (*psVar11 != 0);
          uVar14 = (int)(psVar12 + -0x35f72f) >> 1;
          iVar16 = local_6c[-1];
          iVar8 = iVar16 + (uVar14 & 0x7fffffff);
          FUN_00434ab0(iVar8,iVar8);
          FUN_0062cfd0((int)local_6c + iVar16 * 2,&DAT_006bee60,uVar14 * 2);
          puVar17 = local_6c;
          iVar8 = (int)local_6c + local_6c[-1] * 2;
          FUN_00428380();
          local_78 = (uint *)&DAT_006b78d0;
          uVar7 = FUN_004a4d00(puVar17,iVar8);
          local_71 = FUN_00427bc0(uVar7,0);
          local_14._0_1_ = 0x4c;
          if (local_6c != (uint *)&DAT_006b9e28) {
            FUN_0059c360(local_6c + -1);
          }
          if (local_71 != '\0') {
            local_78 = (uint *)FUN_0063ea48(0x38);
            local_14._0_1_ = 0x72;
            if (local_78 == (uint *)0x0) {
              DAT_007c24d8 = 0;
            }
            else {
              _memset(local_78,0,0x38);
              DAT_007c24d8 = FUN_00427ab0();
            }
            puVar17 = local_7c;
            local_14._0_1_ = 0x4c;
            FUN_00427f70(local_68,*local_7c,local_7c[1]);
            DAT_007c24d0 = *(undefined4 *)(DAT_007c24d8 + 0x1c);
            DAT_007c24d4 = *(undefined4 *)(DAT_007c24d8 + 0x20);
            FUN_0042f710(DAT_007c24d0,DAT_007c24d4,&DAT_007c24cc,DAT_007c24d8,
                         (&DAT_006b9e54)[puVar17[0x108] * 0x16],DAT_007c24d4);
            _DAT_007c24c4 = 0;
            _DAT_007c24c8 = 0;
            DAT_007c24bc = DAT_006daa00 / (float)DAT_007c24dc;
            DAT_007c24c0 = DAT_006daa00 / (float)(int)DAT_007c24e0;
            FUN_0042f370(puVar17[0x110],DAT_007c24cc);
          }
          iVar8 = DAT_007c24d8;
          if (DAT_007c24d8 != 0) {
            FUN_00428380();
            FUN_0062a696(iVar8,0x38);
          }
          DAT_007c24d8 = 0;
          local_14 = (uint)local_14._1_3_ << 8;
          FUN_00428380();
        }
      }
      FUN_004487e0();
      FUN_00444f80();
      DAT_007b5e94 = 0;
      DAT_007852e9 = 1;
      local_71 = 1;
      goto LAB_0044be82;
    }
  }
  local_71 = 0;
LAB_0044be82:
  local_14 = 0xffffffff;
  if (local_28 != (void *)0x0) {
    FID_conflict__free(local_28);
    local_28 = (void *)0x0;
  }
  ExceptionList = local_1c;
  __security_check_cookie(local_24 ^ (uint)&stack0xfffffff0);
  return;
}


```

## `0044b891`

- Function: `FUN_0044aca0`
- Entry: `0044aca0`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_0044aca0(uint *param_1,uint *param_2)

{
  undefined4 *puVar1;
  byte bVar2;
  int *piVar3;
  longlong lVar4;
  short sVar5;
  char cVar6;
  undefined4 uVar7;
  int iVar8;
  void *_Memory;
  undefined4 *puVar9;
  undefined *puVar10;
  short *psVar11;
  undefined4 extraout_ECX;
  undefined4 extraout_ECX_00;
  uint *puVar13;
  uint uVar14;
  float *pfVar15;
  undefined4 extraout_ECX_01;
  int iVar16;
  uint *puVar17;
  float *pfVar18;
  float fVar19;
  float fVar20;
  float fVar21;
  float fVar22;
  float fVar23;
  uint *local_7c;
  uint *local_78;
  char local_71;
  uint *local_70;
  uint *local_6c;
  undefined1 local_68 [56];
  uint local_30;
  uint local_2c;
  void *local_28;
  uint local_24;
  undefined1 *puStack_20;
  void *local_1c;
  undefined1 *puStack_18;
  uint local_14;
  short *psVar12;
  
  puStack_20 = &stack0xfffffffc;
  local_14 = 0xffffffff;
  puStack_18 = &LAB_0065d5ab;
  local_1c = ExceptionList;
  local_24 = DAT_007360c8 ^ (uint)&stack0xfffffff0;
  ExceptionList = &local_1c;
  FUN_00438590(1);
  local_30 = 0;
  local_2c = 0;
  local_28 = (void *)0x0;
  local_14 = 0;
  if ((param_1 == (uint *)0x0) || (param_1 == param_2)) {
LAB_0044bd71:
    puVar9 = (undefined4 *)FUN_0059c260(&local_7c,0x800,2,*(int *)ThreadLocalStoragePointer + 0xc);
    local_6c = (undefined4 *)*puVar9 + 1;
    *(undefined4 *)*puVar9 = 0;
    local_14._0_1_ = 0x13;
    FUN_0044d000(extraout_ECX_01);
    local_7c = param_1;
    uVar14 = (uint)((int)param_2 - (int)param_1) >> 1;
    iVar16 = local_6c[-1];
    iVar8 = iVar16 + uVar14;
    FUN_00434ab0(iVar8,iVar8);
    FUN_0062cfd0((int)local_6c + iVar16 * 2,local_7c,uVar14 * 2);
    psVar11 = (short *)&DAT_006bee50;
    do {
      psVar12 = psVar11;
      psVar11 = psVar12 + 1;
    } while (*psVar11 != 0);
    uVar14 = (int)(psVar12 + -0x35f727) >> 1;
    iVar16 = local_6c[-1];
    iVar8 = iVar16 + (uVar14 & 0x7fffffff);
    FUN_00434ab0(iVar8,iVar8);
    FUN_0062cfd0((int)local_6c + iVar16 * 2,&DAT_006bee50,uVar14 * 2);
    FUN_00434ab0(local_6c[-1],local_6c[-1] + 1);
    *(undefined2 *)((int)local_6c + local_6c[-1] * 2) = 0;
    FUN_004d7ec0();
    local_14 = (uint)local_14._1_3_ << 8;
    if (local_6c != (uint *)&DAT_006b9e28) {
      FUN_0059c360(local_6c + -1);
    }
  }
  else {
    local_70 = (uint *)&DAT_006b78d0;
    uVar7 = FUN_004a4d00(param_1,param_2);
    cVar6 = FUN_0046c600(uVar7);
    if (cVar6 == '\0') goto LAB_0044bd71;
    FUN_004451e0(extraout_ECX);
    if (local_30 + 4 <= local_2c) {
      DAT_007c2498 = *(uint *)(local_30 + (int)local_28);
      local_30 = local_30 + 4;
    }
    if ((((((DAT_007c2498 == 0x20001113) || (DAT_007c2498 == 0x20001114)) ||
          (DAT_007c2498 == 0x20001115)) ||
         ((DAT_007c2498 == 0x20001116 || (DAT_007c2498 == 0x20001117)))) ||
        ((DAT_007c2498 == 0x20001118 ||
         ((DAT_007c2498 == 0x20001119 || (DAT_007c2498 == 0x20001120)))))) ||
       ((DAT_007c2498 == 0x20001121 || (DAT_007c2498 == 0x20001122)))) {
      if (0x20001122 < DAT_007c2498) goto LAB_0044add4;
    }
    else if (DAT_007c2498 == 0x20001123) {
LAB_0044add4:
      if (local_30 + 0x10 <= local_2c) {
        _DAT_007852ec = *(undefined4 *)(local_30 + (int)local_28);
        _DAT_007852f0 = *(undefined4 *)(local_30 + 4 + (int)local_28);
        _DAT_007852f4 = *(undefined4 *)(local_30 + 8 + (int)local_28);
        _DAT_007852f8 = *(undefined4 *)(local_30 + 0xc + (int)local_28);
        local_30 = local_30 + 0x10;
      }
    }
    else {
      DAT_007c2498 = 0;
      local_30 = 0;
      if (local_2c == 0) {
        local_30 = 0xffffffff;
      }
    }
    FUN_0046c6d0(&DAT_006bec44,&DAT_007c24dc);
    FUN_0046c6d0(&DAT_006bec44,&DAT_007c24e0);
    DAT_007b5320 = FUN_00431780("FIELD",extraout_ECX_00);
    iVar8 = FUN_004539c0(&local_30);
    if (iVar8 != 0) {
      DAT_007c2490 = (void *)FUN_0063ea48(DAT_007c24e0 * DAT_007c24dc);
      lVar4 = (ulonglong)(DAT_007c24e0 + 1) * 2;
      DAT_007c2488 = (void *)FUN_0063ea48(-(uint)((int)((ulonglong)lVar4 >> 0x20) != 0) |
                                          (uint)lVar4);
      DAT_007c248c = (void *)FUN_0063ea48(-(uint)((int)((ulonglong)DAT_007c24e0 * 2 >> 0x20) != 0) |
                                          (uint)((ulonglong)DAT_007c24e0 * 2));
      DAT_007c2494 = (void *)FUN_0063ea48(DAT_007c24e0 * DAT_007c24dc);
      lVar4 = (ulonglong)((DAT_007c24e0 + 1) * (DAT_007c24dc + 1)) * 4;
      DAT_007b5328 = FUN_0063ea48(-(uint)((int)((ulonglong)lVar4 >> 0x20) != 0) | (uint)lVar4);
      if (((DAT_007b5320 == 0) || (*(int **)(DAT_007b5320 + 0x48) == (int *)0x0)) ||
         (**(int **)(DAT_007b5320 + 0x48) == 0)) {
        local_6c = (uint *)0x0;
      }
      else {
        local_6c = (uint *)FUN_0046bbc0(0);
      }
      puVar17 = local_6c;
      DAT_007b5324 = FUN_0063ea48(-(uint)((int)(ZEXT48(local_6c) * 4 >> 0x20) != 0) |
                                  (uint)(ZEXT48(local_6c) * 4));
      DAT_007b5408 = FUN_0063ea48(puVar17);
      DAT_007b5404 = FUN_0063ea48(((uint)((int)puVar17 + 0x1f) >> 5) * 4);
      DAT_007b53f0 = FUN_0063ea48(-(uint)((int)(ZEXT48(puVar17) * 4 >> 0x20) != 0) |
                                  (uint)(ZEXT48(puVar17) * 4));
      DAT_007b53f8 = FUN_0063ea48(puVar17);
      DAT_007b53fc = FUN_0063ea48(puVar17);
      DAT_007b53f4 = FUN_0063ea48(puVar17);
      DAT_007b53ec = FUN_0063ea48(-(uint)((int)(ZEXT48(puVar17) * 0xc >> 0x20) != 0) |
                                  (uint)(ZEXT48(puVar17) * 0xc));
      iVar8 = 0;
      iVar16 = **(int **)(DAT_007b5320 + 0x48);
      if ((*(byte *)(iVar16 + 0x10) & 2) == 0) {
        if (*(int *)(iVar16 + 0x14) == 0) {
          iVar8 = 0;
        }
        else {
          iVar8 = *(int *)(*(int *)(iVar16 + 0x14) + 0x10);
        }
      }
      else {
        if (*(int *)(iVar16 + 4) == 0) {
          iVar8 = -1;
        }
        iVar8 = *(int *)(*(int *)(*(int *)(iVar16 + 8) + iVar8 * 4) * 0x94 + 0x10 +
                        *(int *)(iVar16 + 0x14));
      }
      puVar13 = (uint *)0x0;
      if ((uint *)0x3 < puVar17) {
        local_70 = (uint *)((int)puVar17 + -3);
        puVar9 = (undefined4 *)(iVar8 + 0x10);
        do {
          *(undefined4 *)(DAT_007b5324 + (int)puVar13 * 4) = puVar9[-3];
          *(undefined4 *)(DAT_007b5324 + 4 + (int)puVar13 * 4) = *puVar9;
          *(undefined4 *)(DAT_007b5324 + 8 + (int)puVar13 * 4) = puVar9[3];
          puVar1 = puVar9 + 6;
          puVar9 = puVar9 + 0xc;
          *(undefined4 *)(DAT_007b5324 + 0xc + (int)puVar13 * 4) = *puVar1;
          puVar13 = puVar13 + 1;
          puVar17 = local_6c;
        } while (puVar13 < local_70);
      }
      if (puVar13 < puVar17) {
        puVar9 = (undefined4 *)(iVar8 + ((int)puVar13 * 3 + 1) * 4);
        do {
          uVar7 = *puVar9;
          puVar9 = puVar9 + 3;
          *(undefined4 *)(DAT_007b5324 + (int)puVar13 * 4) = uVar7;
          puVar13 = (uint *)((int)puVar13 + 1);
        } while (puVar13 < puVar17);
      }
      _memset(DAT_007c2488,0xff,DAT_007c24e0 * 2 + 2);
      _memset(DAT_007c248c,0xff,DAT_007c24e0 * 2);
      _memset(DAT_007c2490,0,DAT_007c24e0 * DAT_007c24dc);
      _memset(DAT_007c2494,0,DAT_007c24e0 * DAT_007c24dc);
      puVar13 = (uint *)(DAT_007c24e0 * DAT_007c24dc);
      uVar14 = -(uint)((int)(ZEXT48(puVar13) * 0x10 >> 0x20) != 0) | (uint)(ZEXT48(puVar13) * 0x10);
      local_7c = puVar13;
      local_70 = puVar13;
      local_78 = (uint *)FUN_0063ea48(-(uint)(0xfffffffb < uVar14) | uVar14 + 4);
      local_14._0_1_ = 0x26;
      if (local_78 == (uint *)0x0) {
        puVar13 = (uint *)0x0;
      }
      else {
        *local_78 = (uint)puVar13;
        puVar13 = local_78 + 1;
        _eh_vector_constructor_iterator_
                  (puVar13,0x10,(uint)local_70,(_func_void_void_ptr *)&LAB_0044cc30,FUN_0044cc50);
      }
      local_14 = (uint)local_14._1_3_ << 8;
      DAT_007b5410 = 0;
      DAT_007b540c = puVar13;
      if (DAT_007c2498 < 0x20001120) {
        iVar8 = 0;
        puVar17 = local_6c;
        if (0 < (int)(DAT_007c24e0 * DAT_007c24dc)) {
          iVar16 = 0;
          do {
            *(undefined1 *)(iVar16 + (int)DAT_007b540c) = 6;
            sVar5 = (short)iVar8;
            iVar8 = iVar8 + 1;
            *(undefined1 *)(iVar16 + 1 + (int)DAT_007b540c) = 4;
            *(short *)(iVar16 + 2 + (int)DAT_007b540c) = sVar5 * 4;
            *(undefined4 *)(iVar16 + 4 + (int)DAT_007b540c) = 0;
            *(undefined4 *)(iVar16 + 8 + (int)DAT_007b540c) = 0;
            DAT_007b5410 = DAT_007b5410 + (uint)*(byte *)(iVar16 + 1 + (int)DAT_007b540c);
            iVar16 = iVar16 + 0x10;
          } while (iVar8 < (int)(DAT_007c24e0 * DAT_007c24dc));
        }
      }
      else {
        local_70 = (uint *)0x0;
        if (0 < (int)(DAT_007c24e0 * DAT_007c24dc)) {
          iVar8 = 0;
          do {
            puVar17 = DAT_007b540c;
            if (local_30 + 1 <= local_2c) {
              *(undefined1 *)(iVar8 + (int)DAT_007b540c) = *(undefined1 *)(local_30 + (int)local_28)
              ;
              local_30 = local_30 + 1;
            }
            if (local_30 + 2 <= local_2c) {
              *(undefined2 *)(iVar8 + 2 + (int)puVar17) = *(undefined2 *)(local_30 + (int)local_28);
              local_30 = local_30 + 2;
            }
            if (local_30 + 1 <= local_2c) {
              *(undefined1 *)(iVar8 + 0xc + (int)puVar17) =
                   *(undefined1 *)(local_30 + (int)local_28);
              local_30 = local_30 + 1;
            }
            if (local_30 + 1 <= local_2c) {
              *(undefined1 *)(iVar8 + 1 + (int)puVar17) = *(undefined1 *)(local_30 + (int)local_28);
              local_30 = local_30 + 1;
            }
            FID_conflict__free(*(void **)(iVar8 + 4 + (int)puVar17));
            local_70 = (uint *)((int)local_70 + 1);
            *(undefined4 *)(iVar8 + 4 + (int)puVar17) = 0;
            iVar16 = iVar8 + 1;
            iVar8 = iVar8 + 0x10;
            DAT_007b5410 = DAT_007b5410 + (uint)*(byte *)(iVar16 + (int)DAT_007b540c);
            puVar17 = local_6c;
          } while ((int)local_70 < (int)(DAT_007c24e0 * DAT_007c24dc));
        }
      }
      if (DAT_007c2498 < 0x20001122) {
        FUN_0044cd00(1,DAT_007c24e0 * DAT_007c24dc);
        uVar7 = 0;
        if ((_DAT_007b532c & 1) != 0) {
          uVar7 = DAT_007b5334;
        }
        iVar8 = DAT_007b5410 * 8;
        if ((iVar8 != 0) && (iVar8 + local_30 <= local_2c)) {
          FUN_0062cfd0(uVar7,(int)local_28 + local_30,iVar8);
          local_30 = local_30 + iVar8;
        }
      }
      else {
        FUN_0044ce40(&local_30);
      }
      iVar8 = (int)puVar17 * 4;
      if ((iVar8 != 0) && (iVar8 + local_30 <= local_2c)) {
        FUN_0062cfd0(DAT_007b53f0,(int)local_28 + local_30,iVar8);
        local_30 = local_30 + iVar8;
      }
      local_6c = (uint *)0x1;
      local_70 = (uint *)0x0;
      do {
        puVar17 = local_6c;
        if ((_DAT_007b532c & (uint)local_6c) != 0) {
          iVar8 = *(int *)((int)&DAT_007b5334 + (int)local_70);
          local_7c = (uint *)(DAT_007c24e0 * DAT_007c24dc * 4);
          local_78 = (uint *)FUN_0063ea48(-(uint)((int)(ZEXT48(local_7c) * 8 >> 0x20) != 0) |
                                          (uint)(ZEXT48(local_7c) * 8));
          local_14 = local_14 & 0xffffff00;
          FUN_0062cfd0(local_78,iVar8,DAT_007c24e0 * DAT_007c24dc * 0x20);
          iVar16 = 0;
          if (0 < (int)(DAT_007c24e0 * DAT_007c24dc)) {
            pfVar18 = (float *)(iVar8 + 0x1c);
            pfVar15 = (float *)(iVar8 + 8);
            do {
              uVar14 = DAT_006db4a0;
              fVar23 = (pfVar18[-7] + pfVar18[-1]) * DAT_006da974;
              fVar21 = (float)((uint)(pfVar18[-1] - pfVar18[-7]) & DAT_006db490) * _DAT_006da8c4;
              fVar22 = (pfVar18[-6] + *pfVar18) * DAT_006da974;
              fVar20 = (float)((uint)(*pfVar18 - pfVar18[-6]) & DAT_006db490) * _DAT_006da8c4;
              fVar19 = fVar21;
              if (fVar23 <= pfVar15[-2]) {
                fVar19 = (float)((uint)fVar21 ^ DAT_006db4a0);
              }
              pfVar15[-2] = pfVar15[-2] + fVar19;
              fVar19 = fVar20;
              if (fVar22 <= pfVar15[-1]) {
                fVar19 = (float)((uint)fVar20 ^ uVar14);
              }
              pfVar15[-1] = pfVar15[-1] + fVar19;
              fVar19 = fVar21;
              if (fVar23 <= *pfVar15) {
                fVar19 = (float)((uint)fVar21 ^ uVar14);
              }
              *pfVar15 = *pfVar15 + fVar19;
              fVar19 = fVar20;
              if (fVar22 <= pfVar15[1]) {
                fVar19 = (float)((uint)fVar20 ^ uVar14);
              }
              pfVar15[1] = pfVar15[1] + fVar19;
              fVar19 = fVar21;
              if (fVar23 <= pfVar15[2]) {
                fVar19 = (float)((uint)fVar21 ^ uVar14);
              }
              pfVar15[2] = pfVar15[2] + fVar19;
              fVar19 = fVar20;
              if (fVar22 <= pfVar15[3]) {
                fVar19 = (float)((uint)fVar20 ^ uVar14);
              }
              pfVar15[3] = pfVar15[3] + fVar19;
              if (fVar23 <= pfVar15[4]) {
                fVar21 = (float)((uint)fVar21 ^ uVar14);
              }
              pfVar15[4] = pfVar15[4] + fVar21;
              if (fVar22 <= pfVar15[5]) {
                fVar20 = (float)((uint)fVar20 ^ uVar14);
              }
              iVar16 = iVar16 + 1;
              pfVar18 = pfVar18 + 8;
              pfVar15[5] = pfVar15[5] + fVar20;
              pfVar15 = pfVar15 + 8;
              puVar17 = local_6c;
            } while (iVar16 < (int)(DAT_007c24e0 * DAT_007c24dc));
          }
          FID_conflict__free(local_78);
        }
        local_70 = local_70 + 1;
        local_6c = (uint *)((int)puVar17 << 1 | (uint)((int)puVar17 < 0));
      } while (local_70 < (uint *)0x10);
      if (DAT_007c2498 == 0) {
        uVar14 = 0;
        DAT_007b5398 = 10;
        do {
          uVar7 = FUN_0042a47f();
          (&DAT_007b5370)[uVar14] = uVar7;
          FUN_00460c80(&local_30);
          lVar4 = ((longlong)(int)DAT_007c24e0 * (longlong)DAT_007c24dc & 0xffffffffU) * 4;
          uVar7 = FUN_0063ea48(-(uint)((int)((ulonglong)lVar4 >> 0x20) != 0) | (uint)lVar4);
          (&DAT_007b539c)[uVar14] = uVar7;
          uVar14 = uVar14 + 1;
        } while (uVar14 < DAT_007b5398);
      }
      if (0x20001112 < DAT_007c2498) {
        if (local_30 + 4 <= local_2c) {
          DAT_007b5398 = *(uint *)(local_30 + (int)local_28);
          local_30 = local_30 + 4;
        }
        if (DAT_007c2498 < 0x20001122) {
          _Memory = (void *)FUN_0063ea48(DAT_007c24e0 * DAT_007c24dc);
          iVar8 = DAT_007c24e0 * DAT_007c24dc;
          if ((iVar8 != 0) && (local_30 + iVar8 <= local_2c)) {
            FUN_0062cfd0(_Memory,(int)local_28 + local_30,iVar8);
            local_30 = local_30 + iVar8;
          }
          iVar8 = 0;
          if (0 < (int)(DAT_007c24e0 * DAT_007c24dc)) {
            do {
              bVar2 = *(byte *)(iVar8 + (int)_Memory);
              *(undefined1 *)(DAT_007b5344 + iVar8 * 4) = 0;
              puVar17 = (uint *)(DAT_007b5344 + iVar8 * 4);
              *puVar17 = *puVar17 | (uint)bVar2;
              iVar8 = iVar8 + 1;
            } while (iVar8 < (int)(DAT_007c24e0 * DAT_007c24dc));
          }
          FID_conflict__free(_Memory);
          DAT_007b5348 = 0;
          DAT_007b534c = 0;
          _DAT_007b5350 = 0;
          _DAT_007b5354 = 0;
          _DAT_007b5358 = 0;
          _DAT_007b535c = 0;
          _DAT_007b5360 = 0;
          _DAT_007b5364 = 0;
          _DAT_007b5368 = 0;
          _DAT_007b536c = 0;
        }
        else {
          iVar8 = DAT_007b5398 * 4;
          if ((iVar8 != 0) && (uVar14 = iVar8 + local_30, uVar14 <= local_2c)) {
            FUN_0062cfd0(&DAT_007b5348,(int)local_28 + local_30,iVar8);
            local_30 = uVar14;
          }
        }
        uVar14 = 0;
        if (DAT_007b5398 != 0) {
          do {
            uVar7 = FUN_0042a47f();
            (&DAT_007b5370)[uVar14] = uVar7;
            FUN_00460c80(&local_30);
            lVar4 = ((longlong)(int)DAT_007c24e0 * (longlong)DAT_007c24dc & 0xffffffffU) * 4;
            uVar7 = FUN_0063ea48(-(uint)((int)((ulonglong)lVar4 >> 0x20) != 0) | (uint)lVar4);
            (&DAT_007b539c)[uVar14] = uVar7;
            uVar14 = uVar14 + 1;
          } while (uVar14 < DAT_007b5398);
        }
      }
      DAT_007852e8 = 0;
      DAT_007852e0 = (uint *)0x0;
      if (DAT_007852e4 != (uint *)0x0) {
        puVar17 = DAT_007852e4 + -1;
        _eh_vector_destructor_iterator_(DAT_007852e4,0x68,DAT_007852e4[-1],FUN_0044d690);
        FUN_0062a696(puVar17,*puVar17 * 0x68 + 4);
      }
      DAT_007852e4 = (uint *)0x0;
      if (0x20001113 < DAT_007c2498) {
        if (local_30 + 4 <= local_2c) {
          DAT_007852e0 = *(uint **)(local_30 + (int)local_28);
          local_30 = local_30 + 4;
        }
        puVar17 = DAT_007852e0;
        if (DAT_007852e0 != (uint *)0x0) {
          uVar14 = -(uint)((int)(ZEXT48(DAT_007852e0) * 0x68 >> 0x20) != 0) |
                   (uint)(ZEXT48(DAT_007852e0) * 0x68);
          local_7c = DAT_007852e0;
          local_78 = (uint *)FUN_0063ea48(-(uint)(0xfffffffb < uVar14) | uVar14 + 4);
          local_14._0_1_ = 0x4a;
          if (local_78 == (uint *)0x0) {
            puVar13 = (uint *)0x0;
          }
          else {
            puVar13 = local_78 + 1;
            *local_78 = (uint)puVar17;
            _eh_vector_constructor_iterator_(puVar13,0x68,(uint)puVar17,FUN_0044d5b0,FUN_0044d690);
          }
          local_14 = (uint)local_14._1_3_ << 8;
          local_70 = (uint *)0x0;
          DAT_007852e4 = puVar13;
          if (DAT_007852e0 != (uint *)0x0) {
            iVar8 = 0;
            do {
              iVar16 = FUN_0044d830(&local_30,DAT_007c2498);
              if (iVar16 == 0) {
                DAT_007852e0 = (uint *)((int)DAT_007852e0 + -1);
              }
              if (*(int *)((int)DAT_007852e4 + iVar8 + 4) == 1) {
                DAT_007852e8 = 1;
              }
              iVar8 = iVar8 + 0x68;
              local_70 = (uint *)((int)local_70 + 1);
            } while (local_70 < DAT_007852e0);
          }
        }
      }
      DAT_007c24a0 = (uint *)0x0;
      if (0x20001114 < DAT_007c2498) {
        if (local_30 + 4 <= local_2c) {
          DAT_007c24a0 = *(uint **)(local_30 + (int)local_28);
          local_30 = local_30 + 4;
        }
        local_6c = (uint *)0x0;
        local_70 = (uint *)0x0;
        if (DAT_007c24a0 != (uint *)0x0) {
          do {
            puVar17 = local_6c;
            local_7c = (uint *)FUN_00640b15(0x150,0x10);
            local_14._0_1_ = 0x4b;
            if (local_7c == (uint *)0x0) {
              puVar13 = (uint *)0x0;
            }
            else {
              local_78 = local_7c;
              puVar13 = (uint *)FUN_0044d060();
            }
            local_14 = (uint)local_14._1_3_ << 8;
            local_78 = puVar13;
            iVar16 = FUN_0044d430(&local_30);
            iVar8 = DAT_007c24a4;
            if (iVar16 == 0) {
              local_6c = (uint *)((int)puVar17 + 1);
              if (puVar13 != (uint *)0x0) {
                puVar9 = (undefined4 *)puVar13[0xc];
                if (puVar9 != (undefined4 *)0x0) {
                  (**(code **)*puVar9)(0);
                  thunk_FUN_00640afb(puVar9);
                }
                puVar13[0xc] = 0;
                thunk_FUN_00640afb(puVar13);
              }
            }
            else {
              local_78 = (uint *)FUN_00434330(DAT_007c24a4,*(undefined4 *)(DAT_007c24a4 + 4),
                                              &local_78);
              if (DAT_007c24a8 == 0x15555554) {
                    /* WARNING: Subroutine does not return */
                FUN_00627726("list<T> too long");
              }
              DAT_007c24a8 = DAT_007c24a8 + 1;
              *(uint **)(iVar8 + 4) = local_78;
              *(uint **)local_78[1] = local_78;
              iVar8 = *(int *)(puVar13[0xc] + 0x94);
              puVar17 = (uint *)(iVar8 + 0x40);
              *puVar17 = *puVar17 & 0xfffeffff;
              for (iVar8 = *(int *)(iVar8 + 0x5c); iVar8 != 0; iVar8 = *(int *)(iVar8 + 100)) {
                if (*(int *)(iVar8 + 0x44) == -1) {
                  iVar8 = FUN_00456b40(0,1);
                }
              }
            }
            local_70 = (uint *)((int)local_70 + 1);
          } while (local_70 < DAT_007c24a0);
        }
        DAT_007c24a0 = (uint *)((int)DAT_007c24a0 - (int)local_6c);
      }
      if (DAT_007c2498 < 0x20001119) {
LAB_0044ba31:
        FUN_00445610();
      }
      else {
        iVar8 = (DAT_007c24e0 + 1) * (DAT_007c24dc + 1) * 4;
        if ((iVar8 != 0) && (local_30 + iVar8 <= local_2c)) {
          FUN_0062cfd0(DAT_007b5328,(int)local_28 + local_30,iVar8);
          local_30 = local_30 + iVar8;
        }
        if (DAT_007c2498 < 0x20001119) goto LAB_0044ba31;
      }
      puVar17 = DAT_007850d8;
      local_7c = DAT_007850d8;
      if (DAT_007c24cc != (int *)0x0) {
        (**(code **)(*DAT_007c24cc + 8))(DAT_007c24cc);
        DAT_007c24cc = (int *)0x0;
      }
      iVar8 = DAT_007c24d8;
      if (DAT_007c24d8 != 0) {
        FUN_00428380();
        FUN_0062a696(iVar8,0x38);
      }
      DAT_007c24d8 = 0;
      if ((DAT_007850d4 != '\0') && (puVar17 != (uint *)0x0)) {
        DAT_00764330 = DAT_0073ae68;
        if (puVar17[0x110] != 0) {
          FUN_0042f4a0(puVar17[0x110],puVar17[0x108],0,0,*puVar17,puVar17[1]);
        }
        for (puVar17 = param_1;
            puVar17 != (uint *)((int)param_1 + ((int)param_2 - (int)param_1 & 0xfffffffeU));
            puVar17 = (uint *)((int)puVar17 + 2)) {
          if ((short)*puVar17 == 0x2e) goto LAB_0044badf;
        }
        puVar17 = (uint *)0x0;
LAB_0044badf:
        if (puVar17 != (uint *)0x0) {
          _memset(local_68,0,0x38);
          FUN_00427ab0();
          local_14._0_1_ = 0x4c;
          puVar9 = (undefined4 *)
                   FUN_0059c260(&local_78,0x800,2,*(int *)ThreadLocalStoragePointer + 0xc);
          piVar3 = (int *)*puVar9;
          local_6c = (uint *)(piVar3 + 1);
          *piVar3 = 0;
          local_14._0_1_ = 0x5f;
          local_70 = (uint *)((uint)((int)puVar17 - (int)param_1) >> 1);
          iVar8 = *piVar3;
          puVar10 = (undefined *)((int)local_70 + iVar8);
          FUN_00434ab0(puVar10,puVar10);
          FUN_0062cfd0((int)local_6c + iVar8 * 2,param_1,(int)local_70 * 2);
          psVar11 = (short *)&DAT_006bee60;
          do {
            psVar12 = psVar11;
            psVar11 = psVar12 + 1;
          } while (*psVar11 != 0);
          uVar14 = (int)(psVar12 + -0x35f72f) >> 1;
          iVar16 = local_6c[-1];
          iVar8 = iVar16 + (uVar14 & 0x7fffffff);
          FUN_00434ab0(iVar8,iVar8);
          FUN_0062cfd0((int)local_6c + iVar16 * 2,&DAT_006bee60,uVar14 * 2);
          puVar17 = local_6c;
          iVar8 = (int)local_6c + local_6c[-1] * 2;
          FUN_00428380();
          local_78 = (uint *)&DAT_006b78d0;
          uVar7 = FUN_004a4d00(puVar17,iVar8);
          local_71 = FUN_00427bc0(uVar7,0);
          local_14._0_1_ = 0x4c;
          if (local_6c != (uint *)&DAT_006b9e28) {
            FUN_0059c360(local_6c + -1);
          }
          if (local_71 != '\0') {
            local_78 = (uint *)FUN_0063ea48(0x38);
            local_14._0_1_ = 0x72;
            if (local_78 == (uint *)0x0) {
              DAT_007c24d8 = 0;
            }
            else {
              _memset(local_78,0,0x38);
              DAT_007c24d8 = FUN_00427ab0();
            }
            puVar17 = local_7c;
            local_14._0_1_ = 0x4c;
            FUN_00427f70(local_68,*local_7c,local_7c[1]);
            DAT_007c24d0 = *(undefined4 *)(DAT_007c24d8 + 0x1c);
            DAT_007c24d4 = *(undefined4 *)(DAT_007c24d8 + 0x20);
            FUN_0042f710(DAT_007c24d0,DAT_007c24d4,&DAT_007c24cc,DAT_007c24d8,
                         (&DAT_006b9e54)[puVar17[0x108] * 0x16],DAT_007c24d4);
            _DAT_007c24c4 = 0;
            _DAT_007c24c8 = 0;
            DAT_007c24bc = DAT_006daa00 / (float)DAT_007c24dc;
            DAT_007c24c0 = DAT_006daa00 / (float)(int)DAT_007c24e0;
            FUN_0042f370(puVar17[0x110],DAT_007c24cc);
          }
          iVar8 = DAT_007c24d8;
          if (DAT_007c24d8 != 0) {
            FUN_00428380();
            FUN_0062a696(iVar8,0x38);
          }
          DAT_007c24d8 = 0;
          local_14 = (uint)local_14._1_3_ << 8;
          FUN_00428380();
        }
      }
      FUN_004487e0();
      FUN_00444f80();
      DAT_007b5e94 = 0;
      DAT_007852e9 = 1;
      local_71 = 1;
      goto LAB_0044be82;
    }
  }
  local_71 = 0;
LAB_0044be82:
  local_14 = 0xffffffff;
  if (local_28 != (void *)0x0) {
    FID_conflict__free(local_28);
    local_28 = (void *)0x0;
  }
  ExceptionList = local_1c;
  __security_check_cookie(local_24 ^ (uint)&stack0xfffffff0);
  return;
}


```

