# GX v3.24 Blender mask 색공간·datablock 분리

## 문제

companion Red 채널은 색이 아니라 8비트 mask 데이터다. Blender에서 기본 sRGB 이미지로 읽으면 채널 값이 선형화되어 원본 D3D 샘플 값과 달라진다. 또한 `check_existing=True`로 color 이미지와 같은 datablock을 공유한 채 Non-Color로 변경하면 self-reference 1,285슬롯의 RGB 텍스처 색공간까지 바뀐다.

## 수정

- companion 이미지를 `Non-Color`로 로드한다.
- color 이미지와 별도의 mask 전용 image datablock을 생성한다.
- 절대 경로를 `gx_alpha_mask_source`로 기록하고 경로당 하나만 재사용한다.
- 같은 파일이 primary와 alpha 양쪽에 쓰여도 sRGB color와 Non-Color mask가 독립적으로 유지된다.

## 검증

실제 self-reference가 대량 포함된 `arm55_bbs.gx`를 가져와 확인했다.

- explicit companion 재질: 969개, 전부 Separate Color Red 사용
- 일반 color image datablock: 21개
- mask 전용 datablock: 2개
- mask 경로 중복: 0
- color/mask 객체 공유: 0
- mask colorspace: 전부 Non-Color

회귀: `test_blender_v323_red_companion_mask.py`
