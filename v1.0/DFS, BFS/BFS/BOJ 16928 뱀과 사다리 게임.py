# https://www.acmicpc.net/problem/16928

import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append((1, 0)) # (현재 위치, 주사위 굴린 횟수)

    visited = [False] * 101
    visited[1] = True

    while q:
        cur_pos, cnt = q.popleft()

        if cur_pos == 100: # 100번 칸 도착하면 종료
            return cnt

        for dice in range(1, 7): # 주사위 1~6까지 가능
            next_pos = cur_pos + dice
            if next_pos > 100: # 100번 칸을 넘으면 이동 불가
                continue

            if next_pos in ladders: # 사다리 존재하면 이동
                next_pos = ladders[next_pos]
            elif next_pos in snakes: # 뱀 존재하면 이동
                next_pos = snakes[next_pos]

            if not visited[next_pos]: # 방문하지 않은 경우에만 큐에 추가
                q.append((next_pos, cnt + 1))
                visited[next_pos] = True


# 입력 값 받기
N, M = map(int, input().split())
ladders = {}
snakes = {}

for _ in range(N):
    x, y = map(int, input().split())
    ladders[x] = y
for _ in range(M):
    u, v = map(int, input().split())
    snakes[u] = v

# BFS
print(bfs())