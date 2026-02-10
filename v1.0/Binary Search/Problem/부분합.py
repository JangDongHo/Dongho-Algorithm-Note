# https://www.acmicpc.net/problem/1806

### 풀이 1. 이분 탐색 - O(NlogN)

MAX_NUM = 100_001

def parametric_search(left):
	global N, S, psum

	cur = left - 1
	step = N

	while (step != 0):
		while (cur + step <= N) and (psum[cur + step] - psum[left - 1] < S):
			cur += step
		step //= 2

	return (cur + 1)

# Input
N, S = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# Solve (Prefix Sum + Parametric Search)
psum = [0] * (N + 1)

for i in range(1, N+1):
	psum[i] = psum[i-1] + arr[i]

ans = MAX_NUM

for left in range(1, N+1):
	right = parametric_search(left)
	if right <= N:
		ans = min(ans, right - left + 1)

print(ans if ans != MAX_NUM else 0)


### 풀이 2. 투 포인터 - O(N)

MAX_NUM = 100_001

N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Solve (Tow Pointer)
ans = MAX_NUM
right = 0
cur_sum = 0

for left in range(N):
	while (right < N) and (cur_sum < S):
		cur_sum += arr[right]
		right += 1

	if (cur_sum >= S):
		ans = min(ans, right - left)

	cur_sum -= arr[left]

print(ans if ans != MAX_NUM else 0)