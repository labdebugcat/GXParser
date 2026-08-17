# Selected Nova1492 Decompilation

## `00464630`

- Function: `FUN_00464630`
- Entry: `00464630`

```c

/* WARNING: Removing unreachable block (ram,0x0046484e) */
/* WARNING: Removing unreachable block (ram,0x00464822) */
/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00464630(void)

{
  float fVar1;
  size_t _Size;
  bool bVar2;
  bool bVar3;
  byte bVar4;
  char cVar5;
  byte bVar6;
  byte bVar7;
  undefined2 uVar8;
  wchar_t *pwVar9;
  int iVar10;
  char *pcVar11;
  undefined4 *puVar12;
  int iVar13;
  uint *_Dst;
  uint *puVar14;
  undefined4 *puVar15;
  int iVar16;
  uint uVar17;
  uint *puVar18;
  float10 fVar19;
  float *pfVar20;
  undefined4 uVar21;
  undefined1 *puVar22;
  undefined2 *local_77c;
  uint local_740;
  undefined4 local_73c;
  undefined2 *local_72c;
  char *local_728;
  undefined4 local_70c;
  undefined1 local_708;
  undefined4 local_6fc;
  undefined1 local_6f8;
  uint local_6f4;
  undefined1 local_6f0;
  uint local_6ec;
  undefined4 local_6e8;
  undefined4 local_6e4;
  undefined4 local_6e0;
  uint local_6dc;
  undefined4 local_6d8;
  byte local_6d4;
  float local_6d0;
  undefined4 local_6cc;
  undefined4 local_6c8;
  undefined4 local_6c4;
  uint local_6c0;
  float *local_6bc;
  undefined8 local_6b8;
  char local_6b0 [1000];
  char local_2c8 [104];
  char local_260 [40];
  char local_238 [264];
  char local_130;
  char local_12f [267];
  uint local_24;
  undefined1 *puStack_20;
  void *local_1c;
  undefined1 *puStack_18;
  undefined4 local_14;
  
  puStack_20 = &stack0xfffffffc;
  local_14 = 0xffffffff;
  puStack_18 = &LAB_00662260;
  local_1c = ExceptionList;
  local_24 = DAT_007360c8 ^ (uint)&stack0xfffffff0;
  ExceptionList = &local_1c;
  pwVar9 = L"gxdesc.ini";
  do {
    pwVar9 = pwVar9 + 1;
  } while (*pwVar9 != L'\0');
  cVar5 = FUN_004a4340();
  if (cVar5 != '\0') {
    pwVar9 = L"gxdesc.ini";
    do {
      pwVar9 = pwVar9 + 1;
    } while (*pwVar9 != L'\0');
    cVar5 = FUN_00468b20();
    if (cVar5 != '\0') {
      iVar10 = FUN_004692b0();
      if (iVar10 != 0x2b5) {
        FUN_004d7ec0();
      }
      uVar17 = 0;
      puVar15 = &DAT_007c2548;
      uVar21 = local_14;
      do {
        local_14 = uVar21;
        pcVar11 = "Files";
        do {
          pcVar11 = pcVar11 + 1;
        } while (*pcVar11 != '\0');
        iVar10 = FUN_00468d70();
        if (iVar10 == 0) goto LAB_0046727f;
        pcVar11 = "Files";
        do {
          pcVar11 = pcVar11 + 1;
        } while (*pcVar11 != '\0');
        iVar10 = FUN_00468ed0();
        if (iVar10 == 0) goto LAB_0046727f;
        FUN_0046a430(iVar10);
        pcVar11 = &local_130;
        cVar5 = local_130;
        while (cVar5 != '\0') {
          pcVar11 = pcVar11 + 1;
          cVar5 = *pcVar11;
        }
        FUN_00469cd0();
        local_14 = 1;
        if ((undefined2 *)*puVar15 != &DAT_006b9e28) {
          FID_conflict__free((undefined2 *)*puVar15 + -2);
        }
        *puVar15 = local_72c;
        local_72c = &DAT_006b9e28;
        local_14 = 0xffffffff;
        uVar21 = local_14;
        local_14 = 0xffffffff;
        uVar17 = uVar17 + 1;
        puVar15 = puVar15 + 1;
      } while (uVar17 < 0x2b5);
      local_740 = 0;
      do {
        puVar15 = &DAT_007c2548 + local_740;
        FUN_004697f0();
        iVar10 = FUN_00468d70();
        if (iVar10 != 0) {
          pcVar11 = "anispeed";
          do {
            pcVar11 = pcVar11 + 1;
          } while (*pcVar11 != '\0');
          iVar10 = (&DAT_007c2548)[local_740];
          iVar10 = FUN_00469050(iVar10,*(int *)(iVar10 + -4) + iVar10);
          (&DAT_00766064)[local_740 * 0x11] = 0x3f800000;
          if ((iVar10 != 0) && (iVar10 = FUN_00462dc0(), iVar10 != 1)) {
            (&DAT_00766064)[local_740 * 0x11] = 0x3f800000;
          }
          pcVar11 = "scale";
          do {
            pcVar11 = pcVar11 + 1;
          } while (*pcVar11 != '\0');
          iVar10 = (&DAT_007c2548)[local_740];
          iVar10 = FUN_00469050(iVar10,*(int *)(iVar10 + -4) + iVar10);
          (&DAT_00766068)[local_740 * 0x11] = 0x3f800000;
          if ((iVar10 != 0) && (iVar10 = FUN_00462dc0(), iVar10 != 1)) {
            (&DAT_00766068)[local_740 * 0x11] = 0x3f800000;
          }
          (&DAT_00766070)[local_740 * 0x11] = 0xffffffff;
          pcVar11 = "pair";
          do {
            pcVar11 = pcVar11 + 1;
          } while (*pcVar11 != '\0');
          iVar10 = (&DAT_007c2548)[local_740];
          iVar10 = FUN_00469050(iVar10,*(int *)(iVar10 + -4) + iVar10);
          if (((iVar10 != 0) && (iVar10 = FUN_00462dc0(), iVar10 == 1)) &&
             (iVar10 = __stricmp(&local_130,"NULL"), iVar10 != 0)) {
            uVar17 = 0;
            do {
              pcVar11 = &local_130;
              cVar5 = local_130;
              while (cVar5 != '\0') {
                pcVar11 = pcVar11 + 1;
                cVar5 = *pcVar11;
              }
              _Size = *(size_t *)((int)(&DAT_007c2548)[uVar17] + -4);
              if ((_Size == (int)pcVar11 - (int)&local_130) &&
                 (iVar10 = __memicmp((void *)(&DAT_007c2548)[uVar17],&local_130,_Size), iVar10 == 0)
                 ) {
                (&DAT_00766070)[local_740 * 0x11] = uVar17;
                break;
              }
              uVar17 = uVar17 + 1;
            } while (uVar17 < 0x2b5);
            if (uVar17 == 0x2b5) {
              FUN_00433880();
              local_14 = 0x35;
              FUN_004278e0();
              FUN_00433d50();
              FUN_0046a240();
              local_14 = 0xffffffff;
              if (local_77c != &DAT_006b9e28) {
                FUN_0059c360();
              }
            }
          }
          (&DAT_0076606c)[local_740 * 0x11] = 0;
          pcVar11 = "tail";
          do {
            pcVar11 = pcVar11 + 1;
          } while (*pcVar11 != '\0');
          iVar10 = (&DAT_007c2548)[local_740];
          iVar10 = FUN_00469050(iVar10,*(int *)(iVar10 + -4) + iVar10);
          if ((iVar10 != 0) && (iVar10 = FUN_00462dc0(), iVar10 == 1)) {
            pcVar11 = (char *)FUN_00423210();
            pcVar11[-0xffffffff00000004] = '\0';
            pcVar11[-0xffffffff00000003] = '\0';
            pcVar11[-0xffffffff00000002] = '\0';
            pcVar11[-0xffffffff00000001] = '\0';
            local_14 = 0x5a;
            FUN_0045a980();
            FUN_0045a8d0();
            FUN_00423690();
            pcVar11[*(int *)(pcVar11 + -4)] = '\0';
            iVar10 = __stricmp(local_6b0,pcVar11);
            if (iVar10 == 0) {
LAB_00464c3b:
              bVar2 = true;
            }
            else {
              iVar10 = __stricmp(local_6b0,"small");
              bVar2 = false;
              if (iVar10 == 0) goto LAB_00464c3b;
            }
            local_14 = 0xffffffff;
            if (pcVar11 != (char *)&DAT_006b9e28) {
              FUN_0059c360();
            }
            if (bVar2) {
              (&DAT_0076606c)[local_740 * 0x11] = (&DAT_0076606c)[local_740 * 0x11] | 1;
            }
            else {
              pcVar11 = (char *)FUN_00423210();
              pcVar11[-0xffffffff00000004] = '\0';
              pcVar11[-0xffffffff00000003] = '\0';
              pcVar11[-0xffffffff00000002] = '\0';
              pcVar11[-0xffffffff00000001] = '\0';
              local_14 = 0x7f;
              FUN_0045a980();
              FUN_0045a8d0();
              FUN_00423690();
              pcVar11[*(int *)(pcVar11 + -4)] = '\0';
              iVar10 = __stricmp(local_6b0,pcVar11);
              if (iVar10 == 0) {
LAB_00464d3e:
                bVar2 = true;
              }
              else {
                iVar10 = __stricmp(local_6b0,"medium");
                bVar2 = false;
                if (iVar10 == 0) goto LAB_00464d3e;
              }
              local_14 = 0xffffffff;
              FUN_004208e0();
              if (bVar2) {
                (&DAT_0076606c)[local_740 * 0x11] = (&DAT_0076606c)[local_740 * 0x11] | 2;
              }
              else {
                pcVar11 = (char *)FUN_00423210();
                pcVar11[-0xffffffff00000004] = '\0';
                pcVar11[-0xffffffff00000003] = '\0';
                pcVar11[-0xffffffff00000002] = '\0';
                pcVar11[-0xffffffff00000001] = '\0';
                local_14 = 0x92;
                FUN_0045a980();
                FUN_0045a8d0();
                FUN_00423690();
                pcVar11[*(int *)(pcVar11 + -4)] = '\0';
                iVar10 = __stricmp(local_6b0,pcVar11);
                if (iVar10 == 0) {
LAB_00464e20:
                  bVar2 = true;
                }
                else {
                  iVar10 = __stricmp(local_6b0,"large");
                  bVar2 = false;
                  if (iVar10 == 0) goto LAB_00464e20;
                }
                local_14 = 0xffffffff;
                FUN_004208e0();
                if (bVar2) {
                  (&DAT_0076606c)[local_740 * 0x11] = (&DAT_0076606c)[local_740 * 0x11] | 4;
                }
              }
            }
          }
          pcVar11 = "aura";
          do {
            pcVar11 = pcVar11 + 1;
          } while (*pcVar11 != '\0');
          iVar10 = (&DAT_007c2548)[local_740];
          iVar10 = FUN_00469050(iVar10,*(int *)(iVar10 + -4) + iVar10);
          if (iVar10 != 0) {
            iVar10 = FUN_00462dc0(iVar10,"%d %d %d %d",&local_6f4);
            if (iVar10 == 3) {
              local_6e0 = CONCAT13(0xff,(int3)CONCAT31(CONCAT21((short)local_6f4,local_6f0),
                                                       (undefined1)local_6ec));
              uVar21 = local_6e0;
            }
            else {
              if (iVar10 != 4) goto LAB_00464f46;
              uVar21 = CONCAT13(local_708,
                                (int3)CONCAT31(CONCAT21((short)local_6f4,local_6f0),
                                               (undefined1)local_6ec));
            }
            (&DAT_0076606c)[local_740 * 0x11] = (&DAT_0076606c)[local_740 * 0x11] | 8;
            (&DAT_00766074)[local_740 * 0x11] = uVar21;
          }
LAB_00464f46:
          pcVar11 = "aura2";
          do {
            pcVar11 = pcVar11 + 1;
          } while (*pcVar11 != '\0');
          iVar10 = (&DAT_007c2548)[local_740];
          iVar10 = FUN_00469050(iVar10,*(int *)(iVar10 + -4) + iVar10);
          if (iVar10 != 0) {
            iVar10 = FUN_00462dc0(iVar10,"%d %d %d %d",&local_6c0);
            if (iVar10 == 3) {
              local_73c = CONCAT13(0xff,(int3)CONCAT31(CONCAT21((short)local_6c0,
                                                                (undefined1)local_6e8),
                                                       local_6bc._0_1_));
            }
            else {
              if (iVar10 != 4) goto LAB_00465033;
              local_73c = CONCAT13(local_6f8,
                                   (int3)CONCAT31(CONCAT21((short)local_6c0,(undefined1)local_6e8),
                                                  local_6bc._0_1_));
            }
            (&DAT_0076606c)[local_740 * 0x11] = (&DAT_0076606c)[local_740 * 0x11] | 8;
            (&DAT_00766078)[local_740 * 0x11] = local_73c;
          }
LAB_00465033:
          pcVar11 = "aurascale";
          do {
            pcVar11 = pcVar11 + 1;
          } while (*pcVar11 != '\0');
          iVar10 = (&DAT_007c2548)[local_740];
          iVar10 = FUN_00469050(iVar10,*(int *)(iVar10 + -4) + iVar10);
          (&DAT_0076607c)[local_740 * 0x11] = 0x3f800000;
          if (iVar10 != 0) {
            (&DAT_0076606c)[local_740 * 0x11] = (&DAT_0076606c)[local_740 * 0x11] | 8;
            FUN_00462dc0(iVar10);
          }
          (&DAT_0076608c)[local_740 * 0x11] = 1;
          pcVar11 = "auramaterial";
          do {
            pcVar11 = pcVar11 + 1;
          } while (*pcVar11 != '\0');
          iVar10 = (&DAT_007c2548)[local_740];
          iVar10 = FUN_00469050(iVar10,*(int *)(iVar10 + -4) + iVar10);
          if (iVar10 != 0) {
            (&DAT_0076606c)[local_740 * 0x11] = (&DAT_0076606c)[local_740 * 0x11] | 8;
            FUN_00462dc0();
          }
          pcVar11 = "auracycle";
          do {
            pcVar11 = pcVar11 + 1;
          } while (*pcVar11 != '\0');
          iVar10 = (&DAT_007c2548)[local_740];
          iVar10 = FUN_00469050(iVar10,*(int *)(iVar10 + -4) + iVar10);
          (&DAT_00766084)[local_740 * 0x11] = 0x3a83126f;
          pfVar20 = (float *)(&DAT_00766084 + local_740 * 0x11);
          (&DAT_00766088)[local_740 * 0x11] = 1000;
          if (iVar10 != 0) {
            (&DAT_0076606c)[local_740 * 0x11] = (&DAT_0076606c)[local_740 * 0x11] | 8;
            iVar10 = FUN_00462dc0();
            if (iVar10 == 1) {
              *pfVar20 = *pfVar20 * DAT_006da884;
            }
            else {
              *pfVar20 = 0.001;
            }
            fVar1 = *pfVar20;
            local_6b8 = CONCAT44(fVar1,(undefined4)local_6b8);
            if (fVar1 != _DAT_006da830) {
              local_6b8 = (ulonglong)ROUND(1.0 / fVar1);
              (&DAT_00766088)[local_740 * 0x11] = (undefined4)local_6b8;
            }
          }
          pcVar11 = "auratype";
          uVar21 = 0x4651f9;
          FUN_00427430("auratype");
          FUN_00433ff0(puVar15);
          iVar10 = FUN_00469050(uVar21,pcVar11);
          if (iVar10 != 0) {
            _memset(local_260,0,300);
            FUN_00462dc0(iVar10,"%s %s %s");
            local_728 = local_260;
            local_6b8 = CONCAT44(3,(undefined4)local_6b8);
            do {
              FUN_00420fd0();
              local_14 = 0x93;
              FUN_0045a980();
              FUN_00459d90();
              pcVar11 = (char *)FUN_00462c90();
              iVar10 = __stricmp(local_728,pcVar11);
              local_14 = 0xffffffff;
              FUN_004208e0();
              if (iVar10 == 0) {
                (&DAT_0076606c)[local_740 * 0x11] = (&DAT_0076606c)[local_740 * 0x11] | 0x1000000;
              }
              else {
                FUN_00420fd0();
                local_14 = 0x94;
                FUN_0045a980();
                FUN_00459d90();
                pcVar11 = (char *)FUN_00462c90();
                iVar10 = __stricmp(local_728,pcVar11);
                local_14 = 0xffffffff;
                FUN_004208e0();
                if (iVar10 == 0) {
                  (&DAT_0076606c)[local_740 * 0x11] = (&DAT_0076606c)[local_740 * 0x11] | 0x2000000;
                }
                else {
                  FUN_00420fd0();
                  local_14 = 0x95;
                  FUN_0045a980();
                  FUN_00459d90();
                  pcVar11 = (char *)FUN_00462c90();
                  iVar10 = __stricmp(local_728,pcVar11);
                  local_14 = 0xffffffff;
                  FUN_004208e0();
                  if (iVar10 == 0) {
                    (&DAT_0076606c)[local_740 * 0x11] =
                         (&DAT_0076606c)[local_740 * 0x11] | 0x3000000;
                  }
                  else {
                    FUN_00420fd0();
                    local_14 = 0x96;
                    FUN_0045a980();
                    FUN_00459d90();
                    pcVar11 = (char *)FUN_00462c90();
                    iVar10 = __stricmp(local_728,pcVar11);
                    local_14 = 0xffffffff;
                    FUN_004208e0();
                    if (iVar10 == 0) {
                      (&DAT_0076606c)[local_740 * 0x11] =
                           (&DAT_0076606c)[local_740 * 0x11] | 0x4000000;
                    }
                    else {
                      FUN_00420fd0();
                      local_14 = 0x97;
                      FUN_0045a980();
                      FUN_00459d90();
                      pcVar11 = (char *)FUN_00462c90();
                      iVar10 = __stricmp(local_728,pcVar11);
                      local_14 = 0xffffffff;
                      FUN_004208e0();
                      if (iVar10 == 0) {
                        (&DAT_0076606c)[local_740 * 0x11] =
                             (&DAT_0076606c)[local_740 * 0x11] | 0x8000000;
                      }
                      else {
                        FUN_00420fd0();
                        local_14 = 0x98;
                        FUN_0045a980();
                        FUN_00459d90();
                        pcVar11 = (char *)FUN_00462c90();
                        iVar10 = __stricmp(local_728,pcVar11);
                        local_14 = 0xffffffff;
                        FUN_004208e0();
                        if (iVar10 == 0) {
                          (&DAT_0076606c)[local_740 * 0x11] =
                               (&DAT_0076606c)[local_740 * 0x11] | 0xc000000;
                        }
                        else {
                          FUN_00420fd0();
                          local_14 = 0x99;
                          FUN_0045a980();
                          FUN_00459d90();
                          pcVar11 = (char *)FUN_00462c90();
                          iVar10 = __stricmp(local_728,pcVar11);
                          local_14 = 0xffffffff;
                          FUN_004208e0();
                          if (iVar10 == 0) {
                            (&DAT_0076606c)[local_740 * 0x11] =
                                 (&DAT_0076606c)[local_740 * 0x11] | 0x10000000;
                          }
                          else {
                            FUN_00420fd0();
                            local_14 = 0x9a;
                            FUN_0045a980();
                            FUN_00459d90();
                            pcVar11 = (char *)FUN_00462c90();
                            iVar10 = __stricmp(local_728,pcVar11);
                            local_14 = 0xffffffff;
                            FUN_004208e0();
                            if (iVar10 == 0) {
                              (&DAT_0076606c)[local_740 * 0x11] =
                                   (&DAT_0076606c)[local_740 * 0x11] | 0x20000000;
                            }
                            else {
                              FUN_00420fd0();
                              local_14 = 0x9b;
                              FUN_0045a980();
                              FUN_00459d90();
                              pcVar11 = (char *)FUN_00462c90();
                              iVar10 = __stricmp(local_728,pcVar11);
                              local_14 = 0xffffffff;
                              FUN_004208e0();
                              if (iVar10 == 0) {
                                (&DAT_0076606c)[local_740 * 0x11] =
                                     (&DAT_0076606c)[local_740 * 0x11] | 0x30000000;
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
              local_728 = local_728 + 100;
              iVar10 = (int)local_6b8._4_4_ + -1;
              local_6b8 = CONCAT44(iVar10,(undefined4)local_6b8);
            } while (iVar10 != 0);
          }
          puVar12 = (undefined4 *)FUN_00435600(0xff);
          bVar2 = false;
          local_6d8 = *puVar12;
          local_6d4 = 0;
          pcVar11 = "lightcolor";
          local_6c8 = 0x3f800000;
          local_6c4 = 0x3f800000;
          local_6d0 = 1.0;
          local_6cc = 0x3f800000;
          uVar21 = 0x4657cd;
          FUN_00427430("lightcolor");
          FUN_00433ff0(puVar15);
          iVar10 = FUN_00469050(uVar21,pcVar11);
          if ((iVar10 != 0) && (iVar10 = FUN_00462dc0(iVar10,"%d %d %d"), iVar10 == 3)) {
            bVar2 = true;
            puVar12 = (undefined4 *)FUN_00435600(local_6fc);
            local_6d8 = *puVar12;
          }
          pcVar11 = "lighttype";
          uVar21 = 0x465847;
          FUN_00427430("lighttype");
          FUN_00433ff0(puVar15);
          iVar10 = FUN_00469050(uVar21,pcVar11);
          if (iVar10 != 0) {
            FUN_00462dc0(iVar10,"%s %f %f");
            local_6b8 = CONCAT44(DAT_0088a0f0,(undefined4)local_6b8);
            FUN_00420fd0();
            local_14 = 0x9c;
            FUN_0045a980();
            FUN_00459d90();
            pcVar11 = (char *)FUN_00462c90();
            iVar10 = __stricmp(local_6b0,pcVar11);
            local_14 = 0xffffffff;
            FUN_004208e0();
            if (iVar10 == 0) {
              local_6d4 = 5;
            }
            else {
              local_6b8 = CONCAT44(DAT_0088a0f8,(undefined4)local_6b8);
              FUN_00420fd0();
              local_14 = 0x9d;
              FUN_0045a980();
              FUN_00459d90();
              pcVar11 = (char *)FUN_00462c90();
              iVar10 = __stricmp(local_6b0,pcVar11);
              local_14 = 0xffffffff;
              FUN_004208e0();
              if (iVar10 == 0) {
                local_6d4 = 0;
              }
              else {
                local_6b8 = CONCAT44(DAT_0088a100,(undefined4)local_6b8);
                FUN_00420fd0();
                local_14 = 0x9e;
                FUN_0045a980();
                FUN_00459d90();
                pcVar11 = (char *)FUN_00462c90();
                iVar10 = __stricmp(local_6b0,pcVar11);
                local_14 = 0xffffffff;
                FUN_004208e0();
                if (iVar10 == 0) {
                  local_6d4 = 1;
                }
                else {
                  local_6b8 = CONCAT44(DAT_0088a108,(undefined4)local_6b8);
                  FUN_00420fd0();
                  local_14 = 0x9f;
                  FUN_0045a980();
                  FUN_00459d90();
                  pcVar11 = (char *)FUN_00462c90();
                  iVar10 = __stricmp(local_6b0,pcVar11);
                  local_14 = 0xffffffff;
                  FUN_004208e0();
                  if (iVar10 == 0) {
                    local_6d4 = 2;
                  }
                  else {
                    local_6b8 = CONCAT44(DAT_0088a110,(undefined4)local_6b8);
                    FUN_00420fd0();
                    local_14 = 0xa0;
                    FUN_0045a980();
                    FUN_00459d90();
                    pcVar11 = (char *)FUN_00462c90();
                    iVar10 = __stricmp(local_6b0,pcVar11);
                    local_14 = 0xffffffff;
                    FUN_004208e0();
                    if (iVar10 == 0) {
                      local_6d4 = 3;
                    }
                    else {
                      local_6b8 = CONCAT44(DAT_0088a118,(undefined4)local_6b8);
                      FUN_00420fd0();
                      local_14 = 0xa1;
                      FUN_0045a980();
                      FUN_00459d90();
                      pcVar11 = (char *)FUN_00462c90();
                      iVar10 = __stricmp(local_6b0,pcVar11);
                      local_14 = 0xffffffff;
                      FUN_004208e0();
                      if (iVar10 == 0) {
                        local_6d4 = 4;
                      }
                      else {
                        local_6b8 = CONCAT44(DAT_0088a120,(undefined4)local_6b8);
                        FUN_00420fd0();
                        local_14 = 0xa2;
                        FUN_0045a980();
                        FUN_00459d90();
                        pcVar11 = (char *)FUN_00462c90();
                        iVar10 = __stricmp(local_6b0,pcVar11);
                        local_14 = 0xffffffff;
                        FUN_004208e0();
                        if (iVar10 == 0) {
                          local_6d4 = 6;
                        }
                      }
                    }
                  }
                }
              }
            }
            bVar2 = true;
          }
          pcVar11 = "lightsize";
          uVar21 = 0x465c4f;
          FUN_00427430("lightsize");
          FUN_00433ff0(puVar15);
          iVar10 = FUN_00469050(uVar21,pcVar11);
          if (iVar10 != 0) {
            local_6b8 = CONCAT44(0x40400000,(undefined4)local_6b8);
            iVar10 = FUN_00462dc0();
            if (iVar10 == 1) {
              local_6d0 = local_6b8._4_4_;
              if (local_6b8._4_4_ < 0.0) {
                local_6d4 = local_6d4 | 0x80;
                local_6d0 = (float)((uint)local_6b8._4_4_ ^ DAT_006db4a0);
              }
              bVar2 = true;
            }
          }
          pcVar11 = "lightpillar";
          uVar21 = 0x465cc3;
          FUN_00427430("lightpillar");
          FUN_00433ff0(puVar15);
          iVar10 = FUN_00469050(uVar21,pcVar11);
          if (iVar10 != 0) {
            local_6b8 = local_6b8 & 0xffffffff;
            iVar10 = FUN_00462dc0();
            if (iVar10 == 1) {
              if (local_6b8._4_4_ != 0.0) {
                local_6d4 = local_6d4 | 0x80;
              }
              bVar2 = true;
            }
          }
          puVar22 = &stack0xfffff760;
          uVar21 = 0x465d1d;
          FUN_0046a020(&stack0xfffff760);
          FUN_00433ff0(puVar15);
          iVar10 = FUN_00469050(uVar21,puVar22);
          if (iVar10 != 0) {
            local_6b8 = local_6b8 & 0xffffffff;
            iVar10 = FUN_00462dc0();
            if (iVar10 == 1) {
              if (local_6b8._4_4_ != 0.0) {
                local_6d4 = local_6d4 | 0x20;
              }
              bVar2 = true;
            }
          }
          pcVar11 = "lighttime";
          uVar21 = 0x465d7b;
          FUN_00427430("lighttime");
          FUN_00433ff0(puVar15);
          iVar10 = FUN_00469050(uVar21,pcVar11);
          if (((iVar10 != 0) && (iVar10 = FUN_00462dc0(), iVar10 == 1)) || (bVar2)) {
            FUN_0045e650();
          }
        }
        bVar4 = 0;
        bVar2 = false;
        local_740 = local_740 + 1;
      } while (local_740 < 0x2b5);
      local_6dc = 0x3f800000;
      local_73c = 0;
      do {
        FUN_004355f0();
        FUN_00427430();
        uVar21 = local_6e0;
        iVar10 = FUN_00468d70();
        if (iVar10 != 0) {
          iVar16 = local_73c * 0x10;
          *(uint *)(&DAT_007c3020 + iVar16) = 1;
          FUN_0046a050(&stack0xfffff760);
          iVar10 = FUN_00469050(local_6e4,uVar21);
          if (iVar10 != 0) {
            local_6bc = (float *)0x0;
            iVar10 = FUN_00462dc0(iVar10,"%d %s %d");
            if (0 < iVar10) {
              if ((local_6b8._4_4_ == 0.0) ||
                 (uVar17 = (uint)local_6b8._4_4_, 0xff < (uint)local_6b8._4_4_)) {
                uVar17 = 1;
                local_6b8 = CONCAT44(1,(undefined4)local_6b8);
              }
              *(uint *)(&DAT_007c3020 + iVar16) = uVar17;
              if (1 < iVar10) {
                iVar13 = __stricmp(local_2c8,"sync");
                uVar8 = 0;
                if (iVar13 != 0) {
                  iVar13 = __stricmp(local_2c8,"location");
                  if (iVar13 == 0) {
                    uVar8 = 1;
                  }
                  else {
                    iVar13 = __stricmp(local_2c8,"sequence");
                    if (iVar13 == 0) {
                      uVar8 = 2;
                    }
                    else {
                      iVar13 = __stricmp(local_2c8,"transform");
                      if (iVar13 == 0) {
                        uVar8 = 3;
                      }
                      else {
                        __stricmp(local_2c8,"respective");
                        uVar8 = 4;
                      }
                    }
                  }
                }
                *(undefined2 *)(&DAT_007c3024 + iVar16) = uVar8;
                if (2 < iVar10) {
                  *(undefined2 *)(&DAT_007c3026 + iVar16) = local_6bc._0_2_;
                }
              }
            }
          }
          uVar17 = 0;
          if (*(int *)(&DAT_007c3020 + iVar16) != 0) {
            do {
              FUN_00427430("missile");
              iVar10 = FUN_00469050(local_6e4,local_6e0);
              if (iVar10 == 0) {
                FUN_00427430("explosion");
                iVar10 = FUN_00469050(local_6e4,local_6e0);
                if (iVar10 == 0) {
                  FUN_00427430("missilemove");
                  iVar10 = FUN_00469050(local_6e4,local_6e0);
                  if (iVar10 == 0) break;
                }
              }
              uVar17 = uVar17 + 1;
            } while ((uVar17 & 0xffff) < *(uint *)(&DAT_007c3020 + iVar16));
          }
          FUN_0046a3c0();
          local_6f4 = *(uint *)(&DAT_007c3028 + iVar16);
          local_6ec = 0;
          if (local_6f4 != 0) {
            do {
              uVar17 = local_6ec;
              _Dst = (uint *)FUN_00444680();
              _memset(_Dst,0xff,0x4c);
              if ((short)uVar17 == 0) {
                _memset(_Dst,0xff,0x4c);
              }
              else {
                puVar14 = (uint *)FUN_00444680();
                puVar18 = _Dst;
                for (iVar10 = 0x13; iVar10 != 0; iVar10 = iVar10 + -1) {
                  *puVar18 = *puVar14;
                  puVar14 = puVar14 + 1;
                  puVar18 = puVar18 + 1;
                }
              }
              _Dst[0xc] = 0x3f800000;
              FUN_00427430("missile");
              iVar10 = FUN_00469050(local_6e4,local_6e0);
              if (iVar10 == 0) goto LAB_0046727f;
              iVar10 = FUN_00462dc0(iVar10,"%s %s %f");
              if (0 < iVar10) {
                iVar16 = __stricmp(&local_130,"NULL");
                if (iVar16 != 0) {
                  uVar17 = 0;
                  local_6bc = (float *)&DAT_007c2548;
                  do {
                    FUN_00433ff0();
                    FUN_00427430();
                    cVar5 = FUN_00469dc0();
                    if (cVar5 != '\0') {
                      *_Dst = uVar17;
                      break;
                    }
                    uVar17 = uVar17 + 1;
                    local_6bc = local_6bc + 1;
                  } while (uVar17 < 0x2b5);
                }
                if (1 < iVar10) {
                  FUN_00427430();
                  uVar17 = FUN_005920c0();
                  _Dst[1] = uVar17;
                  if (iVar10 == 3) {
                    _Dst[0xc] = local_6dc;
                  }
                }
              }
              FUN_00427430("explosion");
              iVar10 = FUN_00469050(local_6e4,local_6e0);
              if (iVar10 == 0) goto LAB_0046727f;
              iVar10 = FUN_00462dc0(iVar10);
              if (0 < iVar10) {
                iVar16 = __stricmp(&local_130,"NULL");
                if (iVar16 != 0) {
                  uVar17 = 0;
                  do {
                    FUN_00427430();
                    cVar5 = FUN_00469c60();
                    if (cVar5 != '\0') {
                      _Dst[2] = uVar17;
                      break;
                    }
                    uVar17 = uVar17 + 1;
                  } while (uVar17 < 0x2b5);
                }
                if (iVar10 == 2) {
                  FUN_00427430();
                  uVar17 = FUN_005920c0();
                  _Dst[3] = uVar17;
                }
              }
              pfVar20 = (float *)(_Dst + 0xb);
              *pfVar20 = 6.2831855;
              FUN_0046a080(&stack0xfffff760);
              iVar10 = FUN_00469050(local_6e4,local_6e0);
              if (iVar10 != 0) {
                FUN_00462dc0();
                *pfVar20 = *pfVar20 * _DAT_006da8cc;
              }
              *(undefined2 *)((int)_Dst + 0x2a) = 0;
              FUN_00427430("gxname");
              iVar10 = FUN_00469050(local_6e4,local_6e0);
              if ((iVar10 != 0) && (iVar10 = FUN_00462dc0(), iVar10 == 1)) {
                uVar17 = 0;
                do {
                  FUN_00427430();
                  FUN_00433ff0();
                  cVar5 = FUN_00469dc0();
                  if (cVar5 != '\0') {
                    iVar10 = FUN_00431b20();
                    if (iVar10 != 0) {
                      local_6e8 = 0;
                      local_6bc = (float *)0x0;
                      FUN_00469ac0();
                      *(short *)((int)_Dst + 0x2a) = ((short)local_6bc - (short)local_6e8) * 0x21;
                    }
                    break;
                  }
                  uVar17 = uVar17 + 1;
                } while (uVar17 < 0x2b5);
              }
              *(undefined2 *)(_Dst + 10) = 1;
              FUN_00427430("missilecount");
              iVar10 = FUN_00469050(local_6e4,local_6e0);
              if ((iVar10 != 0) && (iVar10 = FUN_00462dc0(), 0 < iVar10)) {
                if ((local_6c0 == 0) || (0xff < local_6c0)) {
                  local_6c0 = 1;
                }
                *(short *)(_Dst + 10) = (short)local_6c0;
              }
              puVar14 = (uint *)FUN_00435600(0xff);
              bVar3 = false;
              _Dst[4] = *puVar14;
              *(undefined1 *)(_Dst + 5) = 0;
              _Dst[8] = 0x3f800000;
              _Dst[9] = 0x3f800000;
              _Dst[6] = 0x40400000;
              _Dst[7] = 0x3e4ccccd;
              FUN_00427430("lightcolor");
              iVar10 = FUN_00469050(local_6e4,local_6e0);
              if ((iVar10 != 0) && (iVar10 = FUN_00462dc0(iVar10,"%d %d %d"), iVar10 == 3)) {
                bVar3 = true;
                puVar14 = (uint *)FUN_00435600(local_70c);
                _Dst[4] = *puVar14;
              }
              FUN_00427430("lighttype");
              iVar10 = FUN_00469050(local_6e4,local_6e0);
              if (iVar10 != 0) {
                bVar3 = true;
                FUN_00462dc0(iVar10,"%s %f %f");
                iVar10 = __stricmp(local_6b0,&DAT_006bf57c);
                if (iVar10 == 0) {
                  *(undefined1 *)(_Dst + 5) = 5;
                }
                else {
                  iVar10 = __stricmp(local_6b0,&DAT_006bf584);
                  if (iVar10 == 0) {
                    *(undefined1 *)(_Dst + 5) = 0;
                  }
                  else {
                    iVar10 = __stricmp(local_6b0,&DAT_006bf58c);
                    if (iVar10 == 0) {
                      *(undefined1 *)(_Dst + 5) = 1;
                    }
                    else {
                      iVar10 = __stricmp(local_6b0,&DAT_006bf598);
                      if (iVar10 == 0) {
                        *(undefined1 *)(_Dst + 5) = 2;
                      }
                      else {
                        iVar10 = __stricmp(local_6b0,&DAT_006bf5a4);
                        if (iVar10 == 0) {
                          *(undefined1 *)(_Dst + 5) = 3;
                        }
                        else {
                          iVar10 = __stricmp(local_6b0,&DAT_006bf5b0);
                          if (iVar10 == 0) {
                            *(undefined1 *)(_Dst + 5) = 4;
                          }
                          else {
                            iVar10 = __stricmp(local_6b0,&DAT_006bf5bc);
                            if (iVar10 == 0) {
                              *(undefined1 *)(_Dst + 5) = 6;
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
              FUN_00427430("lightsize");
              iVar10 = FUN_00469050(local_6e4,local_6e0);
              if (iVar10 != 0) {
                local_6bc = (float *)0x40400000;
                iVar10 = FUN_00462dc0();
                if (iVar10 == 1) {
                  pfVar20 = local_6bc;
                  if ((float)local_6bc < 0.0) {
                    *(byte *)(_Dst + 5) = (byte)_Dst[5] | 0x80;
                    pfVar20 = (float *)((uint)local_6bc ^ DAT_006db4a0);
                  }
                  _Dst[6] = (uint)pfVar20;
                  bVar3 = true;
                }
              }
              FUN_00427430("lighttime");
              iVar10 = FUN_00469050(local_6e4,local_6e0);
              if (((iVar10 == 0) || (iVar10 = FUN_00462dc0(), iVar10 != 1)) && (!bVar3)) {
                _Dst[6] = 0;
              }
              pfVar20 = (float *)(_Dst + 0xf);
              *(undefined2 *)(_Dst + 0xd) = 2;
              *(undefined1 *)((int)_Dst + 0x36) = 0;
              *pfVar20 = 1.0;
              _Dst[0x10] = 0x3f800000;
              _Dst[0x11] = 0x3f800000;
              _Dst[0xe] = 0x42700000;
              local_6bc = pfVar20;
              FUN_00427430("missilemove");
              iVar10 = FUN_00469050(local_6e4,local_6e0);
              if ((iVar10 != 0) && (iVar10 = FUN_00462dc0(iVar10), 0 < iVar10)) {
                FUN_00420fd0();
                local_14 = 0xa3;
                bVar6 = bVar4 | 8;
                FUN_0045a980();
                FUN_00459d90();
                pcVar11 = (char *)FUN_00462c90();
                iVar16 = __stricmp(local_238,pcVar11);
                if (iVar16 == 0) {
LAB_00466804:
                  bVar3 = true;
                }
                else {
                  FUN_00420fd0();
                  local_14 = 0xa4;
                  bVar6 = bVar4 | 0x18;
                  FUN_0045a980();
                  FUN_00459d90();
                  pcVar11 = (char *)FUN_00462c90();
                  iVar16 = __stricmp(local_238,pcVar11);
                  bVar3 = false;
                  if (iVar16 == 0) goto LAB_00466804;
                }
                local_14 = 0xa3;
                if ((bVar6 & 0x10) != 0) {
                  bVar6 = bVar6 & 0xef;
                  FUN_004208e0();
                }
                local_14 = 0xffffffff;
                if ((bVar6 & 8) != 0) {
                  bVar6 = bVar6 & 0xf7;
                  FUN_004208e0();
                }
                if (bVar3) {
                  *(undefined1 *)(_Dst + 0xd) = 0;
                }
                else {
                  FUN_00420fd0();
                  local_14 = 0xa5;
                  FUN_0045a980();
                  FUN_00459d90();
                  pcVar11 = (char *)FUN_00462c90();
                  iVar16 = __stricmp(local_238,pcVar11);
                  local_14 = 0xffffffff;
                  FUN_004208e0();
                  if (iVar16 == 0) {
                    *(undefined1 *)(_Dst + 0xd) = 1;
                  }
                  else {
                    FUN_00420fd0();
                    local_14 = 0xa6;
                    FUN_0045a980();
                    FUN_00459d90();
                    pcVar11 = (char *)FUN_00462c90();
                    iVar16 = __stricmp(local_238,pcVar11);
                    local_14 = 0xffffffff;
                    FUN_004208e0();
                    if (iVar16 == 0) {
                      *(undefined1 *)(_Dst + 0xd) = 2;
                    }
                    else {
                      FUN_00420fd0();
                      local_14 = 0xa7;
                      FUN_0045a980();
                      FUN_00459d90();
                      pcVar11 = (char *)FUN_00462c90();
                      iVar16 = __stricmp(local_238,pcVar11);
                      local_14 = 0xffffffff;
                      FUN_004208e0();
                      if (iVar16 == 0) {
                        *(undefined1 *)(_Dst + 0xd) = 3;
                      }
                      else {
                        FUN_00420fd0();
                        local_14 = 0xa8;
                        FUN_0045a980();
                        FUN_00459d90();
                        pcVar11 = (char *)FUN_00462c90();
                        iVar16 = __stricmp(local_238,pcVar11);
                        local_14 = 0xffffffff;
                        FUN_004208e0();
                        if (iVar16 == 0) {
                          *(undefined1 *)(_Dst + 0xd) = 4;
                        }
                        else {
                          FUN_00420fd0();
                          local_14 = 0xa9;
                          FUN_0045a980();
                          FUN_00459d90();
                          pcVar11 = (char *)FUN_00462c90();
                          iVar16 = __stricmp(local_238,pcVar11);
                          local_14 = 0xffffffff;
                          FUN_004208e0();
                          if (iVar16 == 0) {
                            *(undefined1 *)(_Dst + 0xd) = 5;
                          }
                          else {
                            FUN_00420fd0();
                            local_14 = 0xaa;
                            FUN_0045a980();
                            FUN_00459d90();
                            pcVar11 = (char *)FUN_00462c90();
                            iVar16 = __stricmp(local_238,pcVar11);
                            local_14 = 0xffffffff;
                            FUN_004208e0();
                            if (iVar16 == 0) {
                              *(undefined1 *)(_Dst + 0xd) = 6;
                            }
                            else {
                              FUN_00420fd0();
                              local_14 = 0xab;
                              FUN_0045a980();
                              FUN_00459d90();
                              pcVar11 = (char *)FUN_00462c90();
                              iVar16 = __stricmp(local_238,pcVar11);
                              local_14 = 0xffffffff;
                              FUN_004208e0();
                              if (iVar16 == 0) {
                                *(undefined1 *)(_Dst + 0xd) = 7;
                              }
                              else {
                                FUN_00420fd0();
                                local_14 = 0xac;
                                FUN_0045a980();
                                FUN_00459d90();
                                pcVar11 = (char *)FUN_00462c90();
                                iVar16 = __stricmp(local_238,pcVar11);
                                local_14 = 0xffffffff;
                                FUN_004208e0();
                                if (iVar16 == 0) {
                                  *(undefined1 *)(_Dst + 0xd) = 8;
                                }
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
                bVar4 = bVar6;
                if (1 < iVar10) {
                  FUN_00420fd0();
                  local_14 = 0xad;
                  FUN_0045a980();
                  FUN_00459d90();
                  pcVar11 = (char *)FUN_00462c90();
                  iVar10 = __stricmp(&local_130,pcVar11);
                  local_14 = 0xffffffff;
                  FUN_004208e0();
                  if (iVar10 == 0) {
                    *(undefined1 *)((int)_Dst + 0x35) = 1;
                  }
                  else {
                    FUN_00420fd0();
                    local_14 = 0xae;
                    bVar7 = bVar6 | 0x20;
                    FUN_0045a980();
                    FUN_00459d90();
                    pcVar11 = (char *)FUN_00462c90();
                    iVar10 = __stricmp(&local_130,pcVar11);
                    if (iVar10 == 0) {
LAB_00466f2f:
                      bVar3 = true;
                    }
                    else {
                      FUN_00420fd0();
                      local_14 = 0xaf;
                      bVar7 = bVar6 | 0x60;
                      FUN_0045a980();
                      FUN_00459d90();
                      pcVar11 = (char *)FUN_00462c90();
                      iVar10 = __stricmp(&local_130,pcVar11);
                      bVar3 = false;
                      if (iVar10 == 0) goto LAB_00466f2f;
                    }
                    local_14 = 0xae;
                    if ((bVar7 & 0x40) != 0) {
                      bVar7 = bVar7 & 0xbf;
                      FUN_004208e0();
                    }
                    local_14 = 0xffffffff;
                    if ((bVar7 & 0x20) != 0) {
                      bVar7 = bVar7 & 0xdf;
                      FUN_004208e0();
                    }
                    bVar4 = bVar7;
                    if (bVar3) {
                      *(undefined1 *)((int)_Dst + 0x35) = 2;
                    }
                    else {
                      FUN_00420fd0();
                      local_14 = 0xb0;
                      FUN_0045a980();
                      FUN_00459d90();
                      pcVar11 = (char *)FUN_00462c90();
                      iVar10 = __stricmp(&local_130,pcVar11);
                      local_14 = 0xffffffff;
                      FUN_004208e0();
                      if (iVar10 == 0) {
                        *(undefined1 *)((int)_Dst + 0x35) = 3;
                      }
                      else {
                        FUN_00420fd0();
                        local_14 = 0xb1;
                        FUN_0045a980();
                        FUN_00459d90();
                        pcVar11 = (char *)FUN_00462c90();
                        iVar10 = __stricmp(&local_130,pcVar11);
                        if (iVar10 == 0) {
LAB_004670f0:
                          bVar3 = true;
                        }
                        else {
                          FUN_00420fd0();
                          local_14 = 0xb2;
                          bVar2 = true;
                          FUN_0045a980();
                          FUN_00459d90();
                          pcVar11 = (char *)FUN_00462c90();
                          iVar10 = __stricmp(&local_130,pcVar11);
                          bVar3 = false;
                          if (iVar10 == 0) goto LAB_004670f0;
                        }
                        bVar4 = bVar7 | 0x80;
                        local_14 = 0xb1;
                        if (bVar2) {
                          bVar2 = false;
                          FUN_004208e0();
                        }
                        local_14 = 0xffffffff;
                        if ((char)bVar4 < '\0') {
                          bVar4 = bVar7 & 0x7f;
                          FUN_004208e0();
                        }
                        if (bVar3) {
                          *(undefined1 *)((int)_Dst + 0x35) = 4;
                        }
                        else {
                          FUN_00420fd0();
                          local_14 = 0xb3;
                          FUN_0045a980();
                          FUN_00459d90();
                          pcVar11 = (char *)FUN_00462c90();
                          iVar10 = __stricmp(&local_130,pcVar11);
                          local_14 = 0xffffffff;
                          FUN_004208e0();
                          if (iVar10 == 0) {
                            *(undefined1 *)((int)_Dst + 0x35) = 5;
                          }
                          else {
                            FUN_00420fd0();
                            local_14 = 0xb4;
                            FUN_0045a980();
                            FUN_00459d90();
                            pcVar11 = (char *)FUN_00462c90();
                            iVar10 = __stricmp(&local_130,pcVar11);
                            local_14 = 0xffffffff;
                            FUN_004208e0();
                            pfVar20 = local_6bc;
                            if (iVar10 != 0) goto LAB_00466d48;
                            *(undefined1 *)((int)_Dst + 0x35) = 7;
                          }
                        }
                      }
                    }
                  }
                }
                pfVar20 = (float *)(_Dst + 0xf);
              }
LAB_00466d48:
              FUN_00427430("missilespeed");
              iVar10 = FUN_00469050(local_6e4,local_6e0);
              if (iVar10 != 0) {
                FUN_00462dc0();
              }
              FUN_00427430("missileparam");
              iVar10 = FUN_00469050(local_6e4,local_6e0);
              if (iVar10 != 0) {
                FUN_00462dc0(iVar10,"%f %f %f");
              }
              if ((char)_Dst[0xd] == '\b') {
                fVar19 = (float10)fptan((float10)*pfVar20 * (float10)_DAT_006da8b0 *
                                        (float10)DAT_006dac00);
                *pfVar20 = (float)fVar19;
              }
              _Dst[0x12] = 0;
              FUN_00427430("magazine");
              iVar10 = FUN_00469050(local_6e4,local_6e0);
              if (iVar10 != 0) {
                FUN_00462dc0();
              }
              local_6ec = local_6ec + 1;
            } while ((local_6ec & 0xffff) < local_6f4);
          }
        }
        local_73c = local_73c + 1;
      } while (local_73c < 0x62);
    }
  }
LAB_0046727f:
  ExceptionList = local_1c;
  __security_check_cookie(local_24 ^ (uint)&stack0xfffffff0);
  return;
}


```

