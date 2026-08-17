# Selected Nova1492 Decompilation

## `00426900`

- Function: `FUN_00426900`
- Entry: `00426900`

```c

void __thiscall FUN_00426900(char *param_1,FILE *param_2)

{
  uint uVar1;
  size_t sVar2;
  void *pvVar3;
  size_t sVar4;
  void *_DstBuf;
  undefined4 uVar5;
  uint _Count;
  void *pvVar6;
  int iVar7;
  uint local_28;
  int local_24;
  void *local_20;
  byte local_15;
  uint local_14;
  void *local_10;
  undefined1 *puStack_c;
  undefined4 uStack_8;
  
  uStack_8 = 0xffffffff;
  puStack_c = &LAB_00658bd0;
  local_10 = ExceptionList;
  uVar1 = DAT_007360c8 ^ (uint)&stack0xfffffffc;
  ExceptionList = &local_10;
  local_14 = uVar1;
  if (param_2 == (FILE *)0x0) goto LAB_00426a3f;
  FUN_00427090(uVar1);
  sVar2 = _fread(param_1,0x12,1,param_2);
  if (sVar2 != 0) {
    _fseek(param_2,0x12,0);
    switch(param_1[2]) {
    case '\x01':
    case '\x02':
    case '\t':
    case '\n':
      switch(param_1[0x10]) {
      case '\b':
      case '\x10':
      case '\x18':
      case ' ':
        if (((*param_1 == '\0') && (*(short *)(param_1 + 8) == 0)) &&
           (*(short *)(param_1 + 10) == 0)) {
          if (param_1[0x10] == '\b') {
            pvVar3 = (void *)FUN_0063ea48(0x300);
            *(void **)(param_1 + 0x1c) = pvVar3;
            sVar2 = _fread(pvVar3,0x300,1,param_2);
            if (sVar2 == 0) break;
          }
          _Count = (uint)((byte)param_1[0x10] >> 3);
          sVar2 = (uint)*(ushort *)(param_1 + 0xe) * (uint)*(ushort *)(param_1 + 0xc) * _Count;
          pvVar3 = (void *)FUN_0063ea48(sVar2);
          if ((param_1[2] == '\t') || (param_1[2] == '\n')) {
            local_24 = 0;
            _DstBuf = (void *)FUN_0063ea48(_Count);
            if ((uint)*(ushort *)(param_1 + 0xe) * (uint)*(ushort *)(param_1 + 0xc) != 0) {
              do {
                sVar4 = _fread(&local_15,1,1,param_2);
                if (sVar4 != 1) {
LAB_00426be7:
                  FID_conflict__free(_DstBuf);
                  FID_conflict__free(pvVar3);
                  goto switchD_0042697b_caseD_3;
                }
                if (local_15 < 0x80) {
                  local_15 = local_15 + 1;
                  local_28 = 0;
                  if (local_15 != 0) {
                    pvVar6 = (void *)(local_24 * _Count + (int)pvVar3);
                    do {
                      sVar4 = _fread(_DstBuf,1,_Count,param_2);
                      if (sVar4 != _Count) goto LAB_00426be7;
                      FUN_0062cfd0(pvVar6,_DstBuf,_Count);
                      local_28 = local_28 + 1;
                      local_24 = local_24 + 1;
                      pvVar6 = (void *)((int)pvVar6 + _Count);
                    } while ((int)local_28 < (int)(uint)local_15);
                  }
                }
                else {
                  local_15 = local_15 + 0x81;
                  sVar4 = _fread(_DstBuf,1,_Count,param_2);
                  if (sVar4 != _Count) goto LAB_00426be7;
                  local_28 = (uint)local_15;
                  if (local_28 != 0) {
                    pvVar6 = (void *)(local_24 * _Count + (int)pvVar3);
                    local_24 = local_24 + local_28;
                    do {
                      FUN_0062cfd0(pvVar6,_DstBuf,_Count);
                      pvVar6 = (void *)((int)pvVar6 + _Count);
                      local_28 = local_28 - 1;
                    } while (local_28 != 0);
                  }
                }
              } while (local_24 !=
                       (uint)*(ushort *)(param_1 + 0xe) * (uint)*(ushort *)(param_1 + 0xc));
            }
            FID_conflict__free(_DstBuf);
          }
          else {
            sVar4 = _fread(pvVar3,sVar2,1,param_2);
            if (sVar4 == 0) {
              FID_conflict__free(pvVar3);
              break;
            }
          }
          uVar5 = FUN_0063ea48(sVar2);
          *(undefined4 *)(param_1 + 0x18) = uVar5;
          local_15 = 0;
          if ((param_1[0x11] & 0x20U) == 0) {
            iVar7 = 0;
            if (*(short *)(param_1 + 0xe) != 0) {
              do {
                if (_Count - 1 < 4) {
                  FUN_00427150((void *)((uint)*(ushort *)(param_1 + 0xc) * iVar7 * _Count +
                                       (int)pvVar3),(uint)*(ushort *)(param_1 + 0xc),0,_Count - 1);
                }
                iVar7 = iVar7 + 1;
              } while (iVar7 < (int)(uint)*(ushort *)(param_1 + 0xe));
            }
            local_15 = 1;
          }
          else {
            FUN_0062cfd0(uVar5,pvVar3,sVar2);
          }
          if ((param_1[0x11] & 0x10U) != 0) {
            local_20 = pvVar3;
            if (local_15 != 0) {
              local_20 = *(void **)(param_1 + 0x18);
              uVar5 = FUN_0063ea48(sVar2);
              *(undefined4 *)(param_1 + 0x18) = uVar5;
            }
            iVar7 = 0;
            if (*(short *)(param_1 + 0xe) != 0) {
              do {
                if (_Count - 1 < 4) {
                  FUN_00427150((void *)((int)local_20 +
                                       (uint)*(ushort *)(param_1 + 0xc) * iVar7 * _Count),
                               (uint)*(ushort *)(param_1 + 0xc),1,_Count - 1);
                }
                iVar7 = iVar7 + 1;
              } while (iVar7 < (int)(uint)*(ushort *)(param_1 + 0xe));
            }
            if (local_15 != 0) {
              FID_conflict__free(local_20);
            }
          }
          FID_conflict__free(pvVar3);
          _fclose(param_2);
          goto LAB_00426a3f;
        }
      }
    }
  }
switchD_0042697b_caseD_3:
  FUN_00427090(uVar1);
LAB_00426a3f:
  ExceptionList = local_10;
  __security_check_cookie(local_14 ^ (uint)&stack0xfffffffc);
  return;
}


```

