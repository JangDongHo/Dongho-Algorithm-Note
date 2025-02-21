# https://www.acmicpc.net/problem/4963

import sys
sys.setrecursionlimit(int(1e4))

dx = [-1, 1, 0 ,0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]

def dfs(x, y):
    visited[y][x] = 1
    for d in range(8):
        nx = x + dx[d]
        ny = y + dy[d]
        if (0 <= nx < w) and (0 <= ny < h):
            if (visited[ny][nx] == 0) and (island[ny][nx] == 1):
                dfs(nx, ny)
            
while True:
    # 입력 값 받기
    w, h = map(int, input().split())
    if (w, h) == (0, 0):
        break

    island = [list(map(int, input().split())) for _ in range(h)]

    # DFS
    cnt = 0
    visited = [[0] * (w) for _ in range(h)]
    for y in range(h):
        for x in range(w):
            if (visited[y][x] == 0) and (island[y][x] == 1):
                dfs(x, y)
                cnt += 1
    print(cnt)
