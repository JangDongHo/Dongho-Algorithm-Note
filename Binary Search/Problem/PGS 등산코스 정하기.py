# https://school.programmers.co.kr/learn/courses/30/lessons/118669

import sys
sys.setrecursionlimit(int(1e6))

MAX = int(1e7)

def dfs(node, threshold):
    global n, paths, gates, summits, adj_list, visited, types, candidates
    
    # Base Case
    if visited[node]: return
    visited[node] = True
    
    if types[node] == 'summit':
        candidates.append(node)
        return
    
    # Recursive Case
    for nxt_node, time in adj_list[node]:
        if time <= threshold:
            dfs(nxt_node, threshold)

def graph_search(threshold): # intensity <= threshold 인 경우에 가능한 산봉우리를 반환
    global n, paths, gates, summits, adj_list, visited, types, candidates
    
    candidates = []
    visited = [False for _ in range(n + 1)]
    for gate in gates:
        if not visited[gate]:
            dfs(gate, threshold)
    
    return candidates

def solution(_n, _paths, _gates, _summits):
    global n, paths, gates, summits, adj_list, visited, types, candidates
    n, paths, gates, summits = _n, _paths, _gates, _summits
    
    # 지점 타입 관리 (shelter, gate, summit)
    types = ['shelter' for _ in range(n + 1)]
    for gate in gates:
        types[gate] = 'gate'
    for summit in summits:
        types[summit] = 'summit'
    
    # 그래프 만들기
    adj_list = [[] for _ in range(n + 1)]
    for i, j, w in paths:
        adj_list[i].append((j, w))
        adj_list[j].append((i, w))
        
    # Solve (파라매트릭 서치 + 그래프 탐색)
    cur = 0
    step = MAX
    
    while step != 0:
        while (cur + step <= MAX) and len(graph_search(cur + step)) == 0: # [F, F, F, (F), T, T, ..., T, T]
            cur += step
        step //= 2
    
    candidates = graph_search(cur + 1) # [F, F, F, F, (T), T, ..., T, T]
    return min(candidates), cur + 1
        