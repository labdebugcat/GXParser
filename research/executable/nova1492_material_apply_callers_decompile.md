# Selected Nova1492 Decompilation

## `0042c245`

- Function: `FUN_0042c0a0`
- Entry: `0042c0a0`

```c

void __thiscall FUN_0042c0a0(int param_1,undefined4 param_2,undefined4 param_3,char param_4)

{
  uint uVar1;
  int *piVar2;
  undefined4 *puVar3;
  uint uVar4;
  int iVar5;
  uint *puVar6;
  int iVar7;
  undefined4 uVar8;
  undefined1 auStack_88 [4];
  uint uStack_84;
  int iStack_80;
  int *piStack_7c;
  uint *puStack_78;
  int local_74;
  int iStack_70;
  undefined4 uStack_6c;
  uint uStack_68;
  int *piStack_64;
  undefined1 local_60 [76];
  uint local_14;
  
  local_14 = DAT_007360c8 ^ (uint)auStack_88;
  local_74 = param_1;
  if (*(char *)(param_1 + 0x20113) != '\0') {
    FUN_00459580(param_3,0);
    FUN_0045aa00(local_60);
    (**(code **)(*DAT_007848dc + 0xb0))(DAT_007848dc,3,local_60);
    *(undefined4 *)(param_1 + 0x20134) = 0;
    iStack_80 = 0;
    do {
      iVar7 = iStack_80;
      iVar5 = *(int *)(*(int *)(param_1 + 0x200f0 + iStack_80 * 4) + -4);
      if (iVar5 != 0) {
        *(int *)(param_1 + 0x20134) = *(int *)(param_1 + 0x20134) + iVar5;
        if (iStack_80 == 0) {
          if (*(char *)(param_1 + 0x20244) != '\x01') {
            *(undefined1 *)(param_1 + 0x20244) = 1;
            (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0xe,1);
          }
          if (*(char *)(param_1 + 0x20108) == '\0') goto LAB_0042c209;
          uVar8 = 2;
LAB_0042c20b:
          FUN_00431bf0(uVar8,0);
        }
        else {
          if (iStack_80 == 1) {
            if ((((DAT_0078443c == '\0') || (DAT_00761cd0 == 0)) ||
                (*(int *)(DAT_00761cd0 + 0x20) != 6)) &&
               (FUN_0042cf70(), *(char *)(param_1 + 0x20250) != '\0')) {
              FUN_00431bf0(1,0);
              *(undefined1 *)(param_1 + 0x20250) = 0;
              *(undefined2 *)(param_1 + 0x20244) = 0x101;
            }
            if (*(char *)(param_1 + 0x20244) != '\x01') {
              *(undefined1 *)(param_1 + 0x20244) = 1;
              (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))
                        (*(int **)(param_1 + 0x205ac),0xe,1);
            }
            if (*(char *)(param_1 + 0x20108) != '\0') {
              uVar8 = 2;
              goto LAB_0042c20b;
            }
LAB_0042c209:
            uVar8 = 5;
            goto LAB_0042c20b;
          }
          if (iStack_80 == 2) {
            if (param_4 == '\0') {
              FUN_00446870();
            }
            if (*(char *)(param_1 + 0x2010d) == '\0') {
              FUN_0042b98b(0);
            }
            goto LAB_0042c209;
          }
        }
        piStack_7c = *(int **)(param_1 + 0x200f0 + iVar7 * 4);
        piStack_64 = piStack_7c + piStack_7c[-1] * 2;
        if (piStack_7c != piStack_64) {
          do {
            iVar5 = piStack_7c[1];
            if (iVar5 == 0) {
              if (*(char *)(param_1 + 0x20246) != '\0') {
                *(undefined1 *)(param_1 + 0x20246) = 0;
                (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))
                          (*(int **)(param_1 + 0x205ac),0x1b,0);
              }
              *(undefined4 *)(param_1 + 0x201ec) = 0;
              (**(code **)(**(int **)(param_1 + 0x205ac) + 0x104))(*(int **)(param_1 + 0x205ac),0,0)
              ;
            }
            else if ((iVar7 == 2) && (*(char *)(iVar5 + 4) != '\0')) {
              FUN_004618a0(1,iVar5);
            }
            else {
              FUN_004618a0(2,iVar5);
            }
            DAT_00736c70 = FUN_00428940(DAT_00736c5c,&DAT_00736c64);
            DAT_00736c68 = 0;
            puVar6 = (uint *)*piStack_7c;
            puStack_78 = puVar6 + puVar6[-1] * 6;
            if (puVar6 != puStack_78) {
              do {
                uStack_84 = *puVar6;
                if ((uStack_84 & 8) == 0) {
                  if ((*(char *)(param_1 + 0x20108) == '\0') ||
                     ((iStack_80 != 0 && (iStack_80 != 1)))) {
                    *puVar6 = uStack_84 | 1;
LAB_0042c385:
                    FUN_0042ba63(puVar6,puVar6[2]);
                    param_1 = local_74;
                  }
                  else if ((uStack_84 & 2) == 0) {
                    if ((param_4 == '\0') && (((uint *)puVar6[1])[3] != 0)) {
                      uVar1 = puVar6[3];
                      uVar4 = *(uint *)puVar6[1];
                      if ((*(byte *)(uVar1 + 0x10) & 4) == 0) {
                        if (*(int *)(uVar1 + 0x14) == 0) goto LAB_0042c36b;
                        iVar5 = *(int *)(*(int *)(uVar1 + 0x14) + 0x14);
                      }
                      else {
                        if (*(uint *)(uVar1 + 4) <= uVar4) {
                          uVar4 = *(uint *)(uVar1 + 4) - 1;
                        }
                        iVar5 = *(int *)(*(int *)(*(int *)(uVar1 + 8) + uVar4 * 4) * 0x94 + 0x14 +
                                        *(int *)(uVar1 + 0x14));
                      }
                      if (iVar5 != 0) goto LAB_0042c385;
                    }
LAB_0042c36b:
                    *puVar6 = uStack_84 | 1;
                    FUN_0042ba63(puVar6,puVar6[2] << 0x18);
                    param_1 = local_74;
                  }
                  else {
                    *puVar6 = uStack_84 | 1;
                    FUN_0042ba63(puVar6,*(undefined4 *)(puVar6[1] + 8));
                    param_1 = local_74;
                  }
                }
                else if (*(undefined ***)puVar6[1] != G3DESelectMark::vftable) {
                  (*(code *)(*(undefined ***)puVar6[1])[4])(puVar6[2]);
                }
                puVar6 = puVar6 + 6;
              } while (puVar6 != puStack_78);
            }
            puVar3 = DAT_00736c54;
            if (DAT_00736c70 != 0) {
              if (((*(char *)(DAT_00736c54 + 0xd) != '\0') &&
                  (*(char *)((int)DAT_00736c54 + 0x35) != '\0')) &&
                 (piVar2 = (int *)DAT_00736c54[3], piVar2 != (int *)0x0)) {
                (**(code **)(*piVar2 + 0x30))(piVar2);
                *(undefined1 *)((int)puVar3 + 0x35) = 0;
              }
              DAT_00736c70 = 0;
            }
            iVar5 = DAT_00736c64;
            if (DAT_00736c64 != 0) {
              uStack_6c = DAT_00736c58;
              iStack_70 = DAT_00736c54[2];
              uStack_68 = DAT_00736c68 / 3;
              puStack_78 = (uint *)*DAT_00736c54;
              uStack_84 = DAT_00736c74 * iStack_70 + DAT_00736c54[0xc];
              if ((uStack_84 != 0) && (DAT_00736c64 != 0)) {
                if (DAT_00785098 != puStack_78) {
                  (**(code **)(*DAT_007848dc + 0x164))(DAT_007848dc,puStack_78);
                  DAT_00785098 = puStack_78;
                }
                (**(code **)(*DAT_007848dc + 0x150))
                          (DAT_007848dc,4,0,iVar5,uStack_68,uStack_6c,0x65,uStack_84,iStack_70);
                DAT_00785094 = 0;
                DAT_00785090 = 0;
              }
            }
            piStack_7c = piStack_7c + 2;
            iVar7 = iStack_80;
          } while (piStack_7c != piStack_64);
        }
      }
      iStack_80 = iVar7 + 1;
    } while (iStack_80 < 3);
    if (*(char *)(param_1 + 0x20244) != '\x01') {
      *(undefined1 *)(param_1 + 0x20244) = 1;
      (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0xe,1);
    }
    FUN_00431bf0(5,0);
    FUN_00431490();
    if (DAT_00784570 != 1) {
      DAT_00784570 = 1;
      (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x13,5);
      (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x14,6);
    }
    FUN_00470fc0();
  }
  __security_check_cookie(local_14 ^ (uint)auStack_88);
  return;
}


```

## `0042c24f`

- Function: `FUN_0042c0a0`
- Entry: `0042c0a0`

