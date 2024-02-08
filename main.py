from collections import deque

n = int(input())
school_map = []
teacher_list = []

for i in range(n):
  data = input().split()
  school_map.append(data)
  for j in range(n):
    if data[j] == 'T':
      teacher_list.append((i, j))

# 선생님 이동방향 정의
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


# 학생 찾는 함수
def find_student(x, y, dir):
  while 0 <= x < n and 0 <= y < n:
    if school_map[x][y] == 'S':
      return True
    if school_map[x][y] == 'O':
      break
    x += dx[dir]
    y += dy[dir]
  return False


def can_watch():
  for x, y in teacher_list:
    for dir in range(4):
      if find_student(x, y, dir):
        return True
  return False


def solution(count):
  global answer
  if count == 3:
    if not can_watch():
      answer = True
    return

  for i in range(n):
    for j in range(n):
      if school_map[i][j] == 'X':
        school_map[i][j] = 'O'
        solution(count + 1)
        school_map[i][j] = 'X'


answer = False
solution(0)
if answer:
  print('YES')
else:
  print('NO')
