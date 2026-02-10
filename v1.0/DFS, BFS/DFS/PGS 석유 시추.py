# https://school.programmers.co.kr/learn/courses/30/lessons/250136

import sys
sys.setrecursionlimit(int(1e9))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global n, m, visited, land, cur_oil, cols
    visited[y][x] = True
    cur_oil += 1
    cols.add(x)
    
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and land[ny][nx] == 1:
            dfs(nx, ny)

def solution(_land):
    global n, m, visited, land, cur_oil, cols
    land = _land
    n, m = len(land), len(land[0])
    
    ans_list = [0] * m
    visited = [[False] * m for _ in range(n)]
    
    for y in range(n):
        for x in range(m):
            if not visited[y][x] and land[y][x] == 1:
                cur_oil = 0
                cols = set()
                dfs(x, y)
                for col in cols:
                    ans_list[col] += cur_oil
    
    return max(ans_list)