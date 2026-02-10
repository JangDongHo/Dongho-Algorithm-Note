'''
난이도: 1
목표 시간: 30분
시간 제한: 1초
메모리 제한: 128MB

성공 여부: 실패
'''
'''
접근 방법
- k 값이 충분하다면 음식을 다 먹는데 드는 시간이 가장 적은 것부터 처리해버리자!
- 위와 같은 생각을 거치니 우선순위 큐라는 자료구조를 쉽게 떠올릴 수 있었고 heapq 모듈을 사용해 최소 힙을 구성했습니다.
- 최소 힙의 노드에는 [ 음식을 먹는데 드는 시간, 해당 음식의 index ] 두 가지 정보가 들어가게끔 구성했습니다. 해당 음식의 index는 답을 낼 때 필요한 정보이기 때문입니다.

1. k 값이 충분하면 즉, 음식을 하나 다 먹을 수 있을 만큼 여러번 회전이 가능하면 그에 드는 시간만큼 k 값을 빼주고 heappop을 통해 음식 하나를 제거해줍니다. + 이 과정이 가능할 때 까지 음식을 제거해줍니다.
  - n번 음식을 먹는 시간: (남은 음식의 개수) * (n번 음식을 먹는 시간)

2. 위 과정을 반복하다보면 음식 하나를 다 먹을 수 없을 만큼 k 값이 작아지고 이때부터 heap을 index 기준으로 정렬하여 남은 k 값을 이용해 네트워크 중단 후 먹어야할 음식을 구해줍니다. => 먹어야할 음식의 index = k % len(heap)
'''

### 책 코드

import heapq


def solution(food_times, k):
  # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
  if sum(food_times) <= k:
    return -1

  # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
  q = []
  for i in range(len(food_times)):
    # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
    heapq.heappush(q, (food_times[i], i + 1))

  sum_value = 0  # 먹기 위해 사용한 시간
  previous = 0  # 직전에 다 먹은 음식 시간
  length = len(food_times)  # 남은 음식의 개수

  # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
  while sum_value + ((q[0][0] - previous) * length) <= k:
    now = heapq.heappop(q)[0]
    sum_value += (now - previous) * length
    length -= 1  # 다 먹은 음식 제외
    previous = now  # 이전 음식 시간 재설정

  # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
  result = sorted(q, key=lambda x: x[1])  # 음식의 번호 기준으로 정렬
  return result[(k - sum_value) % length][1]


### GPT 코드
import heapq


def solution(food_times, k):
  if sum(food_times) <= k:
    return -1

  # 우선순위 큐를 사용하여 음식 시간과 인덱스를 튜플로 저장
  pq = []
  for i in range(len(food_times)):
    heapq.heappush(pq, (food_times[i], i + 1))

  total_eaten = 0  # 방송이 중단된 시간까지 섭취한 총 음식 수
  previous_time = 0  # 이전에 섭취한 음식까지의 누적 시간

  while True:
    if not pq:
      break

    # 현재 가장 시간이 적게 걸리는 음식의 정보를 가져옴
    time, index = heapq.heappop(pq)

    # 현재 음식을 먹는 데 걸리는 시간과 이전까지 먹은 음식들의 누적 시간을 계산
    eaten_time = (time - previous_time) * len(pq)

    # 현재 음식을 먹는 데 걸리는 시간이 방송이 중단된 시간보다 작다면
    if total_eaten + eaten_time <= k:
      total_eaten += eaten_time
      previous_time = time
    else:
      # 남은 음식들의 시간을 계산하고 정렬된 순서대로 반환
      result = sorted(pq, key=lambda x: x[1])
      return result[(k - total_eaten) % len(pq)][1]

  return -1
