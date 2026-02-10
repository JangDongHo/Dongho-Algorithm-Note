# https://www.acmicpc.net/problem/2178

from collections import deque

# Input
N, M = map(int, input().split())

maps = [[0 for _ in range(M)]]
for _ in range(N):
	maps.append([0] + list(map(int, input())))

# Init
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[-1 for _ in range(M + 1)] for _ in range(N + 1)]

# Solve (BFS)
q = deque()
q.append((1, 1))
visited[1][1] = 1

while q:
	x, y = q.popleft()

	if x == M and y == N:
		break

	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		if (1 <= nx <= M) and (1 <= ny <= N) and visited[ny][nx] == -1 and maps[ny][nx] == 1:
				q.append((nx, ny))
				visited[ny][nx] = visited[y][x] + 1

print(visited[N][M])