# 폐기 및 재사용 금지 목록

## 즉시 금지된 조립 산출물

- `D:\Project-N\VoxelTests\starship_squad_thunderbolt_160\starship_squad_thunderbolt_authoritative_voxel160.blend`
- 같은 폴더의 PNG, 보고서, 중간 흰색 모델
- `gx_voxelizer_stage1\outputs\starship_squad_thunderbolt_*` 중 자동 조립 입력으로 생성된 모든 합성 결과
- 최근 화면에 나온 스타쉽·스쿼드·선더볼트 조립 복셀 이미지

금지 이유: 몸통-하체 및 몸통-무기의 접합이 원본 조립실과 다르고, 무기가 정상 부착점이 아니라 잘못된 위치에 놓였다. 복셀화 알고리즘이 형태를 충실히 옮겼더라도 입력 합성 메시가 틀렸으므로 결과 전체가 정답이 아니다.

## 금지된 규칙

- 표준 플레이어 조립의 확정 체인인 `BP XFI[2]`를 버리고 AP 유형별 임의 좌우 소켓·수동 간격으로 바꾸는 후대 구현
- 인식하지 못한 AP를 자동으로 `TOP`으로 분류하는 fallback
- 첫 번째 메시 노드를 소켓으로 간주하는 과거 `first_mesh_then_socket_chain`
- `merge_b 약 -0.6` 같은 값을 원본 근거 없이 보기 좋게 만들기 위한 보정값으로 사용하는 것
- AABB 중심·바닥 중앙·메시 중심 정렬을 조립 규칙으로 사용하는 것
- MP/BP/AP를 모두 원점에 두고 “조립 완료”로 부르는 것
- 메탈리언에 플레이어 MP/BP/AP 규칙을 그대로 적용하는 것
- 빌보드/평면 효과 규칙을 모든 GX에 전역 적용하는 것
- XFI ID 하나를 모든 자산에서 동일 행동명으로 강제하는 것

## 이름만 믿으면 안 되는 문서

다음 문서는 역사적 근거와 실험 기록으로 보존하지만, 후속 정정 없이 단독 권위로 사용하지 않는다.

- `PLAYER_ASSEMBLY_REVALIDATION_20260809_KO.md`
- `PLAYER_ASSEMBLY_CLOSURE_20260809_KO.md`의 긍정적 closure 문구
- `ASSEMBLY_GENERATION_RECHECK_KO.md`의 완전 조립 주장
- `gx_voxelizer_stage1\STAGE1_FINAL_AUDIT.md`의 자동 조립 PASS
- `gx_voxelizer_stage1\README_KO.md`의 MP/BP/AP 네이티브 조립 주장
- `D:\Project-N\BlenderAssemblyDiagnostics\20260810\ROOT_CAUSE_REPORT_KO.md`의 v0.5 자동 AP 타입·소켓 완결 주장
- `D:\Project-N\N2\tools\blender_addons\nova1492_gx_importer\README_KO.md`의 자동 조립 사용 안내
- `Project-N1\README.md`의 Blender 조립 verified 표현
- `docs\NOVA1492_PARTS_COMPARATIVE_CATALOG_KO.md` 및 일부 7월 덱 문서: 현재 파일의 한글 디코딩이 깨져 사람용 정본으로 사용 금지. machine JSON에서 UTF-8로 재생성할 것

이 문서들은 단독 권위로 사용하지 않는다. 표준 플레이어 조립의 최종 권위는 `CURRENT_GX_ASSEMBLY_BASELINE.json`, `gx_attachment_native_evidence_20260725.json`, `gx_attachment_completion_audit_20260725.json`과 정본 독립 테스트 2종이다. 후대 Blender/N2/복셀 어댑터가 이 체인을 바꿔 만든 이미지만 폐기한다.

## 과거 구현 계열

- `Client2026` 계열 완성 주장
- 오래된 GX Manager의 고수준 자동 조립
- `legacy_reference`의 코드를 최신 구현으로 직접 복사
- 2026-07 루트 문서를 2026-08 정정 문서보다 우선하기
- 원본 화면 대조 없이 생성된 FLD 사선/탑뷰 이미지를 골든으로 사용

## 보존 정책

폐기 파일을 삭제하지 않는다. 파일이 왜 틀렸는지를 재현할 수 있도록 `REJECTED` 꼬리표와 원인을 남긴다. 단, 배포·N2 이관·새 parser의 기본 입력에서는 제외한다.
