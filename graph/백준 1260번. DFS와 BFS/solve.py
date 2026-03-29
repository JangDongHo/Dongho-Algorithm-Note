"""백준 1260번. DFS와 BFS"""

import sys
from collections import deque
input = sys.stdin.readline

bfs_out = []
dfs_out = []

def bfs(start_node: int):
    q = deque([start_node])
    bfs_visited[start_node] = True
    bfs_out.append(start_node)

    while q:
        cur_node = q.popleft()
        for nxt_node in adj_list[cur_node]:
            if not bfs_visited[nxt_node]:
                q.append(nxt_node)
                bfs_visited[nxt_node] = True
                bfs_out.append(nxt_node)

def dfs(cur_node: int):
    dfs_visited[cur_node] = True
    dfs_out.append(cur_node)
    
    for nxt_node in adj_list[cur_node]:
        if not dfs_visited[nxt_node]:
            dfs(nxt_node)

N, M, V = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

for i in range(1, N + 1):
    adj_list[i].sort()

bfs_visited = [False] * (N + 1)
dfs_visited = [False] * (N + 1)

# DFS
dfs(V)
print(*dfs_out)

# BFS
bfs(V)
print(*bfs_out)