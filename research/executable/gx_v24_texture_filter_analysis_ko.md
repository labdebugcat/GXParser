# GX v2.4 텍스처 필터 분석

## 결론

Nova1492의 GX 모델 텍스처 경로는 다음 sampler filter를 사용한다.

| 상태 | D3D9 값 | 의미 |
|---|---:|---|
| `D3DSAMP_MAGFILTER` (5) | 2 | `D3DTEXF_LINEAR` |
| `D3DSAMP_MINFILTER` (6) | 2 | `D3DTEXF_LINEAR` |
| `D3DSAMP_MIPFILTER` (7) | 별도 설정 없음 | mipmap 미사용 |

Native의 `GL_TEXTURE_MAG_FILTER=GL_LINEAR`, `GL_TEXTURE_MIN_FILTER=GL_LINEAR` 및 단일 레벨 업로드는 이 동작과 일치한다.

## 근거 연결

1. 장치 초기화 함수 `FUN_0042ecbb`는 sampler 0의 MIN/MAG를 값 1(POINT)로 초기화한다.
2. GX 재질 로더 `FUN_00460c80`의 모든 확인된 텍스처 생성 경로는 `FUN_0042a5cd(..., 0x3000)` 또는 `FUN_0042aaf5(0x3000, ...)`를 사용한다.
3. 실제 바인딩 함수 `FUN_0046cd50`은 texture object `+0x444` 플래그를 검사한다.
4. `0x1000`이 있으면 sampler state 5(MAG)를 값 2(LINEAR)로 설정한다.
5. `0x2000`이 있으면 sampler state 6(MIN)를 값 2(LINEAR)로 설정한다.
6. GX 생성 플래그 `0x3000`에는 두 비트가 모두 있으므로 실제 draw 시점에는 MAG/MIN 모두 LINEAR가 된다.
7. 같은 GX 경로에서 sampler state 7(MIPFILTER)을 변경하는 호출은 확인되지 않았다.

초기 POINT 상태만 보고 모델 텍스처가 nearest filtering이라고 결론 내리면 안 된다. 텍스처 바인딩 시 객체별 플래그가 최종 상태를 덮어쓴다.

## 전역 호출 조사

EXE 명령 전체에서 vtable 오프셋 `0x114`를 사용하는 instruction을 수집하고 호출 함수들을 디컴파일했다. GX 관련 상태 변경은 다음 세 계층으로 분류된다.

- 장치 초기화: MIN/MAG POINT 및 U/V CLAMP 기본값.
- 재질 적용 `FUN_004618a0`: 재질 render flags에 따른 ADDRESSU/ADDRESSV.
- 텍스처 바인딩 `FUN_0046cd50`: texture object 플래그에 따른 MAG/MIN POINT 또는 LINEAR.

그 외 호출들은 UI·특수 렌더 경로의 주소 모드 임시 변경이며 GX texture object의 필터 의미를 바꾸지 않는다.

## v2.4 반영

- Native 설정은 이미 정확했으므로 동작 변경 없이 역분석 근거를 코드 주석으로 고정했다.
- Blender의 주 텍스처와 explicit alpha texture를 모두 Linear interpolation으로 명시했다.
- Blender 재질에 `gx_mag_filter=LINEAR`, `gx_min_filter=LINEAR`, `gx_mip_filter=NONE`을 기록한다.

## 검증

- Ghidra scalar `0x114` 전역 instruction 조사 완료.
- sampler 호출 함수 14개 후보 디컴파일 및 분류.
- Python 문법 검사 통과.
- Blender 5.2 sampler 회귀 테스트 통과.
