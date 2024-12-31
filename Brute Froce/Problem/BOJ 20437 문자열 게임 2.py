from collections import defaultdict

T = int(input())

for tc in range(T):
	W = input()
	k = int(input())

	dict = defaultdict(list)
	for i, c in enumerate(W):
		dict[c].append(i)

	min_len, max_len = int(1e9), -1
	for idx_list in dict.values():
		for i in range(len(idx_list) - k + 1):
			length = idx_list[i + k - 1] - idx_list[i] + 1
			min_len = min(min_len, length)
			max_len = max(max_len, length)

	if max_len != -1:
		print(min_len, max_len)
	else:
		print(-1)

	