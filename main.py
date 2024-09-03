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