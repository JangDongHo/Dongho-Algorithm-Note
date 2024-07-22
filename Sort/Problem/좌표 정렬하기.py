N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]

sorted_arr = sorted(arr)

for xy in sorted_arr:
	print(xy[0], xy[1])