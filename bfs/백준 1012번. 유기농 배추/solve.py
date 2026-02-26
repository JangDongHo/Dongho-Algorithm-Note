import sys
from collections import deque


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def bfs(start_x: int, start_y: int, ground: list[list[int]],
        visited: list[list[bool]], m: int, n: int) -> None:
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque([(start_x, start_y)])
    visited[start_y][start_x] = True

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < m and 0 <= ny < n:
                if not visited[ny][nx] and ground[ny][nx] == 1:
                    visited[ny][nx] = True
                    q.append((nx, ny))


def solve(m: int, n: int, cabbages: list[tuple[int, int]]) -> int:
    # 배추 심기
    ground = [[0] * m for _ in range(n)]

    for x, y in cabbages:
        ground[y][x] = 1

    # 그래프 탐색
    visited = [[False] * m for _ in range(n)]
    count = 0

    for y in range(n):
        for x in range(m):
            if ground[y][x] == 1 and not visited[y][x]:
                bfs(x, y, ground, visited, m, n)
                count += 1

    return count


def main() -> None:
    T = int(sys_input())

    for _ in range(T):
        M, N, K = map(int, sys_input().split())
        cabbages = [tuple(map(int, sys_input().split())) for _ in range(K)]

        answer = solve(M, N, cabbages)
        print(answer)


if __name__ == "__main__":
    main()
