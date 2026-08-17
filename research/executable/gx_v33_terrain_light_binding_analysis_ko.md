# Nova1492 GX 분석 v3.3 — 지형광 텍스처 초기화 확정

## 결론

지형 동적광 패스가 사용하는 `DAT_007C4E50`은 `light.bmp`가 아니라 `광원.bmp`다. EXE의 초기화 코드와 설치 리소스가 정적 주소 수준에서 직접 연결됐다.

## 초기화 코드

`0x00468831~0x0046884C`는 다음 순서로 실행된다.

```text
push 0
push 0
push 0x006BF1EC              ; "sight.bmp"
mov  ecx, 0x00764330
mov  [0x007C4E50], eax       ; 직전 로드의 반환값
call FUN_0042A5CD
mov  [0x007C4E54], eax       ; sight.bmp
```

그 직전 호출은 다음과 같다.

```text
push 0x1000
push 0
push 0x006BF1E0              ; CP949 "광원.bmp"
mov  ecx, 0x00764330
call FUN_0042A5CD
```

따라서 `0x0046883F`의 저장 시점에 EAX는 `광원.bmp` 로더의 반환값이고, 이 값이 `DAT_007C4E50`에 들어간다. 이어지는 `sight.bmp` 로드 결과는 별도 슬롯 `DAT_007C4E54`에 들어간다.

## 실제 텍스처 특성

설치본 `datan/common/광원.bmp` 계측 결과:

- 64×64 RGB
- SHA-256 `279551e27968132fbfa0513309339d678197eb0f5ef39e1f6759402526845408`
- 중앙 `(255,255,255)`
- 1/4 지점 중앙 `(252,252,252)`
- 상단 중앙과 우측 중앙 `(12,12,12)`
- 모서리 `(2,2,2)`
- 평균 RGB `(115.948,115.948,115.948)`

이는 타입 0 지형광의 UV 투영과 `ONE/ONE` 가산 블렌딩에 사용되는 방사형 감쇠 마스크다. 외곽이 완전한 0이 아니라 최소 2이므로 원본 클라이언트와 픽셀 단위로 맞추려면 수학적 원형 그라디언트를 새로 생성하지 말고 이 텍스처 또는 동등한 샘플값을 보존해야 한다.

`light.bmp`도 유사한 방사형 이미지지만 128×128이고 이 전역 슬롯과 연결되지 않는다. `sight.bmp`는 64×64 팔레트 이미지이며 다른 전역 슬롯에 배치된다.

## 재현 구현에 미치는 영향

- 지형광 마스크의 canonical asset은 `광원.bmp`다.
- 로드 옵션은 `FUN_0042A5CD(name, 0, 0, 0x1000)` 경로다.
- 지형광 셰이더는 `광원.bmp × packedLightColor`를 목적 버퍼에 가산한다.
- 모델 정점광의 수학 감쇠식과 지형광 텍스처 감쇠는 서로 다른 구현이다.

## 근거 산출물

- `gx_v33_terrain_resource_init_trace.txt`
- `gx_v33_terrain_light_texture_audit.json`
- `trace_v33_terrain_resource_init.py`
- `audit_v33_terrain_light_textures.py`
