# 바킹독 실전 알고리즘 강좌 벼락치기 - Python

## 개요

### 기간

- 1차: 2026년 02월 10일 ~ 2026년 02월 28일 (설 연휴 제외)

### TO-BE

- 백준 어려운 실버 ~ 쉬운 골드 (프로그래머스 Lv3)를 무난하게 풀 수 있다.

### ACTION

- 매일 아침 09:00 ~ 10:30
- 개념(10분), 문제(50분), 풀이 비교(20분), 템플릿 정리(10분)
- 2월 내에 빈출 유형(0x03 array ~ 0x11 greedy) 문제들 1회독

### BACKUP ACTION

- 아침 실패 시 당일 저녁. 30~40분 -> 문제 1개 + 풀이 이해만 하고 종료

---

## Base 코드

모든 풀이는 아래 구조를 따른다.

```py
""" solve.py for 10808번. 알파벳 개수 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(...) -> ...:
    # 핵심 알고리즘 로직
    pass


def main() -> None:
    # 입력 처리
    # solve 호출
    # 출력 처리
    answer = solve(...)
    print(answer)


if __name__ == "__name__":
    main()
```

### 추가 규칙

- 출력이 개행으로 구분된 리스트는 `print(*answer, sep="\n")` 사용

---

## 회고 규칙

풀이를 진행한 뒤 문제의 키워드와 간단한 회고(4L)를 남긴다.

```md
## 문제

https://www.acmicpc.net/problem/0

---

## 핵심 키워드

- 키워드1

---

## 회고

### Learned (새롭게 알게 된 점)

- 

### Lacked (부족했던 점)

- 

### Longed for (시도할 점)

- 

### Liked (좋았던 점)

- 

```

## 참고 자료

- https://github.com/encrypted-def/basic-algo-lecture
- https://github.com/hanXen/basic-algo-lecture-python/tree/main
