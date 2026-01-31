from collections import deque

T = int(input())

def bfs(visited):
    q = deque()
    q.append(i)
    visited[i] = True

    while(q):
        node = q.popleft()

        for adj_node in adj_list[node]:
            if visited[adj_node]:
                continue
            q.append(adj_node)
            visited[adj_node] = True

for t in range(T):
    N = int(input())

    # 순열 생성
    arr1 = list(range(1, N + 1))
    arr2 = list(map(int, input().split()))

    # 그래프 생성
    adj_list = [[] for _ in range(N + 1)]
    for i in range(N):
        adj_list[arr1[i]].append(arr2[i])

    # BFS 탐색
    visited = [False] * (N + 1)
    count = 0

    for i in range(1, N + 1):
        if not visited[i]:
            bfs(visited)
            count += 1

    print(count)

