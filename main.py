import copy

# 입력값
N = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(reversed(copy.deepcopy(arr1)))
arr1 = [0] + arr1
arr2 = [0] + arr2

# DP 테이블 생성
dp1 = [1] * (N+1)
dp2 = [1] * (N+1)

# DP 테이블 초기값
dp1[1] = 1
dp2[1] = 1

# 문제 해결
for i in range(2, N+1):
    for j in range(1, i):
        if arr1[i] > arr1[j]:
            dp1[i] = max(dp1[i], dp1[j] + 1)
        if arr2[i] > arr2[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

dp2 = [0] + list(reversed(dp2))

result = 0
for i in range(1, N+1):
    result = max(result, dp1[i]+dp2[i]-1)

print(result)


