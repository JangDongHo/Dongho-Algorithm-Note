"""백준 9663번. N-Queen"""

import sys

def sys_input() -> str:
    return sys.stdin.readline().rstrip()

N = int(sys_input())
is_used1 = [False] * 30
is_used2 = [False] * 30
is_used3 = [False] * 30
answer = 0

def solve(n: int, y: int) -> int:
    global answer

    # Base Case
    if y == n:
        answer += 1
        return

    for x in range(n):
        # 세로 줄, 좌측 대각선, 우측 대각선 확인
        if is_used1[x] or is_used2[x + y] or is_used3[y - x + n - 1]:
            continue

        is_used1[x] = True
        is_used2[x + y] = True
        is_used3[y - x + n - 1] = True
        solve(n, y + 1)
        is_used1[x] = False
        is_used2[x + y] = False
        is_used3[y - x + n - 1] = False
    
solve(N, 0)
print(answer)