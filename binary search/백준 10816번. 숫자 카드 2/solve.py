"""백준 10816번. 숫자 카드 2"""

import sys

def sys_input() -> str:
    return sys.stdin.readline().rstrip()


# x 초과인 값이 처음 등장하는 인덱스를 구하는 함수
def upper_bound(cards: list[int], x: int) -> int:
    left = 0
    right = len(cards)

    while left < right:
        mid = (left + right) // 2
        if cards[mid] > x:
            right = mid
        else:
            left = mid + 1
    
    return left


# x 이상인 값이 처음 등장하는 인덱스를 구하는 함수
def lowser_bound(cards: list[int], x: int) -> int:
    left = 0
    right = len(cards)

    while left < right:
        mid = (left + right) // 2
        if cards[mid] >= x:
            right = mid
        else:
            left = mid + 1
    
    return left


def solve(cards: list[int], targets: list[int]) -> list[int]:
    out = []

    for x in targets:
        cnt = upper_bound(cards, x) - lowser_bound(cards, x)
        out.append(cnt)

    return out


def main():
    N = int(sys_input())
    cards = sorted(list(map(int, sys_input().split())))
    M = int(sys_input())
    targets = list(map(int, sys_input().split()))

    answer = solve(cards, targets)
    print(*answer)


if __name__ == "__main__":
    main()