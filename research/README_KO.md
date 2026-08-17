# Nova 1492 실행 파일 구조 연구 색인

이 디렉터리는 GXParser 구현에 사용한 실행 파일 구조 분석을 공개합니다. 주소는 문서에
기록된 SHA-256의 실행 파일에서만 유효하며 다른 빌드에 그대로 적용하면 안 됩니다.

## 먼저 읽을 문서

1. [`authority/02_REVERSE_ENGINEERING_KO.md`](authority/02_REVERSE_ENGINEERING_KO.md) — 조사한 실행 계열, 해시와 증거 경계
2. [`authority/03_GX_XFI_GXDESC_RENDERING_KO.md`](authority/03_GX_XFI_GXDESC_RENDERING_KO.md) — GX/XFI/gxdesc 확인 구조
3. [`authority/04_ASSEMBLY_KO.md`](authority/04_ASSEMBLY_KO.md) — 확정 MP/BP/AP 조립 체인
4. [`authority/16_KNOWN_SUCCESSFUL_RESULTS_KO.md`](authority/16_KNOWN_SUCCESSFUL_RESULTS_KO.md) — 재사용 가능한 결과와 한계
5. [`authority/11_REJECTED_AND_DO_NOT_REUSE_KO.md`](authority/11_REJECTED_AND_DO_NOT_REUSE_KO.md) — 폐기된 규칙과 결과

## 세부 분석 75건

[`executable`](executable)에는 다음 주제의 주소·의사 코드·호출자 분석이 있습니다.

- `nova1492_gx_*`, `nova1492_node_*` — GX 리소스, 노드 로더, 행렬과 트리
- `nova1492_material_*`, `gx_v2*` — 재질 상태, blend, alpha, sampler
- `gx_v31*`, `gx_v32*` — 이미지 로더, TGA, companion alpha와 GPU format
- `gx_camera_*`, `gx_post_queue_*` — 카메라와 draw/post queue 경로
- `gx_v3*` — 광원, 투사체, 이동 곡선과 공격 효과
- `nova1492_unit_gx_assembly_contract_ko.md` — 조립 호출 계약

파일명은 연구 진행 순서를 보존합니다. `_decompile.md`는 주소와 의사 코드 중심,
`_analysis_ko.md`는 해당 결과의 해석·검증·한계를 설명합니다.

## 기계 판독 증거와 재현 계약

- [`evidence/CURRENT_GX_ASSEMBLY_BASELINE.json`](evidence/CURRENT_GX_ASSEMBLY_BASELINE.json)
- [`evidence/gx_attachment_completion_audit_20260725.json`](evidence/gx_attachment_completion_audit_20260725.json)
- [`evidence/gx_attachment_native_evidence_20260725.json`](evidence/gx_attachment_native_evidence_20260725.json) — 217개 GX 네이티브 대조 포함
- [`contracts/test_reference_assembly_contract.gd`](contracts/test_reference_assembly_contract.gd)
- [`contracts/test_part_gx_native_evidence_parity.gd`](contracts/test_part_gx_native_evidence_parity.gd)

## 자료 사용 원칙

- 확인된 사실, 구조만 확인된 결과, 후보와 폐기 결과를 섞지 않습니다.
- 실행 파일·클라이언트 바이너리·원본 게임 자산은 이 저장소에 포함하지 않습니다.
- 연구 자료는 상호운용성과 보존을 위한 문서이며 실행 파일 패치나 보호 기능 우회를
  제공하지 않습니다.
