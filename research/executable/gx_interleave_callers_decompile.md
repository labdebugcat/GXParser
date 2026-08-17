# Selected Nova1492 Decompilation

## `0042c5b0`

- Function: `FUN_0042c560`
- Entry: `0042c560`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_0042c560(void)

{
  int *piVar1;
  undefined4 *puVar2;
  int iVar3;
  int iVar4;
  int iVar5;
  int *piVar6;
  undefined4 uVar7;
  uint uVar8;
  undefined4 *puVar9;
  bool bVar10;
  
  iVar5 = DAT_00761cec;
  if (DAT_00761cec != 0) {
    FUN_00480b30();
    piVar6 = &DAT_008b2320;
    piVar1 = &DAT_00764380;
    uVar8 = 0x3c;
    do {
      if (*piVar6 != *piVar1) {
        uVar7 = 1;
        goto LAB_0042c5a7;
      }
      piVar6 = piVar6 + 1;
      piVar1 = piVar1 + 1;
      bVar10 = 3 < uVar8;
      uVar8 = uVar8 - 4;
    } while (bVar10);
    uVar7 = 0;
LAB_0042c5a7:
    puVar2 = &DAT_00764380;
    puVar9 = &DAT_008b2320;
    for (iVar3 = 0x10; iVar3 != 0; iVar3 = iVar3 + -1) {
      *puVar9 = *puVar2;
      puVar2 = puVar2 + 1;
      puVar9 = puVar9 + 1;
    }
    FUN_004804a0();
    puVar2 = &DAT_00764380;
    puVar9 = &DAT_00736d50;
    for (iVar3 = 0x10; iVar3 != 0; iVar3 = iVar3 + -1) {
      *puVar9 = *puVar2;
      puVar2 = puVar2 + 1;
      puVar9 = puVar9 + 1;
    }
    puVar2 = (undefined4 *)FUN_004d4960(&DAT_00736d90);
    puVar9 = &DAT_00736d10;
    for (iVar3 = 0x10; iVar3 != 0; iVar3 = iVar3 + -1) {
      *puVar9 = *puVar2;
      puVar2 = puVar2 + 1;
      puVar9 = puVar9 + 1;
    }
    DAT_00736dd0 = DAT_00736dd0 + 1;
    bVar10 = DAT_00784580 != '\0';
    puVar2 = &DAT_00736d90;
    puVar9 = &DAT_00736e20 + DAT_00736dd0 * 0x10;
    for (iVar3 = 0x10; iVar3 != 0; iVar3 = iVar3 + -1) {
      *puVar9 = *puVar2;
      puVar2 = puVar2 + 1;
      puVar9 = puVar9 + 1;
    }
    if (bVar10) {
      FUN_00431bf0(1,0);
      DAT_00784580 = '\0';
      _DAT_00784574 = 0x101;
    }
    FUN_004388f0();
    FUN_00445b40(uVar7);
    FUN_0042e6c0();
    FUN_00446940();
    FUN_0042c0a0(iVar5,0,0);
    FUN_0044bed0();
    if (DAT_00761cd0 != 0) {
      FUN_00431bf0(5,0);
      FUN_00472d90();
    }
    iVar3 = DAT_00761cd0;
    iVar5 = DAT_00736dd0 * 0x10;
    puVar2 = &DAT_00736e20 + iVar5;
    puVar9 = &DAT_00736d90;
    for (iVar4 = 0x10; iVar4 != 0; iVar4 = iVar4 + -1) {
      *puVar9 = *puVar2;
      puVar2 = puVar2 + 1;
      puVar9 = puVar9 + 1;
    }
    DAT_00736dd0 = DAT_00736dd0 + -1;
    puVar2 = (undefined4 *)FUN_004d4960(&DAT_00736e20 + iVar5);
    bVar10 = DAT_0078443c == '\0';
    puVar9 = &DAT_00736d10;
    for (iVar5 = 0x10; iVar5 != 0; iVar5 = iVar5 + -1) {
      *puVar9 = *puVar2;
      puVar2 = puVar2 + 1;
      puVar9 = puVar9 + 1;
    }
    if (((bVar10) || (iVar3 == 0)) || (*(int *)(iVar3 + 0x20) != 6)) {
      FUN_0042c720();
    }
    FUN_0042dcc0();
    if (DAT_0078447c != 4) {
      DAT_0078447c = 4;
      (**(code **)(*DAT_007848dc + 0x10c))(DAT_007848dc,0,1,4);
    }
  }
  return;
}


