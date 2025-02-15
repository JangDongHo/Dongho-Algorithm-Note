import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    # 입력 받으면서 진입 차수(In-degree) 갱신하기
    N, K = map(int, input().split())
    D = [0] + list(map(int, input().split()))

    adj_list = [[] for _ in range(N + 1)]
    degree = [0] * (N + 1)
    for _ in range(K):
        X, Y = map(int, input().split())
        adj_list[X].append(Y)
        degree[Y] += 1

    W = int(input())

    # 초기 진입 차수 세팅
    q = deque()
    dp = [0] * (N + 1) # 건설 시간 메모이제이션

    for i in range(1, N + 1):
        if degree[i] == 0:
            q.append(i)
            dp[i] = D[i]

    # 큐 돌리기
    while q:
        cur_node = q.popleft()

        for adj_node in adj_list[cur_node]:
            degree[adj_node] -= 1
            # 어느 한 지점에 들어오는 경로가 두 개 이상이라면 그 경로중 건설 시간이 큰 값을 선택
            dp[adj_node] = max(dp[cur_node] + D[adj_node], dp[adj_node])
            if degree[adj_node] == 0:
                q.append(adj_node)

        if cur_node == W:
            break

    print(dp[W])