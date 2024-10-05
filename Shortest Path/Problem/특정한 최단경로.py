# https://www.acmicpc.net/problem/1504

import sys
input = lambda: sys.stdin.readline().rstrip()

from queue import PriorityQueue

INF = int(1e12)

def dijkstra(start_node):
	global N, adj_list
	
	dist = [INF for _ in range(N + 1)]
	pq = PriorityQueue()

	dist[start_node] = 0
	pq.put((0, start_node)) # (dist, node)

	while not pq.empty():
		cur_dist, cur_node = pq.get()

		for adj_node, adj_dist in adj_list[cur_node]:
			temp_dist = cur_dist + adj_dist
			if (temp_dist < dist[adj_node]):
				dist[adj_node] = temp_dist
				pq.put((temp_dist, adj_node))

	return dist

# Input
N, E = map(int, input().split()) # node, edge
adj_list = [[] for _ in range(N + 1)]

for _ in range(1, E + 1):
	a, b, c = map(int, input().split())
	adj_list[a].append((b, c))
	adj_list[b].append((a, c))

v1, v2 = map(int, input().split())

# Solve (다익스트라)
dist_1 = dijkstra(1)
dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)

case1 = dist_1[v1] + dist_v1[v2] + dist_v2[N] # 1 -> v1 -> v2 -> N
case2 = dist_1[v2] + dist_v2[v1] + dist_v1[N] # 1 -> v2 -> v1 -> N
ans = min(case1, case2)

print(ans if ans < INF else -1)