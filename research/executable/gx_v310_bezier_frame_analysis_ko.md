# Nova1492 GX 분석 v3.10 — 베지어 좌표 프레임과 정확한 제어점 식

## 좌표 프레임

`0x0043F2D3~0x0043F43D`의 SIMD 연산과 벡터 셔플을 전개하면 다음 프레임이 만들어진다.

```text
F = normalize(target - start)
R = normalize(worldUp × F)
U = normalize(F × R)
worldUp = (0, 1, 0)
```

상수 벡터 `0x006DB290`은 `(0,1,0,1)`이며 xyz 성분이 기준 상향축이다. `R`은 측면축, `U`는 보조 상향축, `F`는 목표 방향축이다.

프레임은 메모리에 다음 3×4 아핀 행렬 형태로 기록된다.

```text
[ R.x U.x F.x origin.x ]
[ R.y U.y F.y origin.y ]
[ R.z U.z F.z origin.z ]
```

`0x00435730`은 로컬 동차 벡터 `(x,y,z,w)`와 각 행을 내적한다. 따라서 `w=1`이면 origin이 더해지는 로컬→월드 위치 변환이다.

## 설치본 제로 분기의 로컬 벡터

`0x0059C793`은 입력 radians의 sine을 `ecx`, cosine을 `edx`가 가리키는 위치에 쓴다. 제어점 생성부는 고정각 `π/2`와 난수각을 함께 사용하지만 전개하면 측면 성분은 항상 0이다.

```text
local = (0, radius*cos(angle), radius*sin(angle), 1)
world = origin + U*(radius*cos(angle)) + F*(radius*sin(angle))
```

따라서 곡선은 `R` 방향으로 흔들리지 않고 시작-목표 진행축과 보조 상향축이 만드는 평면 안에 놓인다.

## 정확한 P1/P2 식

거리 `D = length(target-start)`이고 네 난수 결과를 `a1`, `r1`, `a2`, `r2`라고 하면 설치본이 사용하는 식은 다음과 같다.

```text
a1 = randomRange(0, 90) degrees
r1 = randomRange(0.1, 0.3) * D
P1 = start  + U*(r1*cos(a1)) + F*(r1*sin(a1))

a2 = randomRange(-90, 0) degrees
r2 = randomRange(1.4, 1.6) * D
P2 = target + U*(r2*cos(a2)) + F*(r2*sin(a2))
```

P2의 음수 각도는 `sin(a2) <= 0`이므로 목표점에서 진행축 반대쪽으로 제어점을 되돌린다. P1은 시작점에서 위쪽과 앞쪽으로 나간다.

## movement parameter 정정

공격 레코드의 세 movement parameter는 `+0x3C`, `+0x40`, `+0x44`에 저장된다. 그러나 베지어 제어점 생성 구간이 직접 읽는 값은 `+0x44`, 즉 세 번째 값뿐이다.

- 설치본 값: `0.7, 1.0, 0.0`
- 제어점 분기 입력: 세 번째 값 `0.0`
- 첫 번째 `0.7`과 두 번째 `1.0`: P1/P2 좌표식에 직접 사용되지 않음

따라서 `0.7`과 `1.0`을 곡률이나 축 배율로 적용하는 구현은 원본과 다르다. 이 값들은 다른 이동/후처리 소비부와의 공용 레코드 필드로 보아야 한다.

## 특이점

`worldUp × F`를 정규화하므로 F가 정확히 수직이면 측면축 길이가 0이 되는 수학적 특이점이 있다. 원본 루틴에는 이 구간에서 별도 대체축을 선택하는 분기가 보이지 않는다. 2026 구현에서는 원본 호환 모드와 안전 대체축 모드를 구분하는 것이 적절하다.
