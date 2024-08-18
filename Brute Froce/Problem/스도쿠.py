# https://www.acmicpc.net/problem/2580
# 시간 복잡도: 풀이1 > 풀이2 > 풀이3

### 풀이1. 일반적인 풀이
def is_possible(y, x, n):
	global matrix

	for c in range(9):
		if matrix[y][c] == n:
			return False
	for r in range(9):
		if matrix[r][x] == n:
			return False
	for r in range(3):
		for c in range(3):
			if matrix[3 * (y // 3) + r][3 * (x // 3) + c] == n:
				return False

	return True

def search(lev):
	global matrix, pos

	# base case
	if lev == len(pos): # 스도쿠 완성
		for i in range(9):
			for j in range(9):
				print(matrix[i][j], end=' ')
			print()
		exit(0)
		return

	y, x = pos[lev]

	# recursive case
	for n in range(1, 10):
		if is_possible(y, x, n):
			matrix[y][x] = n
			search(lev + 1)
			matrix[y][x] = 0


# input
matrix = [list(map(int, input().split())) for _ in range(9)]

# solve
pos = []
for i in range(9):
	for j in range(9):
		cur = matrix[i][j]
		if cur == 0:
			pos.append((i, j))

search(0)


### 풀이2. 셋을 이용한 풀이
def search(lev):
	global row, col, square, matrix, pos

	# base case
	if lev == len(pos): # 스도쿠 완성
		for i in range(9):
			for j in range(9):
				print(matrix[i][j], end=' ')
			print()
		exit(0)

	y, x = pos[lev]

	# recursive case
	for n in range(1, 10):
		if (n not in row[y]) and (n not in col[x]) and (n not in square[y // 3][x // 3]):
			row[y].add(n)
			col[x].add(n)
			square[y // 3][x // 3].add(n)
			matrix[y][x] = n

			search(lev + 1)

			matrix[y][x] = 0
			square[y // 3][x // 3].remove(n)
			col[x].remove(n)
			row[y].remove(n)


#initial settings
row = [set() for _ in range(9)]
col = [set() for _ in range(9)]
square = [[set() for _ in range(3)] for _ in range(3)]

# input
matrix = [list(map(int, input().split())) for _ in range(9)]

# solve
pos = []
for i in range(9):
	for j in range(9):
		cur = matrix[i][j]
		if cur == 0:
			pos.append((i, j))
		else:
			row[i].add(cur)
			col[j].add(cur)
			square[i // 3][j // 3].add(cur)

search(0)


### 풀이3. 리스트를 이용한 풀이

def search(lev):
	global row, col, square, matrix, pos

	# base case
	if lev == len(pos): # 스도쿠 완성
		for i in range(9):
			for j in range(9):
				print(matrix[i][j], end=' ')
			print()
		exit(0)

	y, x = pos[lev]

	# recursive case
	for n in range(1, 10):
		if (not row[y][n]) and (not col[x][n]) and (not square[y // 3][x // 3][n]):
			row[y][n] = col[x][n] = square[y // 3][x // 3][n] = True
			matrix[y][x] = n

			search(lev + 1)

			matrix[y][x] = 0
			row[y][n] = col[x][n] = square[y // 3][x // 3][n] = False


#initial settings
row = [[False] * 10 for _ in range(9)]
col = [[False] * 10 for _ in range(9)]
square = [[[False] * 10 for _ in range(3)] for _ in range(3)]

# input
matrix = [list(map(int, input().split())) for _ in range(9)]

# solve
pos = []
for i in range(9):
	for j in range(9):
		cur = matrix[i][j]
		if cur == 0:
			pos.append((i, j))
		else:
			row[i][cur] = col[j][cur] = square[i // 3][j // 3][cur] = True

search(0)

