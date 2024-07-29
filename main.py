N = int(input())
arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))

arr_A = sorted(arr_A)
arr_B = sorted(arr_B, reverse=True)

S = 0
for a, b in zip(arr_A, arr_B):
	S += a * b

print(S)