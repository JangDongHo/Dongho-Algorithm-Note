'''
난이도: 2
풀이 시간: 30분
시간 제한: 1초
메모리 제한: 128MB

성공 여부: 실패
'''

n, m = map(int, input().split())
array = []
for _ in range(n):
  array.append(int(input()))

d = [10001] * (m + 1)
d[0] = 0

for money_type in array:
  for i in range(money_type, m + 1):
    d[i] = min(d[i], d[i - money_type] + 1)

if d[m] == 10001:
  print(-1)
else:
  print(d[m])
