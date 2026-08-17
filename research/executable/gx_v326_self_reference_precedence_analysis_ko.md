# GX v3.26 self-reference mask 우선순위 감사

## 결과

primary와 companion 이름이 같은 resolved self-reference는 7개 고유 텍스처, 1,285슬롯이다. 이 7개 모두 Red 채널과 내장 Alpha 채널이 픽셀 단위로 완전히 동일했다.

- Red == Alpha 텍스처: 7/7
- Red == Alpha 슬롯: 1,285/1,285
- 다른 픽셀: 0
- 최대 채널 차이: 0

이는 현재 설치본에서 self-reference가 TGA 변환 과정 중 같은 mask를 Red와 Alpha 양쪽에 복제한 호환 자산임을 보여준다. 원본 EXE처럼 명시 companion Red를 우선하는 구현은 유지하되, 현재 데이터에서는 주 Alpha를 사용해도 시각 결과가 동일하다. Blender의 별도 mask datablock은 sRGB/Non-Color 상태 오염을 막기 위해 여전히 필요하다.

원시 감사: `gx_v326_self_reference_precedence_audit.json`
