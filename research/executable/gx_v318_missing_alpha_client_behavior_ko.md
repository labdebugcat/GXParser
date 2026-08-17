# GX v3.18 명시 알파 누락 시 원본 클라이언트 동작

## 결론

GX 재질이 보조 알파 텍스처를 명시했더라도 파일을 열 수 없으면 Nova1492 클라이언트는 주 텍스처의 휘도를 알파로 대체하지 않는다. 보조 이미지 포인터를 `NULL`로 되돌리고 알파 버퍼 없이 주 텍스처를 계속 처리한다. 따라서 기존 Native/Blender의 `primary luminance -> alpha` 자동 대체는 원본 호환 동작이 아니라 복구 추정이었다.

## 정적 분석 근거

- `FUN_00460c80`: GX의 `0xffff0013` 재질 레코드에서 주/보조 텍스처 이름을 읽고 `FUN_0042aaf5`를 호출한다.
- `FUN_0042aaf5`: 텍스처 캐시를 조회하고 새 객체에는 형식별 로더 `FUN_0046e110`을 호출한다.
- `FUN_0046e110`: 이미지 형식에 따라 `FUN_0046cf10` 또는 `FUN_0046d6d0` 등으로 분기하며 주/보조 경로를 전달한다.
- `FUN_0046d6d0`: 보조 파일 열기 `FUN_00427b20`이 실패하면 `param_5 = 0`으로 되돌린다. 이후 보조 이미지 리샘플링도 생략하고 `FUN_0046ca70(NULL)`을 호출한다.
- `FUN_0046ca70`: 입력이 `NULL`이면 알파 버퍼 포인터를 0으로 설정한다. 주 이미지에서 휘도를 계산하는 분기는 없다.

원본 디컴파일 산출물:

- `gx_v318_combined_texture_loader_decompile.md`
- `gx_v318_combined_texture_callees_decompile.md`
- `gx_v318_image_loaders_decompile.md`
- `gx_v318_alpha_combine_decompile.md`

## 데이터 영향 범위

`gx_v318_explicit_alpha_reference_audit.json` 기준:

- 명시 알파 레코드: 25,715
- 명명된 companion 누락: 23,925
- 기타 참조 누락: 327
- 누락 영향 합계: 24,252 슬롯
- 명명 companion 해결: 163
- self-reference 해결: 1,285
- 기타 참조 해결: 15

## 구현 변경

- Native 프리뷰는 명시 알파 파일 누락 시 자동 luminance alpha를 더 이상 만들지 않는다.
- Blender 임포터도 누락 시 주 텍스처 RGB를 알파로 연결하지 않는다.
- Blender 재질에는 `gx_alpha_texture_name`과 `gx_alpha_texture_missing`을 기록하여 손실 자산을 추적할 수 있게 했다.
- 실제 보조 알파가 존재하는 경우의 grayscale mask 결합 및 주 TGA 자체 알파는 그대로 유지한다.

## 검증

- `test_v318_missing_alpha_client_behavior.py`: 통과
- `test_v315_effective_blend.py`: 통과
- `test_v316_alpha_mode_default.py`: 통과
- `test_texture_pipeline.py`: palette 18, XRGB 192, ARGB 22, explicit alpha composition 통과
- Blender `test_blender_unlit_gx_material.py`: 통과
- Blender `test_blender_sampler_address.py`: 통과

실행 목록에 존재하지 않는 `test_blender_gx_importer.py`가 포함되어 한 항목은 실행되지 않았으나, 실제 현재 Blender 회귀 스크립트 2종은 모두 통과했다.
