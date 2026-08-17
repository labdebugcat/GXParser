# GX v3.19 누락 알파 영향도 분석

## 집계 결과

명시 알파 파일이 해결되지 않는 24,252개 슬롯은 404개 GX, 144개 주 텍스처, 99개 알파 이름에 걸쳐 있다.

- 유효 selector 2(normal alpha blend): 11,265 슬롯 / 177 GX
- 유효 selector 3(additive glow): 12,976 슬롯 / 312 GX
- 유효 selector 4(one-one): 11 슬롯 / 5 GX
- 주 TGA가 헤더상 알파를 선언: 225 슬롯
- 주 텍스처가 헤더상 알파를 선언하지 않음: 24,027 슬롯

selector 3/4는 검정 RGB가 가산 블렌드에서 기여하지 않으므로 companion 누락이 곧바로 검정 사각형을 뜻하지 않는다. 반면 selector 2의 11,265 슬롯은 투명도 채널 해석이 직접적인 시각 결과를 좌우한다.

## selector 2 상위 영향 자산

- `a_alp2_12`: 3,025 슬롯
- `a_alp2_30`: 2,722 슬롯
- `a_alp2_7`: 1,995 슬롯
- `pwcn06`: 1,496 슬롯
- `a_alp2_13`: 1,098 슬롯

상위 GX는 `storm.gx` 3,092, `cursearea.gx` 1,326, `cursearea1.gx` 1,326, `cursepoison.gx` 961 순이다.

## 후속 발견

상위 주 텍스처들은 32비트 TGA이지만 descriptor의 attribute bit가 0이며, RGB는 검정이고 실제 영상 신호가 네 번째 바이트에 저장돼 있었다. 따라서 이 집계에서 “헤더상 자체 알파 없음”은 “실제 네 번째 채널 없음”을 의미하지 않는다. 이 발견은 v3.20에서 원본 EXE 포맷 선택과 대조해 수정했다.

원시 집계: `gx_v319_missing_alpha_impact_audit.json`
