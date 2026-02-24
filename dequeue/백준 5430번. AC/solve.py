"""백준 5430번. AC"""

import sys
from collections import deque


def sys_input() -> str:
	return sys.stdin.readline().rstrip()


def solve(funcs: list[str], list_str: str) -> str:
	deq = deque(list_str.split(',')) if list_str else deque()
	reverse = False

	# 함수 실행
	for func in funcs:
		if func == "R":
			reverse = not reverse
		elif func == "D":
			if not deq:
				return "error"

			if reverse:
				deq.pop()
			else:
				deq.popleft()

	# 출력값 정의
	if reverse:
		deq.reverse()

	return "[" + ",".join(deq) + "]"


def main() -> None:
	T = int(sys_input())
	for _ in range(T):
		funcs = list(sys_input())
		_ = int(sys_input())
		list_str = sys_input().lstrip('[').rstrip(']')

		answer: list[str] = solve(funcs, list_str)
		print(answer)


if __name__ == "__main__":
	main()