# https://www.acmicpc.net/problem/1260

from collections import deque

def solve_dfs(node):
	global adj_list, visited
	
	# base case
	if visited[node]:
		return
	visited[node] = True

	print(node, end=' ')

	# recursive case
	for adj_node in adj_list[node]:
		solve_dfs(adj_node)


def solve_bfs(snode):
	global adj_list, visited

	q = deque()
	q.append(snode)
	visited[snode] = True

	while q:
		node = q.popleft()
		print(node, end=' ')

		for adj_node in adj_list[node]:
			if visited[adj_node]:
				continue
			q.append(adj_node)
			visited[adj_node] = True


# input
N, M, S = map(int, input().split())

adj_list = [[] for _ in range(N + 1)]
for _ in range(M):
	a, b = map(int, input().split())
	adj_list[a].append(b)
	adj_list[b].append(a)

for node in range(1, N + 1):
	adj_list[node].sort()

# solve
visited = [False] * (N + 1)
solve_dfs(S)
print()

visited = [False] * (N + 1)
solve_bfs(S)
print()