```c

void __thiscall FUN_0042c0a0(int param_1,undefined4 param_2,undefined4 param_3,char param_4)

{
  uint uVar1;
  int *piVar2;
  undefined4 *puVar3;
  uint uVar4;
  int iVar5;
  uint *puVar6;
  int iVar7;
  undefined4 uVar8;
  undefined1 auStack_88 [4];
  uint uStack_84;
  int iStack_80;
  int *piStack_7c;
  uint *puStack_78;
  int local_74;
  int iStack_70;
  undefined4 uStack_6c;
  uint uStack_68;
  int *piStack_64;
  undefined1 local_60 [76];
  uint local_14;
  
  local_14 = DAT_007360c8 ^ (uint)auStack_88;
  local_74 = param_1;
  if (*(char *)(param_1 + 0x20113) != '\0') {
    FUN_00459580(param_3,0);
    FUN_0045aa00(local_60);
    (**(code **)(*DAT_007848dc + 0xb0))(DAT_007848dc,3,local_60);
    *(undefined4 *)(param_1 + 0x20134) = 0;
    iStack_80 = 0;
    do {
      iVar7 = iStack_80;
      iVar5 = *(int *)(*(int *)(param_1 + 0x200f0 + iStack_80 * 4) + -4);
      if (iVar5 != 0) {
        *(int *)(param_1 + 0x20134) = *(int *)(param_1 + 0x20134) + iVar5;
        if (iStack_80 == 0) {
          if (*(char *)(param_1 + 0x20244) != '\x01') {
            *(undefined1 *)(param_1 + 0x20244) = 1;
            (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0xe,1);
          }
          if (*(char *)(param_1 + 0x20108) == '\0') goto LAB_0042c209;
          uVar8 = 2;
LAB_0042c20b:
          FUN_00431bf0(uVar8,0);
        }
        else {
          if (iStack_80 == 1) {
            if ((((DAT_0078443c == '\0') || (DAT_00761cd0 == 0)) ||
                (*(int *)(DAT_00761cd0 + 0x20) != 6)) &&
               (FUN_0042cf70(), *(char *)(param_1 + 0x20250) != '\0')) {
              FUN_00431bf0(1,0);
              *(undefined1 *)(param_1 + 0x20250) = 0;
              *(undefined2 *)(param_1 + 0x20244) = 0x101;
            }
            if (*(char *)(param_1 + 0x20244) != '\x01') {
              *(undefined1 *)(param_1 + 0x20244) = 1;
              (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))
                        (*(int **)(param_1 + 0x205ac),0xe,1);
            }
            if (*(char *)(param_1 + 0x20108) != '\0') {
              uVar8 = 2;
              goto LAB_0042c20b;
            }
LAB_0042c209:
            uVar8 = 5;
            goto LAB_0042c20b;
          }
          if (iStack_80 == 2) {
            if (param_4 == '\0') {
              FUN_00446870();
            }
            if (*(char *)(param_1 + 0x2010d) == '\0') {
              FUN_0042b98b(0);
            }
            goto LAB_0042c209;
          }
        }
        piStack_7c = *(int **)(param_1 + 0x200f0 + iVar7 * 4);
        piStack_64 = piStack_7c + piStack_7c[-1] * 2;
        if (piStack_7c != piStack_64) {
          do {
            iVar5 = piStack_7c[1];
            if (iVar5 == 0) {
              if (*(char *)(param_1 + 0x20246) != '\0') {
                *(undefined1 *)(param_1 + 0x20246) = 0;
                (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))
                          (*(int **)(param_1 + 0x205ac),0x1b,0);
              }
              *(undefined4 *)(param_1 + 0x201ec) = 0;
              (**(code **)(**(int **)(param_1 + 0x205ac) + 0x104))(*(int **)(param_1 + 0x205ac),0,0)
              ;
            }
            else if ((iVar7 == 2) && (*(char *)(iVar5 + 4) != '\0')) {
              FUN_004618a0(1,iVar5);
            }
            else {
              FUN_004618a0(2,iVar5);
            }
            DAT_00736c70 = FUN_00428940(DAT_00736c5c,&DAT_00736c64);
            DAT_00736c68 = 0;
            puVar6 = (uint *)*piStack_7c;
            puStack_78 = puVar6 + puVar6[-1] * 6;
            if (puVar6 != puStack_78) {
              do {
                uStack_84 = *puVar6;
                if ((uStack_84 & 8) == 0) {
                  if ((*(char *)(param_1 + 0x20108) == '\0') ||
                     ((iStack_80 != 0 && (iStack_80 != 1)))) {
                    *puVar6 = uStack_84 | 1;
LAB_0042c385:
                    FUN_0042ba63(puVar6,puVar6[2]);
                    param_1 = local_74;
                  }
                  else if ((uStack_84 & 2) == 0) {
                    if ((param_4 == '\0') && (((uint *)puVar6[1])[3] != 0)) {
                      uVar1 = puVar6[3];
                      uVar4 = *(uint *)puVar6[1];
                      if ((*(byte *)(uVar1 + 0x10) & 4) == 0) {
                        if (*(int *)(uVar1 + 0x14) == 0) goto LAB_0042c36b;
                        iVar5 = *(int *)(*(int *)(uVar1 + 0x14) + 0x14);
                      }
                      else {
                        if (*(uint *)(uVar1 + 4) <= uVar4) {
                          uVar4 = *(uint *)(uVar1 + 4) - 1;
                        }
                        iVar5 = *(int *)(*(int *)(*(int *)(uVar1 + 8) + uVar4 * 4) * 0x94 + 0x14 +
                                        *(int *)(uVar1 + 0x14));
                      }
                      if (iVar5 != 0) goto LAB_0042c385;
                    }
LAB_0042c36b:
                    *puVar6 = uStack_84 | 1;
                    FUN_0042ba63(puVar6,puVar6[2] << 0x18);
                    param_1 = local_74;
                  }
                  else {
                    *puVar6 = uStack_84 | 1;
                    FUN_0042ba63(puVar6,*(undefined4 *)(puVar6[1] + 8));
                    param_1 = local_74;
                  }
                }
                else if (*(undefined ***)puVar6[1] != G3DESelectMark::vftable) {
                  (*(code *)(*(undefined ***)puVar6[1])[4])(puVar6[2]);
                }
                puVar6 = puVar6 + 6;
              } while (puVar6 != puStack_78);
            }
            puVar3 = DAT_00736c54;
            if (DAT_00736c70 != 0) {
              if (((*(char *)(DAT_00736c54 + 0xd) != '\0') &&
                  (*(char *)((int)DAT_00736c54 + 0x35) != '\0')) &&
                 (piVar2 = (int *)DAT_00736c54[3], piVar2 != (int *)0x0)) {
                (**(code **)(*piVar2 + 0x30))(piVar2);
                *(undefined1 *)((int)puVar3 + 0x35) = 0;
              }
              DAT_00736c70 = 0;
            }
            iVar5 = DAT_00736c64;
            if (DAT_00736c64 != 0) {
              uStack_6c = DAT_00736c58;
              iStack_70 = DAT_00736c54[2];
              uStack_68 = DAT_00736c68 / 3;
              puStack_78 = (uint *)*DAT_00736c54;
              uStack_84 = DAT_00736c74 * iStack_70 + DAT_00736c54[0xc];
              if ((uStack_84 != 0) && (DAT_00736c64 != 0)) {
                if (DAT_00785098 != puStack_78) {
                  (**(code **)(*DAT_007848dc + 0x164))(DAT_007848dc,puStack_78);
                  DAT_00785098 = puStack_78;
                }
                (**(code **)(*DAT_007848dc + 0x150))
                          (DAT_007848dc,4,0,iVar5,uStack_68,uStack_6c,0x65,uStack_84,iStack_70);
                DAT_00785094 = 0;
                DAT_00785090 = 0;
              }
            }
            piStack_7c = piStack_7c + 2;
            iVar7 = iStack_80;
          } while (piStack_7c != piStack_64);
        }
      }
      iStack_80 = iVar7 + 1;
    } while (iStack_80 < 3);
    if (*(char *)(param_1 + 0x20244) != '\x01') {
      *(undefined1 *)(param_1 + 0x20244) = 1;
      (**(code **)(**(int **)(param_1 + 0x205ac) + 0xe4))(*(int **)(param_1 + 0x205ac),0xe,1);
    }
    FUN_00431bf0(5,0);
    FUN_00431490();
    if (DAT_00784570 != 1) {
      DAT_00784570 = 1;
      (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x13,5);
      (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x14,6);
    }
    FUN_00470fc0();
  }
  __security_check_cookie(local_14 ^ (uint)auStack_88);
  return;
}


```

## `00446aea`

- Function: `FUN_00446940`
- Entry: `00446940`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00446940(void)

