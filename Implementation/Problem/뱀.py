'''
난이도: 2
목표 시간: 40분
시간 제한: 1초
메모리 제한: 128MB

1회독 성공 여부: 실패
2회독 성공 여부: 성공
풀이 시간: 40분
'''
'''
접근 방식
- 전형적인 시뮬레이션 문제 유형
- 이러한 시뮬레이션 문제 유형을 가장 쉽게 풀기 위해서는 그림으로 그려보는 것이 좋다.

이 문제는 큐를 이용한 구현 문제로 다음과 같이 접근하였다.

① 먼저 그래프(맵)을 모두 0으로 채워준다.
② 사과 위치는 모두 2로 채워준다.
③ 앞으로 뱀이 차지하고 있는 부분은 1로 채워줄 것이다.
④ 뱀이 이동할 때 마다 머리와 꼬리는 한 칸씩 전진한다. (즉, 몸의 길이는 그대로이다.)
⑤ 이동했을 때 사과를 먹으면 머리는 전진하지만 꼬리는 그대로이다. (즉, 몸의 길이가 한 칸 늘어난다.)
⑥ 방향 전환을 해야 하는 타이밍에 맞춰 L이면 왼쪽, D이면 오른쪽으로 방향전환을 한다.

④의 경우에는 처음 시작 할 때, [0, 0]을 큐에 넣어 몸길이 1 뱀의 초기 위치 상태를 저장하고,
오른쪽으로 한 칸 이동하여 [0, 0]을 큐에서 pop하고
[0, 1]을 큐에 push하여 뱀의 위치 상태를 변경한다.

이런 식으로 뱀을 전진시키면 된다. ( 큐를 뱀의 몸을 나타낸다고 생각하면 된다. )

⑤의 경우는 graph[x][y] = 2일 때 이다. 머리만 전진하면 되므로 큐에서 pop을 하지 않고,
큐에 현재 머리 위치만 push함으로써 뱀의 몸 길이를 늘려준다.

⑥의 경우에는 현재 시간이 방향전환을 해야 하는 시간이면, 입력한 방향에 맞게 전환을 해주면 된다.
(딕셔너리를 이용해 시간을 키값으로, 방향을 밸류값으로 입력받았다.)

출처: https://hongcoding.tistory.com/127
'''

### 2회독 성공 코드
from collections import deque

N = int(input())
K = int(input())
bam_list = deque()  # 뱀 몸통, 꼬리 저장하는 큐
bam_list.append((1, 1))

# 맵 생성
game_map = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(K):
  Y, X = map(int, input().split())
  game_map[Y][X] = 1

# 방향 정의 (북, 동, 남, 서)
dir = 1  #동쪽
steps = [(0, -1), (1, 0), (0, 1), (-1, 0)]

L = int(input())
time_list = deque()
for _ in range(L):
  [time, command] = input().split()
  time_list.append((int(time), command))

time = 0
while True:
  # 방향 전환 시간 확인
  if time_list and time_list[0][0] == time:
    if time_list[0][1] == 'L':
      dir -= 1
      if dir < 0:
        dir = 3
    if time_list[0][1] == 'D':
      dir += 1
      if dir > 3:
        dir = 0
    time_list.popleft()
  [x, y] = bam_list[-1]
  # 이동해보기
  nx = x + steps[dir][0]
  ny = y + steps[dir][1]
  # 벽에 안 부딪혔는지 확인
  if 0 < nx <= N and 0 < ny <= N:
    # 자기 자신의 몸과 안 부딪혔는지 확인
    if (nx, ny) not in bam_list:
      # 이동한 칸에 사과가 있는지 확인
      if game_map[ny][nx] == 1:
        game_map[ny][nx] = 0
      else:
        bam_list.popleft()
      bam_list.append((nx, ny))
      time += 1
      continue
  break

print(time + 1)

### 책 코드
n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)]  # 맵 정보
info = []  # 방향 회전 정보

# 맵 정보(사과 있는 곳은 1로 표시)
for _ in range(k):
  a, b = map(int, input().split())
  data[a][b] = 1

# 방향 회전 정보 입력
l = int(input())
for _ in range(l):
  x, c = input().split()
  info.append((int(x), c))

# 처음에는 오른쪽을 보고 있으므로(동, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def turn(direction, c):
  if c == "L":
    direction = (direction - 1) % 4
  else:
    direction = (direction + 1) % 4
  return direction


def simulate():
  x, y = 1, 1  # 뱀의 머리 위치
  data[x][y] = 2  # 뱀이 존재하는 위치는 2로 표시
  direction = 0  # 처음에는 동쪽을 보고 있음
  time = 0  # 시작한 뒤에 지난 '초' 시간
  index = 0  # 다음에 회전할 정보
  q = [(x, y)]  # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)

  while True:
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
    if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
      # 사과가 없다면 이동 후에 꼬리 제거
      if data[nx][ny] == 0:
        data[nx][ny] = 2
        q.append((nx, ny))
        px, py = q.pop(0)
        data[px][py] = 0
      # 사과가 있다면 이동 후에 꼬리 그대로 두기
      if data[nx][ny] == 1:
        data[nx][ny] = 2
        q.append((nx, ny))
    # 벽이나 뱀의 몸통과 부딪혔다면
    else:
      time += 1
      break
    x, y = nx, ny  # 다음 위치로 머리를 이동
    time += 1
    if index < l and time == info[index][0]:  # 회전할 시간인 경우 회전
      direction = turn(direction, info[index][1])
      index += 1
  return time


print(simulate())

### 블로그 코드
from collections import deque

n = int(input())
k = int(input())

graph = [[0] * n for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(k):
  a, b = map(int, input().split())
  graph[a - 1][b - 1] = 2

l = int(input())
dirDict = dict()
queue = deque()
queue.append((0, 0))

for i in range(l):
  x, c = input().split()
  dirDict[int(x)] = c

x, y = 0, 0
graph[x][y] = 1
cnt = 0
direction = 0


def turn(alpha):
  global direction
  if alpha == 'L':
    direction = (direction - 1) % 4
  else:
    direction = (direction + 1) % 4


while True:
  cnt += 1
  x += dx[direction]
  y += dy[direction]

  if x < 0 or x >= n or y < 0 or y >= n:
    break

  if graph[x][y] == 2:
    graph[x][y] = 1
    queue.append((x, y))
    if cnt in dirDict:
      turn(dirDict[cnt])

  elif graph[x][y] == 0:
    graph[x][y] = 1
    queue.append((x, y))
    tx, ty = queue.popleft()
    graph[tx][ty] = 0
    if cnt in dirDict:
      turn(dirDict[cnt])

  else:
    break

print(cnt)
