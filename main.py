import sys
input = lambda: sys.stdin.readline().rstrip()

def is_possible(d):
	global arr, N, C

	cnt = 1
	prev_x = arr[0]
	for i in range(1, N):
		cur_x = arr[i]
		if cur_x - prev_x >= d:
			cnt += 1
			prev_x = arr[i]
	
	return (cnt >= C)

def parametric_search():
	cur = -1
	step = int(1e9) + 1

	while step != 0:
		while (cur + step <= int(1e9)) and is_possible(cur + step):
			cur += step
		step //= 2

	return cur


# Input
N, C = map(int, input().split())
arr = sorted([int(input()) for _ in range(N)])

# Solve
max_dis = parametric_search()
print(max_dis)