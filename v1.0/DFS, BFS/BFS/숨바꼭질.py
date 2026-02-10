# https://www.acmicpc.net/problem/1697

from collections import deque
MAX = 100_000

# Input
N, K = map(int, input().split())

# Init
q = deque()
q.append((N, 0)) # 수빈이가 있는 위치와 시간

visited = [False for _ in range(MAX + 1)]

# Solve (BFS)
while q:
	x, t = q.popleft()

	if x == K:
		print(t)
		exit()

	for nx in [x - 1, x + 1, 2 * x]:
		if (0 <= nx <= MAX) and not visited[nx]:
			q.append((nx, t + 1))
			visited[nx] = True
