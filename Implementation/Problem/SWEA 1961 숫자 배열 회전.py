# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pq-OKAVYDFAUq&categoryId=AV5Pq-OKAVYDFAUq&categoryType=CODE&problemTitle=%EC%88%AB%EC%9E%90+%EB%B0%B0%EC%97%B4&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

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