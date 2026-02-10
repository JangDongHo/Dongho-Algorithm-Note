# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

import heapq

INF = int(1e9)

# 테스트 케이스 수 입력
T = int(input())
for tc in range(1, T + 1):
    # 지도 크기 입력
    N = int(input())
    matrix = [list(map(int, input().strip())) for _ in range(N)]
    
    # 다익스트라 알고리즘을 위한 최소 비용 배열 초기화
    distance = [[INF] * N for _ in range(N)]
    distance[0][0] = 0  # 시작점의 비용은 0
    
    # 우선순위 큐 설정
    pq = []
    heapq.heappush(pq, (0, 0, 0))  # (복구 시간, x, y)
    
    # 상하좌우 이동
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while pq:
        cost, x, y = heapq.heappop(pq)
        
        # 현재 위치의 최소 비용이 큐에 있는 비용보다 작다면 무시
        if distance[x][y] < cost:
            continue
        
        # 상하좌우 인접 노드 확인
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # 범위 안에 있을 경우에만 이동
            if 0 <= nx < N and 0 <= ny < N:
                new_cost = cost + matrix[nx][ny]
                
                # 더 적은 비용으로 이동할 수 있다면 갱신하고 큐에 추가
                if new_cost < distance[nx][ny]:
                    distance[nx][ny] = new_cost
                    heapq.heappush(pq, (new_cost, nx, ny))
    
    # 최종 결과 출력
    print(f"#{tc} {distance[N-1][N-1]}")
