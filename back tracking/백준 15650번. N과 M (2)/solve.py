"""백준 15650번. N과 M (2)"""

N, M = map(int, input().split())

path = []

def dfs(num):
    if len(path) == M:
        print(*path)
        return
    
    if num > N:
        return

    # 1. 현재 숫자 선택
    path.append(num)
    dfs(num + 1)
    path.pop()

    # 2. 현재 숫자 선택 안 함
    dfs(num + 1)

dfs(1)