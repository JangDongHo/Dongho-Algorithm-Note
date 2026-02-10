# https://www.acmicpc.net/problem/11725

import sys
from collections import deque

input = lambda: sys.stdin.readline()

N = int(input())

# 인접 리스트 초기화
adj_list = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

# BFS
q = deque()
q.append(1) # 트리의 루트는 1

p_nodes = [-1] * (N + 1)
p_nodes[1] = 0 # 루트 노트의 부모 노드는 0으로 설정

while q:
    cur_node = q.popleft()
    for adj_node in adj_list[cur_node]:
        if p_nodes[adj_node] == -1:
            q.append(adj_node)
            p_nodes[adj_node] = cur_node

# 결과 출력
for p_node in p_nodes[2:]:
    print(p_node)