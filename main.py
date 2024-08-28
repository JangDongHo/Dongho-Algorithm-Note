import sys
sys.setrecursionlimit(int(1e6))

def binary_search(left, right, target):
	global sorted_arr
	# Base Case
	if left > right:
		return 0

	# Recursive Case
	mid = (left + right) // 2
	if sorted_arr[mid] == target:
		return 1
	elif sorted_arr[mid] < target:
		return binary_search(mid+1, right, target)
	else:
		return binary_search(left, mid, target)

# 입력값
N = int(input())
arr = list(map(int, input().split()))
M = int(input())
find_arr = list(map(int, input().split()))

# 문제 해결(이분 탐색)
sorted_arr = sorted(arr)

for target in find_arr:
	result = binary_search(0, len(sorted_arr) - 1, target)
	print(result)