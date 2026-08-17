# GX Manager Native TextureFix v3.4 릴리스 요약

## 이번 단계의 핵심 정정

1. 누락 companion에 주 텍스처 luminance를 자동 적용하던 복구 추정을 완전히 제거했다.
2. descriptor alpha=0인 32비트 Nova TGA도 네 번째 바이트를 alpha로 보존한다.
3. 실제 companion은 luminance가 아니라 Red 채널을 alpha로 사용한다.
4. Blender companion은 Non-Color 전용 datablock으로 분리해 self-reference의 RGB 색공간 오염을 막는다.
5. 16비트 TGA는 descriptor와 무관하게 원본의 불투명 X1 계열로 처리한다.

## corpus로 확정한 범위

- GX 전수 파싱: 777/777 성공, 실패 0
- material slot: 65,649 / texture record: 156,929
- 명시 alpha 슬롯: 25,715
- companion 누락: 24,252 — 전부 주 텍스처에 가변 alpha 보유
- resolved companion: 1,463슬롯 / 17 이미지
- 컬러 companion: 1,302슬롯 — Red와 luminance가 다름
- self-reference: 1,285슬롯 — 현재 자산은 Red == Alpha
- non-self companion: 178슬롯 — 13슬롯은 companion이 실제 alpha를 변경
- TGA 전수 디코드: 1,193/1,193 성공
- BMP/PNG 전수 디코드: 1,311/1,311 성공
- 지원 텍스처 합계: 2,504/2,504 성공
- GX 주 텍스처 참조: 65,607/65,607 해결, 누락 0
- descriptor0 32비트 가변 alpha: 192개
- descriptor1 16비트 불투명 정정: 9개

## 원본 EXE 근거

- material/cache loader: `FUN_0042AAF5`
- TGA loader/parser: `FUN_0046CF10`, `FUN_00426900`
- BMP loader: `FUN_0046D6D0`
- TGA/BMP Red mask sampler: `FUN_00426860`, `FUN_00428480`
- alpha byte replacement callback: `0x005AE910`
- internal/GPU format mapping: `FUN_00432C60`, `FUN_00432E00`
- texture upload: `FUN_0046ED60`

## 검증

`run_gx_v34_regression.ps1` 전체 실행 결과: `GX_V34_REGRESSION_OK`

`test_v334_release_manifest.py`: `GX_V334_RELEASE_MANIFEST_OK`

- 일반 Python 회귀: 18개 통과
- Blender 독립 회귀: 7개 통과
- 실제 자산 인자형 Blender 회귀: 4개 통과
- 실제 `acdown.gx`: 누락 companion 재질 374/374 주 alpha 연결
- 실제 `arm55_bbs.gx`: explicit companion 재질 969개 Red 연결, mask cache 2개로 격리
- ZIP 별도 해제본 Native: `a_alp2_12.tga` alpha 0–255 확인
- ZIP 별도 해제본 Blender: `tmissile.gx` 2개 메시/XFI/계층 가져오기 통과

## 패키지

- 파일: `GX_Manager_Native_TextureFix_v3.4.zip`
- 크기: 62,837 bytes
- SHA-256: `3CBC165CE415DBC3054272F5E99CD2309DAAAE179C754BF8FCFAAA19BBBC13E7`
- Blender 애드온: 1.7.0
- 압축 항목: 28, `__pycache__`: 0
