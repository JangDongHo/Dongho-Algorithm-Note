# https://www.acmicpc.net/problem/1707

import sys
from collections import deque

input = sys.stdin.readline

def is_bipartite_graph(start_node) -> bool:
    global visited

    q = deque([start_node])
    visited[start_node] = True

    colors = [-1] * (V + 1)
    colors[start_node] = 0 # 정점 색깔은 0 또는 1

    while q:
        cur_node = q.popleft()
        for adj_node in adj_list[cur_node]:
            # 다음 정점을 방문했고, 현재 정점과 다음 정점 색깔이 같다면 이분 그래프가 아니다.
            if visited[adj_node]:
                if colors[cur_node] == colors[adj_node]:
                    return False
            # 다음 정점을 방문하지 않았다면 큐에 추가
            else:
                q.append(adj_node)
                visited[adj_node] = True
                colors[adj_node] = 0 if colors[cur_node] == 1 else 1 # 다른 정점 색깔 적용

    return True

T = int(input())
for _ in range(T):
    # 입력 값 받기
    V, E = map(int, input().split())

    # 인접 리스트 초기화
    adj_list = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v = map(int, input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)

    # BFS 탐색
    visited = [False] * (V + 1)

    ans = "YES"
    for v in range(1, V + 1):
        if not visited[v] and not is_bipartite_graph(v):
            ans = "NO"
            break

    print(ans)