# https://www.acmicpc.net/problem/11729

def hanoi(a, b, n):
	# Base Case: 원판이 1개일 때는 바로 목표 기둥으로 이동시킨다.
	if n == 1:
		print(a, b)
		return

	# 보조 기둥 번호
	auxiliary = 6 - a - b

	## 1단계: n-1개의 원판을 보조 기둥으로 이동시킨다.
	hanoi(a, auxiliary, n - 1)

	## 2단계: 가장 큰 원판을 목표 기둥으로 이동시킨다.
	print(a, b)

	## 3단계: 보조 기둥에 있는 n-1개의 원판을 목표 기둥으로 이동시킨다.
	hanoi(auxiliary, b, n - 1)

n = int(input())
print(2**n-1)
hanoi(1, 3, n)