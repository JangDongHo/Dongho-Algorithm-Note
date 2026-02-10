# https://www.acmicpc.net/problem/17609

### 풀이. 투 포인터 알고리즘

def is_palindrom(s):
	for left in range(len(s)):
		right = len(s) - left - 1
		if s[left] != s[right]:
			return False
	return True

def is_pseudo_palindrome(s):
	for left in range(len(s)):
		right = len(s) - left - 1
		if s[left] != s[right]:
			s1 = s[:left] + s[left + 1:]
			s2 = s[:right] + s[right + 1:]
			if is_palindrom(s1) or is_palindrom(s2):
				return True
			else:
				return False

def solve():
	# input
	S = input()

	# solve
	if is_palindrom(S):
		print(0)
		return

	if is_pseudo_palindrome(S):
		print(1)
		return

	print(2)


T = int(input())
for _ in range(T):
	solve()