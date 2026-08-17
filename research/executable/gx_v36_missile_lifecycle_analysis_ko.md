# Nova1492 GX 분석 v3.6 — 미사일 생성·이동·폭발 수명주기

## 결론

v3.5에서 복원한 76바이트 공격 레코드가 실제 공격 객체에 선택되고, 미사일 생성부터 충돌 폭발까지 소비되는 경로를 연결했다. 핵심 런타임 함수는 `FUN_0043EBD0`이며 공격 객체 `+0x54`가 선택된 레코드를 가리킨다.

## 변형 선택

생성 함수 `FUN_0043E3B0`의 `0x0043E509~0x0043E583`은 AP 상위 레코드의 모드와 변형 수를 읽어 공격 객체 `+0x78`의 variant index를 결정한다. 이후 계산은 다음과 같다.

```text
variant = selectedIndex % container.capacity
attackRecord = container.data + variant * 0x4C
object.attackRecord(+0x54) = attackRecord
```

`gxname`에서 파생된 레코드 `+0x2A` 값은 현재 시간 기준값에 더해져 객체 `+0x6C`의 시작/예약 시각을 만든다.

## 초기 미사일 생성

`FUN_0043EBD0`은 다음 순서로 초기화한다.

1. `record+0x28`의 missile count를 읽는다.
2. 일부 sequence 모드에서는 상위 attacktypecount와 곱한다.
3. 시작점과 목표점 사이의 3D path distance를 계산한다.
4. `record+0x00`이 `-1`이 아니면 registry에서 미사일 GX/BMP 자원을 얻어 인스턴스를 만든다.
5. `record+0x04`가 `-1`이 아니면 발사 사운드를 재생한다.
6. 각 미사일의 시간·활성 플래그·위치 보간 버퍼를 할당한다.

미사일 자원이 `-1`이어도 논리 발사체와 종료 폭발은 유지된다. 즉 `missile=NULL`은 공격 자체를 제거하는 값이 아니라 비가시 탄도/즉시성 공격을 표현할 수 있다.

## 이동 시간

`0x0043F0B5~0x0043F0EE`의 도달시간 계산은 다음과 같다.

```text
travelTicks = trunc(record[+0x38] * pathDistance)
if travelTicks == 0:
    travelTicks = 1
```

진행률은 런타임에서 `(now-startTime)/travelTicks`로 계산되고 1을 넘으면 종료 경로로 진입한다. 설정 키 이름은 `missilespeed`지만 내부 값은 이 빌드에서 거리와 곱해지는 duration factor처럼 사용된다.

## 이동 타입 디스패치

초기화 시 `record+0x34`의 movement type이 객체 `+0x40`으로 복사된다. 값 2는 특정 거리 조건에서 0으로 대체된다. 업데이트 지점 `0x00440D94~0x00440DA1`은 0~8 범위를 검사한 뒤 9개 점프테이블로 분기한다.

| 타입 | 구현 주소 |
|---:|---:|
| 0 | `0x00440F42` |
| 1 | `0x00440F01` |
| 2 | `0x00440F74` |
| 3 | `0x00441041` |
| 4 | `0x004415C0` |
| 5 | `0x004415C0` |
| 6 | `0x004410C4` |
| 7 | `0x00440DAC` |
| 8 | `0x00441548` |

타입 4와 5는 이 빌드에서 같은 구현 주소를 공유한다. `record+0x35`는 별도의 speed/easing class로 사용되며, `+0x3C~+0x44`의 세 float가 이동식별 매개변수다. 한국어 이동 이름과 0~8 ID의 완전한 대응은 다음 세부 단계에서 각 분기 수식을 복원하며 확정한다.

## 종료와 폭발 생성

진행률이 끝에 도달하면 `0x00440B04`에서 `record+0x08` explosion registry index를 읽는다.

- index가 registry 범위 `0x2B5` 미만이면 현재 미사일 위치를 폭발 transform으로 복사한다.
- `record+0x2C`가 0이면 추가 회전을 적용하지 않는다.
- 0이 아니면 해당 radian 범위를 사용하는 회전 transform을 만든다.
- registry 객체의 생성 가상함수를 호출하므로 BMP 스프라이트와 GX 폭발이 같은 종료 경로를 공유한다.
- `record+0x0C`가 `-1`이 아니면 별도로 폭발 사운드를 재생한다.
- 폭발 생성 후 해당 미사일의 시간 슬롯을 0으로 만들고 완료 플래그를 세운다.

폭발 시각 효과와 사운드는 독립적으로 optional이다. 따라서 `explosion=NULL`이면서 사운드만 있거나, 그 반대인 정의도 그대로 재현해야 한다.

## 근거 산출물

- `gx_v36_missile_consumer_disasm.tsv`
- `gx_v36_missile_jump_tables.json`
- `disasm_v36_missile_consumer.py`
- `extract_v36_missile_jump_tables.py`
- `gx_missile_runtime_v36.py`
- `test_v36_missile_runtime.py`
