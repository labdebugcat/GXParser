# Selected Nova1492 Decompilation

## `0042b89f`

- Function: `FUN_0042b89f`
- Entry: `0042b89f`

```c

void __thiscall FUN_0042b89f(int param_1,int param_2)

{
  if (*(int *)(param_1 + 0x20240) != param_2) {
    *(int *)(param_1 + 0x20240) = param_2;
                    /* WARNING: Could not recover jumptable at 0x0042b8b8. Too many branches */
                    /* WARNING: Treating indirect jump as call */
    (**(code **)(&DAT_0042b95b + param_2 * 4))();
    return;
  }
  return;
}


```

