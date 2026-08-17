# GXParser

GXParser는 Nova 1492의 `.GX`와 `.XFI` 파일에서 현재 확인된 구조만 읽어 내는 순수
Python 파서입니다. Blender나 게임 클라이언트에 의존하지 않으며 입력 파일을 수정하지
않습니다.

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

## 프로젝트 범위

이 저장소는 파서 코어와 재배포 가능한 합성 테스트만 포함합니다. 다음 항목은 포함하지
않습니다.

- Nova 1492 클라이언트 파일과 추출 에셋
- 실행 파일 분석 자료와 과거 연구 덤프
- Blender 자동 파트 조립처럼 검증이 끝나지 않은 기능
- 게임 실행, 서버 통신, 인증 또는 보호 기능을 변경하는 코드

버그 제보에는 원본 파일을 첨부하지 말고 파일 크기, SHA-256, 오류 메시지와 비식별화한
구조 정보만 제공해 주세요.

## 개발

```powershell
python -m unittest discover -s tests -v
python -m build
```

기여 기준은 [`CONTRIBUTING.md`](CONTRIBUTING.md), 비공개 취약점 제보 방법은
[`SECURITY.md`](SECURITY.md)를 참고하세요.

## 권리와 라이선스

Nova 1492와 관련 명칭·데이터의 권리는 각 권리자에게 있습니다. 이 프로젝트는 권리자의
공식 도구가 아닙니다.

현재 저장소에는 별도의 오픈소스 라이선스가 부여되지 않았습니다. 공개 열람이 가능하다는
사실만으로 복제·수정·재배포 권한이 부여되지는 않습니다.
