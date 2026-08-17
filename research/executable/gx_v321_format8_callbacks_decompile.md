# Selected Nova1492 Decompilation

## `005ae910`

- No function found.

## `005ae880`

- Function: `FUN_005ae880`
- Entry: `005ae880`

```c

void __thiscall FUN_005ae880(uint *param_1,undefined4 param_2)

{
  uint uVar1;
  uint uVar2;
  undefined4 *puVar3;
  undefined4 *puVar4;
  uint uVar5;
  uint uVar6;
  undefined4 local_c;
  
  uVar1 = param_1[2];
  uVar2 = param_1[3];
  puVar3 = (undefined4 *)*param_1;
  local_c._3_1_ = (undefined1)((uint)param_2 >> 0x18);
  local_c._0_3_ = CONCAT12((char)param_2,(short)((uint)param_2 >> 8) << 8);
  local_c = CONCAT31(local_c._1_3_,(char)((uint)param_2 >> 0x10));
  puVar4 = (undefined4 *)(param_1[4] * uVar1 + (int)puVar3);
  if (puVar3 != puVar4) {
    do {
      uVar5 = 0;
      uVar6 = uVar2 * 4 + 3 >> 2;
      if (puVar3 + uVar2 < puVar3) {
        uVar6 = 0;
      }
      if (uVar6 != 0) {
        do {
          *puVar3 = local_c;
          uVar5 = uVar5 + 1;
          puVar3 = puVar3 + 1;
        } while (uVar5 != uVar6);
      }
      puVar3 = (undefined4 *)((int)puVar3 + uVar1 + uVar2 * -4);
    } while (puVar3 != puVar4);
  }
  return;
}


```

## `005aec70`

- No function found.

## `005aefc0`

- No function found.

