# https://www.acmicpc.net/problem/1753

import sys
input = lambda: sys.stdin.readline().rstrip()

from queue import PriorityQueue

INF = int(1e12)

# input
V, E = map(int, input().split())
K = int(input())

adj_list = [[] for _ in range(V + 1)]
for _ in range(E):
	u, v, w = map(int, input().split())
	adj_list[u].append([v, w])

# solve (dijkstra)
dist = [INF] * (V + 1)

pq = PriorityQueue()
dist[K] = 0
pq.put([0, K])

while not pq.empty():
	cur_dist, cur_node = pq.get()
	for adj_node, adj_dist in adj_list[cur_node]:
		temp_dist = cur_dist + adj_dist
		if temp_dist < dist[adj_node]:
			dist[adj_node] = temp_dist
			pq.put([temp_dist, adj_node])

for d in dist[1:]:
    print(d if d != INF else 'INF')