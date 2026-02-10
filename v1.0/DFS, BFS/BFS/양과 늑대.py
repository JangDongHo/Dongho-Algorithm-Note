# https://school.programmers.co.kr/learn/courses/30/lessons/92343

from collections import deque

def solution(info, edges):
    N = len(info)
    
    adj_list = [[] for _ in range(N)]
    for a, b in edges:
        adj_list[a].append(b)
        adj_list[b].append(a)
    
    visited = set()
    
    ans = 0
    q = deque()
    q.append(({0}, 1, 0)) # (상태 집합, 양의 개수, 늑대의 개수)
    
    while q:
        cur_set, cur_sheep, cur_wolf = q.popleft()
        ans = max(ans, cur_sheep)
        
        nxt_nodes = set()
        for node in cur_set:
            for adj_node in adj_list[node]:
                if adj_node not in cur_set:
                    nxt_nodes.add(adj_node)
        
        for node in nxt_nodes:
            nxt_set = cur_set | {node}
            if info[node] == 0:
                if tuple(sorted(nxt_set)) not in visited:
                    q.append((nxt_set, cur_sheep + 1, cur_wolf))
                    visited.add(tuple(sorted(nxt_set)))
            elif info[node] == 1 and cur_sheep > cur_wolf + 1:
                if tuple(sorted(nxt_set)) not in visited:
                    q.append((nxt_set, cur_sheep, cur_wolf + 1))
                    visited.add(tuple(sorted(nxt_set)))
    
    return ans