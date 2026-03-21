"""백준 15686번. 치킨 배달"""

import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

chickens = []
houses = []
answer = int(1e9)

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j))

for comb in combinations(chickens, M):
    city_dist = 0  # 이번 조합의 도시 치킨 거리

    for hx, hy in houses:
        min_dist = int(1e9)  # 각 집마다 초기화
        for cx, cy in comb:
            cur_dist = abs(hx - cx) + abs(hy - cy)
            min_dist = min(min_dist, cur_dist)
        city_dist += min_dist  # 집 하나의 최소 치킨 거리 누적

    answer = min(answer, city_dist)

print(answer)
