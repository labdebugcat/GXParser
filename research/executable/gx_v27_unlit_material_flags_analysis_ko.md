# GX v2.7 unlit 재질·render flags 완결 분석

## D3D material과 조명

D3D9 device vtable에서 `IDirect3DDevice9::SetMaterial`은 슬롯 49, 바이트 오프셋 `+0xC4`다. EXE 전체 instruction을 조사한 결과 이 슬롯을 호출하는 명령은 하나도 없다.

장치 초기화 함수는 `SetRenderState(D3DRS_LIGHTING=137, FALSE)`를 실행한다. 상태 번호 `0x89`의 전체 사용 위치를 조사했으며 GX 렌더 구간에서 TRUE로 되돌리는 호출도 없다.

따라서 현재 클라이언트의 GX 렌더는 고정기능 조명을 사용하지 않는다.

## 6 DWORD의 런타임 사용 범위

GX에는 다음 값이 모두 직렬화돼 있다.

1. ambient ARGB
2. diffuse ARGB
3. specular ARGB
4. specular power float
5. emissive ARGB
6. render flags

그러나 현재 EXE의 draw 경로에서 직접 소비되는 것은 다음이다.

- diffuse: 로더가 RGB를 흰색으로 만들고 원래 alpha만 보존한 뒤 draw color/opacity로 사용
- render flags: blend selector, sampler address, render queue 결정

ambient/specular/power/emissive는 리더·라이터가 보존해야 할 포맷 데이터지만 `SetMaterial`로 GPU에 전달되지 않는다. 과거 클라이언트나 제작 도구와의 호환 필드일 가능성이 높다.

## render flags 전수 완결성

알려진 마스크는 다음과 같다.

| 비트 | 의미 |
|---:|---|
| `0x000000FF` | blend selector |
| `0x00010000` | U wrap |
| `0x00020000` | U mirror |
| `0x00040000` | V wrap |
| `0x00080000` | V mirror |
| `0x00100000` | alpha-cutout queue 1 |

설치된 780개 GX의 material slot 57,161개에 대해 아래 값을 계산했다.

```text
unknown = flags & ~(0x000000FF | 0x000F0000 | 0x00100000)
```

결과는 57,161개 모두 `unknown == 0`이다. 현재 코퍼스의 render flags는 위 의미만으로 100% 설명되며 남은 미확인 비트 조합은 없다.

## v2.7 표시 수정

기존 Blender 재질은 texture를 Principled Base Color에 연결해 환경광, 표면 노멀, specular highlight의 영향을 받았다. 이는 unlit인 현재 클라이언트와 다르다.

v2.7은 다음처럼 변경했다.

- Base Color를 검정으로 설정
- specular를 0으로 설정
- roughness를 1로 설정
- texture Color를 Principled Emission에 연결
- emission strength를 1로 설정
- 기존 alpha 연결과 render method는 유지
- `gx_lighting=false`, `gx_runtime_uses_d3d_material=false` 보존

Native OpenGL에도 `glDisable(GL_LIGHTING)`을 명시했다.

## 검증

- 실제 `tree00.gx`의 queue 1 재질을 Blender 5.2에서 생성했다.
- emission texture 연결, 검정 Base Color, specular 0을 확인했다.
- `gx_render_queue=1`, `gx_zwrite=true`를 함께 확인했다.
- Python 문법 검사 통과.
