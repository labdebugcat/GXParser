# Selected Nova1492 Decompilation

## `00455350`

- Function: `FUN_00455350`
- Entry: `00455350`

```c

void __thiscall FUN_00455350(int param_1,int param_2,int param_3)

{
  int iVar1;
  
  if (param_2 != 0) {
    do {
      iVar1 = param_1;
      if (param_3 == 0) {
        return;
      }
      param_1 = *(int *)(iVar1 + 100);
    } while (*(int *)(iVar1 + 100) != 0);
    *(int *)(param_2 + 0x68) = iVar1;
    *(int *)(iVar1 + 100) = param_2;
    *(int *)(param_2 + 0x60) = param_3;
  }
  return;
}


```

## `00455500`

- Function: `FUN_00455500`
- Entry: `00455500`

```c

void __thiscall FUN_00455500(int param_1,int param_2,int param_3,int param_4)

{
  int iVar1;
  undefined4 uVar2;
  undefined4 *puVar3;
  uint uVar4;
  uint uVar5;
  undefined4 *puVar6;
  uint uVar7;
  undefined4 *puVar8;
  uint local_bc;
  undefined4 local_b0;
  undefined4 local_ac;
  undefined4 local_a8;
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
  undefined1 local_60 [16];
  undefined1 local_50 [76];
  
  uVar5 = 0;
  uVar4 = 0;
  uVar7 = 0;
  if (param_2 != 0) {
    uVar5 = *(uint *)(param_2 + 0xc);
  }
  if (param_3 != 0) {
    uVar4 = *(uint *)(param_3 + 0xc);
  }
  if (param_4 != 0) {
    uVar7 = *(uint *)(param_4 + 0xc);
  }
  if (uVar4 < uVar5) {
    uVar4 = uVar5;
  }
  if (uVar7 < uVar4) {
    uVar7 = uVar4;
  }
  if (uVar7 != 0) {
    if (*(int *)(param_1 + 0x4c) != 0) {
      FUN_00431540(*(int *)(param_1 + 0x4c));
      *(undefined4 *)(param_1 + 0x4c) = 0;
    }
    iVar1 = FUN_004316d0();
    if (*(int *)(param_1 + 0x4c) != 0) {
      FUN_00431540(*(int *)(param_1 + 0x4c));
    }
    *(int *)(param_1 + 0x4c) = iVar1;
    if (iVar1 == 0) {
      *(uint *)(param_1 + 0x40) = *(uint *)(param_1 + 0x40) & 0xfffffffb;
    }
    else {
      *(int *)(iVar1 + 8) = *(int *)(iVar1 + 8) + 1;
      *(uint *)(param_1 + 0x40) = *(uint *)(param_1 + 0x40) | 4;
    }
    FUN_00435c10(uVar7 + 1);
    local_bc = 0;
    puVar6 = (undefined4 *)(*(int *)(*(int *)(param_1 + 0x4c) + 4) + 0x1c);
    do {
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
      puVar3 = local_a0;
      puVar8 = puVar6 + -7;
      for (iVar1 = 0x10; iVar1 != 0; iVar1 = iVar1 + -1) {
        *puVar8 = *puVar3;
        puVar3 = puVar3 + 1;
        puVar8 = puVar8 + 1;
      }
      puVar6[-4] = *(undefined4 *)(param_1 + 0xc);
      *puVar6 = *(undefined4 *)(param_1 + 0x1c);
      puVar6[4] = *(undefined4 *)(param_1 + 0x2c);
      if (param_2 != 0) {
        FUN_00435a00(local_bc,&local_b0);
        puVar6[-4] = local_b0;
        *puVar6 = local_ac;
        puVar6[4] = local_a8;
      }
      if (param_3 != 0) {
        FUN_00435a00(local_bc,&local_b0);
        puVar6[-7] = local_b0;
        puVar6[-2] = local_ac;
        puVar6[3] = local_a8;
      }
      if (param_4 != 0) {
        FUN_00435a00(local_bc,local_60);
        uVar2 = FUN_00443e00(local_a0);
        puVar3 = (undefined4 *)FUN_00435620(local_50,uVar2);
        puVar8 = puVar6 + -7;
        for (iVar1 = 0x10; iVar1 != 0; iVar1 = iVar1 + -1) {
          *puVar8 = *puVar3;
          puVar3 = puVar3 + 1;
          puVar8 = puVar8 + 1;
        }
      }
      puVar6 = puVar6 + 0x10;
      local_bc = local_bc + 1;
    } while (local_bc <= uVar7);
  }
  return;
}


```

