# https://www.acmicpc.net/problem/10986

import sys
input = lambda: sys.stdin.readline()

# 입력 값 받기
N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# 누적합 + 나머지 연산
sum = 0
dp_remainder = [0] * M

for i in range(1, N + 1):
    sum += arr[i]
    dp_remainder[sum % M] += 1

# 가능한 조합(Combinations) 구하기
ans = dp_remainder[0] # 누적 합 배열에서 원소 값이 0인 개수 세기
for i in dp_remainder: # 원소 값이 같은 2개의 원소를 뽑는 모든 경우의 수 계산
    ans += i * (i - 1) // 2

print(ans)