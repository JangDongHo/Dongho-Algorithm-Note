# 풀이1. 직접 구현
def combination(idx, lev):
	global choose, arr, k

	# base case
	if lev == 6:
		for u in choose:
			print(u, end=' ')
		print()
		return

	# recursive case
	for i in range(idx, k):
		choose.append(arr[i])
		combination(i + 1, lev + 1)
		choose.pop()


while True:
	choose = []
	I = list(map(int, input().split()))

	k = I[0]
	arr = I[1:]
	if k == 0:
		break

	combination(0, 0)
	print()


# 풀이2. 라이브러리 사용
from itertools import combinations

while True:
	I = list(map(int, input().split()))

	k = I[0]
	arr = I[1:]
	if k == 0:
		break

	for comb in combinations(arr, 6):
		for c in comb:
			print(c, end=" ")
		print()
	print()