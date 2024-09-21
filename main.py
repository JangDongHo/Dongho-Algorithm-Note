# Input
T = int(input())

for _ in range(T):
	text = input()

	# Solve
	ans = 0

	right = len(text) - 1

	for left in range(len(text)):
		print(left, right, ans)
		# 회문 여부 확인
		while (left < right) and (text[left] == text[right]):
			left += 1
			right -= 1

		if (left > right):
			break

		# 유사 회문 여부 확인
		if (left + 1 < len(text)) and (text[left + 1] == text[right]):
			print(left, right, ans)
			left += 1
			ans += 1
		elif (right - 1 >= 0) and (text[right - 1] == text[left]):
			print(left, right, ans)
			right -= 1
			ans += 1



	print(ans)