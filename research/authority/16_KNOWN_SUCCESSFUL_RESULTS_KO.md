# 재사용 가능한 성공 결과

이 문서의 ‘성공’은 범위를 함께 적는다. 범위 밖의 완성을 뜻하지 않는다.

## 1. 클라이언트 provenance 고정 — CONFIRMED

- 현대 EXE와 Wicket EXE의 SHA-256이 현재 설치 파일과 일치한다.
- 세대별 주소/호출 증거를 다른 EXE에 잘못 적용하는 일을 막을 수 있다.
- 재현: `artifact_authority.json`의 `modern_client_exe`, `wicket_client_exe` hash 확인.

## 2. GX 전수 구조 파싱 — CONFIRMED

- 현대 common 자산 GX 777/777 구조 파싱
- 1,554 검사 렌더, 16 contact sheet, billboard focus 98
- parse/index/NaN/extreme bounds와 색 텍스처 missing 0으로 기록된 전수 감사
- 설명: 노드/메시/재질/텍스처를 읽는 기반으로 사용 가능
- 한계: 원본 픽셀 777/777 동일성은 아님
- 대표 보고서: `n2_gx_tooling\reports\GX_FULL_VISUAL_AUDIT_20260731_KO.md`

## 3. 세대 간 GX 렌더 분기 — CONFIRMED/부분

- 공통 GX 711개와 방향 플래그 0x1000/0x2000/0x7000 계열 동형 호출 확인
- 설명: 빌보드를 전역 적용하지 않고 파일/노드 flag별로 분기하는 근거
- 한계: 모든 재질 예외의 픽셀 골든은 미완료
- 대표 보고서: `research\dual_client_20260802\GX_RENDER_GENERATION_RECHECK_KO.md`

## 4. XFI 원시 구조와 시간축 — CONFIRMED

- action ID, `[start,end)`, 행렬/정점/UV/재질 채널을 읽는 구조
- 설명: Blender/Godot에서 원시 clip을 노출하는 기반
- 한계: ID 숫자를 전역 행동명으로 쓰면 안 됨

## 5. FLD/PAS 전수 구조와 자산 해결 — CONFIRMED/부분

- 현대 FLD/PAS 189/189
- Wicket FLD 98/98, PAS 물리 107/논리 106
- 현대 texture 604/604, placed GX 376/376 해결
- 설명: 지도 canonical IR과 viewer/새 런타임 입력으로 사용 가능
- 한계: 원본 FLD/PAS 쓰기, PAS 비트 전체 의미, 동적 이동/착륙은 미완료
- 대표 보고서: `FIELD_MAP_GENERATION_RECHECK_KO.md`, `FIELD_FLD_PAS_CLOSURE_INVENTORY_20260805_KO.md`

## 6. FLD→엔진 JSON 변환 — STRUCTURE_ONLY

- `export_nova_maps.py`가 source hash, surface, texture, placed object, water, alias index를 포함한 JSON 생성
- 설명: 원본을 수정하지 않고 Godot/다른 엔진에서 읽을 중간 자료를 만드는 데 사용
- 한계: JSON→원본 FLD/PAS writer가 아님

## 7. 공격 descriptor와 표시 수명주기 — CONFIRMED/부분

- 16바이트 공격 descriptor, 76바이트 투사체 record
- missile mover, explosion timer/mark/light, 200/500/700ms 수명 구조
- 48 light, 4 mark, 53 AP explosion 자산 분류
- 설명: 새 싱글게임의 원본 공격 외형·타격감 재현 기반
- 한계: 서버 selector/피해 공식과 동시 한 발별 1:1 연결 전수검증 미완료

## 8. 메탈리언 정적 catalog/음향 — CONFIRMED/부분

- 41종 정적 표, 이름/모델 대부분 대응, 음향 27/27 정적 연결
- 설명: 대표 몬스터 자산 선정과 runtime 실험 기반
- 한계: 41종 모두의 5행동+음향 원본 골든은 아님

## 9. Blender 단일 GX import — STRUCTURE_ONLY

- 단일 GX 메시/계층/재질/XFI action 구조와 `.blend` 저장
- 설명: 파츠를 Blender에서 살펴보고 수정하는 출발점
- 한계: 원본 재질 playback 완전 동일 아님; 자동 조립은 실패

## 10. 개별 정지 GX 복셀화 — STRUCTURE_ONLY

- surface/solid, UV color, preview, voxel count, JSON/NPZ/VOX, 결정성
- 설명: 단일 파츠를 새 복셀 아트 파이프라인의 입력으로 바꾸는 기반
- 한계: XFI animation/발광/완전 material 없음; 자동 조립 결과는 실패

## 성공으로 부르면 안 되는 결과

- 자동 MP/BP/AP Blender 조립
- 조립된 스타쉽+스쿼드+선더볼트 복셀
- 원본 Square 완성 게임
- 41종 메탈리언 완전 행동 골든
- 위험 지도 9개 완전 골든
- 서버 판정 공식

