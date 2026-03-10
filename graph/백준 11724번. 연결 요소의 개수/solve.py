"""백준 11724번. 연결 요소의 개수"""

import sys
from collections import deque


def sys_input() -> str:
    return sys.stdin.readline().rstrip()

def bfs(start_node: int, adj_list: list[list[int]], visited: list[bool]) -> None:
    q = deque()
    q.append(start_node)
    visited[start_node] = True

    while q:
        cur_node = q.popleft()
        for nxt_node in adj_list[cur_node]:
            if not visited[nxt_node]:
                q.append(nxt_node)
                visited[nxt_node] = True


def solve(n: int, m: int) -> int:
    answer = 0

    # 그래프 그리기
    adj_list = [[] for _ in range(n + 1)]
    for _ in range(m):
        s, e = map(int, sys_input().split())
        adj_list[s].append(e)
        adj_list[e].append(s)

    visited = [False] * (n + 1)

    for i in range(1, n + 1):
        if not visited[i]:
            bfs(i, adj_list, visited)
            answer += 1

    return answer


def main():
    N, M = map(int, sys_input().split())
    answer = solve(N, M)
    print(answer)


if __name__ == "__main__":
    main()