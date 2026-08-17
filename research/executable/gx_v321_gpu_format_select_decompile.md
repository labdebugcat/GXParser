# Selected Nova1492 Decompilation

## `00432e00`

- Function: `FUN_00432e00`
- Entry: `00432e00`

```c

undefined4 FUN_00432e00(undefined4 *param_1,undefined4 *param_2)

{
  char cVar1;
  
  do {
    if (param_1 == param_2) {
      return 0xffffffff;
    }
    switch(*param_1) {
    case 2:
      cVar1 = DAT_00784474;
      break;
    case 3:
      cVar1 = DAT_00784475;
      break;
    case 4:
      cVar1 = DAT_00784470;
      break;
    case 5:
      cVar1 = DAT_00784471;
      break;
    default:
      goto switchD_00432e2a_caseD_6;
    case 7:
      cVar1 = DAT_00784472;
      break;
    case 8:
      cVar1 = DAT_00784473;
    }
    if (cVar1 != '\0') {
      return *param_1;
    }
switchD_00432e2a_caseD_6:
    param_1 = param_1 + 1;
  } while( true );
}


```

