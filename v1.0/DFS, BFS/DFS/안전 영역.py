# https://www.acmicpc.net/problem/2468

import sys
sys.setrecursionlimit(int(1e6))

def dfs(y, x, h):
	global adj_list, visited, N, dx, dy

	# Base Case
	if not (0 <= y < N and 0 <= x < N):
		return
	if visited[y][x] or adj_list[y][x] <= h:
		return

	# Recursive Case
	visited[y][x] = True

	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		dfs(ny, nx, h)

# Input
N = int(input())
adj_list = []
for _ in range(N):
	adj_list.append(list(map(int, input().split())))

# Solve(DFS)
max_ans = 0
dx = [-1, 1, 0, 0]
dy = [0, 0 , -1, 1]

for h in range(101):
	ans = 0
	visited = [[False for _ in range(N)] for _ in range(N)]
	for i in range(N):
		for j in range(N):
			if (not visited[i][j]) and (adj_list[i][j] > h):
				dfs(i, j, h)
				ans += 1
	max_ans = max(ans, max_ans)

print(max_ans)