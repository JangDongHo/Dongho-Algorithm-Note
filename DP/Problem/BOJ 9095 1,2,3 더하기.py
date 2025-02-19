# https://www.acmicpc.net/problem/9095

## 풀이1. 재귀
def count_ways(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4

    return count_ways(n - 1) + count_ways(n - 2) + count_ways(n - 3)

T = int(input())
for _ in range(T):
    n = int(input())
    print(count_ways(n))

## 풀이2. DP
def count_ways(n):
    # 초기값 설정 (n이 1, 2, 3일 때 직접 반환)
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    
    # DP 테이블 생성
    dp = [0] * (n + 1)
    dp[1], dp[2], dp[3] = 1, 2, 4  # 초기값
    
    # 점화식 적용
    for i in range(4, n + 1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
    return dp[n]

T = int(input())
for _ in range(T):
    n = int(input())
    print(count_ways(n))
