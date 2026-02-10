# BFS(Breadth-First Search)

- 가까운 노드부터 탐색하는 알고리즘
- DFS는 최대한 멀리 있는 노드를 우선으로 탐색하는 방식으로 동작한다고 했는데, BFS는 그 반대이다.
- BFS는 큐 자료구조를 이용하며, 동작 방식은 다음과 같다.
  > 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
  > 2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리한다.
  > 3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.
- 일반적인 경우 실제 수행 시간은 DFS보다 좋은 편이다.

## BFS 소스코드 예제

![DFS](https://images.velog.io/images/jusung-c/post/46148e69-2e6c-46e1-8450-e5bbef15ad37/image.png "DFS")

- deque 라이브러리를 사용하고, 마찬가지로 O(N)의 시간 복잡도를 가진다.

```python
from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
  # 큐(Queue) 구현을 위해 deque 라이브러리 사용
  queue = deque([start])
  # 현재 노드를 방문 처리
  visited[start] = True
  # 큐가 빌 때까지 반복
  while queue:
    # 큐에서 하나의 원소를 뽑아 출력하기
    v = queue.popleft()
    print(v, end=' ')
    # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

# 각 노드가 연결된 정보를 표현 (2차원 리스트)
graph = [
  [], # 노드 0은 없으므로 비워둠
  [2, 3, 8], # 노드 1과 연결된 노드들
  [1, 7], # 노드 2과 연결된 노드들
  [1, 4, 5], # 노드 3과 연결된 노드들
  [3, 5], # 노드 4과 연결된 노드들
  [3, 4], # 노드 5과 연결된 노드들
  [7], # 노드 6과 연결된 노드들
  [2, 6, 8], # 노드 7과 연결된 노드들
  [1, 7] # 노드 8과 연결된 노드들
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)
```
