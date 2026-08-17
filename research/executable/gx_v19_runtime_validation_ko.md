# GX v1.9 실행 검증 및 렌더러 플래그 추적

## `renderer+0x2010d` 접근 경로

- 실행 파일 전체에서 little-endian 변위 `0x0002010d`를 스캔한 결과, 코드 영역의 직접 접근은 두 곳이다.
- `FUN_0042eac0`은 이 값을 읽어 알파 테스트를 선택한다.
  - 0: `ALPHAREF=0`, `ALPHAFUNC=NOTEQUAL`
  - 1: `ALPHAREF=10`, `ALPHAFUNC=GREATER`
- `FUN_0042c0a0`은 투명 렌더 큐 2를 처리할 때 이 값이 0인 경우에만 `FUN_0042b98b(0)`을 호출해 Z-write를 끈다.
- 따라서 이 값은 단순한 재질 속성이 아니며 알파 임계값과 투명 큐 깊이 정책을 함께 바꾸는 렌더러 전역 호환성/경로 플래그이다.
- 현재 실행 파일에서는 이 오프셋에 대한 직접 쓰기가 발견되지 않았다. 생성 시의 블록 초기화 또는 계산된 주소를 통한 대입 가능성을 계속 추적해야 한다.

## v1.9 구현

- Native 뷰어에 실행 파일에서 확인된 두 알파 테스트 경로를 모두 선택할 수 있는 콤보 상자를 추가했다.
  - `Client: alpha > 10` — 기본값
  - `Client: alpha != 0`
- 선택값은 원본/수정본 뷰포트에 동시에 적용된다.
- 기존 투명 메시·삼각형 후면 우선 정렬 및 투명 큐 Z-write 차단은 유지한다.

## 실제 GX 렌더 검증

- Blender 5.2 LTS에서 `mob_ef01.GX`를 가져왔다: 6 objects, 36 materials, matrix animation 5, compressed animation 5, XFI/노드 계층 인식 성공.
- 분홍색 반투명 효과가 검은 사각형 없이 출력됐다.
- `arm32_sppoo.gx`를 가져왔다: 5 objects, 5 materials, matrix animation 4, XFI/노드 계층 인식 성공.
- 각 부품 텍스처와 UV는 정상 출력된다. 부품 배치 이상은 노드 변환 적용/미적용 양쪽에서 동일하여 텍스처 문제가 아니라 GX 원본 포즈·계층 조립 해석 문제로 분리됐다.
- 모든 Blender 재질에서 `gx_alpha_test_ref=10`, `gx_alpha_test_func=GREATER` 메타데이터를 확인했다.
- Python 문법 검사와 전체 텍스처 회귀 테스트를 통과했다.
