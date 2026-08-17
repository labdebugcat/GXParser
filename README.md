# GXParser

GXParser는 Nova 1492의 `.GX`와 `.XFI` 구조를 읽는 순수 Python 파서, Blender 임포터,
그리고 원본 실행 파일에서 확인한 GX 렌더링·조립 구조 연구 자료를 함께 제공합니다.
모든 도구는 클라이언트 파일을 읽기 전용 입력으로 취급합니다.

## 현재 읽는 정보

- GX 노드 이름, 부모 관계와 로컬 행렬
- 메시의 정점, 노멀, UV와 삼각형 인덱스
- 텍스처 참조와 확인된 재질 슬롯
- 행렬·정점·노멀·UV 애니메이션 채널
- XFI 변환 행렬과 원시 action ID의 `[start, end)` 구간

파싱 성공은 원본 게임과 픽셀 단위로 동일하게 렌더링된다는 뜻이 아닙니다. 모든 GX
변형을 지원하지 않으며, 확인되지 않은 필드에는 임의의 의미를 붙이지 않습니다.

## 설치

저장소를 내려받은 뒤 개발 모드로 설치합니다.

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install --upgrade pip
.\.venv\Scripts\python -m pip install -e .
```

런타임 외부 의존성은 없습니다.

## 사용법

```python
from gxparser import read_gx, read_xfi

gx = read_gx(r"C:\path\to\model.gx")
if gx["ok"]:
    print(len(gx["nodes"]), len(gx["meshes"]))

xfi = read_xfi(r"C:\path\to\animation.xfi")
if xfi["ok"]:
    for clip in xfi["clips"]:
        print(clip["animation_id"], clip["start_frame"], clip["end_frame"])
```

`read_gx()`와 `read_xfi()`는 성공 여부를 `ok`에 담은 사전을 반환합니다. XFI가 GX 옆에
있을 때 자동으로 찾으려면 `read_for_gx()`를 사용합니다.

## Blender 임포터

[`blender_addon/nova1492_gx_importer`](blender_addon/nova1492_gx_importer)에는 서로 다른
두 작업 흐름이 있습니다.

- **단일 파츠 임포터**: GX 하나의 계층, 메시, 재질, 텍스처와 XFI action을 Blender로 가져옵니다.
- **복합 조립 임포터**: 플레이어 MP/BP/AP 세 파츠를 `MP XFI[0]`과 `BP XFI[2]`의 확정 체인으로 조립합니다.

기존의 AP 유형별 0/2/3 소켓 추측과 TOP fallback은 정식 버전에서 제거했습니다. Blender
5.2.0 LTS에서 대표 단일 파츠 2개와 조립 조합 2개를 검사해 메시 수와 최종 BP/AP 위치가
권위 계약값과 일치함을 확인했습니다. 설치법과 제한은
[`blender_addon/README_KO.md`](blender_addon/README_KO.md)에 분리해 설명합니다.

## 실행 파일 구조 연구

[`research`](research)에는 Nova 1492 실행 파일에서 확인한 다음 내용을 공개합니다.

- GX 노드·행렬·리소스 로더와 draw submission 호출 구조
- 재질 플래그, alpha test/blend, 투명 큐와 texture upload
- TGA/BMP/companion alpha 처리와 sampler 상태
- XFI socket 선택과 MP/BP/AP 조립 계약
- 카메라, 시간 함수, 동적 광원, 투사체·효과 관련 GX 경로
- 실행 파일 해시별 주소 적용 범위와 클라이언트/서버 경계

75개의 세부 분석 기록, 권위 판정 문서, 217개 GX 대조를 포함한 기계 판독 증거와 재현
계약을 주제별로 찾을 수 있도록 [`research/README_KO.md`](research/README_KO.md)에 색인을
두었습니다.

## 공개 범위

저장소에는 코드, 문서, 주소·호출 관계와 비식별화된 기계 판독 증거를 포함합니다. 다음은
포함하지 않습니다.

- Nova 1492 실행 파일과 클라이언트 원본 바이너리
- GX/XFI/텍스처 등 원본 게임 자산
- 계정·서버·인증 또는 보호 기능을 우회하는 구현
- 후속 검증에서 틀린 것으로 판정된 조립 이미지와 보정값

버그 제보에는 원본 파일을 첨부하지 말고 파일 크기, SHA-256, 오류 메시지와 비식별화한
구조 정보만 제공해 주세요.

## 개발

```powershell
python -m unittest discover -s tests -v
python -m build
```

Blender 5.2.0 LTS와 합법적으로 보유한 로컬 클라이언트가 있는 경우 실제 임포터 검사는
다음처럼 실행합니다.

```powershell
blender --background --factory-startup --python tests/blender_smoke.py -- `
  "C:\Program Files (x86)\Nova1492\datan\common"
```

기여 기준은 [`CONTRIBUTING.md`](CONTRIBUTING.md), 비공개 취약점 제보 방법은
[`SECURITY.md`](SECURITY.md)를 참고하세요.

## 권리와 라이선스

Nova 1492와 관련 명칭·데이터의 권리는 각 권리자에게 있습니다. 이 프로젝트는 권리자의
공식 도구가 아닙니다.

현재 저장소에는 별도의 오픈소스 라이선스가 부여되지 않았습니다. 공개 열람이 가능하다는
사실만으로 복제·수정·재배포 권한이 부여되지는 않습니다.
