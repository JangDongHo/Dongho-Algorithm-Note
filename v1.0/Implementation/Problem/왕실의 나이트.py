'''
난이도: 1
풀이 시간: 20분
시간 제한: 1초
메모리 제한: 128MB

성공 여부: 성공(16분)
'''

### 내가 푼 코드

input = input()
row, col = input[1], input[0]  # 행, 열
result = 0

# 열 숫자 변환
col_dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
x = int(row)
y = col_dic[col]

dx = [-2, -2, 2, 2, -1, 1, -1, 1]
dy = [-1, 1, -1, 1, -2, -2, 2, 2]

for i in range(len(dx)):
  nx = x + dx[i]
  ny = y + dy[i]
  if nx < 1 or nx > 8 or ny < 1 or ny > 8:
    continue
  result += 1

print(result)

### 책 코드

input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2),
         (-2, 1)]

result = 0
for step in steps:
  next_row = row + step[0]
  next_column = col + step[1]
  if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
    result += 1

print(result)
"""
새로 알게된 점
1. ord 함수
- 하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환합니다.
  - ex) ord('a')를 넣으면 정수 97을 반환합니다.

2. dx, dy 리스트를 선언하여 이동할 방향을 기록할 수도 있지만, 이번 문제에서는 steps 변수를 dx와 dy 변수의 기능을 대신하여 수행할 수 있도록 만들었다. 2가지 형태 모두 자주 사용되므로, 참고하도록 하자.
"""
