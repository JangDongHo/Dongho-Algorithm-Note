"""백준 2751번 수 정렬하기 2"""
import sys
input = sys.stdin.readline

def quick_sort(st: int, en: int):
	if en - st <= 1:
		return

	left = st + 1
	right = en - 1
	pivot = arr[st]

	while True:
		while left <= right and arr[left] <= pivot:
			left += 1

		while left <= right and arr[right] > pivot:
			right -= 1

		if left > right:
			break

		# 아니라면 left랑 right 자리를 바꿈
		arr[left], arr[right] = arr[right], arr[left]

	arr[st], arr[right] = arr[right], arr[st]
	quick_sort(st, right)
	quick_sort(right + 1, en)

N = int(input())
arr = [int(input()) for _ in range(N)]
tmp = [0] * N

quick_sort(0, N)
print(*arr, sep="\n")