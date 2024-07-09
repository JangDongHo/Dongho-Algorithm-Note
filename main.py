def fibo_func(x):
	global arr

	# base case
	if arr[x] != -1:
		return arr[x]

	# recursive case
	arr[x] = fibo_func(x - 1) + fibo_func(x - 2)
	return arr[x]

n = int(input())

arr = [-1] * (n + 2)
arr[0] = 0
arr[1] = 1

print(fibo_func(n))