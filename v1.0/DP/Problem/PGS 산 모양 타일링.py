# https://school.programmers.co.kr/learn/courses/30/lessons/258705

def solution(n, tops):
    tops = [0] + tops
    
    dp = [0] * (n + 1)
    sub_dp = [0] * (n + 1)
    dp[0] = sub_dp[0] = 1
    
    for i in range(1, n + 1):
        # sub_dp
        if tops[i] == 0: # 삼각형이 위에 없는 경우
            sub_dp[i] = (dp[i - 1] + sub_dp[i - 1]) % 10007
        if tops[i] == 1: # 삼각형이 위에 있는 경우
            sub_dp[i] = (dp[i - 1] * 2 + sub_dp[i - 1]) % 10007
        # dp
        dp[i] = (sub_dp[i] + dp[i - 1]) % 10007
        
    return dp[n]