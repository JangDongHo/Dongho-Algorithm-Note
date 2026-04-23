"""백준 12852번. 1로 만들기 2"""

N = int(input())

dp = [0] * (N + 1)
pre = [0] * (N + 1)

for i in range(2, N + 1):
	dp[i] = dp[i - 1] + 1
	pre[i] = i - 1

	if i % 3 == 0 and dp[i // 3] + 1 < dp[i]:
		dp[i] = dp[i // 3] + 1
		pre[i] = i // 3

	if i % 2 == 0 and dp[i // 2] + 1 < dp[i]:
		dp[i] = dp[i // 2] + 1
		pre[i] = i // 2

print(dp[N])

cur = N
answer = []

while True:
	answer.append(cur)
	if cur == 1:
		break
	cur = pre[cur]

print(*answer)