{
  undefined4 uVar1;
  int *piVar2;
  int iVar3;
  int *piVar4;
  int iVar5;
  int iVar6;
  uint uVar7;
  int iVar8;
  undefined4 *puVar9;
  int iVar10;
  uint extraout_ECX;
  uint uVar11;
  uint uVar12;
  uint uVar13;
  uint uVar14;
  int iVar15;
  undefined4 *puVar16;
  bool bVar17;
  undefined8 uVar18;
  uint uStack_98;
  int *piStack_94;
  uint uStack_90;
  uint uStack_8c;
  int iStack_88;
  uint uStack_84;
  uint uStack_80;
  undefined1 auStack_50 [76];
  
  if ((DAT_007b5320 != 0) && (DAT_00784440 != '\0')) {
    if (DAT_007c5eca == '\0') {
      if (DAT_00784577 != '\0') {
        DAT_00784577 = '\0';
        (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0xf,0);
      }
    }
    else if (DAT_00784577 != DAT_007852e8) {
      DAT_00784577 = DAT_007852e8;
      (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0xf,DAT_007852e8);
    }
    DAT_00764330 = DAT_0073ae68;
    if ((*(int **)(DAT_007b5320 + 0x48) != (int *)0x0) && (**(int **)(DAT_007b5320 + 0x48) != 0)) {
      puVar9 = &DAT_00736d50;
      puVar16 = &DAT_00736de0;
      for (iVar10 = 0x10; iVar10 != 0; iVar10 = iVar10 + -1) {
        *puVar16 = *puVar9;
        puVar9 = puVar9 + 1;
        puVar16 = puVar16 + 1;
      }
      FUN_00480830();
      FUN_004804a0();
      iVar10 = FUN_0046bd80(0);
      piVar4 = DAT_007848dc;
      FUN_00431bf0(5,0);
      uStack_90 = 0;
      do {
        uStack_84 = 0;
        if (DAT_007b5398 != 0) {
          piStack_94 = &DAT_007b5370;
          do {
            if ((piStack_94[-10] == uStack_90) && (iVar8 = piStack_94[0x15], iVar8 != 0)) {
              if (*(int *)(*piStack_94 + 4) != 0) {
                FUN_004618a0(1,*(undefined4 *)(*piStack_94 + 0xc));
              }
              uStack_80 = iVar8 * 4;
              uStack_8c = uStack_80;
              if (300 < uStack_80) {
                uStack_8c = 300;
              }
              uStack_98 = 0;
              iVar5 = FUN_00428860(uStack_8c,&DAT_007c2480);
              if (iVar5 == 0) {
                return;
              }
              iVar6 = FUN_004455e0(uStack_90);
              iStack_88 = 0;
              if (0 < iVar8) {
                do {
                  iVar3 = DAT_007c2478;
                  uVar7 = uStack_98 + 4;
                  if (uStack_8c < uVar7) {
                    if ((*(char *)(DAT_007c2478 + 0x34) != '\0') &&
                       (*(char *)(DAT_007c2478 + 0x35) != '\0')) {
                      piVar2 = *(int **)(DAT_007c2478 + 0xc);
                      uVar7 = 0;
                      if (piVar2 != (int *)0x0) {
                        (**(code **)(*piVar2 + 0x30))(piVar2);
                        *(undefined1 *)(iVar3 + 0x35) = 0;
                        uVar7 = extraout_ECX;
                      }
                    }
                    FUN_00428ab0(uVar7,DAT_007c2480,uStack_98,DAT_007c2484,uVar7,
                                 (uStack_98 >> 2) * 6);
                    uStack_8c = uStack_80 - uStack_98;
                    uStack_98 = 0;
                    if (300 < uStack_8c) {
                      uStack_8c = 300;
                    }
                    uStack_80 = uStack_80 - uStack_8c;
                    iVar5 = FUN_00428860(uStack_8c,&DAT_007c2480);
                    if (iVar5 == 0) {
                      return;
                    }
                  }
                  iVar3 = *(int *)(piStack_94[0xb] + iStack_88 * 4);
                  uVar11 = (uint)*(ushort *)(iVar10 + iVar3 * 8);
                  uVar12 = (uint)*(ushort *)(iVar10 + 2 + iVar3 * 8);
                  uVar13 = (uint)*(ushort *)(iVar10 + 4 + iVar3 * 8);
                  uVar7 = (uint)*(ushort *)(iVar10 + 6 + iVar3 * 8);
                  iVar15 = iVar3 * 0x20;
                  if (*(char *)(DAT_007b540c + 0xc + iVar3 * 0x10) == -0x10) {
                    *(undefined4 *)(iVar5 + 0x14 + uStack_98 * 0x1c) =
                         *(undefined4 *)(iVar15 + 0x10 + iVar6);
                    *(undefined4 *)(iVar5 + 0x18 + uStack_98 * 0x1c) =
                         *(undefined4 *)(iVar15 + 0x14 + iVar6);
                    *(undefined4 *)(iVar5 + 0x30 + uStack_98 * 0x1c) =
                         *(undefined4 *)(iVar15 + iVar6);
                    *(undefined4 *)(iVar5 + 0x34 + uStack_98 * 0x1c) =
                         *(undefined4 *)(iVar15 + 4 + iVar6);
                    *(undefined4 *)(iVar5 + 0x4c + uStack_98 * 0x1c) =
                         *(undefined4 *)(iVar15 + 0x18 + iVar6);
                    *(undefined4 *)(iVar5 + 0x50 + uStack_98 * 0x1c) =
                         *(undefined4 *)(iVar15 + 0x1c + iVar6);
                    *(undefined4 *)(iVar5 + 0x68 + uStack_98 * 0x1c) =
                         *(undefined4 *)(iVar15 + 8 + iVar6);
                    uVar1 = *(undefined4 *)(iVar15 + 0xc + iVar6);
                  }
                  else {
                    *(undefined4 *)(iVar5 + 0x14 + uStack_98 * 0x1c) =
                         *(undefined4 *)(iVar15 + iVar6);
                    *(undefined4 *)(iVar5 + 0x18 + uStack_98 * 0x1c) =
                         *(undefined4 *)(iVar15 + 4 + iVar6);
                    *(undefined4 *)(iVar5 + 0x30 + uStack_98 * 0x1c) =
                         *(undefined4 *)(iVar15 + 8 + iVar6);
                    *(undefined4 *)(iVar5 + 0x34 + uStack_98 * 0x1c) =
                         *(undefined4 *)(iVar15 + 0xc + iVar6);
                    *(undefined4 *)(iVar5 + 0x4c + uStack_98 * 0x1c) =
                         *(undefined4 *)(iVar15 + 0x10 + iVar6);
                    *(undefined4 *)(iVar5 + 0x50 + uStack_98 * 0x1c) =
                         *(undefined4 *)(iVar15 + 0x14 + iVar6);
                    *(undefined4 *)(iVar5 + 0x68 + uStack_98 * 0x1c) =
                         *(undefined4 *)(iVar15 + 0x18 + iVar6);
                    uVar1 = *(undefined4 *)(iVar15 + 0x1c + iVar6);
                  }
                  *(undefined4 *)(iVar5 + 0x6c + uStack_98 * 0x1c) = uVar1;
                  uVar14 = (uint)*(byte *)(DAT_007b53f8 + uVar11);
                  *(uint *)(iVar5 + 0x10 + uStack_98 * 0x1c) =
                       ((uVar14 | 0xffffff00) << 8 | uVar14) << 8 | uVar14;
                  uVar14 = (uint)*(byte *)(DAT_007b53f8 + uVar12);
                  *(uint *)(iVar5 + 0x2c + uStack_98 * 0x1c) =
                       ((uVar14 | 0xffffff00) << 8 | uVar14) << 8 | uVar14;
                  uVar14 = (uint)*(byte *)(DAT_007b53f8 + uVar13);
                  *(uint *)(iVar5 + 0x48 + uStack_98 * 0x1c) =
                       ((uVar14 | 0xffffff00) << 8 | uVar14) << 8 | uVar14;
                  uVar14 = (uint)*(byte *)(DAT_007b53f8 + uVar7);
                  *(uint *)(iVar5 + 100 + uStack_98 * 0x1c) =
                       ((uVar14 | 0xffffff00) << 8 | uVar14) << 8 | uVar14;
                  *(undefined4 *)(iVar5 + uStack_98 * 0x1c) =
                       *(undefined4 *)(DAT_007b53ec + uVar11 * 0xc);
                  *(undefined4 *)(iVar5 + 4 + uStack_98 * 0x1c) =
                       *(undefined4 *)(DAT_007b53ec + 4 + uVar11 * 0xc);
                  *(undefined4 *)(iVar5 + 8 + uStack_98 * 0x1c) =
                       *(undefined4 *)(DAT_007b53ec + 8 + uVar11 * 0xc);
                  *(undefined4 *)(iVar5 + 0xc + uStack_98 * 0x1c) = 0x3f800000;
                  *(undefined4 *)(iVar5 + 0x1c + uStack_98 * 0x1c) =
                       *(undefined4 *)(DAT_007b53ec + uVar12 * 0xc);
                  *(undefined4 *)(iVar5 + 0x20 + uStack_98 * 0x1c) =
                       *(undefined4 *)(DAT_007b53ec + 4 + uVar12 * 0xc);
                  *(undefined4 *)(iVar5 + 0x24 + uStack_98 * 0x1c) =
                       *(undefined4 *)(DAT_007b53ec + 8 + uVar12 * 0xc);
                  *(undefined4 *)(iVar5 + 0x28 + uStack_98 * 0x1c) = 0x3f800000;
                  *(undefined4 *)(iVar5 + 0x38 + uStack_98 * 0x1c) =
                       *(undefined4 *)(DAT_007b53ec + uVar13 * 0xc);
                  *(undefined4 *)(iVar5 + 0x3c + uStack_98 * 0x1c) =
                       *(undefined4 *)(DAT_007b53ec + 4 + uVar13 * 0xc);
                  *(undefined4 *)(iVar5 + 0x40 + uStack_98 * 0x1c) =
                       *(undefined4 *)(DAT_007b53ec + 8 + uVar13 * 0xc);
                  *(undefined4 *)(iVar5 + 0x44 + uStack_98 * 0x1c) = 0x3f800000;
                  *(undefined4 *)(iVar5 + 0x54 + uStack_98 * 0x1c) =
                       *(undefined4 *)(DAT_007b53ec + uVar7 * 0xc);
                  uVar11 = uStack_98 + 4;
                  *(undefined4 *)(iVar5 + 0x58 + uStack_98 * 0x1c) =
                       *(undefined4 *)(DAT_007b53ec + 4 + uVar7 * 0xc);
                  uVar1 = *(undefined4 *)(DAT_007b53ec + 8 + uVar7 * 0xc);
                  iStack_88 = iStack_88 + 1;
                  *(undefined4 *)(iVar5 + 0x60 + uStack_98 * 0x1c) = 0x3f800000;
                  *(undefined4 *)(iVar5 + 0x5c + uStack_98 * 0x1c) = uVar1;
                  uStack_98 = uVar11;
                } while (iStack_88 < iVar8);
              }
              iVar8 = DAT_007c2478;
              if (((*(char *)(DAT_007c2478 + 0x34) != '\0') &&
                  (*(char *)(DAT_007c2478 + 0x35) != '\0')) &&
                 (piVar2 = *(int **)(DAT_007c2478 + 0xc), piVar2 != (int *)0x0)) {
                (**(code **)(*piVar2 + 0x30))(piVar2);
                *(undefined1 *)(iVar8 + 0x35) = 0;
              }
              if (uStack_98 != 0) {
                FUN_00428ab0(uStack_98,DAT_007c2480,uStack_98,DAT_007c2484,uStack_98,
                             (uStack_98 >> 2) * 6);
              }
            }
            uStack_84 = uStack_84 + 1;
            piStack_94 = piStack_94 + 1;
          } while (uStack_84 < DAT_007b5398);
        }
        uStack_90 = uStack_90 + 1;
      } while (uStack_90 < 4);
      if (DAT_007850d4 != '\0') {
        (**(code **)(*piVar4 + 0x104))(piVar4,1,0);
        FUN_00431bf0(5,0);
        if (DAT_007844a0 != 3) {
          DAT_007844a0 = 3;
          (**(code **)(*DAT_007848dc + 0x114))(DAT_007848dc,1,1,3);
        }
        if (DAT_007844c0 != 3) {
          DAT_007844c0 = 3;
          (**(code **)(*DAT_007848dc + 0x114))(DAT_007848dc,1,2,3);
        }
      }
      FUN_00447c00(DAT_007c2170,&DAT_007c1e70,9,0);
      FUN_00447c00(DAT_007c2474,&DAT_007c2174,10,0);
      switch(DAT_00784434) {
      case 1:
      case 2:
        if (DAT_007b78dc != 0) {
          FUN_00447250(&DAT_007b6bbc,1,0);
        }
        break;
      case 3:
      case 4:
        if (((DAT_0078443c == '\0') || (DAT_00761cd0 == 0)) || (*(int *)(DAT_00761cd0 + 0x20) != 6))
        {
          FUN_0044bf60();
        }
      }
      if (DAT_007850d4 != '\0') {
        FUN_0044c680();
      }
      FUN_00447c00(DAT_007c1e6c,&DAT_007c0eac,8,0);
      if (DAT_007b8600 != 0) {
        FUN_00447250(&DAT_007b78e0,2,0);
      }
      if ((DAT_0078443c != '\0') &&
         (FUN_00447c00(DAT_007c0184,&DAT_007bf1c4,7,1), DAT_007b6bb8 != 0)) {
        FUN_00447250(&DAT_007b5e98,0,0);
      }
      if (DAT_007ba048 != 0) {
        FUN_00447250(&DAT_007b9328,4,0);
      }
      if (DAT_007bad6c != 0) {
        FUN_00447250(&DAT_007ba04c,5,0);
      }
      if (DAT_007bba90 != 0) {
        FUN_00447250(&DAT_007bad70,6,0);
      }
      if (DAT_007bc7b4 != 0) {
        FUN_00447250(&DAT_007bba94,0xb,0);
      }
      if (DAT_007bd4d8 != 0) {
        FUN_00447250(&DAT_007bc7b8,0xc,0);
      }
      if (DAT_007be1fc != 0) {
        FUN_00447250(&DAT_007bd4dc,0xd,0);
      }
      FUN_004745a0();
      uVar7 = 0;
      if (DAT_007c36a4 != 0) {
        iVar10 = 0;
        uVar11 = DAT_007c36a4;
        do {
          iVar8 = DAT_007c36a0 + iVar10;
          if ((*(int *)(iVar8 + 0x14) != 0) && (*(char *)(iVar8 + 0x24d) != '\0')) {
            FUN_00447250(iVar8,0,*(int *)(iVar8 + 0x14));
            uVar11 = DAT_007c36a4;
          }
          uVar7 = uVar7 + 1;
          iVar10 = iVar10 + 0x2b0;
        } while (uVar7 < uVar11);
      }
      if (DAT_00784574 != '\x01') {
        DAT_00784574 = '\x01';
        (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0xe,1);
      }
      if (((DAT_007c5eca != '\0') && (DAT_007852e4 != 0)) && (uVar7 = 0, DAT_007852e0 != 0)) {
        iVar8 = 0;
        uVar11 = DAT_007852e0;
        iVar10 = DAT_007852e4;
        do {
          if (*(int *)(iVar10 + 4 + iVar8) != 0) {
            FUN_0044f410();
            uVar11 = DAT_007852e0;
            iVar10 = DAT_007852e4;
          }
          uVar7 = uVar7 + 1;
          iVar8 = iVar8 + 0x68;
        } while (uVar7 < uVar11);
      }
      iVar10 = DAT_00736dd0 * 0x10;
      puVar9 = &DAT_00736e20 + iVar10;
      puVar16 = &DAT_00736d90;
      for (iVar8 = 0x10; iVar8 != 0; iVar8 = iVar8 + -1) {
        *puVar16 = *puVar9;
        puVar9 = puVar9 + 1;
        puVar16 = puVar16 + 1;
      }
      DAT_00736dd0 = DAT_00736dd0 + -1;
      uVar18 = FUN_004d4960(&DAT_00736e20 + iVar10);
      puVar9 = (undefined4 *)uVar18;
      puVar16 = &DAT_00736d10;
      for (iVar10 = 0x10; iVar10 != 0; iVar10 = iVar10 + -1) {
        *puVar16 = *puVar9;
        puVar9 = puVar9 + 1;
        puVar16 = puVar16 + 1;
      }
      puVar9 = &DAT_00736de0;
      puVar16 = (undefined4 *)((ulonglong)uVar18 >> 0x20);
      for (iVar10 = 0x10; iVar10 != 0; iVar10 = iVar10 + -1) {
        *puVar16 = *puVar9;
        puVar9 = puVar9 + 1;
        puVar16 = puVar16 + 1;
      }
      puVar9 = (undefined4 *)FUN_00435620(auStack_50,&DAT_00736d90);
      bVar17 = DAT_00784577 != '\x01';
      puVar16 = &DAT_00736d10;
      for (iVar10 = 0x10; iVar10 != 0; iVar10 = iVar10 + -1) {
        *puVar16 = *puVar9;
        puVar9 = puVar9 + 1;
        puVar16 = puVar16 + 1;
      }
      if (bVar17) {
        DAT_00784577 = '\x01';
        (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0xf,1);
      }
      if (DAT_00784570 != 1) {
        DAT_00784570 = 1;
        (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x13,5);
        (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x14,6);
      }
      FUN_00431490();
    }
  }
  return;
}


