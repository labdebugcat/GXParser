# GX v3.32 주 텍스처 참조 전수 감사

설치본 모든 GX의 material slot 및 material set이 없는 mesh texture를 전수 검사했다.

- 주 텍스처 참조: 65,607
- 실제 BMP/TGA/PNG로 해결: 65,607
- 누락 참조: 0
- 고유 누락 파일: 0
- primary가 없는 빈/sentinel material slot: 42
- primary 없이 alpha만 있는 비정상 slot: 0

42개 빈 슬롯은 alpha도 없는 sentinel/비표시 슬롯이다. 즉 현재 corpus에는 주 텍스처 파일 누락이나 alpha-only 비정상 레코드 때문에 표시되지 않는 GX가 없다. 남아 있던 표시 문제는 파일 존재 여부가 아니라 32비트/16비트 TGA 채널 해석과 companion 결합 규칙에서 발생했다.

원시 감사: `gx_v332_primary_texture_resolution_audit.json`
