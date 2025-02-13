# https://www.acmicpc.net/problem/2240

# 입력 받기
T, W = map(int, input().split())
drops = [int(input()) for _ in range(T)]

# DP 테이블 초기화
dp = [[0] * (W + 1) for _ in range(T + 1)]

# DP 수행
for t in range(1, T + 1):
    for w in range(W + 1):
        # 현재 자두가 떨어지는 나무 번호
        tree = drops[t - 1]

        # 현재 움직인 횟수에 따라 자두를 받을 수 있는지 확인
        if w == 0: # 한 번도 이동하지 않은 경우 (1번 나무 아래)
            dp[t][w] = dp[t - 1][w] + (1 if tree == 1 else 0)
        else: # 이동한 경우 (이전 상태 고려)
            dp[t][w] = max(dp[t - 1][w], dp[t - 1][w - 1]) + (1 if (tree == 1 and w % 2 == 0) or (tree == 2 and w % 2 == 1) else 0)

print(max(dp[T]))