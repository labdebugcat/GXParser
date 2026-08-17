# Blender 임포터

지원 기준은 Blender 4.0 이상이며, 정식 검증 환경은 Blender 5.2.0 LTS입니다.

현재 정식 지원 대상은 서비스 중인 Nova1492AR의 정식 GX/XFI 리소스입니다. OR 원본,
OR 외형을 AR 리소스 위에 덮은 스킨용 혼합본과 개인 수정본은 아직 지원하지 않습니다.
혼합 리소스의 실제 실패 사례는 [`docs/COMPATIBILITY_KO.md`](../docs/COMPATIBILITY_KO.md)에
정리되어 있습니다.

## 설치

릴리스의 `GXParser-Blender-Addon-<version>.zip`을 받아 Blender의
`Edit > Preferences > Add-ons > Install from Disk`에서 설치합니다. 압축을 푼 소스에서는
`blender_addon/nova1492_gx_importer` 폴더를 직접 압축해도 됩니다.

## 단일 파츠 임포터

`File > Import > Nova1492 GX/XFI (.gx)`에서 GX 하나를 선택합니다. 노드 계층, 메시,
재질, 텍스처와 옆에 있는 XFI action을 가져옵니다.

가져온 직후 모델이 회색으로 보여도 텍스처 누락이라고 단정하지 마세요. Blender의 기본
`Solid` 모드는 텍스처를 표시하지 않습니다. `Z`를 누르고 `Material Preview`를 선택하거나
뷰포트 오른쪽 위의 재질 미리보기 구 아이콘을 누릅니다.

- 텍스처가 없으면 흰 모델로 조용히 대체하지 않고 누락 이름을 표시합니다.
- `Pack textures into .blend`를 사용하면 로드한 이미지를 `.blend`에 포함합니다.
- XFI action ID는 의미를 임의로 이름 붙이지 않고 원시 숫자로 노출합니다.

## 복합 조립 임포터

`File > Import > Nova1492 Assembled Unit (MP/BP/AP)`에서 MP, BP, AP GX를 각각 지정합니다.

정식 조립 체인은 다음 하나뿐입니다.

```text
BP world = MP visual root × MP XFI transforms[0]
AP world = BP world × BP visual root × BP XFI transforms[2]
```

팔형·어깨형·탑형을 추측해 다른 소켓으로 보내지 않으며, AABB/메시 중심 정렬이나 수동
간격 보정을 사용하지 않습니다. ACP와 서브코어는 외형 메시 조립 대상이 아닙니다.

## 실제 조립 예시

![토들러N, 플래툰, 헤비배럴 쿼드뷰](../docs/images/toddler-n_platoon_heavy-barrel_quad-view.png)

| 역할 | 파츠 | GX |
| --- | --- | --- |
| MP | 토들러N | `n_legs41_tdr.gx` |
| BP | 플래툰 | `body2_prt.gx` |
| AP | 헤비배럴 | `arm2_hbbr.gx` |

정식 `v0.6.0`에서 13 / 1 / 5개 메시와 5개 패킹 텍스처를 확인했습니다. 자세한 설치,
메뉴 사용 순서와 오류별 확인 방법은 [`docs/BLENDER_GUIDE_KO.md`](../docs/BLENDER_GUIDE_KO.md)를
참고하세요.

## 검증 결과

Blender 5.2.0 LTS에서 다음 두 조합을 실제 클라이언트 파일로 검사했습니다.

| MP / BP / AP | 메시 수 | 계약 |
| --- | ---: | --- |
| `legs24_sts` / `n_body44_brps` / `arm76_orns` | 16 / 8 / 25 | 통과 |
| `legs50_pps` / `body20_prsd` / `arm81_rtro` | 25 / 3 / 15 | 통과 |

단일 임포트 2/2, 복합 조립 2/2에서 메시 수와 최종 파츠 위치가 정본 계약값과
일치했습니다. 테스트 스크립트는 [`tests/blender_smoke.py`](../tests/blender_smoke.py)에
있으며 원본 자산은 저장소에 포함하지 않습니다.

## 알려진 한계

- 재질과 UV 애니메이션이 원본 Direct3D 출력과 픽셀 단위로 동일하다는 보장은 없습니다.
- 이 조립식은 표준 플레이어 MP/BP/AP용이며 메탈리언에는 적용하지 않습니다.
- OR 및 OR 외형을 덮은 AR 혼합 리소스의 XFI action·다중 AP 접속 규칙은 지원하지 않습니다.
- 서버가 결정하는 공격 대상, 피해, 명중 판정은 임포터 범위가 아닙니다.
