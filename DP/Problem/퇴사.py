'''
난이도: 2
목표 시간: 30분
시간 제한: 2초
메모리 제한: 512MB

성공 여부: 실패
'''
'''
접근 방식
- 뒤쪽부터 매 상담에 대하여 '현재 상담 일자의 이윤(p[i]) + 현재 상담을 마친 일자부터의 최대 이윤(dp[t[i] + i])'을 계산하면 된다.
- 이후에 계산된 각각의 값 중에서 최댓값을 출력하면 된다.
- dp[i] = i번째 날부터 마지막 날까지 낼 수 있는 최대 이익
- dp[i] = max(p[i] + dp[t[i] + i], max_value)가 된다.
- max_value는 뒤에서부터 계산할 때, 현재까지의 최대 상담 금액에 해당하는 변수이다.
'''

N = int(input())
time_list = []
point_list = []
dp = [0] * (N + 1)
max_value = 0

for _ in range(N):
  T, P = map(int, input().split())
  time_list.append(T)
  point_list.append(P)

for current_day in range(N - 1, -1, -1):
  next_day = time_list[current_day] + current_day
  if next_day <= N:
    dp[current_day] = max(point_list[current_day] + dp[next_day], max_value)
    max_value = dp[current_day]
  else:
    dp[current_day] = max_value

print(max_value)
