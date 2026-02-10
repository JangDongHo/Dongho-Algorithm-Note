# https://www.acmicpc.net/problem/2606

def dfs(node):
	global ans, adj_list, visited

	# Base Case
	if visited[node]:
		return

	# Recursive Case
	visited[node] = True
	ans += 1

	for next_node in adj_list[node]:
		dfs(next_node)

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

dfs(1)
print(ans - 1)