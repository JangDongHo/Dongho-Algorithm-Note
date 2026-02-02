import sys
sys.setrecursionlimit(2000)

T = int(input())

def dfs(node):
    if visited[node]:
        return

    visited[node] = True
    next_node = arr[node]

    dfs(next_node)

for _ in range(T):
    N = int(input())
    arr = [0] + list(map(int, input().split()))

    visited = [False] * (N + 1)
    cnt = 0

    for i in range(1, N + 1):
        if not visited[i]:
            dfs(i)
            cnt += 1

    print(cnt)