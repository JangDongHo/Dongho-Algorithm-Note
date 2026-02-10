'''
난이도: 1
풀이 시간: 15분
시간 제한: 2초
메모리 제한: 128MB

성공 여부: 실패
'''

### 내가 푼 코드 (실패)
n = int(input())
h, m, s = 0, 0, 0
result = 0

while h < n:
  time = str(h + m + s)
  if time.find('3') != -1:
    result += 1
  s += 1
  if s == 60:
    m += 1
    s = 0
  if m == 60:
    h += 1
    m = 0

print(result)

### 책 코드

n = int(input())
result = 0

for i in range(n + 1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i) + str(j) + str(k):
        result += 1

print(result)
