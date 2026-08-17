# GX v2.6 투명 렌더 큐·Z-write 분석

## 실행 파일의 세 큐

GX 노드 순회 함수는 현재 프레임의 material slot을 선택한 뒤 `FUN_00470e40`에 draw 데이터를 제출한다. 이 함수는 최종 queue를 다음처럼 결정한다.

| 조건 | queue | Z-write |
|---|---:|---|
| blend selector가 0 | 0 | ON |
| selector가 0이 아니고 flags `0x100000` 설정 | 1 | ON |
| selector가 0이 아니고 `0x100000` 없음 | 2 | OFF |

큐 처리 순서는 0 → 1 → 2다. `FUN_0042c0a0`은 queue 2에 진입할 때만 `FUN_0042b98b(0)`을 호출해 `D3DRS_ZWRITEENABLE`을 끈다. 처리 완료 후 Z-write를 복구한다. 깊이 검사 자체는 계속 유지된다.

## 정렬 단위

`FUN_00470e40`이 queue entry에 저장하는 값은 material 식별자와 0x18바이트 draw record 배열이다. 카메라 거리나 view-space depth key는 저장하지 않는다.

- 같은 material entry가 이미 있으면 draw record를 그 entry에 추가한다.
- 없으면 현재 queue 끝에 새 entry를 추가한다.
- queue 처리도 배열의 저장 순서대로 수행한다.

따라서 확인된 GX 경로에는 mesh 중심 정렬이나 triangle별 back-to-front 정렬이 없다. 기존 Native의 거리 기반 mesh/triangle 정렬은 시각적 보정이었지만 클라이언트 재현은 아니었다.

## 전체 코퍼스 결과

설치된 GX 780개, material slot 57,161개를 전수 분류했다.

| queue | 슬롯 수 | 특징 |
|---:|---:|---|
| 0 | 4,909 | selector 0 |
| 1 | 12 | selector 2 + `0x100000` |
| 2 | 52,240 | selector 2/3/4, `0x100000` 없음 |

queue 1의 12개는 모두 `tree00.gx`부터 `tree08.gx` 계열의 `0x00150002` 재질이다. 이들은 foliage alpha mask를 사용하지만 Z-write를 유지하는 alpha-cutout 경로다. 기존 Native는 explicit alpha가 있다는 이유만으로 이 재질의 Z-write를 껐으므로 나무 잎 겹침과 다른 지형 오브젝트 사이의 깊이가 틀릴 수 있었다.

queue 2 세부 분포:

- selector 2: 12,908
- selector 3: 39,186
- selector 4: 146
- diffuse alpha 255 미만: 49,878
- explicit alpha texture: 23,110

## v2.6 구현

- `client_render_queue()`로 EXE와 같은 queue 분류를 추가했다.
- Native가 queue 0, 1, 2 순으로 mesh를 제출하고 각 큐 내부 원본 순서를 유지한다.
- queue 2에서만 `glDepthMask(GL_FALSE)`를 사용한다.
- alpha texture, glow, one-one, diffuse alpha만으로 queue를 추정하던 코드를 제거했다.
- mesh/triangle 카메라 깊이 정렬을 제거했다.
- Blender 재질에 `gx_render_queue`와 `gx_zwrite`를 보존한다.

## 검증 한계

실제 클라이언트 화면 A/B는 사용할 수 없지만, queue 분류·저장 구조·처리 순서·Z-write 전환은 EXE의 제출 함수와 소비 함수를 직접 연결해 확인했다. GPU/드라이버가 동일 깊이에서 만드는 미세한 rasterization 차이는 정적 분석 범위 밖이다.
