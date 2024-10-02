# https://www.acmicpc.net/problem/7576

### 풀이1. BFS 알고리즘
from collections import deque

# Input
M, N = map(int, input().split()) # M: 가로, N: 세로
adj_list = [] # 1: 익은 토마토, 0: 익지 않은 토마토, -1: 빈 칸
for _ in range(N):
	adj_list.append(list(map(int, input().split())))
visited = [[-1 for _ in range(M)] for _ in range(N)]

# Solve(BFS)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()

for y in range(N):
	for x in range(M):
		if adj_list[y][x] == 1:
			q.append((x, y))
			visited[y][x] = 0

while q:
	x, y = q.popleft()

	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]

		if (0 <= nx < M) and (0 <= ny < N) and (visited[ny][nx] == -1) and (adj_list[ny][nx] != -1):
			q.append((nx, ny))
			visited[ny][nx] = visited[y][x] + 1
			adj_list[ny][nx] = 1

max_ans = -1
for y in range(N):
	for x in range(M):
		if adj_list[y][x] == 0:
			print(-1)
			exit()
		max_ans = max(max_ans, visited[y][x])
print(max_ans)

### 풀이2. 풀이1 개선
from collections import deque

# Input
M, N = map(int, input().split())  # M: 가로, N: 세로
adj_list = [list(map(int, input().split())) for _ in range(N)]  # 토마토 상태 입력

# BFS 탐색을 위한 방향 설정 (상, 하, 좌, 우)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 익은 토마토의 위치를 큐에 미리 추가
q = deque()
for y in range(N):
    for x in range(M):
        if adj_list[y][x] == 1:
            q.append((x, y))

# BFS 탐색
while q:
    x, y = q.popleft()

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        # 범위 내에 있고, 익지 않은 토마토가 있는 경우
        if 0 <= nx < M and 0 <= ny < N and adj_list[ny][nx] == 0:
            adj_list[ny][nx] = adj_list[y][x] + 1  # 날짜를 1씩 증가시킴
            q.append((nx, ny))

# 결과 계산
max_days = 0
for row in adj_list:
    if 0 in row:  # 익지 않은 토마토가 남아있는 경우
        print(-1)
        exit()
    max_days = max(max_days, max(row))

# 첫날이 1로 표시되었으므로 1을 빼줌
print(max_days - 1)
