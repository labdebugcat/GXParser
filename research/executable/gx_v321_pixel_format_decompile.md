# Selected Nova1492 Decompilation

## `00427ab0`

- Function: `FUN_00427ab0`
- Entry: `00427ab0`

```c

undefined4 * __fastcall FUN_00427ab0(undefined4 *param_1)

{
  param_1[2] = 0;
  param_1[5] = 0;
  *param_1 = 0;
  param_1[1] = 0;
  param_1[3] = 0;
  param_1[4] = 0;
  param_1[9] = 0;
  param_1[7] = 0;
  param_1[8] = 0;
  param_1[6] = 1;
  param_1[10] = 0;
  param_1[0xb] = 0;
  param_1[0xc] = 0;
  *(undefined2 *)(param_1 + 0xd) = 0;
  return param_1;
}


```

## `00428480`

- Function: `FUN_00428480`
- Entry: `00428480`

```c

int __thiscall FUN_00428480(int param_1,int param_2,int param_3)

{
  uint uVar1;
  uint uVar2;
  
  uVar2 = (uint)(*(ushort *)(*(int *)(param_1 + 4) + 0xe) >> 3);
  if (uVar2 == 0) {
    uVar1 = *(int *)(param_1 + 0x1c) + 0x1fU >> 3;
  }
  else {
    uVar1 = *(int *)(param_1 + 0x1c) * uVar2 + 3 & 0xfffffffc;
  }
  if (uVar2 == 1) {
    return CONCAT31((int3)((uint)*(int *)(param_1 + 8) >> 8),
                    *(undefined1 *)
                     (*(int *)(param_1 + 8) + 2 +
                     (uint)*(byte *)(uVar1 * param_3 + *(int *)(param_1 + 0xc) + param_2) * 4));
  }
  if (uVar2 == 2) {
    return (*(byte *)(uVar1 * param_3 + param_2 * 2 + 1 + *(int *)(param_1 + 0xc)) & 0x7c) * 2;
  }
  if ((uVar2 != 3) && (uVar2 != 4)) {
    return CONCAT31((int3)((uint)*(int *)(param_1 + 4) >> 8),0xff);
  }
  return CONCAT31((int3)((uint)*(int *)(param_1 + 0xc) >> 8),
                  *(undefined1 *)(uVar2 * param_2 + uVar1 * param_3 + 2 + *(int *)(param_1 + 0xc)));
}


```

## `0046fa00`

- Function: `FUN_0046fa00`
- Entry: `0046fa00`

```c

void __thiscall
FUN_0046fa00(uint *param_1,uint param_2,undefined4 param_3,uint param_4,uint param_5,uint param_6,
            int param_7,undefined4 param_8)

{
  uint uVar1;
  undefined4 local_224;
  undefined1 local_220 [524];
  int local_14;
  undefined4 local_10;
  uint local_c;
  
  local_c = DAT_007360c8 ^ (uint)&local_224;
  param_1[2] = 0;
  if (((param_4 & param_4 - 1) == 0) && ((param_5 & param_5 - 1) == 0)) {
    uVar1 = FUN_00432c60(param_3);
    param_1[0x108] = uVar1;
    if (uVar1 != 0xffffffff) {
      if (param_7 != 0) {
        local_224 = 0x5c;
        local_14 = 0;
        local_10 = 0;
        FUN_00433710(&local_14,&local_224);
        if (local_14 != 0) {
          param_7 = local_14 + 2;
          param_8 = local_10;
        }
        FUN_00470310(&param_7);
        FUN_004703b0(local_220);
      }
      FUN_0046ccf0();
      *param_1 = param_4;
      param_1[1] = param_5;
      param_1[0x111] = param_6 & 0xf000 | param_2 & 0xf00000;
      __security_check_cookie(local_c ^ (uint)&local_224);
      return;
    }
  }
  else {
    FUN_004d8000();
  }
  __security_check_cookie(local_c ^ (uint)&local_224);
  return;
}


```

