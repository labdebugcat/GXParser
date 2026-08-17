# Nova1492 GX 분석 v3.2 — 장면 광원 제출·공간 판정·지형 합성

## 이번 단계에서 확정한 결과

`G3DEILight`의 독립 장면 광원 경로는 D3D9 고정기능 `SetLight`가 아니다. 클라이언트는 활성 광원을 자체 20바이트 배열에 모은 뒤 지형 오버레이와 GX 메시 색상 처리에 사용한다.

## 전역 장면 광원 배열

`FUN_00448F10`은 `DAT_007B5E98`에 20바이트 레코드를 추가한다.

| 오프셋 | 의미 |
|---:|---|
| +0x00 | 중심 X |
| +0x04 | 중심 Y |
| +0x08 | 중심 Z |
| +0x0C | 반경 |
| +0x10 | packed ARGB 색상 |

- 개수는 `DAT_007B6BB8`이다.
- 최대치는 `0xA7`, 즉 167개다.
- 가득 차면 추가 레코드는 무시된다.
- 프레임 초기화 경로 `0x0044491E`, `0x0044BED0`에서 개수가 0으로 돌아간다.

## GX 노드 부착 광원

`FUN_004570F0(node, light)`은 별도의 장면 제출 함수가 아니다.

- `node+0x58`이 가리키는 메시 렌더 데이터의 `+0x0C`에 광원 포인터를 저장한다.
- 광원이 있으면 `node+0x40`의 `0x200` 비트를 켜고, 없으면 끈다.
- 첫 자식 `node+0x5C`와 다음 형제 `node+0x64`를 따라 전체 하위 트리에 같은 포인터를 재귀 전파한다.

따라서 `lightfollow`가 활성화된 GX 광원은 모델 트리 전체에 연결되고, 비활성/독립 광원은 전역 장면 배열로 제출된다.

## 공간 판정

`FUN_0045E060`은 렌더 대상 GX 인스턴스의 X/Z 좌표를 각 장면 광원과 비교한다.

```text
dx = light.x - object.x
dz = light.z - object.z
inside = dx*dx + dz*dz < radius*radius
```

- Y축은 포함하지 않는 XZ 평면 원 판정이다.
- 배열 순서대로 검사하고 처음 포함되는 광원 하나만 선택한다.
- 선택된 20바이트 레코드 포인터는 `FUN_00456FC0`으로 전달된다.
- 포함 광원이 없으면 null이 전달된다.

`FUN_00456FC0`은 지형 밝기에서 얻은 RGB 세 바이트를 메시 렌더 데이터 `+0x04~+0x06`에 복사하고, 선택된 광원 포인터를 `+0x0C`에 기록하며 자식 노드로 재귀 전파한다. 호출 인자에 따라 노드 플래그 `0x40000000`도 갱신한다.

## 지형 광원 합성

메인 렌더 경로는 광원 개수가 0이 아니면 다음 호출을 수행한다.

```c
FUN_00447250(&DAT_007B5E98, DAT_007B6BB8, 0, 0);
```

`FUN_00447250`의 타입 0 경로는 각 광원에 대해 다음 작업을 한다.

1. 광원 중심과 반경을 지형 격자 범위로 변환한다.
2. 지형 가시성 마스크가 켜진 셀만 순회한다.
3. 각 셀의 네 지형 정점을 복사해 쿼드를 만든다.
4. 네 정점 모두에 광원 packed ARGB를 기록한다.
5. 중심에서 반경까지의 상대 위치를 UV로 변환한다.
6. 동적 버퍼를 `(vertexCount / 4) * 6` 인덱스로 그린다.

UV 변환은 중심이 약 0.5가 되고 반경 경계가 0 또는 1이 되는 원형 감쇠 텍스처 방식이다. 즉 지형 광원은 장면의 실제 점광원이라기보다 지형 표면에 투영되는 색상 오버레이 패스다.

타입 0의 렌더 상태도 확정됐다.

- `D3DRS_SRCBLEND(19) = ONE(2)`
- `D3DRS_DESTBLEND(20) = ONE(2)`
- alpha blend 활성
- Z-write 비활성
- texture-stage source는 기존 경로와 같이 `texture × diffuse`

따라서 지형 합성식은 개념적으로 `destination + radialTexture × packedLightColor`인 가산광 패스다. v3.3 재검증에서 `0x0046883F`가 `DAT_007C4E50`에 `FUN_0042A5CD("광원.bmp", 0, 0, 0x1000)`의 반환값을 직접 기록한다는 사실을 확정했다. 실제 입력은 `light.bmp`가 아니라 설치본의 64×64 RGB `광원.bmp`다. 중앙은 `(255,255,255)`, 모서리는 `(2,2,2)`, 상단 중앙은 `(12,12,12)`인 방사형 감쇠 텍스처다. 다음 슬롯 `DAT_007C4E54`는 `sight.bmp`로 별도 로드된다.

