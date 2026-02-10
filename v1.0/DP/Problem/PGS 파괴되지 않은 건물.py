# https://school.programmers.co.kr/learn/courses/30/lessons/92344?language=python3

def solution(board, skill):
    N = len(board) # 세로
    M = len(board[0]) # 가로
    
    # Solve (DP 차이 배열)
    dp = [[0 for _ in range(M + 2)] for _ in range(N + 2)] # 1-index

    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            degree = -degree
        r1, c1, r2, c2 = r1 + 1, c1 + 1, r2 + 1, c2 + 1
        dp[r1][c1] += degree
        dp[r1][c2 + 1] -= degree
        dp[r2 + 1][c1] -= degree
        dp[r2 + 1][c2 + 1] += degree
    
    for y in range(1, N + 1):
        for x in range(1, M + 1):
            dp[y][x] += dp[y - 1][x] + dp[y][x - 1] - dp[y - 1][x - 1]
    
    ans = 0
    for y in range(N):
        for x in range(M):
            ans += (board[y][x] + dp[y + 1][x + 1] > 0)
    
    return ans