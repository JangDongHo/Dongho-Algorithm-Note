"""백준 2164. 카드2"""

from collections import deque

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int) -> int:
    cards = deque(range(1, n + 1))

    while len(cards) > 1:
        cards.popleft()
        cards.append(cards.popleft())

    return cards[0]


def main() -> None:
    N = int(sys_input())

    answer = solve(N)
    print(answer)


if __name__ == "__main__":
    main()
