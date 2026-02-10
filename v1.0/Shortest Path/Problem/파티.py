# https://www.acmicpc.net/problem/1238

import sys
input = lambda: sys.stdin.readline().rstrip()

from queue import PriorityQueue

MAX = int(1e9)

# 다익스트라 알고리즘
def dijkstra(start_node):
	global N, adj_list

	pq = PriorityQueue()
	pq.put((0, start_node))

	dist = [MAX for _ in range(N + 1)]
	dist[start_node] = 0

	while not pq.empty():
		cur_dist, cur_node = pq.get()

		for adj_node, adj_dist in adj_list[cur_node]:
			temp_dist = adj_dist + cur_dist
			if temp_dist < dist[adj_node]:
				pq.put((temp_dist, adj_node))
				dist[adj_node] = temp_dist

	return dist

# Input
N, M, X = map(int, input().split()) # 마을 수, 도로 수, 파티 장소
adj_list = [[] for _ in range(N + 1)]

for _ in range(M):
	s_i, e_i, t_i = map(int, input().split())
	adj_list[s_i].append((e_i, t_i))

# Solve (dijkstra)
ans = 0
X_to_start_dist = dijkstra(X)

for i in range(1, N + 1):
	start_to_X_dist = dijkstra(i)
	ans = max(ans, start_to_X_dist[X] + X_to_start_dist[i])

print(ans)