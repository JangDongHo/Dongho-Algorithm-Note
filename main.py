def rotate_matrix(m):
	global N
	ret = [[0] * N for _ in range(N)]

	for i in range(N):
		for j in range(N):
			ret[j][N - 1 - i] = m[i][j]

	return ret

T = int(input())

for tc in range(1, T + 1):
	N = int(input())
	matrix = []
	for n in range(N):
		matrix.append(list(input().split()))

	# Solve
	ans = []
	for _ in range(3):
		matrix = rotate_matrix(matrix)
		ans.append(matrix)

	# Output
	print(f"#{tc}")
	for i in range(N):
		for j in range(3):
			print("".join(ans[j][i]), end=" ")
		print()