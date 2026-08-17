# Nova1492 GX 분석 v3.15 — 큐별 유효 블렌드 selector

## 재질 적용 함수의 두 번째 인자

`FUN_004618A0(material, mode)`의 mode는 단순 플래그가 아니라 실제 blend selector 선택 방식을 바꾼다.

```text
mode == 0: alpha blend disable
mode == 1: material에 저장된 selector byte 사용
mode >= 2: mode 자체를 selector로 사용
```

함수 마지막에서는 mode가 0이 아니고, mode 1일 때 저장 selector가 0이 아닌 경우 알파 블렌드를 활성화한다. mode 2는 항상 알파 블렌드를 활성화한다.

## GX 큐 소비 경로

`FUN_0042C0A0`의 실제 호출은 다음과 같다.

| 큐 | 재질 적용 호출 | 유효 selector |
|---:|---|---:|
| 0 | `FUN_004618A0(material, 2)` | 강제 2 |
| 1 | `FUN_004618A0(material, 2)` | 강제 2 |
| 2 | `FUN_004618A0(material, 1)` | 재질 하위 바이트 |

따라서 저장 selector가 0인 queue 0 재질도 렌더 시에는 selector 2의 `SRC_ALPHA / INV_SRC_ALPHA`를 사용한다. queue 1 역시 강제 selector 2다.

## selector 1과 2

블렌드 점프 테이블에서 selector 1과 2는 모두 `0x0042B8BF`로 연결된다.

```text
D3DRS_SRCBLEND  = 5  (SRC_ALPHA)
D3DRS_DESTBLEND = 6  (INV_SRC_ALPHA)
```

두 값은 이 실행 파일의 blend factor 결과가 같다. 차이는 호출자가 selector를 선택하는 문맥 및 저장값 호환성에 있다.

## 구현 반영

- `client_effective_blend_selector()`를 추가했다.
- Native blend mode는 저장 selector가 아니라 큐를 반영한 유효 selector로 결정한다.
- Blender 재질에 원본 `gx_blend_selector`와 실제 `gx_effective_blend_selector`를 모두 기록한다.

기존 화면 결과에서 selector 0이 normal blend였던 것은 맞았지만, 이제 그 근거가 queue 0의 강제 selector 2 호출로 코드에 명시됐다.
