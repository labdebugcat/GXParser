# GX v2.5 material animation 시간 분석

## 확정된 시간식

클라이언트의 관련 렌더 경로는 다음 계산을 사용한다.

```text
elapsed_seconds = FUN_00480070()
frame = round_or_integer_convert(elapsed_seconds * 10.0)
mapped_slot = frame_map[frame % frame_map_count]
```

`FUN_00480070`은 64비트 tick 차이에 `_DAT_007641F4`를 곱한다. 이 값은 tick frequency의 역수이므로 결과는 경과 초다. Ghidra 메모리에서 직접 확인한 `DAT_006DACC8`은 `10.0f`다.

따라서 GX transform/shape/material animation의 기준 cadence는 초당 10프레임, 즉 프레임당 100ms다.

## material frame map 구조

런타임 material set은 다음 구조로 로드된다.

| 오프셋 | 의미 |
|---:|---|
| `+0x00` | material slot count |
| `+0x04` | 0x1C바이트 slot 배열 포인터 |
| `+0x08` | frame map count |
| `+0x0C` | DWORD frame-to-slot map 포인터 |

설치 코퍼스에서는 대표적으로 121, 81, 71, 61, 51, 41프레임 맵이 반복된다. 10fps 기준 각각 12.1, 8.1, 7.1, 6.1, 5.1, 4.1초 길이다. 이 배열을 polygon별 재질 인덱스로 해석해서는 안 된다.

## anispeed 관계

`gxdesc.ini`의 `anispeed`는 모델 메타데이터 레코드 `+0x18`에 저장되는 signed animation-rate multiplier다.

- 기본값 `1.0`: 10fps 정방향
- `2.0`: 20fps 정방향
- `0.5`: 5fps 정방향
- `-1.0`: 10fps 역방향
- `-2.0`: 20fps 역방향
- `0`: 정지

따라서 실효 속도는 `10 * abs(anispeed)` fps이며 부호는 방향을 나타낸다. `anispeed`는 특정 텍스처 한 장의 UV 스크롤 값이 아니라 해당 GX 리소스 애니메이션 재생률 메타데이터다.

## 발견된 구현 오류와 수정

- Native가 80ms를 기준 간격으로 사용해 원본보다 25% 빠르게 재생하고 있었다. v2.5에서 100ms로 수정했다.
- Native 타임라인 길이 계산이 shape frame map과 matrix animation만 포함하고 material frame map을 누락하고 있었다. material-only GX가 사실상 1프레임으로 보일 수 있던 문제를 수정했다.
- Native의 재질 선택 자체는 이미 `material.frame_map[current_frame % count]`를 사용하고 있어 올바르다.
- Blender에는 `gx_animation_base_fps`, `gx_animation_effective_fps`, `gx_animation_direction`을 보존한다. material slot 전환을 메시 polygon 속성에 강제로 bake하지 않아 GX 왕복 데이터는 그대로 유지한다.

## 남은 경계

게임 실행 A/B 검증은 할 수 없으므로 정수 변환 시 반 프레임 경계에서 x87 rounding mode가 미치는 차이는 정적 분석 한계로 남는다. 그러나 기준 배율 `10.0`, 100ms cadence, modulo frame-map 선택은 실행 파일에서 직접 확인됐다.
