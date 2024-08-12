def sum_arr(chess, sy, sx):
	global board
	sum = 0

	for i in range(8):
		for j in range(8):
			sum += board[sy + i][sx + j] != chess[i][j]

	return sum


# Init
chess1 = [['' for _ in range(8)] for _ in range(8)]
chess2 = [['' for _ in range(8)] for _ in range(8)]

for i in range(8):
	for j in range(8):
		chess1[i][j] = 'B' if (i + j) % 2 == 0 else 'W'
		chess2[i][j] = 'W' if (i + j) % 2 == 0 else 'B'

# Input
N, M = map(int, input().split())
board = [input() for _ in range(N)]

# Solve
best = int(1e9)
for y in range(N):
	for x in range(M):
		if (y + 7 >= N) or (x + 7 >= M):
			continue
		case1 = sum_arr(chess1, y, x)
		case2 =	sum_arr(chess2, y, x)
		best = min(best, case1, case2)

print(best)