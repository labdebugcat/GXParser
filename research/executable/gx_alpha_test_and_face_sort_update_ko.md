# GX 알파 테스트·투명 삼각형 정렬 분석 갱신

## 실행 파일에서 확정한 상태

- 렌더러 초기화 함수 `FUN_0042eac0`에서 D3D9 상태 `15=ALPHATESTENABLE`, `24=ALPHAREF`, `25=ALPHAFUNC` 설정을 확인했다.
- 렌더러 모드 플래그가 0이면 `ALPHAREF=0`, `ALPHAFUNC=NOTEQUAL(6)`이다. 알파가 정확히 0인 픽셀을 버린다.
- 모드 플래그가 1이면 `ALPHAREF=10`, `ALPHAFUNC=GREATER(5)`이다. 8비트 알파가 10 이하인 픽셀을 버린다.
- 이는 재질별 플래그가 아니라 렌더러 전역 품질 경로이다.

## 구현 반영

- Native 뷰어에는 더 엄격한 클라이언트 경로인 `GL_GREATER, 10/255`를 적용했다. 완전 투명하거나 거의 투명한 가장자리 픽셀이 깊이·블렌드 단계에 들어가 생기는 테두리를 줄인다.
- Blender 재질에는 정확한 상태를 `gx_alpha_test_ref=10`, `gx_alpha_test_func=GREATER` 사용자 속성으로 보존하며 DITHERED 투명 렌더링을 사용한다.
- Native 뷰어의 투명 정렬을 메시 단위에서 삼각형 단위까지 확장했다. 현재 애니메이션 변환과 카메라 yaw/pitch를 반영한 view-space 중심 깊이로 투명 삼각형을 뒤에서 앞으로 그린다.
- normal, glow, one-one 및 explicit-alpha 경로 모두 기존의 투명 메시 판정과 깊이 쓰기 차단을 유지한다.

## 검증

- Python 문법 검사 통과.
- TGA 분류·디코딩 및 explicit-alpha 합성 회귀 테스트 통과: palette 18, XRGB 192, ARGB 22.
- `gxdesc.ini`의 normal/glow/one-one 경로 테스트 통과.
- PyOpenGL에서 `GL_ALPHA_TEST`, `GL_GREATER` 상수 로드 확인.

## 남은 불확실성

- 실행 파일의 두 알파 테스트 경로를 선택하는 `renderer+0x2010d` 플래그가 사용자 설정의 어느 항목과 연결되는지는 아직 이름까지 확정되지 않았다.
- 현재 도구는 시각적 결함을 더 잘 억제하는 `GREATER/10` 경로를 기본값으로 선택한다.
