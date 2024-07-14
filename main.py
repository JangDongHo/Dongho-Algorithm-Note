from itertools import permutations

N = int(input())
arr = [i for i in range(1, N+1)]

for per in permutations(arr, 3):
	for u in per:
		print(u, end=' ')
	print()