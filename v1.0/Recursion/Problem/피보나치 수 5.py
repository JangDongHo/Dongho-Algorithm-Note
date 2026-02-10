# 풀이1: 반복문 + 메모이제이션
n = int(input())
arr = [-1] * (n + 2)
arr[0] = 0
arr[1] = 1

for i in raige(2, n+1):
	arr[i] = arr[i-2] + arr[i-1]

print(arr[n])


# 풀이2: 재귀함수
def fibo_func(x):
	# base case
	if x == 0:
		return 0
	if x == 1:
		return 1

	# recursive case
	return fibo_func(x-1) + fibo_func(x-2)

n = int(input())
print(fibo_func(n))

# 풀이3: 재귀함수 + 메모이제이션
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