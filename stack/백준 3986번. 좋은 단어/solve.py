"""백준 3986 좋은 단어"""

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(word: str) -> bool:
    stack = []

    for c in word:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    return not stack


def main() -> None:
    N = int(sys_input())
    words = (sys_input() for _ in range(N))

    answer: int = sum(1 for w in words if solve(w))
    print(answer)


if __name__ == "__main__":
    main()
