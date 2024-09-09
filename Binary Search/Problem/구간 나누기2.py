# https://www.acmicpc.net/problem/13397

### 풀이1. 브루트 포스
import sys
input = lambda: sys.stdin.readline().rstrip()

MAX_NUM = 10_000

def is_possible(k):
	global arr, N, M

	min_num = arr[0]
	max_num = arr[0]
	cnt = 0

	for i in range(1, N):
		if arr[i] > max_num:
			max_num = arr[i]
		if arr[i] < min_num:
			min_num = arr[i]

		gap = max_num - min_num
		if gap > k:
			max_num = arr[i]
			min_num = arr[i]
			cnt += 1
	cnt += 1

	return (cnt <= M)

N, M = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(0, MAX_NUM):
	if is_possible(i):
		print(i)
		break

### 풀이2. 파라매트릭 서치
import sys
input = lambda: sys.stdin.readline().rstrip()

MAX_NUM = 10_000

def is_possible(k):
	global arr, N, M

	min_num = arr[0]
	max_num = arr[0]
	cnt = 0

	for i in range(1, N):
		if arr[i] > max_num:
			max_num = arr[i]
		if arr[i] < min_num:
			min_num = arr[i]

		gap = max_num - min_num
		if gap > k:
			max_num = arr[i]
			min_num = arr[i]
			cnt += 1
	cnt += 1

	return (cnt <= M)

def parametric_search(arr):
	cur = -1
	step = MAX_NUM

	while step != 0:
		while (cur + step <= MAX_NUM) and not is_possible(cur + step):
			cur += step
		step //= 2

	return cur

N, M = map(int, input().split())
arr = list(map(int, input().split()))

result = parametric_search(arr)
print(result + 1)