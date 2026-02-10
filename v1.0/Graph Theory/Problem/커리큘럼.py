'''
난이도: 3
목표 시간: 50분
시간 제한: 2초
메모리 제한: 128MB

성공 여부: 실패
'''
'''
접근 방법
- 위상 정렬 알고리즘의 응용문제
- 각 노드(강의)에 대하여 인접한 노드를 확인할 때, 인접한 노드에 대하여 현재보다 강의 시간이 더 긴 강우를 찾는다면, 더 오랜 시간이 걸리는 경우의 시간 값을 저장하는 방식으로 결과 테이블을 갱신하여 답을 구할 수 있다.
'''

from collections import deque
import copy

n = int(input())
graph = [[] for i in range(n + 1)]
indegree = [0] * (n + 1)
time = [0] * (n + 1)

# 그래프 입력
for i in range(1, n + 1):
  inputs = list(map(int, input().split()))
  time[i] = inputs[0]
  for j in inputs[1:-1]:
    graph[j].append(i)
    indegree[i] += 1

# 위상 정렬
result = copy.deepcopy(time)
q = deque()

# 진입 차수가 0인 노드 큐에 삽입
for i in range(1, n + 1):
  if indegree[i] == 0:
    q.append(i)

while q:
  now = q.popleft()

  for i in graph[now]:
    result[i] = max(result[i], result[now] + time[i])
    indegree[i] -= 1
    if indegree[now] == 0:
      q.append(i)

for i in range(1, n + 1):
  print(result[i])
