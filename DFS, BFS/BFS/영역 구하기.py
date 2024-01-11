'''
플랫폼: 백준(https://www.acmicpc.net/problem/2583)
난이도: 실버1
풀이 시간: 30분
시간 제한: 1초
메모리 제한: 128MB

성공 여부: 실패
'''

### 해설 코드
from collections import deque

m, n, k = map(int, input().split())
graph = [[False] * n for _ in range(m)]

# 모눈 종이에 직사각형 그리기
for _ in range(k):
  x1, y1, x2, y2 = map(int, input().split())
  for i in range(y1, y2):
    for j in range(x1, x2):
      graph[i][j] = True

# 이동 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# bfs 함수 정의
def bfs(x, y):
  global result
  size = 1
  q = deque()
  q.append((x, y))
  graph[x][y] = True

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < m and 0 <= ny < n and not graph[nx][ny]:
        graph[nx][ny] = True
        size += 1
        q.append((nx, ny))

  result.append(size)


result = []
for i in range(m):
  for j in range(n):
    if not graph[i][j]:
      bfs(i, j)

# 결과 출력
print(len(result))
result.sort()
for size in result:
  print(size, end=' ')
