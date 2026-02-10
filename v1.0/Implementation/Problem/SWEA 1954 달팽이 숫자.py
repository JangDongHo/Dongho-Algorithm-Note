# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PobmqAPoDFAUq&categoryId=AV5PobmqAPoDFAUq&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=2&pageSize=10&pageIndex=1

# 방향 정의
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

T = int(input())

for tc in range(1, T + 1):
	N = int(input())

	matrix = [[0] * N for _ in range(N)]

	x, y = 0, 0
	d = 0 # 방향(동->남->서->북)

	for cnt in range(1, N * N + 1):
		matrix[y][x] = cnt

		nx = x + dx[d]
		ny = y + dy[d]

		if (0 <= nx < N) and (0 <= ny < N) and matrix[ny][nx] == 0:
			x = nx
			y = ny
		else:
			d = (d + 1) % 4
			x += dx[d]
			y += dy[d]

	# 출력
	print(f"#{tc}")
	for m in matrix:
		print(" ".join(map(str, m)))