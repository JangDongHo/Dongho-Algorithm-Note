"""백준 15683번. 감시"""

import sys

input = sys.stdin.readline
N, M = map(int, input().split())
office = list(list(map(int, input().split())) for _ in range(N))
answer = int(1e9)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cctv_dir = {
    1: [[0], [1], [2], [3]],                 			# 한 방향
    2: [[0, 2], [1, 3]],                     			# 상하 / 좌우
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],     			# 직각
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]], 	# 세 방향
    5: [[0, 1, 2, 3]]                        			# 네 방향
}

def watch(x: int, y: int, dirs: list[int]):
	changed = [] # (nx, ny)

	for d in dirs:
		nx, ny = x, y
		while True:
			nx += dx[d]
			ny += dy[d]

			if not (0 <= nx < N and 0 <= ny < M):
				break
			if office[nx][ny] == 6:
				break

			if office[nx][ny] == 0:
				office[nx][ny] = -1
				changed.append((nx, ny))

	return changed


def dfs(idx: int) -> None:
	global answer

	# Base Case 
	if idx == len(cctv_list):
		cnt = sum(row.count(0) for row in office)
		answer = min(answer, cnt)
		return

	x, y, t = cctv_list[idx]

	for dirs in cctv_dir[t]:
		changed = watch(x, y, dirs)
		dfs(idx + 1)
		for nx, ny in changed:
			office[nx][ny] = 0


# CCTV 초기 좌표 구하기
cctv_list = [] # (x, y, type)
for i in range(N):
	for j in range(M):
		cur_type = office[i][j]
		if cur_type in range(1, 6):
			cctv_list.append((i, j, cur_type))

dfs(0)
print(answer)