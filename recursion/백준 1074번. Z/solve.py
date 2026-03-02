"""백준 1074번. Z"""

import sys


def sys_input() -> str:
	return sys.stdin.readline().rstrip()


def solve(n: int, r: int, c: int) -> int:
	# Base Case
	if n == 0:
		return 0

	# Recursive Case
	half = 2 ** (n - 1) # 한 변 길이의 절반
	if (r < half and c < half): # (r,c)가 1사분면일 때
		return solve(n - 1, r, c)
	if (r < half and c >= half): # (r,c)가 2사분면일 때
		return half * half + solve(n - 1, r, c - half)
	if (r >= half and c < half): # (r,c)가 3사분면일 때
		return 2 * half * half + solve(n - 1, r - half, c)
	if (r >= half and c >= half): # (r,c)가 4사분면일 때
		return 3 * half * half + solve(n - 1, r - half, c - half)


def main() -> None:
	N, r, c = map(int, sys_input().split())

	answer: int = solve(N, r, c)
	print(answer)


if __name__ == "__main__":
	main()