# Selected Nova1492 Decompilation

## `00435620`

- Function: `FUN_00435620`
- Entry: `00435620`

```c

void __thiscall FUN_00435620(float *param_1,int param_2,float *param_3)

{
  float *pfVar1;
  float fVar2;
  float fVar3;
  float fVar4;
  float fVar5;
  float fVar6;
  float fVar7;
  float fVar8;
  float fVar9;
  float fVar10;
  float fVar11;
  float fVar12;
  float fVar13;
  float fVar14;
  float fVar15;
  float fVar16;
  float fVar17;
  int iVar18;
  
  iVar18 = 4;
  param_2 = param_2 - (int)param_1;
  do {
    fVar2 = *param_1;
    fVar3 = param_1[1];
    fVar4 = param_1[2];
    fVar5 = param_1[3];
    fVar6 = param_3[5];
    fVar7 = param_3[6];
    fVar8 = param_3[7];
    fVar9 = param_3[1];
    fVar10 = param_3[2];
    fVar11 = param_3[3];
    fVar12 = param_3[9];
    fVar13 = param_3[10];
    fVar14 = param_3[0xb];
    fVar15 = param_3[0xd];
    fVar16 = param_3[0xe];
    fVar17 = param_3[0xf];
    pfVar1 = (float *)(param_2 + (int)param_1);
    *pfVar1 = fVar3 * param_3[4] + fVar2 * *param_3 + fVar4 * param_3[8] + fVar5 * param_3[0xc];
    pfVar1[1] = fVar3 * fVar6 + fVar2 * fVar9 + fVar4 * fVar12 + fVar5 * fVar15;
    pfVar1[2] = fVar3 * fVar7 + fVar2 * fVar10 + fVar4 * fVar13 + fVar5 * fVar16;
    pfVar1[3] = fVar3 * fVar8 + fVar2 * fVar11 + fVar4 * fVar14 + fVar5 * fVar17;
    param_1 = param_1 + 4;
    iVar18 = iVar18 + -1;
  } while (iVar18 != 0);
  return;
}


```

