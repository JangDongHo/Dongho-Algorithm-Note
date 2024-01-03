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
