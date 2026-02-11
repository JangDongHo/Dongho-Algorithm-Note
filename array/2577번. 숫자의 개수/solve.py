""" solve.py for 2577번. 숫자의 개수 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(A: int, B: int, C: int) -> list[int]:
    number = str(A * B * C)

    counts = [0] * 10
    for n in number:
        counts[int(n)] += 1
    return counts


def main() -> None:
    A, B, C = [int(sys_input()) for _ in range(3)]

    answer: list[int] = solve(A, B, C)

    print(*answer, sep="\n")


if __name__ == "__main__":
    main()