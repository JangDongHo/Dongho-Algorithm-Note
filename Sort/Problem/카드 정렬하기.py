'''
난이도: 2
목표 시간: 30분
시간 제한: 2초
메모리 제한: 128MB

성공 여부: 실패
'''
'''
접근 방식
- 이 문제의 핵심 아이디어는 항상 가장 작은 크기의 두 카드 묶음을 합쳤을 때 최적의 해를 보장한다는 점이다.
- 이러한 과정을 매우 효과적으로 수행할 수 있는 자료구조는 우선순위 큐
- 힙에 원소가 1개가 남을 때 까지 우선순위큐에서 두 개의 숫자를 pop 한 다음 더한 뒤에 삽입하는 것을 반복하면 된다.
'''

import heapq

n = int(input())

# 힙(Heap)에 초기 카드 묶음을 모두 삽입
heap = []
for i in range(n):
  data = int(input())
  heapq.heappush(heap, data)

result = 0

# 힙(Heap)에 원소가 1개 남을 때까지
while len(heap) != 1:
  # 가장 작은 2개의 카드 묶음 꺼내기
  one = heapq.heappop(heap)
  two = heapq.heappop(heap)
  # 카드 묶음을 합쳐서 다시 삽입
  sum_value = one + two
  result += sum_value
  heapq.heappush(heap, sum_value)

print(result)
