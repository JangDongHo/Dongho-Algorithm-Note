"""백준 1182번. 부분수열의 합"""

import sys

n, s = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

def solve(level: int, total: int) -> int:
	global answer

	# Base Case
	if level == n:
		if total == s:
			answer += 1
		return

	# 현재 원소를 선택하는 경우
	solve(level + 1, total + arr[level])

	# 현재 원소를 선택하지 않는 경우
	solve(level + 1, total)

solve(0, 0) # 모든 부분수열 탐색

# S가 0일 땐 공집합 제외
if s == 0:
	answer -= 1

print(answer)