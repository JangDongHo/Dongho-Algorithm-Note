from collections import deque

N = int(input())  # 맵 크기
map_list = []  # 맵
teacher_list = []  # 선생님 위치
result = False

# 맵 생성
for i in range(N):
  input_data = list(input().split())
  for j in range(N):
    if input_data[j] == 'T':
      teacher_list.append((j, i))
  map_list.append(input_data)

# 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 감시 피할 수 있는지 확인하는 함수
def is_can_avoid(test_map):
  q = deque(teacher_list)
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x
      ny = y
      while 0 <= nx < N and 0 <= ny < N:
        if test_map[ny][nx] == 'S':
          return False
        if test_map[ny][nx] == 'O':
          break
        nx += dx[i]
        ny += dy[i]
  return True


# 벽 설치 함수
def create_wall(count):
  if count == 3:
    if is_can_avoid(map_list):
      global result
      result = True
    return None
  for i in range(N):
    for j in range(N):
      if map_list[i][j] == 'X':
        map_list[i][j] = 'O'
        create_wall(count + 1)
        map_list[i][j] = 'X'


create_wall(0)

if result:
  print("YES")
else:
  print("NO")
