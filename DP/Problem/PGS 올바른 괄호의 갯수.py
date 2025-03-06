# https://school.programmers.co.kr/learn/courses/30/lessons/12929

def dfs(open_count, close_count):
    global n, dp

    # Base Case
    if open_count == n and close_count == n:
        return 1
    if close_count > open_count or open_count > n or close_count > n:
        return 0
    if dp[open_count][close_count] != -1:
        return dp[open_count][close_count]

    # Recursive Case
    answer = dfs(open_count + 1, close_count) + \
        dfs(open_count, close_count + 1)
    dp[open_count][close_count] = answer

    return answer


def solution(_n):
    global n, dp
    n = _n

    dp = [[-1] * (n + 1) for _ in range(n + 1)]
    return dfs(0, 0)
