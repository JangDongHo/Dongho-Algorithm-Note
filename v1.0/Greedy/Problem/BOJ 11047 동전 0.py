# 입력 값 받기
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.reverse()

# 큰 동전부터 그리디하게 사용
answer = 0
for coin in coins:
    cnt = K // coin
    if cnt > 0:
        K %= coin
        answer += cnt

print(answer)