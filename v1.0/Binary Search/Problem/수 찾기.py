# https://www.acmicpc.net/problem/1920

### 풀이1. 이분 탐색
def is_exist(arr, num):
	left = 0
	right = len(arr) - 1

	while left <= right:
		mid = (left + right) // 2

		if arr[mid] < num: 
			left = mid + 1

		if arr[mid] > num: 
			right = mid - 1

		if arr[mid] == num: 
			return 1

	return 0


N = int(input())
arr = sorted(list(map(int, input().split())))

M = int(input())
nums = list(map(int, input().split()))

for num in nums:
	print(is_exist(arr, num))

### 풀이2. set 자료구조 이용
N = int(input())
arr = set(map(int, input().split()))

M = int(input())
nums = list(map(int, input().split()))

for num in nums:
	print(1 if num in arr else 0)