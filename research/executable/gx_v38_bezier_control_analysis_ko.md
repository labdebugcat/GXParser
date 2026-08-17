# Nova1492 GX 분석 v3.8 — 베지어 제어점과 집중선 별칭

## 베지어 메모리 구조

타입 7 초기화는 `0x0043F16E`에서 movement type을 검사하고 다음 할당을 수행한다.

```text
vectorCount = missileCount × 2
controlBuffer = allocate_aligned_vectors(vectorCount)
object.controlBuffer(+0x68) = controlBuffer
```

벡터 하나는 16바이트 정렬 float4다. 따라서 발사체 하나당 32바이트이며 레이아웃은 다음과 같다.

```text
controlBuffer + missileIndex×32 + 0x00 = P1
controlBuffer + missileIndex×32 + 0x10 = P2
startBuffer   + missileIndex×16        = P0
object target position (+0x20)         = P3
```

소멸자 `0x0043EB79~0x0043EB86`에서 `+0x68` 버퍼는 독립적으로 해제된다.

## 정확한 위치식

`0x00440DAC~0x00440E48`의 SIMD 곱셈을 정리하면 다음과 같다.

```text
u = 1-t
position = P0×u³ + P1×3tu² + P2×3t²u + P3×t³
```

EXE 상수도 확인했다.

- `0x006DB400 = (3,3,3,3)`
- `0x006DAF3C = -3.0` (접선 미분식의 부호 계수)
- `0x006DAA00 = 1.0`

위치 계산 뒤 이어지는 `0x00440E4B~0x00440EFC`는 같은 제어점으로 곡선 접선/방향을 계산한다. 따라서 GX 미사일 모델의 위치뿐 아니라 진행 방향도 곡선의 미분값에 맞춰 회전한다.

## 제어점 생성

`0x0043F292~0x0043F85D`는 각 발사체에 대해 P1/P2를 생성한다.

- 기본 시작/목표 방향을 기준으로 직교 프레임을 만든다.
- 발사체 index와 missile count를 이용해 서로 다른 각도/방향을 배치한다.
- 난수 및 클라이언트 상수로 측면·높이 오프셋을 만든다.
- 최종 P1은 `buffer+i×32`, P2는 `buffer+i×32+16`에 저장한다.
- 일부 조건에서는 P2를 P1과 동일하게 복사한다.

정확한 난수 시드까지 고정하지 않으면 매 실행의 제어점 자체는 달라질 수 있지만, 저장 구조와 cubic 소비식은 확정됐다. 2026 구현에서는 결정론적 리플레이가 필요하면 원본 난수 호출 순서를 보존하거나 생성된 P1/P2를 네트워크·리플레이 데이터로 기록해야 한다.

## 집중선 재검증

로더는 `직선`과 `집중선` 문자열 비교가 성공했을 때 모두 `record+0x34 = 0`을 기록한다. 별도의 구분 비트나 보조 필드는 남기지 않는다.

따라서 공격 레코드가 완성된 뒤에는 두 이름을 구분할 수 없으며, 둘 다 다음 수식을 사용한다.

```text
position = start + (target-start)×t²
```

설치 설정에서 보이는 집중 효과는 `missilecount`, 시작/목표점 입력 또는 공격 상위 모드의 차이에서 만들어지며 `missilemove=집중선` 자체의 별도 런타임 수식은 아니다. 호환 파서는 두 문자열을 모두 타입 0으로 받아들여야 한다.

## 근거 산출물

- `gx_v36_missile_consumer_disasm.tsv`
- `gx_v38_bezier_constants.json`
- `extract_v38_bezier_constants.py`
- `gx_missile_motion_v37.py`
- `test_v38_bezier_layout.py`
