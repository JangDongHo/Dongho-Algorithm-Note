'''
난이도: 2
풀이 시간: 40분
시간 제한: 1초
메모리 제한: 128MB

성공 여부: 실패
'''

### 내가 푼 코드 (실패)
'''
접근 방법
1. 바라보는 방향을 기준으로 dx, dy 리스트를 만들어 캐릭터를 이동(전진)
2. 맵에서 방문한 곳은 -1로 변경
3. rotate_count 변수를 만들어 네 방향 모두 회전했는지 검사
'''
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

### 책 코드
# N, M을 공백을 기준으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1  # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
  array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 왼쪽으로 회전
def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3


# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
  # 왼쪽으로 회전
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]
  # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
  if d[nx][ny] == 0 and array[nx][ny] == 0:
    d[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_time = 0
    continue
  # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
  else:
    turn_time += 1
  # 네 방향 모두 갈 수 없는 경우
  if turn_time == 4:
    nx = x - dx[direction]
    ny = y - dy[direction]
    # 뒤로 갈 수 있다면 이동하기
    if array[nx][ny] == 0:
      x = nx
      y = ny
    # 뒤가 바다로 막혀있는 경우
    else:
      break
    turn_time = 0

# 정답 출력
print(count)
'''
새롭게 알게된 점
1. 리스트 컴프리헨션
- 리스트 컴프리헨션은 리스트를 초기화하는 방법 중 하나
- 대괄호([]) 안에 조건문과 반복문을 넣는 방식으로 리스트를 초기화
- 코딩 테스트에서 2차원 리스트를 초기화할 때 매우 효과적으로 사용 가능
  ```
  # N x M 크기의 2차원 리스트 초기화
  n = 3
  m = 4
  array = [[0] * m for _ in range(n)]
  print(array)
  ```
2. 이러한 시뮬레이터 문제는 별도의 알고리즘이 필요하기보다는 문제에서 요구하는 내용을 오류 없이 성실하게 구현만 할 수 있다면 풀 수 있다는 특징이 있다. 나 같은 경우는 맵의 외곽은 항상 바다로 돼있다는 점을 놓쳐서 문제를 푸는데 상당히 애를 먹었다.
'''
