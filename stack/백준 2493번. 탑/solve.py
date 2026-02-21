""" 백준 2493번. 탑 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int) -> list[int]:
    arr = list(map(int, sys_input().split()))
    result = [0] * n

    stack = []  # (인덱스, 높이) 형태로 저장
    for i, h in enumerate(arr):
        while stack and h > stack[-1][1]:
            stack.pop()
        result[i] = stack[-1][0] if stack else 0
        stack.append((i + 1, h))

    return result


def main() -> None:
    N = int(sys_input())
    answer = solve(N)
    print(*answer)


if __name__ == "__main__":
    main()
