import sys
sys.setrecursionlimit(int(1e9))

def dfs(depth):
	global N, c, num_list, visited, answer

	# Base Case
	if depth == c:
		num = int("".join(num_list))
		answer = max(answer, num)
		return

	# Recursive Case
	for i in range(N - 1):
		for j in range(1, N):
			num_list[i], num_list[j] = num_list[j], num_list[i]
			num = int("".join(num_list))
			if (depth, num) not in visited:
				dfs(depth + 1)
				visited.append((depth, num))
			num_list[i], num_list[j] = num_list[j], num_list[i]
	

T = int(input())

for tc in range(1, T + 1):
	num_str, c = input().split()

	c = int(c)
	num_list = list(num_str)
	N = len(num_list)

	# Solve(DFS)
	visited = [] #(depth, num_str)
	answer = 0
	dfs(0)

	print(f"#{tc} {answer}")