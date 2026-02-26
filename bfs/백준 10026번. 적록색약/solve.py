"""백준 10026. 적록색약"""

import sys
import copy
from collections import deque


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def bfs(n: int, grid: list[list[str]], visited: list[list[bool]],
        sx: int, sy: int) -> None:
    target_color = grid[sx][sy]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = True

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and grid[nx][ny] == target_color:
                    q.append((nx, ny))
                    visited[nx][ny] = True


def solve(n: int, normal_grid: list[list[str]],
          special_grid: list[list[str]]) -> tuple[int, int]:
    normal_cnt = 0
    special_cnt = 0

    normal_visited = [[False] * n for _ in range(n)]
    special_visited = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if not normal_visited[i][j]:
                bfs(n, normal_grid, normal_visited, i, j)
                normal_cnt += 1

    for i in range(n):
        for j in range(n):
            if not special_visited[i][j]:
                bfs(n, special_grid, special_visited, i, j)
                special_cnt += 1

    return (normal_cnt, special_cnt)


def main() -> None:
    N = int(sys_input())
    normal_grid = [list(sys_input()) for _ in range(N)]  # 일반인 그리드
    special_grid = copy.deepcopy(normal_grid)  # 적록색약인 그리드

    for i in range(N):
        for j in range(N):
            if special_grid[i][j] == 'G':
                special_grid[i][j] = 'R'

    a1, a2 = solve(N, normal_grid, special_grid)
    print(a1, a2)


if __name__ == "__main__":
    main()
