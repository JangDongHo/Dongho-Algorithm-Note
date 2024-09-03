# https://www.acmicpc.net/problem/3020

### 풀이1. DP
import sys
input = lambda: sys.stdin.readline().rstrip()

# Input
N, H = map(int, input().split())

bottoms = [0] * (H+1)
tops = [0] * (H+1)

for i in range(N):
	num = int(input())
	if i % 2 == 0:
		bottoms[num] += 1
	else:
		tops[H-num+1] += 1

# Solve
dp = [0] * (H+1)
dp[1] = N // 2

min_cnt = dp[1]
result_cnt = 1

for h in range(2, H+1):
	dp[h] = dp[h-1] - bottoms[h-1] + tops[h]

	if dp[h] == min_cnt:
		result_cnt += 1
	if dp[h] < min_cnt:
		result_cnt = 1
		min_cnt = dp[h]

print(min_cnt, result_cnt)

### 풀이2. DP 사용 X
import sys
input = lambda: sys.stdin.readline().rstrip()

# input
N, H = map(int, input().split())

tops = [0] * (H + 1)
bots = [0] * (H + 1)

for i in range(N):
	num = int(input())
	if i % 2 == 0:
		bottoms[num] += 1
	else:
		tops[H - num + 1] += 1

# solve
min_cnt = int(1e12)
result_cnt = 0

cnt = N // 2
for h in range(1, H + 1):
    cnt -= bottoms[h - 1]
    cnt += tops[h]
	
    if min_cnt  == cnt:
        result_cnt += 1

    if min_cnt > cnt:
        min_cnt = cnt
        result_cnt = 1

print(min_cnt, result_cnt)

### 풀이3. 이분 탐색
import sys
input = lambda: sys.stdin.readline().rstrip()

def get_idx(arr, num): # return 'idx' if arr[idx] = num
	cur = -1
	step = len(arr)
	
	while step != 0:
		while cur + step < len(arr) and arr[cur + step] <= num:
			cur += step
		step //= 2
		
	return cur


# input
N, H = map(int, input().split())

tops = []
bottoms = []

for i in range(N):
	num = int(input())
	if i % 2 == 0:
		bottoms.append(num)
	else:
		tops.append(H - num + 1)

tops = sorted(tops)
bottoms = sorted(bottoms)

# solve
min_cnt = int(1e12)
result_cnt = 0

for h in range(1, H + 1):
	cnt_bot = (N // 2) - (get_idx(bottoms, h - 1) + 1)
	cnt_top = get_idx(tops, h) + 1
	
	if min_cnt == cnt_bot + cnt_top:
		result_cnt += 1

	if min_cnt > cnt_bot + cnt_top:
		min_cnt = cnt_bot + cnt_top
		result_cnt = 1

print(min_cnt, result_cnt)