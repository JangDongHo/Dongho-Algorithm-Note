from collections import deque

# 0: 갈 수 없는 땅
# 1: 갈 수 있는 땅
# 2: 목표 지점

# 입력 값 받기
n, m = map(int, input().split())
matrix = []

for i in range(n):
    line = list(map(int, input().split()))
    matrix.append(line)

# BFS
visited = [[-1] * m for _ in range(n)]
q = deque()
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            visited[i][j] = 0
        elif matrix[i][j] == 2:
            q.append((j, i))
            visited[i][j] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    x, y = q.popleft()
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if (0 <= nx < m) and (0 <= ny < n) and (visited[ny][nx] == -1):
            visited[ny][nx] = visited[y][x] + 1
            q.append((nx, ny))

# 출력
for i in range(n):
    print(" ".join(map(str, visited[i])))