"""백준 14499번. 주사위 굴리기"""

from collections import deque

CEIL_INDEX = 0
FLOOR_INDEX = 2

dx = [0, 0, -1, 1]  # 동 서 북 남
dy = [1, -1, 0, 0]

q1 = deque([0] * 4)  # 천장-남-바닥-북
q2 = deque([0] * 4)  # 천장-동-바닥-서


def solve(x: int, y: int, cmd: int):
    # 먼저 이동 가능한지 확인
    nx = x + dx[cmd - 1]
    ny = y + dy[cmd - 1]

    if not (0 <= nx < N and 0 <= ny < M):
        return x, y

    # 주사위 굴리기
    if cmd in (1, 2):
        q2.rotate(1 if cmd == 1 else -1)
        q1[CEIL_INDEX] = q2[CEIL_INDEX]
        q1[FLOOR_INDEX] = q2[FLOOR_INDEX]

    elif cmd in (3, 4):
        q1.rotate(1 if cmd == 4 else -1)
        q2[CEIL_INDEX] = q1[CEIL_INDEX]
        q2[FLOOR_INDEX] = q1[FLOOR_INDEX]

    if board[nx][ny] == 0:
        board[nx][ny] = q1[FLOOR_INDEX]
    else:
        q1[FLOOR_INDEX] = board[nx][ny]
        q2[FLOOR_INDEX] = board[nx][ny]
        board[nx][ny] = 0

    # 주사위 윗면 숫자 출력
    print(q1[CEIL_INDEX])

    return nx, ny


N, M, x, y, K = map(int, input().split())
board = list(list(map(int, input().split())) for _ in range(N))
cmds = list(map(int, input().split()))

for cmd in cmds:
    x, y = solve(x, y, cmd)
