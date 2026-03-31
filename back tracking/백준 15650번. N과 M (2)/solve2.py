"""백준 15650번. N과 M (2)"""

N, M = map(int, input().split())

path = []

def dfs(start):
    if len(path) == M:
        print(*path)
        return

    for num in range(start, N + 1):
        path.append(num)
        dfs(num + 1)
        path.pop()

dfs(1)