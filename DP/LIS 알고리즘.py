# 가장 긴 증가하는 부분 수열(LIS) 알고리즘
for i in range(1, N):
  for j in range(i):
    if input_list[j] < input_list[i]:
      dp[i] = max(dp[i], dp[j] + 1)
