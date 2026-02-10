# https://school.programmers.co.kr/learn/courses/15009/lessons/121690

from collections import deque

def bfs(n, m, map_list, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q = deque()
    q.append((0, 0, False))  # (X, Y, 신발 사용 여부)
    visited[0][0][0] = True
    ret = 0  # 이동 거리
    
    while q:
        for _ in range(len(q)):  # 현재 큐의 모든 노드 처리
            x, y, used = q.popleft()
            if (x, y) == (n - 1, m - 1):  # 도착 지점 도달
                return ret
            
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                
                # 1. 일반 이동
                if 0 <= nx < n and 0 <= ny < m and not visited[ny][nx][used] and map_list[ny][nx] == 0:
                    q.append((nx, ny, used))
                    visited[ny][nx][used] = True
                
                # 2. 신발 사용 이동 (used=False인 경우만)
                if not used:
                    nx2, ny2 = nx + dx[d], ny + dy[d]
                    if 0 <= nx2 < n and 0 <= ny2 < m and not visited[ny2][nx2][1] and map_list[ny2][nx2] == 0:
                        q.append((nx2, ny2, True))
                        visited[ny2][nx2][1] = True
        
        ret += 1  # BFS 레벨 증가 (모든 현재 노드 처리 후)
    
    return -1  # 목표 지점 도달 불가능


def solution(n, m, holes):
    # 지도 및 방문 배열 초기화
    map_list = [[0] * n for _ in range(m)]
    visited = [[[False] * 2 for _ in range(n)] for _ in range(m)]  # [y][x][신발 사용 여부]
    
    for (x, y) in holes:
        map_list[y - 1][x - 1] = 1  # 구멍 표시
    
    return bfs(n, m, map_list, visited)
