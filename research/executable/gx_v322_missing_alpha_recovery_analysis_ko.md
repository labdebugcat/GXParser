# GX v3.22 누락 companion 복구 필요성 전수 판정

## 결론

현재 설치본에서 명시 companion을 찾을 수 없는 24,252개 슬롯은 모두 주 텍스처 자체에 가변 알파를 보유한다. 실제 마스크 데이터가 없는 슬롯은 0개다.

- 누락 companion 슬롯: 24,252
- 주 텍스처 가변 알파 보유: 24,252 (100%)
- 주 텍스처 불투명/고정/0 알파: 0
- 주 텍스처 누락 또는 디코드 실패: 0
- 영향 GX: 404개
- 고유 주 텍스처: 144개

유효 블렌드별로도 모두 주 알파가 존재한다.

- selector 2: 11,265
- selector 3: 12,976
- selector 4: 11

따라서 GX의 옛 companion 이름은 현재 `.tga` 변환 자산에 alpha가 내장된 뒤에도 남은 legacy reference로 해석된다. v3.18에서 자동 luminance 복구를 제거하고 v3.20에서 descriptor 0인 32비트 TGA의 네 번째 채널을 보존한 조합이 현재 설치본에 대한 정확한 처리다.

원시 감사: `gx_v322_missing_alpha_recovery_audit.json`
