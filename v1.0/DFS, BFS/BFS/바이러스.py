# https://www.acmicpc.net/problem/2606

from collections import deque

def bfs():
	global ans, visited, adj_list

	q = deque()
	q.append(1)
	visited[1] = True

	while q:
		node = q.popleft()
		ans += 1

		for adj_node in adj_list[node]:
			if not visited[adj_node]:
				q.append(adj_node)
				visited[adj_node] = True

# Input
N = int(input()) # 컴퓨터의 수
M = int(input()) # 컴퓨터 쌍의 수

adj_list = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

for _ in range(1, M + 1):
	sn, en = map(int, input().split())
	adj_list[sn].append(en)
	adj_list[en].append(sn)

# solve
ans = 0

bfs()
print(ans - 1)