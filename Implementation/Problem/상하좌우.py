'''
난이도: 1
풀이 시간: 15분
시간 제한: 1초
메모리 제한: 128MB

성공 여부: 성공(13분)
'''

### 내가 푼 코드

n = int(input())
movements = list(input().split())
y, x = 1, 1

for mv in movements:
  if mv == 'R':
    if y < n:
      y += 1
  if mv == 'L':
    if y > 1:
      y -= 1
  if mv == 'U':
    if x > 1:
      x -= 1
  if mv == 'D':
    if x < n:
      x += 1

print(x, y)

### 책 코드

n = int(input())
x, y = 1, 1
movements = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for move_type in movements:
  for i in range(len(move_types)):
    if move_type == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  if nx < 1 or nx > n or ny < 1 or ny > n:
    continue
  x, y = nx, ny

print(x, y)
'''
새롭게 알게된 점
- 연산 횟수: 이동 횟수 (시간복잡도 O(N))
- 이러한 문제는 일련의 명령을 따라서 개체를 차례대로 이동시킨다는 점에서 시뮬레이션 유형으로 분류되며 구현이 중요한 대표적인 문제이다.
'''
