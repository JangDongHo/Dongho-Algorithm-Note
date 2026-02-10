# https://www.acmicpc.net/problem/32347

from collections import deque

def is_possible(T):
    q = deque()
    q.append((N, 0)) # (현재 날짜, 타임머신 사용 횟수)

    visited = [False] * (N + 1)
    visited[N] = True

    while q:
        cur_day, k = q.popleft()

        # 1일에 도달했을 경우 성공 처리
        if cur_day == 1:
            return True

        # 타임 머신을 사용할 수 있을 경우 사용하고, 아니라면 +1일
        if days[cur_day] == 1 and k < K:
            next_day = cur_day - T if cur_day - T > 0 else 1
            k += 1
        else:
            next_day = cur_day + 1

        if not visited[next_day]:
            q.append((next_day, k))
            visited[next_day] = True

    return False

def binary_search():
    left, right = 1, N # 최소 1일 ~ 최대 N일까지 탐색
    answer = N # 최댓값으로 초기화

    while left <= right:
        mid = (left + right) // 2
        if is_possible(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer


N, K = map(int, input().split())
days = [0] + list(map(int, input().split())) # 1-index
T = binary_search()
print(T)
