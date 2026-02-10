# https://school.programmers.co.kr/learn/courses/30/lessons/258711

## 풀이 1. 각 노드의 출발과 도착 간선 수를 계산하여, 그래프 종류 파악 - O(|edges|)
MAX = int(1e6)

def solution(edges):
    in_degree = [0] * (MAX + 1) # in_degree[x]: 노드 x로 들어오는 간선의 개수
    out_degree = [0] * (MAX + 1) # out_degree[x]: 노드 x에서 나가는 간선의 개수
    
    for a, b in edges:
        out_degree[a] += 1
        in_degree[b] += 1
    
    total = 0 # 전체 그래프 개수
    ans = [-1, 0, 0, 0] # (추가된 노드, 도넛 개수, 막대 개수, 8자 개수)
    for i in range(1, MAX + 1):
        if in_degree[i] == 0 and out_degree[i] == 0:
            continue
        
        # 8자 모양 그래프
        if in_degree[i] >= 2 and out_degree[i] == 2:
            ans[3] += 1
        
        # 막대 모양 그래프
        elif out_degree[i] == 0:
            ans[2] += 1
        
        # 추가된 노드
        elif in_degree[i] == 0 and out_degree[i] >= 2:
            ans[0] = i
            total = out_degree[i]
        
    # 도넛 모양 그래프
    ans[1] = total - (ans[2] + ans[3])
    
    return ans

### 풀이 2. 부분 그래프의 노드와 간선의 개수를 계산하여, 그래프 종류 파악 - $O(|nodes| + |edges|)$
import sys
sys.setrecursionlimit(int(1e6))

# 그래프 탐색
def dfs(node):
    global adj_list, visited, n_cnt, e_cnt
    
    # Base Case
    if visited[node]:
        return (n_cnt, e_cnt)
    
    visited[node] = True
    n_cnt += 1 # 노드의 개수 더해주기
    
    # Recursive Case
    for adj_node in adj_list[node]:
        e_cnt += 1 # 간선의 개수 더해주기
        dfs(adj_node)
    
def get_node_edge_cnt(start_node):
    global adj_list, visited, n_cnt, e_cnt
    
    n_cnt = 0
    e_cnt = 0
    dfs(start_node)
    
    return (n_cnt, e_cnt)
    
def solution(edges):
    global adj_list, visited, n_cnt, e_cnt
    
    # 유효한 노드만 남기기
    nodes = set()
    for a, b in edges:
        nodes.add(a)
        nodes.add(b)
    MAX = max(nodes)
    
    # 그래프 만들기
    adj_list = [[] for _ in range(MAX + 1)]
    in_degree = [0] * (MAX + 1)
    out_degree = [0] * (MAX + 1)
    
    for a, b in edges:
        adj_list[a].append(b)
        out_degree[a] += 1
        in_degree[b] += 1
    
    ans = [-1, 0, 0, 0] # (추가된 노드, 도넛 개수, 막대 개수, 8자 개수)    
    
    # 추가된 노드 탐색 - O(|nodes|)
    for node in nodes:
        if in_degree[node] == 0 and out_degree[node] >= 2:
            ans[0] = node
            break
    
    # 추가된 노드와 부분 그래프 연결 끊기
    for node in adj_list[ans[0]]:
        in_degree[node] -= 1
        
    # 그래프 탐색 - O(|nodes| + |edges|)
    visited = [False] * (MAX + 1)
    
    start_nodes = [] # 막대 그래프의 시작점들을 찾기 위해 in_degree가 0인 노드들만 담는다.
    for node in nodes:
        if node != ans[0] and in_degree[node] == 0:
            start_nodes.append(node)
    
    # 막대 그래프 탐색
    for node in start_nodes:
        n, e = get_node_edge_cnt(node)
        ans[2] += (e == (n - 1)) # 막대 모양
    
    # 도넛 모양, 8자 모양 그래프 탐색
    for node in nodes:
        if visited[node] or node == ans[0]:
            continue
        n, e = get_node_edge_cnt(node)
        ans[1] += (e == n) # 도넛 모양
        ans[3] += (e == (n + 1)) # 8자 모양
    
    return ans