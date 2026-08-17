# GX v3.28 확장자별 내장 알파 정책 감사

## EXE 레코드

`FUN_0042AAF5`가 초기화하는 확장자 테이블의 문자열과 값은 다음과 같다.

- `png`: format/type 2, embedded-alpha 플래그 1
- `jpg`: format/type 3, embedded-alpha 플래그 0
- `tga`: format/type 1, embedded-alpha 플래그 1

내장 알파 플래그가 설정된 형식은 별도 companion 인수를 비우는 분기가 있다. 설치본에서는 디스크 자산이 TGA로 변환됐더라도 GX 내부 이름이 BMP이면 legacy companion 조회를 유지하고, 실패 시 주 TGA 내장 알파가 남는다.

## corpus 결과

명시 alpha 레코드 25,715슬롯의 primary 직렬화 확장자는 전부 `.bmp`였다.

- `.bmp`: 25,715
- `.tga/.png/.jpg/기타`: 0

따라서 현재 corpus에서는 TGA/PNG 명시 companion 무시 분기가 직접 실행되지 않는다. 현재 resolver가 GX의 BMP 이름으로 companion 존재 여부를 판단한 뒤 같은 stem의 변환 TGA를 로드하는 동작은 설치 자산 구조와 일치한다.

원시 감사: `gx_v328_embedded_alpha_extension_audit.json`
