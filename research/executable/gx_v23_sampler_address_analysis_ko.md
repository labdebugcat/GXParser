# GX v2.3 재질 sampler-address 분석

## 핵심 정정

이전 단계에서 D3D 장치 vtable `+0x114`를 texture-stage-state 호출로 본 해석은 잘못이었다. 현재 클라이언트는 Direct3D 9 인터페이스를 사용하며 해당 슬롯은 `IDirect3DDevice9::SetSamplerState`이다.

관련 슬롯은 다음과 같다.

| vtable 오프셋 | D3D9 메서드 |
|---:|---|
| `+0xE4` | `SetRenderState` |
| `+0x104` | `SetTexture` |
| `+0x108` | `GetTextureStageState` |
| `+0x10C` | `SetTextureStageState` |
| `+0x110` | `GetSamplerState` |
| `+0x114` | `SetSamplerState` |

따라서 `FUN_004618a0`에서 `(device, 0, 1/2, value)` 형태로 실행되는 코드는 texture color operation이 아니라 sampler 0의 U/V 주소 모드를 설정한다.

## render flags 상위 비트

재질의 여섯 번째 DWORD를 `flags`라고 할 때 클라이언트의 분기는 다음과 같다.

| 축 | 우선 비트 | 결과 | 차선 비트 | 결과 | 기본값 |
|---|---:|---|---:|---|---|
| U | `0x10000` | WRAP | `0x20000` | MIRROR | CLAMP |
| V | `0x40000` | WRAP | `0x80000` | MIRROR | CLAMP |

즉 `0x50000`은 U/V 모두 WRAP이고, `0x10000`은 U만 WRAP하고 V는 CLAMP한다. 하위 바이트의 blend selector와는 독립적인 필드다.

57,161개 material slot의 주요 분포는 다음과 같다.

| flags | 개수 | 주소 모드 및 하위 selector |
|---:|---:|---|
| `0x50003` | 31,755 | U wrap / V wrap / blend 3 |
| `0x50002` | 12,841 | U wrap / V wrap / blend 2 |
| `0x000003` | 5,184 | U clamp / V clamp / blend 3 |
| `0x10003` | 2,247 | U wrap / V clamp / blend 3 |
| `0x10000` | 1,945 | U wrap / V clamp |
| `0x000000` | 1,550 | U clamp / V clamp |
| `0x50000` | 1,414 | U wrap / V wrap |

특히 혼합 U/V 모드가 수천 개 존재하므로 모든 텍스처를 무조건 repeat 처리하면 atlas 경계가 번지거나 반대편 texel이 나타날 수 있다. GX 텍스처가 일부 모델에서 잘못 보이는 현상과 직접 연결될 수 있는 차이다.

## v2.3 구현

- Native OpenGL: face를 그릴 때 재질별로 `GL_TEXTURE_WRAP_S/T`를 `GL_REPEAT`, `GL_MIRRORED_REPEAT`, `GL_CLAMP_TO_EDGE` 중 하나로 설정한다.
- Blender: `gx_address_u`, `gx_address_v`를 재질 사용자 속성에 보존한다.
- 두 축이 같으면 Image Texture의 `REPEAT`, `EXTEND`, `MIRROR`를 사용한다.
- 두 축이 다르면 UV를 분리하고 WRAP=`FRACT`, MIRROR=`PINGPONG`, CLAMP=`MAXIMUM/MINIMUM` 노드로 축별 처리한 뒤 다시 결합한다.
- companion alpha texture에도 주 텍스처와 완전히 같은 좌표 입력을 연결한다.

## 검증

- 두 수정 Python 파일 문법 검사 통과.
- Blender 5.2.0 LTS에서 U wrap/V clamp 혼합 노드와 U/V mirror extension 생성 테스트 통과.
- 기존 XFI matrix-convention 회귀 테스트 통과.

이 문서의 sampler 해석은 이전 문서에 적힌 `+0x114 = texture-stage-state` 해석을 대체한다.