## GX 정점별 광원 방정식

최종 draw 함수 `FUN_0042BA63`은 메시 렌더 데이터 `+0x0C`의 광원 레코드를 읽고 각 고유 정점에 다음 계산을 적용한다.

```text
dy = 0                              if light.y == -10000
     light.y - vertex.y             otherwise
d  = sqrt((light.x-vertex.x)^2 + dy^2 + (light.z-vertex.z)^2)
f  = clamp(2 * (1 - (d/radius)^2), 0, 1)
vertex.rgb = light.rgb * f
```

- `-10000.0`은 Y축을 무시하는 투영광 sentinel이다.
- 배율 상수는 EXE의 `0x006DAB58 = 2.0`이다.
- 반경의 약 70.71%(`sqrt(0.5)`)까지는 `f=1`로 포화되고 외곽에서 0까지 감소한다.
- packed ARGB의 RGB 바이트만 위 계산에 사용하며 정점 alpha는 draw 호출 측 값으로 별도 기록된다.
- 여러 광원이 겹쳐도 `FUN_0045E060`이 첫 번째 포함 광원만 선택하므로 메시 정점광은 단일 광원 방식이다.

## `lightdiffusechange` 0x20 재검증

v3.1에서 이 비트가 이후 합성 경로를 선택한다고 추정했지만 v3.2의 최종 소비 함수 추적으로 정정할 수 있다.

- 로더는 `lightdiffusechange=1`을 G3DEILight `+0x34`의 `0x20`으로 보존한다.
- 프레임 업데이트 `FUN_00437BA0`은 같은 바이트에서 하위 타입 4비트와 `0x80`만 읽는다.
- 전역 장면 배열로 복사되는 레코드는 객체 `+0x0C~+0x1F`의 20바이트뿐이므로 `+0x34`의 `0x20`은 전달되지 않는다.
- 노드 부착 경로도 최종 draw에서 위치·반경·색상 레코드만 사용하고 `0x20`을 검사하지 않는다.
- 설치본에서는 `death.gx` 한 슬롯만 이 키를 사용한다.

따라서 현재 EXE에서 `0x20`은 파싱·보존되지만 관찰 가능한 렌더 분기를 만들지 않는 legacy/호환성 비트로 판정한다. 다른 빌드에서의 소비 가능성은 남기되, 2026 설치본 재현 구현에서는 별도 광원 방정식을 적용하지 않는 것이 클라이언트와 일치한다.

## 남은 v3.2 경계

- v3.4에서 지형광 겹침은 `saturate(destination + Σ(mask × color))`의 순서 독립 포화 가산으로 확정했다.
- 다른 Nova1492 클라이언트 빌드에서 `lightdiffusechange 0x20` 소비자가 존재하는지 교차 비교

## v3.2 도구 반영 및 검증

- GX Manager/Blender 애드온 v3.2 사본에 20바이트 레코드, 167개 제한, 첫 XZ 포함광원 선택과 정확한 감쇠식을 추가했다.
- Blender 사용자 속성에 `gxdesc_light_record_size`, `gxdesc_light_scene_capacity`, `gxdesc_light_selection`, `gxdesc_light_attenuation`, `gxdesc_light_ignore_y`, `gxdesc_light_ignore_y_sentinel`, `gxdesc_lightdiffusechange_runtime`을 추가했다.
- 기존 `_numbers()` 코드 배치 오류를 수정해 `lightcolor`, `aura`, `aura2` 숫자 목록이 다시 tuple로 파싱되게 했다.
- 설치본 `gxdesc.ini` 693개 Files 슬롯 검증을 통과했다.
- `death.gx`는 index 129, `lightcolor=(100,82,130)`, `진동=5`, 반경 15, Y 무시, legacy `lightdiffusechange`로 복원됐다.
- Blender 5.2 백그라운드 가져오기에서 36개 메시 전체가 v3.2 광원 메타데이터 검증을 통과했다.

## 근거 파일

- `gx_v32_light_submission_disasm.tsv`
- `gx_v32_light_xrefs.tsv`
- 기존 `nova1492_all_sampler_callers_decompile.md`의 `FUN_00447250`
- 기존 `nova1492_anispeed_math_candidates.md`의 `FUN_0045E060`
- 기존 `nova1492_draw_submission_decompile.md`의 `FUN_0042BA63`
- `gx_v32_light_texture_audit.json`
- `gx_v33_terrain_resource_init_trace.txt`
- `gx_v33_terrain_light_texture_audit.json`
- `gx_v34_light_overlap_and_sight_analysis_ko.md`
