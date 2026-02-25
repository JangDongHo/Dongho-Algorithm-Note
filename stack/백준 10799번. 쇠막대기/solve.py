"""백준 10799 쇠막대기"""

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(s: str) -> int:
    stack = []
    cnt = 0

    for i in range(len(s)):
        if s[i] == '(':
            stack.append('(')
        else:  # ')'
            stack.pop()
            if s[i - 1] == '(':  # 레이저
                cnt += len(stack)
            else:  # 막대기 끝
                cnt += 1

    return cnt


def main() -> None:
    S = sys_input()

    answer: int = solve(S)
    print(answer)


if __name__ == "__main__":
    main()
