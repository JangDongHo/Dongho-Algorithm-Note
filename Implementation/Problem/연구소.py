'''
난이도: 2
목표 시간: 40분
시간 제한: 2초
메모리 제한: 512MB

성공 여부: 실패
'''
'''
접근 방법
- 이 문제는 벽을 3개 설치하는 모든 경우의 수를 다 계산해야 한다.
  - 전체 맵의 크기가 8 x 8이므로, 벽을 설치할 수 있는 모든 조합의 수는 최악의 경우 64c3
  - 계산해보니, 대략 40,000개 정도로 완전 탐색을 이용해도 제한 시간 안에 문제를 해결할 수 있다.
- 따라서, 벽의 개수가 3개가 되는 모든 조합을 찾은 뒤에 그러한 조합에 대해서 안전 영역의 크기를 계산하면 된다.(BFS 사용)
'''

from collections import deque
import copy


# bfs
def bfs():
  q = deque()
  test_map = copy.deepcopy(lab_map)
  for i in range(n):
    for j in range(m):
      if test_map[i][j] == 2:
        q.append((i, j))

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if (0 <= nx < n) and (0 <= ny < m):
        if test_map[nx][ny] == 0:
          test_map[nx][ny] = 2
          q.append((nx, ny))

  global result
  result = max(result, get_score(test_map))


# 안전지역 계산
def get_score(test_map):
  count = 0
  for i in range(n):
    for j in range(m):
      if test_map[i][j] == 0:
        count += 1
  return count


# 벽 치기
def make_wall(count):
  if count == 3:
    bfs()
    return

  for i in range(n):
    for j in range(m):
      if lab_map[i][j] == 0:
        lab_map[i][j] = 1
        make_wall(count + 1)
        lab_map[i][j] = 0


n, m = map(int, input().split())
lab_map = []

for _ in range(n):
  lab_map.append(list(map(int, input().split())))

# 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

make_wall(0)
print(result)
