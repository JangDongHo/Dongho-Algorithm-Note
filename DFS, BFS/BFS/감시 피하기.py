'''
난이도: 2.5
목표 시간: 60분
시간 제한: 2초
메모리 제한: 256MB

성공 여부: 실패
'''
'''
접근 방법
- 이전에 풀었었던 '연구소'와 유사한 문제
- 연구소 문제와 차이점은 사방으로 퍼지는 바이러스와 달리, 탐색 순서는 크게 상관없다는 것과 일직선으로 체크를 해야한다는 것
- 복도의 크기는 최악의 경우 6x6으로, 완전 탐색 시 36c3으로 모든 조합을 고려하여 완전 탐색을 수행하여도 시간 초과 없이 문제 해결이 가능
- 따라서, 나는 DFS 혹은 BFS를 이용하여 문제를 해결하는 방법을 생각했음
'''
### 내가 생각한 이상적인 코드

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


# 맵 실험
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

### 책 코드
'''
새롭게 알게된 점
- 파이썬의 조합 라이브러리를 사용하는 방법도 존재한다.
'''
from itertools import combinations

n = int(input())  # 복도의 크기
board = []  # 복도 정보 (N x N)
teachers = []  # 모든 선생님 위치 정보
spaces = []  # 모든 빈 공간 위치 정보

for i in range(n):
  board.append(list(input().split()))
  for j in range(n):
    # 선생님이 존재하는 위치 저장
    if board[i][j] == 'T':
      teachers.append((i, j))
    # 장애물을 설치할 수 있는 (빈 공간) 위치 저장
    if board[i][j] == 'X':
      spaces.append((i, j))


# 특정 방향으로 감시를 진행 (학생 발견: True, 학생 미발견: False)
def watch(x, y, direction):
  # 왼쪽 방향으로 감시
  if direction == 0:
    while y >= 0:
      if board[x][y] == 'S':  # 학생이 있는 경우
        return True
      if board[x][y] == 'O':  # 장애물이 있는 경우
        return False
      y -= 1
  # 오른쪽 방향으로 감시
  if direction == 1:
    while y < n:
      if board[x][y] == 'S':  # 학생이 있는 경우
        return True
      if board[x][y] == 'O':  # 장애물이 있는 경우
        return False
      y += 1
  # 위쪽 방향으로 감시
  if direction == 2:
    while x >= 0:
      if board[x][y] == 'S':  # 학생이 있는 경우
        return True
      if board[x][y] == 'O':  # 장애물이 있는 경우
        return False
      x -= 1
  # 아래쪽 방향으로 감시
  if direction == 3:
    while x < n:
      if board[x][y] == 'S':  # 학생이 있는 경우
        return True
      if board[x][y] == 'O':  # 장애물이 있는 경우
        return False
      x += 1
  return False


# 장애물 설치 이후에, 한 명이라도 학생이 감지되는지 검사
def process():
  # 모든 선생의 위치를 하나씩 확인
  for x, y in teachers:
    # 4가지 방향으로 학생을 감지할 수 있는지 확인
    for i in range(4):
      if watch(x, y, i):
        return True
  return False


find = False  # 학생이 한 명도 감지되지 않도록 설치할 수 있는지의 여부

# 빈 공간에서 3개를 뽑는 모든 조합을 확인
for data in combinations(spaces, 3):
  # 장애물들을 설치해보기
  for x, y in data:
    board[x][y] = 'O'
  # 학생이 한 명도 감지되지 않는 경우
  if not process():
    # 원하는 경우를 발견한 것임
    find = True
    break
  # 설치된 장애물을 다시 없애기
  for x, y in data:
    board[x][y] = 'X'

if find:
  print('YES')
else:
  print('NO')