```

## `0044bed0`

- Function: `FUN_0044bed0`
- Entry: `0044bed0`

```c

void FUN_0044bed0(void)

{
  DAT_007b6bb8 = 0;
  DAT_007b78dc = 0;
  DAT_007ba048 = 0;
  DAT_007bad6c = 0;
  DAT_007bba90 = 0;
  DAT_007bc7b4 = 0;
  DAT_007bd4d8 = 0;
  DAT_007be1fc = 0;
  DAT_007b8600 = 0;
  DAT_007c0184 = 0;
  DAT_007c0ea8 = 0;
  DAT_007c1e6c = 0;
  DAT_007c2170 = 0;
  DAT_007c2474 = 0;
  return;
}


```

## `004541e0`

- Function: `FUN_004541e0`
- Entry: `004541e0`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void __thiscall
FUN_004541e0(int param_1,uint param_2,undefined4 param_3,undefined4 param_4,undefined4 param_5)

{
  longlong lVar1;
  uint uVar2;
  float fVar3;
  int extraout_EDX;
  float10 fVar4;
  float10 fVar5;
  undefined4 uVar6;
  undefined4 uVar7;
  undefined4 uVar8;
  undefined4 uVar9;
  undefined1 auStack_28 [4];
  uint local_24;
  undefined4 uStack_20;
  undefined4 local_1c;
  undefined4 local_18;
  undefined4 local_14;
  uint local_10;
  uint local_8;
  
  local_8 = DAT_007360c8 ^ (uint)auStack_28;
  if ((param_2 & 0x100000) == 0) {
    uVar2 = *(uint *)(param_1 + 0x44);
    if ((((0x2b4 < uVar2) || (uVar2 * 0x44 == -0x76604c)) ||
        (((&DAT_0076606c)[uVar2 * 0x11] & 8) == 0)) || (*(int *)(param_1 + 0x58) == 0))
    goto LAB_004542fa;
    uVar9 = (&DAT_00766078)[uVar2 * 0x11];
    uVar7 = *(undefined4 *)(&DAT_00766080 + uVar2 * 0x44);
    uVar8 = (&DAT_00766074)[uVar2 * 0x11];
    param_2 = param_2 | (&DAT_0076606c)[uVar2 * 0x11] & 0x3f000000;
    local_14 = (&DAT_0076608c)[uVar2 * 0x11];
    uVar6 = (&DAT_0076607c)[uVar2 * 0x11];
    local_10 = param_2;
    fVar4 = (float10)FUN_00480070(uVar6,uVar7,uVar8,uVar9);
    fVar5 = (float10)*(int *)(extraout_EDX + 0x28);
    if (*(int *)(extraout_EDX + 0x28) < 0) {
      fVar5 = fVar5 + (float10)_DAT_006daed8;
    }
    lVar1 = (longlong)ROUND(fVar5 + fVar4 * (float10)_DAT_006dae94);
    local_24 = (uint)lVar1;
    local_24 = local_24 % (uint)(&DAT_00766088)[uVar2 * 0x11];
    uStack_20 = (undefined4)((ulonglong)lVar1 >> 0x20);
    fVar3 = (float)(int)local_24;
    if ((int)local_24 < 0) {
      fVar3 = fVar3 + _DAT_006daed8;
    }
    FUN_00453f60(fVar3 * (float)(&DAT_00766084)[uVar2 * 0x11],uVar6,uVar7,uVar8,uVar9);
  }
  else {
    local_1c = param_4;
    local_18 = param_5;
    local_14 = param_3;
    local_10 = param_2;
  }
  FUN_00457140(&local_1c);
LAB_004542fa:
  FUN_0042c0a0(param_1,param_2,1);
  __security_check_cookie(local_8 ^ (uint)auStack_28);
  return;
}


```

