"""백준 1629 곱셈"""

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(a: int, b: int, c: int) -> int:
    if b == 0:
        return 1
    half = solve(a, b//2, c)
    half = (half * half) % c
    if b % 2 == 0:
        return half
    return (half * a) % c


def main() -> None:
    A, B, C = map(int, sys_input().split())

    answer: int = solve(A, B, C)
    print(answer)


if __name__ == "__main__":
    main()
