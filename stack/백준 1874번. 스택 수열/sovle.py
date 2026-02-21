""" 백준 1874번. 스택 수열 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int) -> list[str]:
    stack = []
    out = []
    cur = 1

    for _ in range(n):
        target = int(sys_input())
        # 조건이 만족할 때까지 push 연산
        while cur <= target:
            stack.append(cur)
            out.append('+')
            cur += 1
        # pop 연산 가능한지 체크
        if stack[-1] == target:
            stack.pop()
            out.append('-')
        else:
            return ['NO']

    return out


def main() -> None:
    n = int(sys_input())

    answer: list[str] = solve(n)
    print(*answer, sep='\n')


if __name__ == "__main__":
    main()
