# Nova1492 GX 재질 분석 업데이트

작성일: 2026-07-19

## 이번 단계에서 확정한 내용

- 설치 코퍼스 780개 GX에서 재질 슬롯 57,161개를 조사했다.
- 슬롯마다 저장된 6 DWORD는 현재 증거상 다음 구조와 일치한다.
  1. ambient ARGB
  2. diffuse/tint + opacity ARGB
  3. specular ARGB
  4. power/shininess float
  5. emissive ARGB
  6. render flags (상위/하위 16비트)
- 두 번째 DWORD의 알파는 0~255 전 범위에 분포한다. 다른 색 필드의 알파는 거의 항상 0 또는 255이므로, 두 번째 DWORD가 실제 재질 불투명도를 포함한다는 통계적 증거가 강하다.
- 네 번째 DWORD의 대표값은 float 0.0(51,747개), 0.05(2,691개), 20.0(1,329개), 17.0(882개)로, D3D 재질의 specular power와 일치한다.
- 여섯 번째 DWORD는 상위 16비트가 주로 5/0/1, 하위 16비트가 주로 3/2/0으로 갈린다. 정확한 D3D 렌더 상태 대응은 추가 역분석 대상이다.

## 구현 반영

- Native 뷰어와 Blender 애드온 모두 텍스처 색/알파에 재질 diffuse 색과 opacity를 곱한다.
- Blender 재질에 6개 필드를 개별 사용자 속성으로 보존한다.
- explicit alpha, TGA 자체 alpha, 누락 alpha의 luminance fallback이 모두 재질 opacity와 결합된다.
- glow/one-one 경로도 diffuse tint가 적용된 출력을 사용한다.
- 다중 재질 뒤의 배열을 면별 재질 인덱스로 취급하던 잘못된 Blender 로직을 제거했다. 이 배열은 코퍼스 증거와 리더 구조상 재질 애니메이션의 frame-to-slot map이다.
- 정지 상태에서는 frame map의 첫 슬롯을 전체 메시가 사용하고, 전체 맵은 `gx_material_frame_map` 속성에 보존한다.

## 실행 파일로 확정한 render flags

- `FUN_00460c80`은 여섯 번째 DWORD를 런타임 재질 구조체의 `+0x04` 플래그로 저장한다.
- 구형 `0xFFFF000E` 재질은 `0x10000`이 있으면 `0x40000`, `0x20000`이 있으면 `0x80000`도 자동으로 켠다.
- `FUN_004618a0`은 상위 플래그를 D3D9 stage 0의 `D3DTSS_COLOROP`와 `D3DTSS_COLORARG1`에 전달한다.
- 플래그 하위 바이트는 `FUN_0042b89f`의 블렌드 선택 인덱스다.
  - 1/2: `SRC_ALPHA / INV_SRC_ALPHA`
  - 3: `SRC_ALPHA / ONE` (glow/additive)
  - 4: `ONE / ONE` (fully additive)
- Native 뷰어와 Blender 애드온은 이제 GX 내부 선택값 1~4를 `gxdesc.ini`보다 우선한다.

## depth 및 렌더 큐

- `FUN_0042c0a0`은 제출된 GX draw item을 3개 큐(0, 1, 2) 순서로 처리한다.
- D3D9 상태 번호는 `14=ZWRITEENABLE`, `15=ALPHATESTENABLE`, `19=SRCBLEND`, `20=DESTBLEND`, `27=ALPHABLENDENABLE`로 확인했다.
- 불투명 큐에서는 Z-write를 켠다.
- 세 번째 투명 큐 진입 시 `FUN_0042b98b(0)`을 통해 Z-write를 끄고, 모든 큐 처리가 끝나면 다시 켠다. 깊이 검사 자체는 유지된다.
- Native 뷰어도 explicit alpha, material opacity, glow/one-one 항목에서 `glDepthMask(GL_FALSE)`를 사용하고 면 처리가 끝난 뒤 복구하도록 수정했다.
- 클라이언트처럼 Native도 불투명 메시를 원본 제출 순서로 먼저 그리고 투명 메시를 뒤에 그린다.
- 투명 메시는 현재 애니메이션 행렬과 카메라 yaw/pitch를 반영한 view-space 중심 깊이로 먼 것부터 정렬한다.
- 현재 정렬 단위는 메시다. 한 메시 내부에서 서로 교차하는 투명 삼각형의 개별 정렬은 하지 않는다.

## diffuse 필드 정정

- 파일의 두 번째 DWORD가 diffuse ARGB인 것은 맞지만 `FUN_00460c80`은 로드 직후 RGB를 `FFFFFF`로 덮고 원래 알파 바이트만 보존한다.
- 따라서 현재 클라이언트에서 이 필드는 texture tint가 아니라 material opacity로 작동한다.
- Native/Blender 구현에서 잘못 추가했던 RGB tint 곱셈을 제거하고 알파만 적용하도록 교정했다.

## 검증

- Python 문법 검사 통과.
- TGA 1,193개 전체 디코드 성공.
- palette/RLE TGA 18개, XRGB 32-bit 192개, ARGB 32-bit 22개 회귀 검사 통과.
- explicit alpha 합성 및 gxdesc의 normal/glow/one-one 모드 검사 통과.
- `mob_ef01.GX` 재렌더에서 검은 사각형 없이 반투명 분홍 효과가 유지된다.

## arm32_sppoo 관찰

- 5개 메시 모두 단일 재질이며 material frame map은 없다.
- 참조 텍스처는 `larm62.bmp`, `larm51.bmp`이고 UV는 정상화 범위 안에 있다.
- 따라서 렌더의 긴 두 판과 분리된 부품은 텍스처 디코딩/재질 슬롯 오류가 아니다. 원본 기하 또는 아직 완전히 확정되지 않은 GX 노드 조립 행렬 의미의 문제로 분리해 추적해야 한다.

## 남은 핵심 과제

- render flags의 정확한 D3D9 상태 대응
- material frame map과 `gxdesc.ini`의 `anispeed` 시간 단위 결합
- 노드 레코드의 scope와 로컬/월드 행렬 의미를 클라이언트 디컴파일로 재검증
- 투명 메시의 depth-write/depth-test 및 정렬 순서를 실제 게임과 대조

## anispeed 중간 확인

- `anispeed` 문자열의 참조는 `FUN_00464630`으로 모이며, 이 함수가 `gxdesc.ini` 항목을 읽어 기본값 `1.0f`인 런타임 메타데이터 필드에 저장한다.
- 설치 데이터에는 양수뿐 아니라 `-0.5`, `-1`, `-2.0`도 존재하므로 단순한 “프레임당 대기 초”가 아니라 방향을 포함하는 signed animation-rate multiplier로 보는 것이 타당하다.
- 메타데이터 레코드는 0x44바이트이고 시작 주소는 `0x0076604C`, anispeed는 레코드 `+0x18`에 저장된다.
- `blindarea.gx`는 `-2.0`이면서 11프레임 변환 애니메이션을, `mob20dam.gx`는 `1.0`이면서 16프레임 변환/재질 애니메이션을 가진다. 부호가 재생 방향, 절댓값이 재생률이라는 해석과 일치한다.
- Native 뷰어는 이제 `80ms / abs(anispeed)` 간격으로 진행하며 음수이면 프레임을 역방향으로 순환한다. 0이면 정지한다.
- Blender 가져오기는 각 메시 오브젝트에 `gx_anispeed` 값을 보존한다. Blender 키프레임 시간 재매핑은 내보내기 왕복 보존과 충돌할 수 있어 자동 적용하지 않았다.
