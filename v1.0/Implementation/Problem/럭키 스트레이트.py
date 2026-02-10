'''
난이도: 1
목표 시간: 20분
시간 제한: 1초
메모리 제한: 256MB

성공 여부: 성공
풀이 시간: 5분
'''

### 내가 푼 코드

n = input()
middle_index = len(n) // 2
sum_left = 0
sum_right = 0

for i in range(middle_index):
  sum_left += int(n[i])
for i in range(middle_index, len(n)):
  sum_right += int(n[i])

if sum_left == sum_right:
  print("LUCKY")
else:
  print("READY")

### 책 코드
n = input()
length = len(n)  # 점수 값의 총 자릿수
summary = 0

# 왼쪽 부분의 자릿수의 합 더하기
for i in range(length // 2):
  summary += int(n[i])

# 오른쪽 부분의 자릿수의 합 빼기
for i in range(length // 2, length):
  summary -= int(n[i])

# 왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검사
if summary == 0:
  print("LUCKY")
else:
  print("READY")
