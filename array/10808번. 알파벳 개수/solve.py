""" solve.py for 10808번. 알파벳 개수 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(S: str) -> list[int]:
    counts = [0] * 26
    for s in S:
        counts[ord(s) - ord('a')] += 1
    return counts


def main() -> None:
    S = sys_input()

    answer: list[int] = solve(S)

    print(*answer)


if __name__ == "__main__":
    main()