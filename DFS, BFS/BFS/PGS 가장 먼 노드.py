# https://school.programmers.co.kr/learn/courses/30/lessons/49189

from collections import deque
def bfs(n, adj_list):
    q = deque()
    q.append(1)
    
    visited = [-1] * (n + 1)
    visited[1] = 0
    
    while q:
        cur_node = q.popleft()
        for adj_node in adj_list[cur_node]:
            if visited[adj_node] == -1:
                q.append(adj_node)
                visited[adj_node] = visited[cur_node] + 1
    
    return visited

def solution(n, edge):
    adj_list = [[] for _ in range(n + 1)]
    for a, b in edge:
        adj_list[a].append(b)
        adj_list[b].append(a)
    
    distances = bfs(n, adj_list)
    max_dist = max(distances)
    
    cnt = 0
    for dist in distances:
        if dist == max_dist:
            cnt += 1
    
    return cnt
    
        