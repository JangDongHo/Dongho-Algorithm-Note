# https://www.acmicpc.net/problem/11660

import sys
input = lambda: sys.stdin.readline()

# 입력 값 받기
N, M = map(int, input().split())

matrix = [[0] * (N + 1)]
for _ in range(N):
    matrix.append([0] + list(map(int, input().split())))

# 누적 합 행렬 생성
psum = [[0] * (N + 1) for _ in range(N + 1)]

for y in range(1, N + 1):
    for x in range(1, N + 1):
        psum[y][x] = (psum[y - 1][x] + psum[y][x - 1] - psum[y - 1][x - 1]) + matrix[y][x]

# 합 연산 수행
for _ in range(M):
    y1, x1, y2, x2 = map(int, input().split())
    total = psum[y2][x2] - (psum[y2][x1 - 1] + psum[y1 - 1][x2] - psum[y1 - 1][x1 - 1])
    print(total)
