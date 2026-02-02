T = int(input())

def dfs(node):
    next_node = node
    while not visited[next_node]:
        visited[next_node] = True
        next_node = arr[next_node]

for _ in range(T):
    N = int(input())
    arr = [0] + list(map(int, input().split()))

    visited = [False] * (N + 1)
    count = 0

    for i in range(1, N + 1):
        if not visited[i]:
            dfs(i)
            count += 1

    print(count)
