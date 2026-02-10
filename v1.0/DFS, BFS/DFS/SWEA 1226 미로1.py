# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14vXUqAGMCFAYD

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
	# Base Case
    if matrix[y][x] == 3:  # 도착 지점 확인
        return 1
    visited[y][x] = True

    # Recursive Case
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if (0 <= nx < N) and (0 <= ny < N) and not visited[ny][nx] and matrix[ny][nx] != 1:
            if dfs(nx, ny):  # 경로가 있으면 1을 반환
                return 1
    return 0  # 경로가 없으면 0을 반환

T = 10
for _ in range(1, T + 1):
    tc = int(input())
    N = 16
    matrix = [list(map(int, input())) for _ in range(N)]
    
    # 시작점과 방문 배열 초기화
    ans = 0
    visited = [[False] * N for _ in range(N)]
    ans = dfs(1, 1)
    
    print(f"#{tc} {ans}")
