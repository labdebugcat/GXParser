# Nova1492 GX 텍스처 파이프라인 분석 및 1차 수정

작성일: 2026-07-19

## 확인된 결함

- GX 파서는 별도 `alpha_texture`를 읽었지만 Native/Blender 렌더러가 실제 합성하지 않았다.
- 알파 비트가 0인 32비트 TGA를 A8R8G8B8처럼 읽어 X 바이트를 투명도로 오인했다.
- color-mapped RLE TGA(type 9) 18개가 디코더에서 거부됐다.
- 명시적 알파 파일이 현재 설치 데이터에서 누락된 효과 모델은 검은 사각형으로 표시됐다.
- 모든 재질이 `SRC_ALPHA / INV_SRC_ALPHA`로 고정되어 `glow`, `one-one` 설정이 무시됐다.
- 텍스처 하나만 누락돼도 모델 전체의 텍스처 모드가 비활성화됐다.
- Blender 가져오기는 이미지 깊이만 보고 TGA 알파를 연결해 XRGB를 ARGB로 오인할 수 있었다.

## 코퍼스 조사

- GX: 780개
- 이미지: 2,805개
- GX primary texture 레코드: 57,114개
- GX explicit alpha 레코드: 23,208개
- explicit alpha가 있는 GX: 333개
- 현재 폴더에서 explicit alpha 파일이 누락된 GX: 325개
- TGA: 1,193개, 새 디코더 전수 해독 1,193/1,193 성공
- palette/RLE TGA: 18개
- XRGB 32-bit TGA: 192개
- 명시적 8-bit alpha 32-bit TGA: 22개
- 파일명 companion alpha 쌍: 186개

## 구현한 수정

- TGA type 1/2/3/9/10 및 8/16/24/32bpp 디코딩
- TGA color map origin/length/entry depth 처리
- descriptor alpha bits가 0인 32bpp TGA를 XRGB 불투명 이미지로 처리
- GX explicit alpha 및 gxdesc companion alpha를 grayscale mask로 합성
- GX가 alpha를 선언했지만 파일이 없으면 primary luminance를 alpha로 사용하는 보존적 대체
- `normal`, `glow`, `one-one` 블렌드 상태 분기
- 부분 텍스처 실패 허용
- Blender 노드에도 explicit/fallback alpha와 emission 연결

## 검증

- Python 문법 검사 통과
- 포맷별 자동 회귀시험 통과
- TGA 1,193개 전체 해독 실패 0
- `mob_ef01.GX` Blender 렌더에서 기존 검은 사각형 제거 확인

## 아직 남은 분석

- GX packed material 6 DWORD의 정확한 D3D9 상태 대응
- 투명 메시의 게임과 동일한 depth-write, depth-test 및 정렬 순서
- texture filtering/mipmap/anisotropy의 실제 설정
- material frame map의 시간 단위와 `anispeed` 결합
- 누락 alpha 파일이 원래 배포에서 제외된 것인지 패치 과정에서 제거된 것인지 provenance 확인
- 게임 런타임 A/B 비교

`휘도 기반 alpha`는 현재 데이터 손실을 보완하는 명시적 fallback이며 원본 포맷 의미로 확정한 것은 아니다.
