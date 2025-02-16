# https://www.acmicpc.net/problem/2252

from collections import deque

# 입력 받기 + 진입 차수 만들기
N, M = map(int, input().split())

adj_list = [[] for _ in range(N + 1)]
degree = [0] * (N + 1)

for _ in range(M):
    A, B = map(int, input().split())
    adj_list[A].append(B)
    degree[B] += 1

# 위상 정렬
q = deque()
for i in range(1, N + 1):
    if degree[i] == 0:
        q.append(i)

result = []
while q:
    cur_node = q.popleft()
    result.append(cur_node)

    for adj_node in adj_list[cur_node]:
        degree[adj_node] -= 1
        if degree[adj_node] == 0:
            q.append(adj_node)

print(*result)