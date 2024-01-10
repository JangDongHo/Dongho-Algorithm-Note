'''
플랫폼: 백준(https://www.acmicpc.net/problem/7569)
난이도: 골드5
풀이 시간: 40분
시간 제한: 1초
메모리 제한: 256MB

성공 여부: 실패
'''

# 내가 푼 코드 (실패)

from collections import deque

# 입력값 받기
m, n, h = map(int, input().split())
graph = []
distance = []
for _ in range(h):
  temp = []
  for _ in range(n):
    temp.append(list(map(int, input().split())))
  graph.append(temp)
for _ in range(h):
  temp = []
  for _ in range(n):
    temp.append([0] * m)
  distance.append(temp)

# 이동 방향 정의
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

# 모든 상자 탐색
for i in range(h):
  for j in range(n):
    for k in range(m):
      # 덜 익은 토마토이거나 토마토가 없을 경우 continue
      if graph[i][j][k] != 1:
        continue
      # 이미 방문했을 경우 continue
      if distance[i][j][k] > 0:
        continue
      # 3차원 bfs 수행
      queue = deque()
      queue.append((i, j, k))
      while queue:
        z, y, x = queue.popleft()
        for l in range(6):
          nx = x + dx[l]
          ny = y + dy[l]
          nz = z + dz[l]
          if nx < 0 or ny < 0 or nz < 0 or nx >= m or ny >= n or nz >= h:
            continue
          if graph[nz][ny][nx] != 0:
            continue
          if distance[nz][ny][nx] > 0:
            continue
          queue.append((nz, ny, nx))
          distance[nz][ny][nx] = distance[z][y][x] + 1

print(distance)

# 풀이 코드

from collections import deque

m,n,h = map(int,input().split()) # mn크기, h상자수
graph = []
queue = deque([])

for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int,input().split())))
        for k in range(m):
            if tmp[j][k]==1:
                queue.append([i,j,k])
    graph.append(tmp)

dx = [-1,1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

while(queue):
    x,y,z = queue.popleft()

    for i in range(6):
        a = x+dx[i]
        b = y+dy[i]
        c = z+dz[i]
        if 0<=a<h and 0<=b<n and 0<=c<m and graph[a][b][c]==0:
            queue.append([a,b,c])
            graph[a][b][c] = graph[x][y][z]+1

day = 0
for i in graph:
    for j in i:
        for k in j:
            if k==0:
                print(-1)
                exit(0)
        day = max(day,max(j))
print(day-1)