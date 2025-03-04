# https://school.programmers.co.kr/learn/courses/30/lessons/72413

import heapq
INF = int(1e9)

def dijkstra(start):
    global n, adj_list
    
    hq = []
    heapq.heappush(hq, (0, start)) # (요금, 노드)
    
    dists = [INF] * (n + 1)
    dists[start] = 0
    
    while hq:
        cur_cost, cur_node = heapq.heappop(hq)
        for adj_node, adj_cost in adj_list[cur_node]:
            tmp_dist = dists[cur_node] + adj_cost
            if tmp_dist < dists[adj_node]:
                dists[adj_node] = tmp_dist
                heapq.heappush(hq, (adj_cost, adj_node))
    
    return dists

def solution(_n, s, a, b, fares):
    global n, adj_list
    n = _n
    
    adj_list = [[] for _ in range(n + 1)] # (노드, 요금)
    for c, d, f in fares:
        adj_list[c].append((d, f))
        adj_list[d].append((c, f))
    
    dist_from_s = dijkstra(s)
    dist_from_a = dijkstra(a)
    dist_from_b = dijkstra(b)
    
    ans = INF
    for i in range(1, n + 1):
        ans = min(ans, dist_from_s[i] + dist_from_a[i] + dist_from_b[i])
    
    return ans