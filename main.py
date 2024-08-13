def check_board(x, y):
	global N, board
	best = 0

	count = 0
	bef = '-'
	for i in range(N):
		if board[y][i] == bef:
			count += 1
		else:
			count = 1
		bef = board[y][i]
		best = max(best, count)

	count = 0
	bef = '-'
	for j in range(N):
		if board[j][x] == bef:
			count += 1
		else:
			count = 1
		bef = board[j][x]
		best = max(best, count)

	return best

# Input
N = int(input())
board = [list(input()) for _ in range(N)]

# Init
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
answer = 0

# Brute Force
for y in range(N):
	for x in range(N):
		if y == x:
			answer = max(answer, check_board(x, y))
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if (0 <= nx < N) and (0 <= ny < N):
				if board[y][x] != board[ny][nx]:
					board[ny][nx], board[y][x] = board[y][x], board[ny][nx]
					answer = max(answer, check_board(x, y))
					board[ny][nx], board[y][x] = board[y][x], board[ny][nx]

print(answer)