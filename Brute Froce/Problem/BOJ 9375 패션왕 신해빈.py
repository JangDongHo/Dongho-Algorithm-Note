# https://www.acmicpc.net/problem/9375

import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().strip()

# 테스트 케이스 개수
T = int(input())

for _ in range(T):
    # 의상 개수
    n = int(input())

    # 의상 종류별 개수 저장
    clothes = defaultdict(int)

    # 의상 입력 받기
    for _ in range(n):
        _, category = input().split()
        clothes[category] += 1  # 해당 카테고리의 의상 개수 증가

    # 조합의 수 계산 (각 카테고리에서 선택 안 하는 경우 +1 포함)
    result = 1
    for count in clothes.values():
        result *= (count + 1)

    # 알몸(아무것도 안 입은 경우) 제외
    print(result - 1)