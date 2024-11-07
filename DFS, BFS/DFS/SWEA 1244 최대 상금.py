# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&problemLevel=4&contestProbId=AV15Khn6AN0CFAYD&categoryId=AV15Khn6AN0CFAYD&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=4&pageSize=10&pageIndex=1

def dfs(depth):
    global ans

    if depth == M:
        ans = max(ans, int(''.join(arr)))
        return

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]

            check = int(''.join(arr))
            if (depth, check) not in visited:
                visited.append((depth, check))
                dfs(depth + 1)

            arr[i], arr[j] = arr[j], arr[i]


result = []
T = int(input())
for case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(str(N))
    visited = []
    ans = 0
    dfs(0)

    print(f"#{case} {ans}")