"""백준 15649번. N과 M (1)"""

import sys

def sys_input() -> str:
    return sys.stdin.readline().rstrip()

n, m = map(int, sys_input().split())
choose = [] # 나열한 원소를 보관
used = [False] * (n + 1) # 원소 사용 여부를 체크

def permutation(level: int) -> None:
    # Base Case
    if level == m:
        print(*choose)
        return

    # Recursive Case
    for i in range(1, n + 1):
        if not used[i]:
            choose.append(i)
            used[i] = True
            permutation(level + 1)
            used[i] = False
            choose.pop()

permutation(0)