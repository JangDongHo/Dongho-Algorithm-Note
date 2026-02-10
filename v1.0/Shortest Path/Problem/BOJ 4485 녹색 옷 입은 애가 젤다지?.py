# https://www.acmicpc.net/problem/4485

from collections import deque
INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

t = 0
while True:
    t += 1

    N = int(input())
    if N == 0:
        break

    adj_matrix = [[0] * (N + 1)] # 동굴 행렬
    for _ in range(N):
        adj_matrix.append([0] + list(map(int, input().split())))

    # DP 테이블 초기화
    dp = [[INF] * (N + 1) for _ in range(N + 1)]
    dp[1][1] = adj_matrix[1][1]
    
    # BFS 큐 초기화
    q = deque([(1, 1)])
    
    while q:
        x, y = q.popleft()
        
        for d in range(4):
            nx = dx[d] + x
            ny = dy[d] + y
            if 0 < nx <= N and 0 < ny <= N:
                tmp_dist = dp[y][x] + adj_matrix[ny][nx]
                if tmp_dist < dp[ny][nx]:
                    dp[ny][nx] = tmp_dist
                    q.append((nx, ny))
                
    print(f"Problem {t}: {dp[N][N]}")