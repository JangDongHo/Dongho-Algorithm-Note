"""백준 1021. 회전하는 큐"""

from collections import deque

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, targets: list[int]) -> int:
    q = deque(range(1, n + 1))
    min_count = 0

    for t in targets:
        idx = q.index(t)

        if idx <= len(q) - idx:
            q.rotate(-idx)
            min_count += idx
        else:
            q.rotate(len(q) - idx)
            min_count += len(q) - idx

        q.popleft()

    return min_count


def main() -> None:
    N, _ = map(int, sys_input().split())
    targets = list(map(int, sys_input().split()))

    answer: int = solve(N, targets)
    print(answer)


if __name__ == "__main__":
    main()
