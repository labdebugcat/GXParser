# GX v2.8 blend·texture-stage 방정식 분석

## blend selector jump table

`FUN_0042b89f`는 selector를 캐시한 뒤 `0x0042B95B + selector*4`의 jump table로 분기한다. jump table과 case 코드를 직접 디스어셈블한 결과는 다음과 같다.

| selector | D3DRS_SRCBLEND | D3DRS_DESTBLEND | 식 |
|---:|---|---|---|
| 0 | 상태 유지 | 상태 유지 | 초기 normal 상태 사용 |
| 1 | SRC_ALPHA (5) | INV_SRC_ALPHA (6) | `Cs*As + Cd*(1-As)` |
| 2 | SRC_ALPHA (5) | INV_SRC_ALPHA (6) | `Cs*As + Cd*(1-As)` |
| 3 | SRC_ALPHA (5) | ONE (2) | `Cs*As + Cd` |
| 4 | ONE (2) | ONE (2) | `Cs + Cd` |

selector 0은 factor를 변경하지 않는다. GX queue 0이 먼저 처리되고 초기 factor가 SRC_ALPHA/INV_SRC_ALPHA이므로 실제 결과는 normal blend다.

현재 설치 코퍼스에는 selector 0, 2, 3, 4가 있고 selector 1은 없다. 리더와 렌더러는 구형 파일 호환을 위해 selector 1도 normal로 처리한다.

## alpha blend enable

`FUN_004618a0`은 material draw에서 `D3DRS_ALPHABLENDENABLE(27)`을 활성화한다. selector 0 재질은 대부분 alpha 255이므로 normal blend가 불투명 복사와 같은 결과를 낸다. alpha test는 별도의 `GREATER 10` 또는 호환 `NOTEQUAL 0` 상태다.

## texture stage 0

장치 초기화의 `SetTextureStageState` 호출은 다음과 같다.

| state | 값 | 의미 |
|---|---:|---|
| COLOROP (1) | 4 | MODULATE |
| COLORARG1 (2) | 2 | TEXTURE |
| COLORARG2 (3) | 0 | DIFFUSE |
| ALPHAOP (4) | 4 | MODULATE |
| ALPHAARG1 (5) | 2 | TEXTURE |
| ALPHAARG2 (6) | 0 | DIFFUSE |

따라서 source fragment는 다음과 같다.

```text
source.rgb = texture.rgb * diffuse.rgb
source.a   = texture.a   * diffuse.a
```

현재 EXE의 GX material loader는 serialized diffuse RGB를 흰색으로 덮으므로 일반 GX 결과는 texture RGB 그대로다. diffuse alpha는 유지되어 texture alpha와 곱해진다. companion alpha 이미지는 texture object 생성 시 alpha channel로 결합된다.

## v2.8 수정

- Native에서 slot이 존재하면 selector 0도 명시적으로 normal blend로 결정한다.
- selector가 없는 legacy/non-material 경로에서만 gxdesc fallback을 사용한다.
- Blender에 `gx_blend_selector`, `gx_src_blend`, `gx_dst_blend`, `gx_alpha_blend_enabled`를 저장한다.
- 기존 unlit emission과 alpha 연결은 위 source 방정식을 유지한다.

## 검증

- jump table 포인터와 selector case 코드를 Ghidra에서 직접 추출했다.
- Native selector 0~4 mapping 단위 검사 통과.
- 실제 `tree00.gx` selector 2 재질에서 SRC_ALPHA/INV_SRC_ALPHA 메타데이터 확인.
