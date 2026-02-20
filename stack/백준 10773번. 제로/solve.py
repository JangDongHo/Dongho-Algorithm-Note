"""백준 10773. 제로"""

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(k: int) -> int:
    stack = []

    for _ in range(k):
        num = int(sys_input())
        if num == 0:
            stack.pop()
        else:
            stack.append(num)

    return sum(stack)


def main() -> None:
    K = int(sys_input())

    answer = solve(K)
    print(answer)


if __name__ == "__main__":
    main()
