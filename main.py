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