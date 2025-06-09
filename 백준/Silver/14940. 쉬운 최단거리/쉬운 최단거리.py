from collections import deque
import sys
input = sys.stdin.readline

# 입력 값 받기
n, m = map(int, input().split())
matrix = []

for i in range(n):
    line = list(map(int, input().split()))
    matrix.append(line)

# BFS
dist = [[-1] * m for _ in range(n)]

q = deque()
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            dist[i][j] = 0
        elif matrix[i][j] == 2:
            q.append((j, i))
            dist[i][j] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    x, y = q.popleft()
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if (0 <= nx < m) and (0 <= ny < n) and (dist[ny][nx] == -1):
            dist[ny][nx] = dist[y][x] + 1
            q.append((nx, ny))

# 출력
for i in range(n):
    print(" ".join(map(str, dist[i])))