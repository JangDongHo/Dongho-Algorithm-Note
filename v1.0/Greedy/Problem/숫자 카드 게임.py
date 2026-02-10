'''
난이도: 1
풀이 시간: 30분
시간 제한: 1초
메모리 제한: 128MB
기출: 2019 국가 교육기관 코딩 테스트

성공 여부: 성공(15분)
'''

### 내가 푼 코드
n, m = map(int, input().split())
num_lists = []

for i in range(n):
  num_list = list(map(int, input().split()))
  num_lists.append(num_list)

result = 0

for num_list in num_lists:
  min_num = min(num_list)
  if min_num > result:
    result = min_num

print(result)

### 책 코드
n, m = map(int, input().split())

result = 0
for i in range(n):
  data = list(map(int, input().split()))
  min_num = min(data)
  result = max(result, min_num)

print(result)
