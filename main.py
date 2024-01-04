n, m = map(int, input().split())  # 맵의 세로 크기, 가로 크기
a, b, d = map(int, input().split())  # 맵의 시작 위치 (a, b)와 바라보는 방향

# 2차원 리스트 맵 생성
map_data = []
for i in range(n):
  map_input = list(map(int, input().split()))
  map_data.append(map_input)
map_data[a - 1][b - 1] = -1  # 이미 가본 곳은 -1로 표시 (시작 지점)

# 바라보는 방향 전진 기준 dx, dy
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

rotate_count = 0
result = 0

while True:
  nx, ny = 0, 0
  d -= 1  # 왼쪽 방향으로 회전
  rotate_count += 1
  if (d < 0):
    d = 3
  for j in range(4):
    if j == d:
      nx = a + dx[j]
      ny = b + dy[j]
      if map_data[nx][ny] != 0:
        continue
      rotate_count = 0
      result += 1
      map_data[nx][ny] = -1  # 이미 가본 곳은 -1로 표시

  # 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 경우
  if rotate_count > 5:
    # 후진이 가능한지 확인
    nx = -1 * nx
    ny = -1 * ny
    # 뒤쪽 방향이 바다일 경우 반복문 탈출
    if map_data[nx][ny] == 1:
      break

print(result)
