'''
난이도: 2
목표 시간: 40분
시간 제한: 1초
메모리 제한: 512MB

성공 여부: 성공
풀이 시간: 35분
'''
'''
접근 방법
- 기존에 존재하는 치킨집을 M개로 줄여서, 일반 집들로부터 M개의 치킨집까지의 거리를 줄이는 것이 목표
- 파이썬의 조합 라이브러리를 사용하여 M개의 치킨집을 고를 수 있는 경우의 수와 모든 집까지의 최소 거리들의 합을 구해서, 치킨 거리의 최솟값을 구해 출력하면 된다.
  - 치킨집의 개수는 최대 13개고, M이 어떤 값이 되던 간에 13개 중에 m개를 뽑는 값은 100,000을 넘지 않는다. 또한, 집의 개수 또한 최대 100개 이므로, 모든 경우의 개수를 다 계산하더라도 시간 초과 없이 문제를 해결할 수 있다.
'''

### 내가 푼 코드

from itertools import combinations

n, m = map(int, input().split())
house_list = []
chicken_list = []
result = []
for i in range(n):
  data = list(map(int, input().split()))
  for j in range(n):
    if data[j] == 1:
      house_list.append((i, j))
    if data[j] == 2:
      chicken_list.append((i, j))


def chicken_street_distance(house_list, chicken_list):
  min_distance_sum = 0
  for house in house_list:
    min_distance = 10000
    [house_x, house_y] = house
    for chicken in chicken_list:
      [chicken_x, chicken_y] = chicken
      distance = abs(chicken_x - house_x) + abs(chicken_y - house_y)
      min_distance = min(distance, min_distance)
    min_distance_sum += min_distance
  return min_distance_sum


def choice_chicken_house(house_list, chicken_list):
  choice_lists = list(combinations(chicken_list, m))
  for choice_list in choice_lists:
    result.append(chicken_street_distance(house_list, choice_list))


choice_chicken_house(house_list, chicken_list)
print(min(result))

### 책 코드
from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
  data = list(map(int, input().split()))
  for c in range(n):
    if data[c] == 1:
      house.append((r, c))  # 일반 집
    elif data[c] == 2:
      chicken.append((r, c))  # 치킨집

# 모든 치킨 집 중에서 m개의 치킨 집을 뽑는 조합 계산
candidates = list(combinations(chicken, m))


# 치킨 거리의 합을 계산하는 함수
def get_sum(candidate):
  result = 0
  # 모든 집에 대하여
  for hx, hy in house:
    # 가장 가까운 치킨 집을 찾기
    temp = 1e9
    for cx, cy in candidate:
      temp = min(temp, abs(hx - cx) + abs(hy - cy))
    # 가장 가까운 치킨 집까지의 거리를 더하기
    result += temp
  # 치킨 거리의 합 반환
  return result


# 치킨 거리의 합의 최소를 찾아 출력
result = 1e9
for candidate in candidates:
  result = min(result, get_sum(candidate))

print(result)
