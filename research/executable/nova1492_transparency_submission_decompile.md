# Selected Nova1492 Decompilation

## `00470e40`

- Function: `FUN_00470e40`
- Entry: `00470e40`

```c

void __thiscall FUN_00470e40(int param_1,int *param_2,undefined4 *param_3,int param_4)

{
  undefined4 *puVar1;
  int *piVar2;
  undefined4 *puVar3;
  int iVar4;
  int *piVar5;
  int iVar6;
  undefined4 *puVar7;
  undefined4 *puVar8;
  undefined4 extraout_ECX;
  int *piVar9;
  bool bVar10;
  void *local_10;
  undefined1 *puStack_c;
  undefined4 local_8;
  
  local_8 = 0xffffffff;
  puStack_c = &LAB_00664818;
  local_10 = ExceptionList;
  ExceptionList = &local_10;
  if (param_4 == 3) {
    if ((param_2 == (int *)0x0) || ((char)param_2[1] == '\0')) {
      param_4 = 0;
    }
    else {
      param_4 = 2 - (uint)(((uint)param_2[1] >> 0x14 & 1) != 0);
    }
  }
  piVar9 = *(int **)(param_1 + param_4 * 4);
  iVar4 = piVar9[-1];
  piVar2 = piVar9 + iVar4 * 2;
  do {
    if (piVar9 == piVar2) {
      FUN_00471430(iVar4 + 1,iVar4 + 1);
      piVar2 = (int *)(*(int *)(param_1 + param_4 * 4) + iVar4 * 8);
      piVar9 = piVar2;
      while (piVar5 = piVar9, piVar5 != piVar2 + 2) {
        piVar9 = piVar5 + 2;
        if (piVar5 != (int *)0x0) {
          *piVar5 = (int)&DAT_006b9e28;
          local_8 = 0xffffffff;
        }
      }
      piVar2[1] = (int)param_2;
      iVar6 = *(int *)(*piVar2 + -4);
      iVar4 = iVar6 + 1;
      FUN_004714f0(iVar4,iVar4);
      puVar3 = (undefined4 *)(*piVar2 + iVar6 * 0x18);
      puVar8 = puVar3;
      while (puVar7 = puVar8, puVar7 != puVar3 + 6) {
        puVar8 = puVar7 + 6;
        if (puVar7 != (undefined4 *)0x0) {
          *puVar7 = *param_3;
          puVar7[1] = param_3[1];
          puVar7[2] = param_3[2];
          puVar7[3] = param_3[3];
          puVar7[4] = param_3[4];
          puVar1 = param_3 + 5;
          param_3 = param_3 + 6;
          puVar7[5] = *puVar1;
        }
      }
      ExceptionList = local_10;
      return;
    }
    piVar5 = (int *)piVar9[1];
    if (piVar5 == (int *)0x0) {
      bVar10 = param_2 == (int *)0x0;
LAB_00470ec0:
      if (bVar10) {
        iVar4 = *(int *)(*piVar9 + -4) + 1;
        FUN_004714f0(iVar4,iVar4);
        FUN_004717e0(extraout_ECX);
        ExceptionList = local_10;
        return;
      }
    }
    else if ((param_2 != (int *)0x0) && (*piVar5 == *param_2)) {
      bVar10 = piVar5[1] == param_2[1];
      goto LAB_00470ec0;
    }
    piVar9 = piVar9 + 2;
  } while( true );
}


```

## `0042c0a0`

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

## `004627c0`

- Function: `FUN_004627c0`
- Entry: `004627c0`

```c

uint __thiscall FUN_004627c0(int param_1,uint param_2)

{
  int iVar1;
  
  iVar1 = *(int *)(param_1 + 4);
  if (iVar1 != 0) {
    if ((*(int *)(param_1 + 0xc) != 0) && (param_2 < *(uint *)(param_1 + 8))) {
      return *(uint *)(iVar1 + 4 + *(int *)(*(int *)(param_1 + 0xc) + param_2 * 4) * 0x1c) &
             0x100000;
    }
    if (iVar1 != 0) {
      return *(uint *)(iVar1 + 4) & 0x100000;
    }
  }
  return 0;
}


```

## `00462670`

- Function: `FUN_00462670`
- Entry: `00462670`

```c

int __thiscall FUN_00462670(int param_1,uint param_2)

{
  int iVar1;
  
  iVar1 = *(int *)(param_1 + 4);
  if ((iVar1 != 0) && (*(int *)(param_1 + 0xc) != 0)) {
    return iVar1 + *(int *)(*(int *)(param_1 + 0xc) + (param_2 % *(uint *)(param_1 + 8)) * 4) * 0x1c
    ;
  }
  return iVar1;
}


```

