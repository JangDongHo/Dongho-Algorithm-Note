# https://www.acmicpc.net/problem/11724

import sys
sys.setrecursionlimit(int(1e4))
input = lambda: sys.stdin.readline()

def dfs(node):
    visited[node] = True

    for adj_node in adj_list[node]:
        if not visited[node]:
            dfs(adj_node)

# 입력 값 받기
N, M = map(int, input().split())

adj_list = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

cnt = 0
visited = [False] * (N + 1)
for node in range(1, N + 1):
    if not visited[node]:
        cnt += 1
        dfs(node)
        
print(cnt)
