# 조립 규칙 — 현재 권위

## 결론

표준 플레이어 MP/BP/AP 조립을 찾기 위한 현대 Nova1492 실행파일 역추적은 완료되었다. 다시 EXE를 처음부터 분석하지 않는다.

- BP 월드 행렬: `MP 시각 루트 × MP XFI transforms[0]`
- AP 월드 행렬: `BP 월드 행렬 × BP 시각 루트 × BP XFI transforms[2]`
- 부모 XFI 프레임이 바뀌면 자식 BP/AP 행렬도 같은 시간축에서 갱신한다.
- ACP와 서브코어는 완성 유닛 외형에 메시를 추가하지 않는다.
- 메탈리언은 표준 플레이어 MP/BP/AP 규칙의 적용 대상이 아니다.

팔형·어깨형·탑형은 공격 동작과 발사점 등 후속 표현 분류에 필요하지만, 표준 AP를 임의 좌우 소켓으로 옮기는 근거가 아니다.

## 확정 근거

1. 현대 EXE SHA-256: `A07AA081ED9BF87D18C58C209E5B8F5D35884F2323A27DCE5C7181CB5EEB516D`
2. 접속 선택기: `0x00469A40`, 점프 테이블 `0x00469A98`
3. `gx_attachment_native_evidence_20260725.json`: 원본 노드·부모·플래그·행렬과 네이티브 주소 증거
4. `gx_attachment_completion_audit_20260725.json`: 요구사항 10/10 통과
5. 정본 독립 검사: GX 네이티브 증거 `217/217`, 대표 조립 계약 `2/2`

권위 데이터 위치:

- `02_REPRODUCIBLE_TOOLS/format_sources/source/outputs/CURRENT_GX_ASSEMBLY_BASELINE.json`
- `02_REPRODUCIBLE_TOOLS/format_sources/source/outputs/gx_attachment_native_evidence_20260725.json`
- `02_REPRODUCIBLE_TOOLS/format_sources/source/outputs/gx_attachment_completion_audit_20260725.json`
- `02_REPRODUCIBLE_TOOLS/authoritative_godot_runtime/`

## 왜 최근 이미지가 틀렸는가

실행파일 역추적이 실패한 것이 아니다. 이후 N2·Blender·복셀 자동 조립기가 권위 체인을 그대로 소비하지 않고 다음 추측을 다시 섞었다.

- AP 유형별 임의 좌우 소켓 선택
- `merge_b -0.6` 같은 수동 간격
- 첫 메시, AABB, 바닥 또는 메시 중심 정렬
- 인식 실패 AP를 TOP으로 보내는 fallback

따라서 틀린 최근 렌더는 네이티브 규칙의 반증이 아니라 후대 어댑터의 구현 오류다.

## 앞으로의 사용 원칙

Godot, Blender, 복셀 변환기는 각자 조립 규칙을 추측하지 않는다. `authoritative_godot_runtime`과 동일한 파츠 월드 행렬을 계산하거나, 그 결과 행렬이 기록된 중간 자료를 입력받는다. 두 독립 검사를 통과하지 못한 변경은 정본으로 승격하지 않는다.
