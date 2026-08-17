# Selected Nova1492 Decompilation

## `00427b20`

- Function: `FUN_00427b20`
- Entry: `00427b20`

```c

void FUN_00427b20(undefined4 param_1,undefined4 param_2,undefined4 param_3)

{
  undefined4 uVar1;
  
  FUN_00428380();
  uVar1 = FUN_004a4d00(param_2,param_3);
  FUN_00427bc0(uVar1,param_1);
  return;
}


```

## `00427bc0`

- Function: `FUN_00427bc0`
- Entry: `00427bc0`

```c

void __thiscall FUN_00427bc0(undefined4 *param_1,FILE *param_2,byte param_3)

{
  ushort uVar1;
  uint uVar2;
  long _Offset;
  int iVar3;
  int *_DstBuf;
  uint uVar4;
  uint uVar5;
  uint uVar6;
  int iVar7;
  int local_20;
  uint local_1c;
  void *local_10;
  undefined1 *puStack_c;
  undefined4 local_8;
  
  local_8 = 0xffffffff;
  puStack_c = &LAB_00659608;
  local_10 = ExceptionList;
  uVar2 = DAT_007360c8 ^ (uint)&stack0xfffffffc;
  ExceptionList = &local_10;
  if ((param_2 != (FILE *)0x0) &&
     (uVar4 = uVar2, _fread(param_1 + 10,0xe,1,param_2), *(short *)(param_1 + 10) == 0x4d42)) {
    _Offset = FUN_0063583d(param_2,uVar4);
    _fseek(param_2,0,2);
    iVar3 = FUN_0063583d(param_2);
    param_1[9] = iVar3 + -0xe;
    _fseek(param_2,_Offset,0);
    _DstBuf = (int *)FUN_0063ea48(param_1[9]);
    _fread(_DstBuf,param_1[9],1,param_2);
    _fclose(param_2);
    param_1[5] = _DstBuf;
    *param_1 = _DstBuf;
    param_1[1] = _DstBuf;
    param_1[4] = 1 << (*(byte *)((int)_DstBuf + 0xe) & 0x1f);
    param_1[3] = *(int *)((int)param_1 + 0x32) + -0xe + (int)_DstBuf;
    param_1[2] = *_DstBuf + (int)_DstBuf;
    param_1[7] = _DstBuf[1];
    param_1[8] = _DstBuf[2];
    param_1[6] = (uint)param_3;
    if (param_3 != 0) {
      uVar1 = *(ushort *)((int)_DstBuf + 0xe);
      uVar6 = param_1[8] + 1 >> 1;
      uVar5 = param_1[7] * (uint)uVar1 >> 3;
      uVar4 = (uint)(uVar1 >> 3) * param_1[7] & 3;
      if (uVar4 != 0) {
        uVar5 = uVar5 + (4 - uVar4);
      }
      if (uVar1 != 1) {
        FUN_00427d90(uVar5);
        local_8 = 0;
        local_1c = 0;
        if (uVar6 != 0) {
          local_20 = 0;
          do {
            iVar3 = local_20 + param_1[3];
            iVar7 = ((param_1[8] - local_1c) + -1) * uVar5 + param_1[3];
            FUN_0062cfd0(0,iVar7,uVar5);
            FUN_0062cfd0(iVar7,iVar3,uVar5);
            FUN_0062cfd0(iVar3,0,uVar5);
            local_1c = local_1c + 1;
            local_20 = local_20 + uVar5;
          } while (local_1c < uVar6);
        }
        local_8 = 0xffffffff;
        FUN_0059c360(0xfffffffc);
      }
    }
  }
  ExceptionList = local_10;
  __security_check_cookie(uVar2 ^ (uint)&stack0xfffffffc);
  return;
}


```

