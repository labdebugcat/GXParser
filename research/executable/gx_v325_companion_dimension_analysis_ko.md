# GX v3.25 companion 크기 일치 전수 검사

## 결과

현재 설치본에서 실제로 해결되는 주/보조 텍스처 조합은 23개 고유 pair, 1,463 참조 슬롯이다.

- 크기 일치 pair: 23/23
- 크기 일치 슬롯: 1,463/1,463
- 크기 불일치: 0

따라서 현재 자산에서는 companion mask 리샘플링 분기가 실행되지 않는다. 두 텍스처 노드는 동일 UV와 sampler address mode를 사용하면 된다. Native에 남아 있는 크기 불일치용 bilinear 안전 처리는 현재 설치 corpus의 결과에는 영향을 주지 않는다.

원시 감사: `gx_v325_companion_dimension_audit.json`
