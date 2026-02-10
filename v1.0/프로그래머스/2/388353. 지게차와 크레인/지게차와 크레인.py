from collections import deque

def crane(grid, target):
    n, m = len(grid), len(grid[0])
    for i in range(n):
        for j in range(m):
            if grid[i][j] == target:
                grid[i][j] = '.'


def forklift(grid, target):
    n, m = len(grid), len(grid[0])
    
    # 외부 통로와 연결돼있는지 체크용
    visited = [[False]*m for _ in range(n)]
    q = deque()

    # 테두리에 있는 '.'을 시작으로 외부 통로 bfs
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n-1 or j == 0 or j == m-1:
                if grid[i][j] == '.' and not visited[i][j]:
                    visited[i][j] = True
                    q.append((i, j))

    # 외부와 연결된 모든 '.' 영역 탐색 (내부에 갇힌 '.'은 제외)
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    while q:
        x, y = q.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and grid[nx][ny] == '.':
                    visited[nx][ny] = True
                    q.append((nx, ny))

    # 외부와 맞닿아있는 target 컨테이너만 제거
    for i in range(n):
        for j in range(m):
            if grid[i][j] == target:
                for dx, dy in dirs:
                    ni, nj = i + dx, j + dy
                    # 이미 외부이거나, 외부와 통로가 이어져있는 경우
                    if not (0 <= ni < n and 0 <= nj < m) or visited[ni][nj]:
                        grid[i][j] = '.'
                        break


def solution(storage, requests):
    grid = [list(row) for row in storage]

    for req in requests:
        if len(req) == 1:
            forklift(grid, req)
        else:
            crane(grid, req[0])

    # 남은 컨테이너 개수
    return sum(cell != '.' for row in grid for cell in row)