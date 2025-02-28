# https://www.acmicpc.net/problem/2206

from collections import deque
import sys
input = lambda: sys.stdin.readline().strip()

def bfs():
    global N, M, adj_matrix, visited

    # 방향 정의
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    # 방문 배열: visited[x][y][0] -> 벽을 부수지 않음, visited[x][y][1] -> 벽을 부숨
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    
    # BFS 시작 (x좌표, y좌표, 벽을 부순 여부)
    queue = deque([(0, 0, 0)])
    visited[0][0][0] = 1  # 시작점 방문 처리
    
    while queue:
        x, y, broken = queue.popleft()
        
        # 목적지 도달하면 결과 출력
        if x == N - 1 and y == M - 1:
            print(visited[x][y][broken])
            return
        
        # 네 방향 이동
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M:
                # 이동 가능하고 아직 방문하지 않은 경우
                if adj_matrix[nx][ny] == 0 and visited[nx][ny][broken] == 0:
                    visited[nx][ny][broken] = visited[x][y][broken] + 1
                    queue.append((nx, ny, broken))
                
                # 벽을 만났고, 아직 벽을 부수지 않았다면
                elif adj_matrix[nx][ny] == 1 and broken == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    queue.append((nx, ny, 1))
    
    # 도착 불가능하면 -1 출력
    print(-1)

N, M = map(int, input().split())
adj_matrix = []

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

for i in range(N):
    adj_matrix.append(list(map(int, input())))

bfs()