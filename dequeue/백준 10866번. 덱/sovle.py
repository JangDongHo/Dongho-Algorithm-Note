"""백준 10866번. 덱"""

from collections import deque

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int) -> list[int]:
    out = []
    q = deque()

    for _ in range(n):
        cmd = sys_input().split()
        op = cmd[0]

        match op:
            case 'push_front':
                q.appendleft(int(cmd[1]))
            case 'push_back':
                q.append(int(cmd[1]))
            case 'pop_front':
                out.append(q.popleft() if q else -1)
            case 'pop_back':
                out.append(q.pop() if q else -1)
            case 'size':
                out.append(len(q))
            case 'empty':
                out.append(0 if q else 1)
            case 'front':
                out.append(q[0] if q else -1)
            case 'back':
                out.append(q[-1] if q else -1)
    return out


def main() -> None:
    N = int(sys_input())

    answer = solve(N)
    print(*answer, sep='\n')


if __name__ == "__main__":
    main()
