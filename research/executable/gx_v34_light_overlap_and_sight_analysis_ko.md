# Nova1492 GX 분석 v3.4 — 지형광 중첩과 sight 자원

## 결론

타입 0 지형광은 제출 배열의 20바이트 레코드를 앞에서부터 순회해 `광원.bmp × packed RGB` 쿼드를 만든다. 렌더 상태는 `SRCBLEND=ONE`, `DESTBLEND=ONE`이므로 겹치는 광원의 최종 RGB는 다음과 같다.

```text
final.rgb = saturate(destination.rgb + Σ(mask_i.rgb × light_i.rgb))
```

모든 기여가 비음수이고 채널별 포화만 적용되므로 최종 RGB는 광원 제출 순서와 무관하다. 실제 프리미티브 생성 순서는 배열 순서지만 순서를 바꿔도 같은 포화 합이 된다.

## 호출 규약과 순회 순서

메인 호출 지점 `0x00447012`는 다음과 같다.

```text
mov ecx, [0x007B6BB8]       ; 광원 개수
test ecx, ecx
push 0                     ; 텍스처 override 없음
push 0                     ; type 0
push 0x007B5E98            ; 20바이트 광원 배열
call 0x00447250
```

즉 Ghidra가 `__thiscall` 형태로 복원한 첫 인자/카운트는 ECX로 전달된다. 함수 내부에서는 레코드 포인터를 5 DWORD, 즉 20바이트씩 증가시키고 개수를 하나씩 줄인다.

동적 버퍼가 부족하면 현재까지 생성한 쿼드를 먼저 draw하고 버퍼를 다시 잠근다. 이 분할은 합성식을 바꾸지 않는다. Z-write는 꺼져 있고 각 draw에 동일한 가산 상태가 유지된다.

## `sight.bmp` 슬롯 재검증

`sight.bmp` 로더 반환값은 초기화 중 `DAT_007C4E54`에 저장된다. 그러나 현재 EXE 이미지에서 주소 `0x007C4E54`의 리틀엔디언 리터럴은 이 저장 명령 한 번만 존재한다.

- 직접 읽기 참조 없음
- 렌더 함수 바인딩 참조 없음
- 종료 시 개별 해제 참조 없음

따라서 이 클라이언트 빌드에서는 `sight.bmp`가 선로딩되지만 전역 슬롯을 통한 관찰 가능한 소비는 없는 레거시/예약 자원으로 분류한다. 주소를 산술적으로 만들어 접근할 가능성까지 형식적으로 배제할 수는 없지만, 인접 리소스들은 모두 절대주소로 접근하므로 실제 소비자일 가능성은 낮다. 리소스 관리자가 소유권을 보존하므로 별도 전역 해제가 없어도 로더 내부에서 정리될 수 있다.

## 재현 규칙

- 지형광 canonical mask: `광원.bmp`, 64×64 RGB
- 텍스처 단계: mask × packed diffuse color
- 프레임버퍼 단계: ONE + ONE
- 겹침: 채널별 포화 가산
- 모델 메시: 첫 XZ 포함광원 하나만 선택하므로 지형광 누적과 다름
- `sight.bmp`: 현재 빌드의 필수 렌더 입력으로 취급하지 않음

## 근거 산출물

- `gx_v34_light_overlap_and_sight_trace.txt`
- `gx_terrain_light_runtime_v34.py`
- `test_v34_light_overlap_and_sight.py`
