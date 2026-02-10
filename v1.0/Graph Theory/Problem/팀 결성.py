'''
난이도: 2
목표 시간: 20분
시간 제한: 2초
메모리 제한: 128MB

성공 여부: 성공
풀이 시간: 15분
'''

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]


def find_team(x):
  # 루트 노드가 아니라면 특정 루트 노드를 찾을 때까지 재귀 호출
  if parent[x] != x:
    parent[x] = find_team(parent[x])
  return parent[x]


def union_team(a, b):
  a = find_team(a)
  b = find_team(b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b


for _ in range(m):
  order_type, a, b = map(int, input().split())
  if order_type == 0:  # 팀 합치기
    union_team(a, b)
  elif order_type == 1:  # 같은 팀 여부 확인
    if find_team(a) == find_team(b):
      print("YES")
    else:
      print("NO")