## `00426860`

- Function: `FUN_00426860`
- Entry: `00426860`

```c

uint __thiscall FUN_00426860(int param_1,undefined4 param_2,undefined4 param_3)

{
  int iVar1;
  uint uVar2;
  
  switch(*(undefined1 *)(param_1 + 0x10)) {
  case 8:
    iVar1 = FUN_00426780(param_2,param_3);
    return CONCAT31((int3)((uint)*(int *)(param_1 + 0x1c) >> 8),
                    *(undefined1 *)(iVar1 * 3 + 2 + *(int *)(param_1 + 0x1c)));
  default:
    return 0;
  case 0x10:
    uVar2 = FUN_00426780(param_2,param_3);
    return uVar2 >> 7 & 0xf8;
  case 0x18:
  case 0x20:
    uVar2 = FUN_00426780(param_2,param_3);
    return uVar2 >> 0x10;
  }
}


```

## `00427460`

- Function: `FUN_00427460`
- Entry: `00427460`

```c

int * __thiscall FUN_00427460(int *param_1,int *param_2)

{
  uint uVar1;
  uint *puVar2;
  uint uVar3;
  void *local_10;
  undefined1 *puStack_c;
  undefined4 local_8;
  
  puStack_c = &LAB_006592d0;
  local_10 = ExceptionList;
  uVar1 = DAT_007360c8 ^ (uint)&stack0xfffffffc;
  ExceptionList = &local_10;
  *param_1 = (int)&DAT_006b9e28;
  local_8 = 0xf;
  uVar3 = (uint)(param_2[1] - *param_2) >> 1;
  if (uVar3 == 0) {
    *param_1 = (int)&DAT_006b9e28;
  }
  else {
    puVar2 = (uint *)FUN_00640b8b(uVar3 * 2 + 4,2,4,uVar1);
    *param_1 = (int)(puVar2 + 1);
    *puVar2 = uVar3;
  }
  FUN_0062cfd0(*param_1,*param_2,param_2[1] - *param_2 & 0xfffffffe);
  uVar1 = (uint)(param_2[1] - *param_2) >> 1;
  FUN_00427730(uVar1,uVar1);
  ExceptionList = local_10;
  return param_1;
}


```

