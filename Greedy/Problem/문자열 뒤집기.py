'''
난이도: 1
목표 시간: 20분
시간 제한: 2초
메모리 제한: 128MB

성공 여부: 성공
풀이 시간: 19분
'''

### 내가 푼 코드

data = input()
count = [0, 0]
now_group = int(data[0])

for i in range(1, len(data)):
  now_num = int(data[i])
  if now_num == now_group:
    continue
  count[now_group] += 1
  now_group = now_num

count[int(data[-1])] += 1
print(min(count))

### 책 코드
data = input()
count0 = 0  # 전부 0으로 바꾸는 경우
count1 = 0  # 전부 1로 바꾸는 경우

# 첫 번째 원소에 대해서 처리
if data[0] == '1':
  count0 += 1
else:
  count1 += 1

# 두 번째 원소부터 모든 원소를 확인하며
for i in range(len(data) - 1):
  if data[i] != data[i + 1]:
    # 다음 수에서 1로 바뀌는 경우
    if data[i + 1] == '1':
      count0 += 1
    # 다음 수에서 0으로 바뀌는 경우
    else:
      count1 += 1

print(min(count0, count1))
