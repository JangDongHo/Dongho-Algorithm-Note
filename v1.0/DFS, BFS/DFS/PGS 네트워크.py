https://school.programmers.co.kr/learn/courses/30/lessons/43162

import sys
sys.setrecursionlimit(1000)

def dfs(cur_node):
    global adj_list, visited
    
    # Base Case
    if visited[cur_node]:
        return
    
    visited[cur_node] = True
    
    # Recursive Case
    for adj_node in adj_list[cur_node]:
        dfs(adj_node)

def solution(n, computers):
    global adj_list, visited
    
    adj_list = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                adj_list[i].append(j)
    
    # DFS
    ans = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            dfs(i)
            ans += 1
    
    return ans
    