# N과 M (4)

def dfs(start):
    # Base Case
    if len(s) == M:
        print(" ".join(map(str, s)))
        return

    # Recursive Case
    for i in range(start, N + 1):
        s.append(i)
        dfs(i)
        s.pop()

N, M = map(int, input().split())
s = []
dfs(1)