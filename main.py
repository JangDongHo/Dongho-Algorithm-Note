def func(k):
	# base case
	if k == 0:
		return '-'

	# recursive case
	return func(k-1) + ' ' * (3 ** (k-1)) + func(k-1)

while True:
	try:
		N = int(input())
		print(func(N))
	except:
		break
