# https://www.acmicpc.net/problem/13549

from queue import PriorityQueue

INF = int(1e12)
MAX = int(1e5)

# Input
N, K = map(int, input().split())

# Solve (다익스트라)
pq = PriorityQueue()
pq.put((0, N)) # (시간, 노드)

times = [INF for _ in range(MAX + 1)]
times[N] = 0

while not pq.empty():
	cur_time, cur_node = pq.get()

	nexts = [
		(cur_node - 1, cur_time + 1),
		(cur_node + 1, cur_time + 1),
		(cur_node * 2, cur_time)
	]

	for next_node, next_time in nexts:
		if 0 <= next_node <= MAX:
			if next_time < times[next_node]:
				pq.put((next_time, next_node))
				times[next_node] = next_time

print(times[K])