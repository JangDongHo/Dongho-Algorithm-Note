'''
난이도: 2
목표 시간: 40분
시간 제한: 5초
메모리 제한: 128MB

성공 여부: 실패
'''
'''
접근 방법
- A에서 B로 도달이 가능하거나, B에서 A로 도달이 가능하면 '성적 비교'가 가능하다.
이 문제에서는 학생의 수 N이 500 이하의 정수이므로 O(N^3)의 시간 복잡도로 동작하는 플로이드 워셜 알고리즘을 이용해 문제를 해결할 수 있다.
- 따라서 플로이드 워셜 알고리즘을 수행한 뒤에, 모든 노드에 대하여 다른 노드와 서로 도달이 가능한지를 체크하여 문제를 해결할 수 있다.
- 이때 자기 자신은 항상 도달이 가능하다고 보고, 카운트를 진행한다.
- 결과적으로 특정한 노드의 카운트 값이 N이라면, 해당 노드의 정확한 순위를 알 수 있다는 것을 의미한다.
'''

INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
  for b in range(1, n + 1):
    if a == b:
      graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
  # A에서 B로 가는 비용을 1로 설정
  a, b = map(int, input().split())
  graph[a][b] = 1

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0
# 각 학생을 번호에 따라 한 명씩 확인하며 도달 가능한지 체크
for i in range(1, n + 1):
  count = 0
  for j in range(1, n + 1):
    if graph[i][j] != INF or graph[j][i] != INF:
      count += 1
  if count == n:
    result += 1
print(graph)
print(result)
