# DFS(Depth-First Search)

- 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘

## 그래프(Graph)

- 노드(Node)와 간선(Edge)으로 표현
  - 노드를 정점(Vertex)이라고도 부름
- 그래프 탐색이란 하나의 노드를 시작으로 다수의 노드를 방문하는 것을 말함
- 두 노드가 간선으로 연결되어 있다면 '두 노드는 인접하다'라고 표현
- 프로그래밍에서 그래프를 표현하는 방식

### 1. **인접 행렬(Adjacency Matrix)**

![인접 행렬](https://gilbertlim.github.io/assets/images/posts/algorithm/this_is_coding_test/graph.png "인접 행렬")
![인접 행렬2](https://gilbertlim.github.io/assets/images/posts/algorithm/this_is_coding_test/Adjacency-matrix.png "인접 행렬2")

- 2차원 배열로 그래프의 연결 관계를 표현하는 방식
- 연결되어 있지 않은 노드끼리는 무한의 비용이라고 작성

```
INF = 999999999 # 무한의 비용 선언

graph = [
  [0, 7, 5],
  [7, 0, INF],
  [5, INF, 0]
]

print(graph)
```

### 2. **인접 리스트(Adjacency List)**

![인접 리스트](https://gilbertlim.github.io/assets/images/posts/algorithm/this_is_coding_test/Adjacency-list.png "인접 리스트")

- 리스트로 그래프의 연결 관계를 표현하는 방식
- 연결 리스트(Linked List)를 이용해서 구현할 수 있다.
- 파이썬으로 인접 리스트를 이용해 그래프를 표현하고자 할 때에 단순히 2차원 리스트를 이용하면 된다는 점을 기억하자.

  ```
  graph = [[] for _ in range(3)]

  # 노드 0에 연결된 노드 정보 저장 (노드, 거리)
  graph[0].append((1, 7))
  graph[0].append((2, 5))

  # 노드 1에 연결된 노드 정보 저장 (노드, 거리)
  graph[1].append((0, 7))

  # 노드 2에 연결된 노드 정보 저장 (노드, 거리)
  graph[2].append((0, 5))

  print(graph)
  # 출력 결과: [[(1, 7), (2, 5)], [(0, 7)], [(0, 5)]]
  ```

- 두 방식의 차이?
  - 인접 행렬 방식은 모든 관계를 저장하므로 노드 개수가 많을수록 메모리가 불필요하게 낭비된다.
  - 인접 리스트 방식은 연결된 정보만을 저장하기 때문에 메모리를 효율적으로 사용한다.
  - 하지만 인접 리스트 방식은 인접 행렬 방식에 비해 특정한 두 노드가 연결되어 있는지에 대한 정보를 얻는 속도가 느리다.
    - 예시: 노드 1과 노드 7이 연결되어 있는지 확인하는 경우
      - 인접 행렬 방식: graph[1][7]만 확인하면 된다.
      - 인접 리스트 방식: 노드 1에 대한 인접 리스트를 앞에서부터 차례대로 확인해야 한다.
