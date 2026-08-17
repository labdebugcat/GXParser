# Nova1492 GX 분석 v3.5 — 공격·폭발 정의 레코드

## 이번 단계 결론

`gxdesc.ini`의 AP 공격 정의는 공격 변형 하나당 76바이트(`0x4C`) 고정 레코드로 변환된다. 설치본에는 AP 섹션 98개가 있으며 `attacktypecount`를 펼치면 총 108개 변형 레코드가 만들어진다.

## 컨테이너 접근 규칙

`FUN_00444680(container, index)`의 정확한 계산은 다음과 같다.

```text
slot = index % container.capacity       // container +0x08
record = container.data + slot * 0x4C   // container +0x0C
```

런타임 생성 경로 `0x0043E56E~0x0043E583`도 같은 나눗셈 나머지와 `0x4C` stride를 사용해 선택한 레코드 포인터를 공격 객체 `+0x54`에 저장한다. 공격 객체의 `+0x78` 값이 변형 선택 인덱스로 사용된다.

## AP 상위 구조

공격 섹션별 메타 레코드는 16바이트 간격으로 보관된다.

- `+0x00`: `attacktypecount`, 기본 1, 허용 1~255
- `+0x04`: 동기화 모드 ID
- `+0x06`: 선택적 모드 인자
- `+0x08`: 변형 레코드 컨테이너

모드 문자열 매핑:

| 문자열 | ID |
|---|---:|
| `sync` | 0 |
| `location` | 1 |
| `sequence` | 2 |
| `transform` | 3 |
| `respective` | 4 |

## 0x4C 변형 레코드

| 오프셋 | 크기 | 의미 |
|---:|---:|---|
| `+0x00` | 4 | missile GX/이미지 registry index |
| `+0x04` | 4 | missile sound handle/index |
| `+0x08` | 4 | explosion GX/이미지 registry index |
| `+0x0C` | 4 | explosion sound handle/index |
| `+0x10` | 4 | packed light color |
| `+0x14` | 1 | light type 및 `0x80` 플래그 |
| `+0x18` | 4 | light size |
| `+0x1C~0x24` | 12 | light animation parameters |
| `+0x28` | 2 | missile count, 기본 1, 허용 1~255 |
| `+0x2A` | 2 | `gxname`에서 파생된 GX 노드 오프셋 |
| `+0x2C` | 4 | explosion rotation, radians |
| `+0x30` | 4 | missile scale, 기본 1.0 |
| `+0x34` | 1+1 | missile movement type / speed class |
| `+0x38` | 4 | missile speed, 기본 60.0 |
| `+0x3C~0x44` | 12 | missile movement parameters, 기본 1/1/1 |
| `+0x48` | 4 | magazine 값 |

`explosionrotation`의 내부 기본값은 `2π`다. 키가 있으면 입력 각도에 `π/180`을 곱해 radians로 저장한다. 따라서 명시적인 `0`과 키가 없는 기본 360도는 최종 회전 범위가 다르다.

## 설치본 전수 결과

- AP 섹션: 98
- 변형 레코드: 108
- 다중 변형 섹션: 6
- 공격 모드: sync 94, sequence 10, location 2, respective 2
- missile: GX 74, BMP 3, NULL 31
- explosion: BMP 89, GX 9, NULL 10
- explosion rotation: 명시적 0도 12, 기본 360도 96
- 이동: 포물선 보통 78, 직선 보통 14, 각 보통 6, 베지어 보통 6, 집중선 보통 3, 표면 보통 1
- 광원 타입: 포물선 37, 선형감소 9, 진동 7, 없음 55

폭발은 BMP 전용이 아니다. 9개 공격 변형은 GX를 explosion asset으로 사용하므로 2026 구현에서는 스프라이트 폭발과 GX 모델 폭발을 같은 registry 필드에서 확장자에 따라 분기해야 한다.

## 아직 남은 경계

이번 단계는 설정 로드, 레코드 배치, 런타임 변형 선택까지 확정했다. 다음 단계에서는 공격 객체 `+0x54`가 가리키는 레코드의 missile movement 계산과 충돌/종료 시 `+0x08` explosion registry 항목을 생성하는 소비 함수를 추적해야 한다.

## 근거 산출물

- `nova1492_gxdesc_loader_decompile.md`
- `gx_v35_attack_record_trace.txt`
- `gx_v35_attack_definition_audit.json`
- `audit_v35_attack_definitions.py`
- `test_v35_attack_definitions.py`