```

## `0044f4d9`

- Function: `FUN_0044f410`
- Entry: `0044f410`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void __fastcall FUN_0044f410(int *param_1)

{
  float *pfVar1;
  ushort uVar2;
  undefined1 uVar3;
  uint uVar4;
  float *pfVar5;
  undefined4 *puVar6;
  int extraout_ECX;
  int extraout_ECX_00;
  uint extraout_ECX_01;
  uint extraout_ECX_02;
  int iVar7;
  undefined4 *extraout_ECX_03;
  undefined4 *extraout_ECX_04;
  undefined4 *extraout_ECX_05;
  float *pfVar8;
  undefined4 *puVar9;
  float fVar10;
  int *piVar11;
  float *pfVar12;
  undefined4 **ppuVar13;
  uint uVar14;
  float fVar15;
  float fVar16;
  float fVar17;
  float fVar18;
  float fVar19;
  undefined1 auStack_1c8 [4];
  float *pfStack_1c4;
  undefined4 *puStack_1c0;
  float *local_1bc;
  int *local_1b8;
  int iStack_1b4;
  uint local_1b0;
  float *pfStack_1ac;
  undefined4 *puStack_1a8;
  float *pfStack_1a4;
  float fStack_1a0;
  float fStack_19c;
  undefined4 *puStack_198;
  undefined4 *puStack_194;
  float fStack_190;
  uint uStack_18c;
  uint uStack_188;
  uint uStack_184;
  undefined4 *puStack_180;
  undefined4 uStack_17c;
  undefined4 *puStack_178;
  undefined4 uStack_174;
  float fStack_170;
  float fStack_16c;
  float fStack_168;
  float fStack_164;
  undefined4 *apuStack_160 [3];
  float fStack_154;
  undefined4 uStack_150;
  undefined4 uStack_14c;
  undefined4 uStack_148;
  float fStack_144;
  float fStack_140;
  float fStack_13c;
  float fStack_138;
  float fStack_134;
  undefined4 uStack_130;
  undefined4 uStack_12c;
  undefined4 uStack_128;
  undefined4 uStack_124;
  float afStack_120 [4];
  float fStack_110;
  float fStack_10c;
  float fStack_108;
  float fStack_104;
  float fStack_100;
  float fStack_fc;
  undefined4 uStack_f8;
  float fStack_f4;
  float fStack_f0;
  undefined4 uStack_ec;
  undefined4 uStack_e8;
  float fStack_e4;
  float afStack_e0 [4];
  float fStack_d0;
  float fStack_cc;
  float fStack_c8;
  float fStack_c4;
  float fStack_c0;
  float fStack_bc;
  float fStack_b8;
  float fStack_b4;
  float fStack_b0;
  float fStack_ac;
  float fStack_a8;
  float fStack_a4;
  undefined4 auStack_a0 [16];
  undefined4 auStack_60 [19];
  uint local_14;
  
  local_14 = DAT_007360c8 ^ (uint)auStack_1c8;
  local_1b8 = param_1;
  if ((param_1[2] != 0) && (param_1[0x13] != 0)) {
    FUN_0044ed30();
    uVar14 = 0;
    local_1b0 = 0;
    if (param_1[2] != 0) {
      local_1bc = (float *)0x0;
      do {
        if (*(char *)(local_1b0 + param_1[0xe]) != '\0') {
          puVar9 = (undefined4 *)(param_1[0x15] + (int)local_1bc);
          iVar7 = param_1[0x16];
          *(undefined4 *)(iVar7 + uVar14 * 2) = *puVar9;
          *(undefined4 *)(iVar7 + 4 + uVar14 * 2) = puVar9[1];
          *(undefined4 *)(iVar7 + 8 + uVar14 * 2) = puVar9[2];
          uVar14 = uVar14 + 6;
        }
        local_1b0 = local_1b0 + 1;
        local_1bc = local_1bc + 3;
      } while (local_1b0 < (uint)param_1[2]);
      if (uVar14 != 0) {
        if (*(int *)(param_1[0x13] + 4) != 0) {
          FUN_004618a0(1,*(undefined4 *)(param_1[0x13] + 0xc));
        }
        DAT_00764330 = DAT_0073ae68;
        FUN_00431bf0(5,0);
        if (DAT_0078449c != 2) {
          DAT_0078449c = 2;
          (**(code **)(*DAT_007848dc + 0x114))(DAT_007848dc,0,1,2);
        }
        if (DAT_007844bc != 2) {
          DAT_007844bc = 2;
          (**(code **)(*DAT_007848dc + 0x114))(DAT_007848dc,0,2,2);
        }
        FUN_00432690(4,0x144,param_1[0xc],param_1[0x14],uVar14 / 3,param_1[0x16],0x1c);
        if (DAT_0078449c != 3) {
          DAT_0078449c = 3;
          (**(code **)(*DAT_007848dc + 0x114))(DAT_007848dc,0,1,3);
        }
        if (DAT_007844bc != 3) {
          DAT_007844bc = 3;
          (**(code **)(*DAT_007848dc + 0x114))(DAT_007848dc,0,2,3);
        }
        FUN_00431bf0(5,0);
        if (param_1[1] == 0) {
          iStack_1b4 = 0;
          pfStack_1a4 = (float *)DAT_007c2478[4];
          if ((DAT_007b9324 != 0) && (*param_1 != 0)) {
            if (DAT_007c4e5c != 0) {
              FUN_0046cd50(DAT_007c4e5c);
            }
            if (DAT_00784570 != 4) {
              DAT_00784570 = 4;
              (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x13,2);
              (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x14,2);
            }
            if (DAT_00784576 != '\x01') {
              DAT_00784576 = '\x01';
              (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x1b,1);
            }
            if (DAT_00784574 != '\0') {
              DAT_00784574 = '\0';
              (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0xe,0);
            }
            fVar15 = 0.0;
            fStack_1a0 = 0.0;
            puStack_1c0 = (undefined4 *)FUN_00428860(pfStack_1a4,&iStack_1b4);
            if (puStack_1c0 != (undefined4 *)0x0) {
              uStack_184 = 0;
              iVar7 = extraout_ECX;
              if (DAT_007b9324 != 0) {
                pfStack_1c4 = (float *)&DAT_007b8614;
                iVar7 = DAT_007c24dc;
                fVar16 = DAT_006da944;
                fVar10 = DAT_006daa00;
                do {
                  fVar17 = pfStack_1c4[-1];
                  fVar18 = pfStack_1c4[-4];
                  puStack_194 = (undefined4 *)(fVar17 * DAT_006dab58);
                  puVar9 = (undefined4 *)pfStack_1c4[-2];
                  uVar14 = (uint)((fVar18 - fVar17) * fVar16);
                  local_1b0 = 0;
                  if (0 < (int)uVar14) {
                    local_1b0 = uVar14;
                  }
                  pfStack_1ac = (float *)(int)(fVar18 * fVar16 + fVar17 * fVar16);
                  if (iVar7 <= (int)pfStack_1ac) {
                    pfStack_1ac = (float *)(iVar7 + -1);
                  }
                  uVar4 = (uint)(((float)puVar9 - fVar17) * fVar16);
                  uVar14 = 0;
                  if (0 < (int)uVar4) {
                    uVar14 = uVar4;
                  }
                  fStack_19c = (float)(int)((float)puVar9 * fVar16 + fVar17 * fVar16);
                  if (DAT_007c24e0 <= (int)fStack_19c) {
                    fStack_19c = (float)(DAT_007c24e0 + -1);
                  }
                  puStack_1a8 = puVar9;
                  fStack_190 = fVar18;
                  uStack_188 = uVar14;
                  if ((int)uVar14 <= (int)fStack_19c) {
                    do {
                      uStack_18c = local_1b0;
                      param_1 = local_1b8;
                      uStack_188 = uVar14;
                      if ((int)local_1b0 <= (int)pfStack_1ac) {
                        do {
                          puVar6 = DAT_007c2478;
                          uVar2 = *(ushort *)(*param_1 + (iVar7 * uVar14 + uStack_18c) * 2);
                          pfVar5 = (float *)(uint)uVar2;
                          if ((uVar2 != 0xffff) &&
                             (local_1bc = pfVar5, *(char *)((int)pfVar5 + param_1[0xe]) != '\0')) {
                            if (pfStack_1a4 < (float *)((int)fVar15 + 4)) {
                              if (((*(char *)(DAT_007c2478 + 0xd) != '\0') &&
                                  (*(char *)((int)DAT_007c2478 + 0x35) != '\0')) &&
                                 (piVar11 = (int *)DAT_007c2478[3], piVar11 != (int *)0x0)) {
                                (**(code **)(*piVar11 + 0x30))(piVar11);
                                *(undefined1 *)((int)puVar6 + 0x35) = 0;
                              }
                              FUN_00428ab0(fStack_1a0,iStack_1b4,fStack_1a0,DAT_007c2484,fStack_1a0,
                                           ((uint)fStack_1a0 >> 2) * 6);
                              puStack_1c0 = (undefined4 *)FUN_00428860(pfStack_1a4,&iStack_1b4);
                              fStack_1a0 = 0.0;
                              fVar18 = fStack_190;
                              puVar9 = puStack_1a8;
                              fVar10 = DAT_006daa00;
                            }
                            fVar17 = fVar10 / (float)puStack_194;
                            uVar14 = (uint)*(ushort *)(param_1[0x15] + (int)local_1bc * 0xc);
                            iVar7 = local_1b8[0xc];
                            *puStack_1c0 = *(undefined4 *)(iVar7 + uVar14 * 0x1c);
                            puStack_1c0[1] = *(undefined4 *)(iVar7 + 4 + uVar14 * 0x1c);
                            puStack_1c0[2] = *(undefined4 *)(iVar7 + 8 + uVar14 * 0x1c);
                            puStack_1c0[3] = 0x3f800000;
                            puStack_1c0[4] = *pfStack_1c4;
                            fVar16 = DAT_006da974;
                            fVar15 = *(float *)(local_1b8[0xd] + 8 + uVar14 * 0x10);
                            puStack_1c0[5] =
                                 (*(float *)(local_1b8[0xd] + uVar14 * 0x10) - fVar18) * fVar17 +
                                 DAT_006da974;
                            puStack_1c0[6] = fVar17 * (fVar15 - (float)puVar9) + fVar16;
                            iVar7 = local_1b8[0xc];
                            uVar14 = (uint)*(ushort *)(local_1b8[0x15] + 2 + (int)local_1bc * 0xc);
                            puStack_1c0[7] = *(undefined4 *)(iVar7 + uVar14 * 0x1c);
                            puStack_1c0[8] = *(undefined4 *)(iVar7 + 4 + uVar14 * 0x1c);
                            puStack_1c0[9] = *(undefined4 *)(iVar7 + 8 + uVar14 * 0x1c);
                            puStack_1c0[10] = 0x3f800000;
                            puStack_1c0[0xb] = *pfStack_1c4;
                            fVar15 = *(float *)(local_1b8[0xd] + 8 + uVar14 * 0x10);
                            puStack_1c0[0xc] =
                                 (*(float *)(local_1b8[0xd] + uVar14 * 0x10) - fVar18) * fVar17 +
                                 fVar16;
                            puStack_1c0[0xd] = fVar17 * (fVar15 - (float)puVar9) + fVar16;
                            iVar7 = local_1b8[0xc];
                            uVar14 = (uint)*(ushort *)(local_1b8[0x15] + 4 + (int)local_1bc * 0xc);
                            puStack_1c0[0xe] = *(undefined4 *)(iVar7 + uVar14 * 0x1c);
                            puStack_1c0[0xf] = *(undefined4 *)(iVar7 + 4 + uVar14 * 0x1c);
                            puStack_1c0[0x10] = *(undefined4 *)(iVar7 + 8 + uVar14 * 0x1c);
                            puStack_1c0[0x11] = 0x3f800000;
                            puStack_1c0[0x12] = *pfStack_1c4;
                            fVar15 = *(float *)(local_1b8[0xd] + 8 + uVar14 * 0x10);
                            puStack_1c0[0x13] =
                                 (*(float *)(local_1b8[0xd] + uVar14 * 0x10) - fVar18) * fVar17 +
                                 fVar16;
                            puStack_1c0[0x14] = fVar17 * (fVar15 - (float)puVar9) + fVar16;
                            iVar7 = local_1b8[0xc];
                            uVar14 = (uint)*(ushort *)(local_1b8[0x15] + 10 + (int)local_1bc * 0xc);
                            puStack_1c0[0x15] = *(undefined4 *)(iVar7 + uVar14 * 0x1c);
                            puStack_1c0[0x16] = *(undefined4 *)(iVar7 + 4 + uVar14 * 0x1c);
                            puStack_1c0[0x17] = *(undefined4 *)(iVar7 + 8 + uVar14 * 0x1c);
                            puStack_1c0[0x18] = 0x3f800000;
                            puStack_1c0[0x19] = *pfStack_1c4;
                            fVar15 = *(float *)(local_1b8[0xd] + 8 + uVar14 * 0x10);
                            puStack_1c0[0x1a] =
                                 fVar17 * (*(float *)(local_1b8[0xd] + uVar14 * 0x10) - fVar18) +
                                 fVar16;
                            puStack_1c0[0x1b] = fVar17 * (fVar15 - (float)puVar9) + fVar16;
                            puStack_1c0 = puStack_1c0 + 0x1c;
                            fVar15 = (float)((int)fStack_1a0 + 4);
                            uVar14 = uStack_188;
                            param_1 = local_1b8;
                            fVar18 = fStack_190;
                            local_1bc = (float *)((int)local_1bc * 6);
                            fStack_1a0 = fVar15;
                          }
                          uStack_18c = uStack_18c + 1;
                          iVar7 = DAT_007c24dc;
                        } while ((int)uStack_18c <= (int)pfStack_1ac);
                      }
                      uVar14 = uVar14 + 1;
                      fVar16 = DAT_006da944;
                      uStack_188 = uVar14;
                    } while ((int)uVar14 <= (int)fStack_19c);
                  }
                  uStack_184 = uStack_184 + 1;
                  pfStack_1c4 = pfStack_1c4 + 5;
                } while (uStack_184 < DAT_007b9324);
              }
              puStack_194 = DAT_007c2478;
              if ((*(char *)(DAT_007c2478 + 0xd) != '\0') &&
                 (*(char *)((int)DAT_007c2478 + 0x35) != '\0')) {
                piVar11 = (int *)DAT_007c2478[3];
                iVar7 = 0;
                if (piVar11 != (int *)0x0) {
                  (**(code **)(*piVar11 + 0x30))(piVar11);
                  *(undefined1 *)((int)puStack_194 + 0x35) = 0;
                  iVar7 = extraout_ECX_00;
                }
              }
              if (fVar15 != 0.0) {
                FUN_00428ab0(iVar7,iStack_1b4,fVar15,DAT_007c2484,iVar7,((uint)fVar15 >> 2) * 6);
              }
            }
          }
          DAT_007b9324 = 0;
          if ((DAT_007bf1c0 != (undefined4 *)0x0) && (*param_1 != 0)) {
            if (DAT_007c4e34 != 0) {
              FUN_0046cd50(DAT_007c4e34);
            }
            if (DAT_00784570 != 4) {
              DAT_00784570 = 4;
              (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x13,2);
              (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x14,2);
            }
            if (DAT_00784576 != '\x01') {
              DAT_00784576 = '\x01';
              (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x1b,1);
            }
            if (DAT_00784574 != '\0') {
              DAT_00784574 = '\0';
              (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0xe,0);
            }
            pfVar5 = (float *)0x0;
            pfStack_1ac = (float *)0x0;
            puStack_1c0 = (undefined4 *)FUN_00428860(pfStack_1a4,&iStack_1b4);
            if (puStack_1c0 != (undefined4 *)0x0) {
              puStack_1a8 = (undefined4 *)0x0;
              uVar14 = extraout_ECX_01;
              if (DAT_007bf1c0 != (undefined4 *)0x0) {
                pfStack_1c4 = (float *)&DAT_007be210;
                fVar15 = DAT_006da944;
                do {
                  fVar16 = pfStack_1c4[-2];
                  fStack_19c = pfStack_1c4[-4];
                  puStack_198 = (undefined4 *)(fVar16 * DAT_006dab58);
                  fStack_1a0 = pfStack_1c4[-3];
                  uVar14 = (uint)((fStack_19c - fVar16) * fVar15);
                  uStack_184 = 0;
                  if (0 < (int)uVar14) {
                    uStack_184 = uVar14;
                  }
                  uVar14 = (uint)(fStack_19c * fVar15 + fVar16 * fVar15);
                  if (DAT_007c24dc <= (int)uVar14) {
                    uVar14 = DAT_007c24dc - 1;
                  }
                  fVar17 = (float)(int)((fStack_1a0 - fVar16) * fVar15);
                  fVar10 = 0.0;
                  if (0 < (int)fVar17) {
                    fVar10 = fVar17;
                  }
                  local_1bc = (float *)(int)(fStack_1a0 * fVar15 + fVar16 * fVar15);
                  if (DAT_007c24e0 <= (int)local_1bc) {
                    local_1bc = (float *)(DAT_007c24e0 + -1);
                  }
                  fStack_190 = fVar10;
                  uStack_18c = uVar14;
                  if ((int)fVar10 <= (int)local_1bc) {
                    do {
                      uStack_188 = uStack_184;
                      fStack_190 = fVar10;
                      if ((int)uStack_184 <= (int)uVar14) {
                        do {
                          puVar9 = DAT_007c2478;
                          uVar2 = *(ushort *)
                                   (*param_1 + ((int)fVar10 * DAT_007c24dc + uStack_188) * 2);
                          puVar6 = (undefined4 *)(uint)uVar2;
                          if ((uVar2 != 0xffff) &&
                             (puStack_194 = puVar6, *(char *)((int)puVar6 + param_1[0xe]) != '\0'))
                          {
                            if (pfStack_1a4 < pfVar5 + 1) {
                              if (((*(char *)(DAT_007c2478 + 0xd) != '\0') &&
                                  (*(char *)((int)DAT_007c2478 + 0x35) != '\0')) &&
                                 (piVar11 = (int *)DAT_007c2478[3], piVar11 != (int *)0x0)) {
                                (**(code **)(*piVar11 + 0x30))(piVar11);
                                *(undefined1 *)((int)puVar9 + 0x35) = 0;
                              }
                              FUN_00428ab0(pfStack_1ac,iStack_1b4,pfStack_1ac,DAT_007c2484,
                                           pfStack_1ac,((uint)pfStack_1ac >> 2) * 6);
                              puStack_1c0 = (undefined4 *)FUN_00428860(pfStack_1a4,&iStack_1b4);
                              pfStack_1ac = (float *)0x0;
                            }
                            local_1b0 = (int)puStack_194 * 6;
                            fVar19 = DAT_006daa00 / (float)puStack_198;
                            uVar14 = (uint)*(ushort *)(param_1[0x15] + (int)puStack_194 * 0xc);
                            iVar7 = local_1b8[0xc];
                            *puStack_1c0 = *(undefined4 *)(iVar7 + uVar14 * 0x1c);
                            puStack_1c0[1] = *(undefined4 *)(iVar7 + 4 + uVar14 * 0x1c);
                            puStack_1c0[2] = *(undefined4 *)(iVar7 + 8 + uVar14 * 0x1c);
                            puStack_1c0[3] = 0x3f800000;
                            puStack_1c0[4] = pfStack_1c4[-1];
                            fVar10 = DAT_006da974;
                            fVar15 = (*(float *)(local_1b8[0xd] + 8 + uVar14 * 0x10) - fStack_1a0) *
                                     fVar19;
                            fVar17 = (*(float *)(local_1b8[0xd] + uVar14 * 0x10) - fStack_19c) *
                                     fVar19;
                            fVar16 = fVar15 * pfStack_1c4[1] + fVar17 * *pfStack_1c4 + DAT_006da974;
                            puStack_1c0[5] =
                                 (fVar17 * pfStack_1c4[1] - fVar15 * *pfStack_1c4) + DAT_006da974;
                            puStack_1c0[6] = fVar16;
                            iVar7 = local_1b8[0xc];
                            uVar14 = (uint)*(ushort *)(local_1b8[0x15] + 2 + (int)puStack_194 * 0xc)
                            ;
                            puStack_1c0[7] = *(undefined4 *)(iVar7 + uVar14 * 0x1c);
                            puStack_1c0[8] = *(undefined4 *)(iVar7 + 4 + uVar14 * 0x1c);
                            puStack_1c0[9] = *(undefined4 *)(iVar7 + 8 + uVar14 * 0x1c);
                            puStack_1c0[10] = 0x3f800000;
                            puStack_1c0[0xb] = pfStack_1c4[-1];
                            fVar15 = *pfStack_1c4;
                            fVar16 = pfStack_1c4[1];
                            fVar18 = (*(float *)(local_1b8[0xd] + uVar14 * 0x10) - fStack_19c) *
                                     fVar19;
                            fVar17 = (*(float *)(local_1b8[0xd] + 8 + uVar14 * 0x10) - fStack_1a0) *
                                     fVar19;
                            puStack_1c0[0xc] = (fVar18 * fVar16 - fVar17 * fVar15) + fVar10;
                            puStack_1c0[0xd] = fVar17 * fVar16 + fVar18 * fVar15 + fVar10;
                            iVar7 = local_1b8[0xc];
                            uVar14 = (uint)*(ushort *)(local_1b8[0x15] + 4 + (int)puStack_194 * 0xc)
                            ;
                            puStack_1c0[0xe] = *(undefined4 *)(iVar7 + uVar14 * 0x1c);
                            puStack_1c0[0xf] = *(undefined4 *)(iVar7 + 4 + uVar14 * 0x1c);
                            puStack_1c0[0x10] = *(undefined4 *)(iVar7 + 8 + uVar14 * 0x1c);
                            puStack_1c0[0x11] = 0x3f800000;
                            puStack_1c0[0x12] = pfStack_1c4[-1];
                            fVar15 = pfStack_1c4[1];
                            fVar16 = *pfStack_1c4;
                            fVar17 = (*(float *)(local_1b8[0xd] + 8 + uVar14 * 0x10) - fStack_1a0) *
                                     fVar19;
                            fVar18 = (*(float *)(local_1b8[0xd] + uVar14 * 0x10) - fStack_19c) *
                                     fVar19;
                            puStack_1c0[0x13] = (fVar18 * fVar15 - fVar17 * fVar16) + fVar10;
                            puStack_1c0[0x14] = fVar17 * fVar15 + fVar18 * fVar16 + fVar10;
                            iVar7 = local_1b8[0xc];
                            uVar14 = (uint)*(ushort *)
                                            (local_1b8[0x15] + 10 + (int)puStack_194 * 0xc);
                            puStack_1c0[0x15] = *(undefined4 *)(iVar7 + uVar14 * 0x1c);
                            puStack_1c0[0x16] = *(undefined4 *)(iVar7 + 4 + uVar14 * 0x1c);
                            puStack_1c0[0x17] = *(undefined4 *)(iVar7 + 8 + uVar14 * 0x1c);
                            puStack_1c0[0x18] = 0x3f800000;
                            puStack_1c0[0x19] = pfStack_1c4[-1];
                            fVar15 = *pfStack_1c4;
                            fVar16 = pfStack_1c4[1];
                            fVar17 = fVar19 * (*(float *)(local_1b8[0xd] + uVar14 * 0x10) -
                                              fStack_19c);
                            fVar19 = fVar19 * (*(float *)(local_1b8[0xd] + 8 + uVar14 * 0x10) -
                                              fStack_1a0);
                            puStack_1c0[0x1a] = (fVar17 * fVar16 - fVar19 * fVar15) + fVar10;
                            puStack_1c0[0x1b] = fVar19 * fVar16 + fVar17 * fVar15 + fVar10;
                            puStack_1c0 = puStack_1c0 + 0x1c;
                            pfVar5 = pfStack_1ac + 1;
                            fVar10 = fStack_190;
                            param_1 = local_1b8;
                            pfStack_1ac = pfVar5;
                          }
                          uStack_188 = uStack_188 + 1;
                          uVar14 = uStack_18c;
                        } while ((int)uStack_188 <= (int)uStack_18c);
                      }
                      fVar10 = (float)((int)fVar10 + 1);
                      fVar15 = DAT_006da944;
                      fStack_190 = fVar10;
                    } while ((int)fVar10 <= (int)local_1bc);
                  }
                  puStack_1a8 = (undefined4 *)((int)puStack_1a8 + 1);
                  pfStack_1c4 = pfStack_1c4 + 6;
                } while (puStack_1a8 < DAT_007bf1c0);
              }
              puStack_198 = DAT_007c2478;
              if ((*(char *)(DAT_007c2478 + 0xd) != '\0') &&
                 (*(char *)((int)DAT_007c2478 + 0x35) != '\0')) {
                piVar11 = (int *)DAT_007c2478[3];
                uVar14 = 0;
                if (piVar11 != (int *)0x0) {
                  (**(code **)(*piVar11 + 0x30))(piVar11);
                  *(undefined1 *)((int)puStack_198 + 0x35) = 0;
                  uVar14 = extraout_ECX_02;
                }
              }
              if (pfVar5 != (float *)0x0) {
                FUN_00428ab0(uVar14,iStack_1b4,pfVar5,DAT_007c2484,uVar14,((uint)pfVar5 >> 2) * 6);
              }
            }
          }
          DAT_007bf1c0 = (undefined4 *)0x0;
          if ((DAT_007c0ea8 != (undefined4 *)0x0) && (*param_1 != 0)) {
            if (DAT_007c4e30 != 0) {
              FUN_0046cd50(DAT_007c4e30);
            }
            if (DAT_00784570 != 4) {
              DAT_00784570 = 4;
              (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x13,2);
              (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x14,2);
            }
            if (DAT_00784576 != '\x01') {
              DAT_00784576 = '\x01';
              (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x1b,1);
            }
            if (DAT_00784574 != '\0') {
              DAT_00784574 = '\0';
              (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0xe,0);
            }
            FUN_00481730(apuStack_160);
            pfVar5 = pfStack_1a4;
            pfVar12 = (float *)&DAT_00736d50;
            pfVar8 = afStack_e0;
            for (iVar7 = 0x10; iVar7 != 0; iVar7 = iVar7 + -1) {
              *pfVar8 = *pfVar12;
              pfVar12 = pfVar12 + 1;
              pfVar8 = pfVar8 + 1;
            }
            pfStack_1c4 = (float *)0x0;
            local_1b0 = FUN_00428860(pfStack_1a4,&iStack_1b4);
            if (local_1b0 != 0) {
              puStack_1a8 = (undefined4 *)0x0;
              puVar9 = extraout_ECX_03;
              pfVar12 = (float *)0x0;
              if (DAT_007c0ea8 != (undefined4 *)0x0) {
                local_1bc = (float *)&DAT_007c0188;
                piVar11 = local_1b8;
                fVar15 = DAT_006da944;
                fVar16 = DAT_006daa00;
                do {
                  uVar2 = *(ushort *)
                           (*piVar11 +
                           ((int)(local_1bc[2] * fVar15) * DAT_007c24dc + (int)(*local_1bc * fVar15)
                           ) * 2);
                  puVar6 = (undefined4 *)(uint)uVar2;
                  puVar9 = (undefined4 *)0xffff;
                  if ((uVar2 != 0xffff) &&
                     (puVar9 = puVar6, puStack_198 = puVar6,
                     *(char *)((int)puVar6 + piVar11[0xe]) != '\0')) {
                    if (pfVar5 < pfStack_1c4 + 1) {
                      FUN_00428a00();
                      FUN_00428ab0(pfStack_1c4,iStack_1b4,pfStack_1c4,DAT_007c2484,pfStack_1c4,
                                   ((uint)pfStack_1c4 >> 2) * 6);
                      local_1b0 = FUN_00428860(pfVar5,&iStack_1b4);
                      pfStack_1c4 = (float *)0x0;
                      fVar16 = DAT_006daa00;
                    }
                    fStack_fc = local_1bc[3];
                    fStack_100 = fStack_fc * DAT_006da974;
                    fStack_154 = *local_1bc;
                    fStack_134 = local_1bc[2];
                    afStack_120[0] = _DAT_008b23d0 * fStack_100;
                    afStack_120[1] = fRam008b23d4 * fStack_fc;
                    afStack_120[2] = fRam008b23d8 * 0.0;
                    afStack_120[3] = fRam008b23dc * fVar16;
                    fStack_110 = _DAT_008b23d0 * fStack_100;
                    fStack_10c = fRam008b23d4 * 0.0;
                    fStack_108 = fRam008b23d8 * 0.0;
                    fStack_104 = fRam008b23dc * fVar16;
                    uStack_f8 = 0;
                    fStack_144 = *(float *)(piVar11[0xb] + 0xc + (int)puStack_198 * 0x10) -
                                 fStack_fc * DAT_006da920;
                    uStack_ec = 0;
                    uStack_e8 = 0;
                    fStack_f4 = fVar16;
                    fStack_f0 = fStack_100;
                    fStack_e4 = fVar16;
                    puVar9 = (undefined4 *)FUN_00435620(auStack_60,apuStack_160);
                    uVar14 = local_1b0;
                    puVar6 = auStack_a0;
                    for (iVar7 = 0x10; iVar7 != 0; iVar7 = iVar7 + -1) {
                      *puVar6 = *puVar9;
                      puVar9 = puVar9 + 1;
                      puVar6 = puVar6 + 1;
                    }
                    FUN_00450c70(afStack_120,0);
                    fVar15 = DAT_006da944;
                    *(float *)(uVar14 + 0x10) = local_1bc[4];
                    *(float *)(uVar14 + 0x2c) = local_1bc[4];
                    *(float *)(uVar14 + 0x48) = local_1bc[4];
                    *(float *)(uVar14 + 100) = local_1bc[4];
                    *(undefined4 *)(uVar14 + 0x14) = 0;
                    *(undefined4 *)(uVar14 + 0x18) = 0;
                    *(undefined4 *)(uVar14 + 0x30) = 0;
                    *(undefined4 *)(uVar14 + 0x34) = 0x3f800000;
                    *(undefined4 *)(uVar14 + 0x4c) = 0x3f800000;
                    *(undefined4 *)(uVar14 + 0x50) = 0;
                    *(undefined4 *)(uVar14 + 0x68) = 0x3f800000;
                    *(undefined4 *)(uVar14 + 0x6c) = 0x3f800000;
                    local_1b0 = uVar14 + 0x70;
                    pfStack_1c4 = pfStack_1c4 + 1;
                    puVar9 = extraout_ECX_04;
                    piVar11 = local_1b8;
                    pfVar5 = pfStack_1a4;
                  }
                  local_1bc = local_1bc + 5;
                  puStack_1a8 = (undefined4 *)((int)puStack_1a8 + 1);
                  pfVar12 = pfStack_1c4;
                } while (puStack_1a8 < DAT_007c0ea8);
              }
              puVar6 = DAT_007c2478;
              if ((*(char *)(DAT_007c2478 + 0xd) != '\0') &&
                 (*(char *)((int)DAT_007c2478 + 0x35) != '\0')) {
                piVar11 = (int *)DAT_007c2478[3];
                puVar9 = (undefined4 *)0x0;
                if (piVar11 != (int *)0x0) {
                  (**(code **)(*piVar11 + 0x30))(piVar11);
                  *(undefined1 *)((int)puVar6 + 0x35) = 0;
                  puVar9 = extraout_ECX_05;
                }
              }
              if (pfVar12 != (float *)0x0) {
                FUN_00428ab0(puVar9,iStack_1b4,pfVar12,DAT_007c2484,puVar9,((uint)pfVar12 >> 2) * 6)
                ;
              }
            }
          }
          DAT_007c0ea8 = (undefined4 *)0x0;
          if (DAT_007c4e38 != 0) {
            FUN_0046cd50(DAT_007c4e38);
          }
          if (DAT_00784570 != 4) {
            DAT_00784570 = 4;
            (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x13,2);
            (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x14,2);
          }
          if (DAT_00784576 != '\x01') {
            DAT_00784576 = '\x01';
            (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x1b,1);
          }
          if (DAT_00784574 != '\0') {
            DAT_00784574 = '\0';
            (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0xe,0);
          }
          pfVar5 = pfStack_1a4;
          puVar9 = &DAT_00736d50;
          puVar6 = auStack_a0;
          for (iVar7 = 0x10; iVar7 != 0; iVar7 = iVar7 + -1) {
            *puVar6 = *puVar9;
            puVar9 = puVar9 + 1;
            puVar6 = puVar6 + 1;
          }
          puStack_1c0 = (undefined4 *)0x0;
          local_1b0 = FUN_00428860(pfStack_1a4,&iStack_1b4);
          if (local_1b0 != 0) {
            pfVar12 = (float *)local_1b8[0x19];
            pfVar8 = pfVar12 + (int)pfVar12[-1] * 0xb;
            puVar9 = (undefined4 *)0x0;
            pfStack_1c4 = pfVar8;
            if (pfVar12 != pfVar8) {
              pfVar12 = pfVar12 + 1;
              piVar11 = local_1b8;
              fVar15 = DAT_006daa00;
              do {
                pfStack_1ac = pfVar12;
                if (*pfVar12 < fVar15) {
                  puStack_1a8 = (undefined4 *)(int)(pfVar12[7] * DAT_006da944);
                  pfVar8 = pfStack_1c4;
                  if (((((int)puStack_1a8 < DAT_007c24dc) &&
                       ((int)(pfVar12[9] * DAT_006da944) < DAT_007c24e0)) &&
                      (uVar2 = *(ushort *)
                                (*piVar11 +
                                ((int)(pfVar12[9] * DAT_006da944) * DAT_007c24dc + (int)puStack_1a8)
                                * 2), uVar2 != 0xffff)) &&
                     (*(char *)((uint)uVar2 + piVar11[0xe]) != '\0')) {
                    if (pfVar5 < puStack_1c0 + 1) {
                      FUN_00428a00();
                      FUN_00428ab0(puStack_1c0,iStack_1b4,puStack_1c0,DAT_007c2484,puStack_1c0,
                                   ((uint)puStack_1c0 >> 2) * 6);
                      local_1b0 = FUN_00428860(pfVar5,&iStack_1b4);
                      puStack_1c0 = (undefined4 *)0x0;
                      fVar15 = DAT_006daa00;
                    }
                    fStack_a8 = *pfVar12 * DAT_006dab58 + DAT_006da974;
                    fStack_ac = _DAT_006dafe0;
                    fStack_a4 = _UNK_006dafe4;
                    afStack_e0[0] = fVar15 * _DAT_008b2430;
                    afStack_e0[1] = _DAT_006dafe0 * fRam008b2434;
                    afStack_e0[2] = fStack_a8 * fRam008b2438;
                    afStack_e0[3] = _UNK_006dafe4 * fRam008b243c;
                    fStack_c0 = fVar15 * _DAT_008b2440;
                    fStack_bc = _DAT_006dafe0 * fRam008b2444;
                    fStack_b8 = fStack_a8 * fRam008b2448;
                    fStack_b4 = _UNK_006dafe4 * fRam008b244c;
                    fStack_d0 = fVar15 * _DAT_008b23d0;
                    fStack_cc = _DAT_006dafe0 * fRam008b23d4;
                    fStack_c8 = fStack_a8 * fRam008b23d8;
                    fStack_c4 = _UNK_006dafe4 * fRam008b23dc;
                    fVar16 = _DAT_008b23d0;
                    fVar10 = fRam008b23d4;
                    fVar17 = fRam008b23d8;
                    fVar18 = fRam008b23dc;
                    fVar19 = DAT_006da974;
                    fStack_b0 = fVar15;
                    FUN_0059c793(pfVar12[-1] * DAT_006daf40 * _DAT_006da8b0);
                    puStack_180 = puStack_194;
                    uStack_17c = 0;
                    puStack_178 = puStack_198;
                    uStack_174 = 0;
                    apuStack_160[0] = puStack_194;
                    apuStack_160[1] = (undefined4 *)0x0;
                    apuStack_160[2] = puStack_198;
                    fStack_154 = 0.0;
                    uStack_150 = DAT_008b22f0;
                    uStack_14c = DAT_008b22f4;
                    uStack_148 = DAT_008b22f8;
                    fStack_144 = DAT_008b22fc;
                    fStack_170 = fVar16 * (float)puStack_198;
                    fStack_16c = fVar10 * 0.0;
                    fStack_168 = fVar17 * (float)puStack_194;
                    fStack_164 = fVar18 * 0.0;
                    fStack_140 = fStack_170;
                    fStack_13c = fStack_16c;
                    fStack_138 = fStack_168;
                    fStack_134 = fStack_164;
                    uStack_130 = DAT_008b2310;
                    uStack_12c = DAT_008b2314;
                    uStack_128 = DAT_008b2318;
                    uStack_124 = DAT_008b231c;
                    ppuVar13 = apuStack_160;
                    pfVar5 = afStack_120;
                    for (iVar7 = 0x10; iVar7 != 0; iVar7 = iVar7 + -1) {
                      *pfVar5 = (float)*ppuVar13;
                      ppuVar13 = ppuVar13 + 1;
                      pfVar5 = pfVar5 + 1;
                    }
                    afStack_120[3] = pfStack_1ac[7];
                    fStack_104 = pfStack_1ac[8];
                    fStack_f4 = pfStack_1ac[9];
                    puVar9 = (undefined4 *)FUN_00435620(apuStack_160,afStack_120);
                    uVar14 = local_1b0;
                    puVar6 = auStack_60;
                    for (iVar7 = 0x10; iVar7 != 0; iVar7 = iVar7 + -1) {
                      *puVar6 = *puVar9;
                      puVar9 = puVar9 + 1;
                      puVar6 = puVar6 + 1;
                    }
                    FUN_00450c70(afStack_e0,0);
                    fVar15 = DAT_006daa00;
                    fVar10 = 0.0;
                    fVar16 = *pfStack_1ac;
                    if ((fVar19 <= fVar16) || (fVar16 < 0.0)) {
                      if (fVar16 < DAT_006daa00) {
                        fVar10 = DAT_006dae64 - (fVar16 - fVar19) * DAT_006dae64 * DAT_006dab58;
                      }
                    }
                    else {
                      fVar10 = fVar16 * DAT_006dae64 * DAT_006dab58;
                    }
                    uVar3 = (undefined1)(int)fVar10;
                    local_1bc = (float *)CONCAT31(CONCAT21(CONCAT11(0xff,uVar3),uVar3),uVar3);
                    *(float **)(uVar14 + 0x10) = local_1bc;
                    *(float **)(uVar14 + 0x2c) = local_1bc;
                    *(float **)(uVar14 + 0x48) = local_1bc;
                    *(float **)(uVar14 + 100) = local_1bc;
                    *(undefined4 *)(uVar14 + 0x14) = 0;
                    *(undefined4 *)(uVar14 + 0x18) = 0x3f800000;
                    *(undefined4 *)(uVar14 + 0x30) = 0x3f800000;
                    *(undefined4 *)(uVar14 + 0x34) = 0x3f800000;
                    *(undefined4 *)(uVar14 + 0x4c) = 0;
                    *(undefined4 *)(uVar14 + 0x50) = 0;
                    *(undefined4 *)(uVar14 + 0x68) = 0x3f800000;
                    *(undefined4 *)(uVar14 + 0x6c) = 0;
                    local_1b0 = uVar14 + 0x70;
                    puStack_1c0 = puStack_1c0 + 1;
                    pfVar8 = pfStack_1c4;
                    piVar11 = local_1b8;
                    pfVar5 = pfStack_1a4;
                  }
                }
                pfVar12 = pfStack_1ac + 0xb;
                pfVar1 = pfStack_1ac + 10;
                puVar9 = puStack_1c0;
                pfStack_1ac = pfVar12;
              } while (pfVar1 != pfVar8);
            }
            puVar6 = DAT_007c2478;
            puStack_1a8 = DAT_007c2478;
            if (((*(char *)(DAT_007c2478 + 0xd) != '\0') &&
                (*(char *)((int)DAT_007c2478 + 0x35) != '\0')) &&
               (piVar11 = (int *)DAT_007c2478[3], piVar11 != (int *)0x0)) {
              (**(code **)(*piVar11 + 0x30))(piVar11);
              *(undefined1 *)((int)puVar6 + 0x35) = 0;
              puStack_1a8 = DAT_007c2478;
            }
            piVar11 = DAT_007848dc;
            DAT_007c2478 = puStack_1a8;
            if (puVar9 != (undefined4 *)0x0) {
              uVar14 = ((uint)puVar9 >> 2) * 6;
              puStack_198 = (undefined4 *)(uVar14 / 3);
              if (*(char *)(puStack_1a8 + 0xd) == '\0') {
                FUN_00432690(4,*puStack_1a8,puStack_1a8[2] * iStack_1b4 + puStack_1a8[0xc],puVar9,
                             puStack_198,*(undefined4 *)(DAT_007c2484 + 0x18),puStack_1a8[2]);
              }
              else {
                FUN_0042f270(puStack_1a8,DAT_007c2484,uVar14);
                (**(code **)(*piVar11 + 0x148))(piVar11,4,iStack_1b4,0,puVar9,0,puStack_198);
              }
            }
          }
          if (DAT_00784570 != 1) {
            DAT_00784570 = 1;
            (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x13,5);
            (**(code **)(*DAT_007848dc + 0xe4))(DAT_007848dc,0x14,6);
          }
        }
      }
    }
  }
  __security_check_cookie(local_14 ^ (uint)auStack_1c8);
  return;
}


```

## `0046187c`

- Function: `FUN_00461850`
- Entry: `00461850`

```c

void __thiscall FUN_00461850(int param_1,undefined4 param_2,uint param_3)

{
  if (*(int *)(param_1 + 4) != 0) {
    if ((*(int *)(param_1 + 0xc) != 0) && (param_3 < *(uint *)(param_1 + 8))) {
      FUN_004618a0(param_2,param_1);
      return;
    }
    FUN_004618a0(param_2,param_1);
  }
  return;
}


```

## `0046188c`

- Function: `FUN_00461850`
- Entry: `00461850`

```c

void __thiscall FUN_00461850(int param_1,undefined4 param_2,uint param_3)

{
  if (*(int *)(param_1 + 4) != 0) {
    if ((*(int *)(param_1 + 0xc) != 0) && (param_3 < *(uint *)(param_1 + 8))) {
      FUN_004618a0(param_2,param_1);
      return;
    }
    FUN_004618a0(param_2,param_1);
  }
  return;
}


```

