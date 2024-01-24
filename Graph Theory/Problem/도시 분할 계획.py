'''
난이도: 2
목표 시간: 40분
시간 제한: 2초
메모리 제한: 256MB

성공 여부: 실패
'''
'''
접근 방법
- 전체 그래프에서 2개의 최소 신장 트리를 만들어야 한다.
- 가장 간단한 방법은 크루스칼 알고리즘으로 최소 신장 트리를 찾은 뒤에 최소 신장 트리를 구성하는 간선 중에서 가장 비용이 큰 간선을 제거하는 것이다.
- 그러면 최소 신장 트리가 2개의 부분 그래프로 나누어지며, 문제에서 요구하는 최적의 해를 만족한다.
'''


def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]


def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b


n, m = map(int, input().split())
edges = []
parent = [i for i in range(n + 1)]

for _ in range(m):
  a, b, cost = map(int, input().split())
  edges.append((cost, a, b))

edges.sort()

result = 0
last = 0

for edge in edges:
  cost, a, b = edge
  # 사이클이 발생하지 않는 경우에만 집합에 포함
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost
    last = cost

print(result - last)
