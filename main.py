from collections import deque

T = int(input())

for _ in range(T):
    # 입력 값 받기
    N, K = map(int, input().split())
    build_list = [0] + list(map(int, input().split()))

    # 그래프 및 진입 차수
    adj_list = [[] for _ in range(N + 1)]
    degrees = [0] * (N + 1)
    for _ in range(K):
        X, Y = map(int, input().split())
        adj_list[X].append(Y)
        degrees[Y] += 1

    W = int(input())

    q = deque()
    dp = [0] * (N + 1)

    for i in range(1, N + 1):
        if degrees[i] == 0:
            q.append(i)
            dp[i] = build_list[i]

    # 위상 정렬
    while q:
        cur_node = q.popleft()

        for adj_node in adj_list[cur_node]:
            degrees[adj_node] -= 1
            dp[adj_node] = max(dp[adj_node], dp[cur_node] + build_list[adj_node])
            if degrees[adj_node] == 0:
                q.append(adj_node)

        if cur_node == W:
            break

    print(dp[W])

