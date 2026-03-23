"""백준 11559번. Puyo Puyo"""

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(i: int, j: int, visited: list[list[bool]]) -> list[str]:
    color = field[i][j]
    q = deque([(i, j)])
    group = [(i, j)]
    visited[i][j] = True

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and field[nx][ny] == color:
                    q.append((nx, ny))
                    group.append((nx, ny))
                    visited[nx][ny] = True

    return group

N, M = 12, 6
field = list(list(input()) for _ in range(N))
chain = 0

while True:
    # 터질 그룹 찾기
    to_remove = []
    visited = [[False] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if field[i][j] == '.' or visited[i][j]:
                continue

            group = bfs(i, j, visited)

            if len(group) >= 4:
                to_remove.extend(group)

    # 없다면 종료
    if not to_remove:
        break

    # 있으면 한 번에 제거
    for x, y in to_remove:
        field[x][y] = '.'

    # 중력 적용
    for y in range(M):
        col = []

        for x in range(N):
            if field[x][y] != '.':
                col.append(field[x][y])

        for x in range(N - 1, -1, -1):
            if col:
                field[x][y] = col.pop()
            else:
                field[x][y] = '.'

    # 연쇄 +1
    chain += 1

print(chain)