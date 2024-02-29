'''
난이도: 3
목표 시간: 60분
시간 제한: 1초
메모리 제한: 128MB

성공 여부: 실패
'''

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
  x, y, z = map(int, input().split())
  graph[x].append((y, z))


def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, node = heapq.heappop(q)
    if distance[node] < dist:
      continue
    for i in graph[node]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))


dijkstra(c)

time = 0
count = 0
for i in distance:
  if 0 < i < INF:
    count += 1
    if i > time:
      time = i

print(count, time)
