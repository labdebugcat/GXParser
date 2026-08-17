# GX v3.27 non-self companion 우선순위 감사

## 결과

primary와 companion이 서로 다른 resolved 조합은 16개 pair, 178슬롯이다.

- companion Red와 primary Alpha가 동일: 8 pair / 165슬롯
- companion Red가 primary Alpha와 다름: 8 pair / 13슬롯

대부분은 변환된 주 TGA에 mask가 이미 복제돼 있다. 대표적으로 `a_alp2_35.tga + a_alp2_35A.bmp` 151슬롯은 픽셀 단위로 동일하다. 그러나 다음과 같은 13슬롯은 별도 companion이 실제 결과를 바꾼다.

- `Watt130.GX`: `A_awt/A_awta`, `A_awt1/A_awt1a`
- `Pw25.GX`: `A_apw1/A_apw1a`, `A_apw2/A_apw2a`
- `Hp240.GX`: `A_ahp1/A_ahp1a`, `acp_hp240_01/A_acp_hp240_01`
- `arm23_rkog.gx`: `A_FIRE/A_FIREA`, `A_fires/A_firesa`

따라서 companion이 존재하면 Red 채널로 primary Alpha를 덮어쓰는 원본 우선순위를 유지해야 한다. 내장 알파만 사용하는 단순화는 현재 corpus에서도 13슬롯을 손상시킨다.

원시 감사: `gx_v327_nonself_companion_precedence_audit.json`
