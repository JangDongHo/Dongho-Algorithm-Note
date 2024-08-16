from collections import deque

# 이동 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# Input
R, C = map(int, input().split()) # 세로, 가로
board = [list(input()) for _ in range(R)]

# Solve
answer = 1

q = deque()
q.append((0, 0, board[0][0]))

while q:
    x, y, used = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < C and 0 <= ny < R and board[ny][nx] not in used:
            q.append((nx, ny, used + board[ny][nx]))
            answer = max(answer, len(used)+1)

print(answer)




