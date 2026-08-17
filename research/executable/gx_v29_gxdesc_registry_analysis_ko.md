# Nova1492 GX 분석 v2.9 — gxdesc.ini 레지스트리 복원

## 결론

`gxdesc.ini`는 텍스처 옵션 파일만이 아니다. 클라이언트가 사용하는 693개 그래픽 자산 슬롯과 모델별 렌더·결합·꼬리·오라·동적광원 속성, 공격 연출 정의를 함께 보관하는 그래픽 자산 레지스트리다.

이번 단계에서 설치본 전체를 읽는 CP949 호환 파서를 만들고 Native 도구와 Blender 애드온에 공통 적용했다. 원본 게임 데이터는 수정하지 않았다.

## 설치본 전수 결과

- `[Files]` 슬롯: 693개, 고유 파일명 684개
- 유효 메타데이터 섹션: 372개
- 텍스처 메타데이터 엔트리: 108개
- `pair` 지정: 14건, 전부 Files 슬롯으로 역참조 성공
- `tail` 지정: 5건, 전부 플래그 변환 성공
- EXE의 GX 모델 레코드 크기: 0x44바이트(17 DWORD)

## EXE 로더에서 확정한 모델 레코드

레코드 기준 배열은 `DAT_0076604C`, 한 슬롯의 간격은 0x44바이트다. `DAT_00766064`는 레코드 시작이 아니라 첫 레코드의 +0x18 필드다.

| 레코드 오프셋 | gxdesc 키 | 의미/기본값 | 확신도 |
|---:|---|---|---|
| +0x18 | `anispeed` | 애니메이션 배속, 기본 1.0 | 확정 |
| +0x1C | `scale` | 모델 배율, 기본 1.0 | 확정 |
| +0x20 | `tail` 등 | small=1, medium=2, large=4, aura=8 및 aura 유형 비트 | 확정 |
| +0x24 | `pair` | Files 슬롯 인덱스, 기본 -1 | 확정 |
| +0x28 | `aura` | 첫 번째 ARGB 색 | 확정 |
| +0x2C | `aura2` | 두 번째 ARGB 색 | 확정 |
| +0x30 | `aurascale` | 첫 번째 오라 배율, 기본 1.0 | 확정 |
| +0x34 | 오라 배율 범위 끝 | 보간 함수에 전달되는 두 번째 배율 | 부분 확정 |
| +0x38 | `auracycle` | 클라이언트 시간 단위로 변환되는 주기 | 확정 |
| +0x3C | 파생값 | aura cycle의 역수 기반 프레임/주기 값, 기본 1000 | 확정 |
| +0x40 | `auramaterial` | 오라 재질 번호, 기본 1 | 확정 |

`auratype`은 최대 3개의 토큰을 읽고 각 토큰을 내부 유형 상수와 비교하여 +0x08 플래그에 기록한다. 정확한 한국어 유형명과 각 비트의 시각 동작은 소비 함수 추적이 더 필요하다.

동적광원 키 `lightcolor`, `lighttype`, `lightsize`, `lightpillar`, `lightdiffusechange`, `lighttime`도 같은 로더에서 확정됐다. `lightsize`가 음수이거나 `lightpillar`가 0이 아니면 유형 바이트의 0x80 비트를 켠다. `lightdiffusechange`는 0x20 비트를 사용한다. 최종 광원 객체 생성 함수는 `FUN_0045e650`이다.

## v2.9 도구 반영

- `//`와 `;` 인라인 주석, CP949, 대소문자 무시, 중복 키를 처리한다.
- 모든 gxdesc 값을 보존하며, 이전의 `blend`·`anispeed` 선택 파싱을 대체한다.
- Native 비교 보고서에 원본 모델 메타데이터, Files/pair 인덱스, tail 플래그, scale을 표시한다.
- Blender GX 메시마다 모든 모델 값을 `gxdesc_*` 사용자 속성으로 보존한다.
- Blender에 확정 파생값 `gxdesc_files_index`, `gxdesc_pair_index`, `gxdesc_tail_flags`, `gxdesc_scale`을 기록한다.

## 검증

- Python 문법 검사 통과
- 실제 설치본 전체 파싱 통과
- `pair` 14건 전부 참조 성공
- `tail` 5건: small/medium 값이 각각 1/2로 변환됨
- Blender 5.2 백그라운드에서 `tmissile.gx` 실제 임포트 성공
- 임포트된 두 GX 메시 모두 Files index 12, tail flags 1, scale 1.0 확인

## 아직 남은 분석

이번 결과는 gxdesc의 GX 모델 메타 레코드와 파서 기반을 확정한 것이며, `nova1492.exe` 전체 분석 완료를 뜻하지 않는다. 다음 우선순위는 aura 유형 상수의 실제 문자열/동작, 동적광원 소비·렌더 경로, AP 공격 정의(`missile*`, `explosion*`, `attacktypecount`)의 런타임 구조와 재생 규칙이다.
