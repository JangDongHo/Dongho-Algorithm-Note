# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

MAX_NUM = int(1e9)

def dfs(idx, cnt):
    global N, stations, ans

    # Base Case
    if idx >= N - 1:
        ans = min(ans, cnt)
        return

    # 현재 교체 횟수가 이미 최솟값을 넘는 경우 가지치기
    if cnt >= ans:
        return

    # 현재 정류장에서 배터리를 교환하고 갈 수 있는 모든 경우의 수 탐색
    for i in range(1, stations[idx] + 1):
        dfs(idx + i, cnt + 1)

T = int(input())
for tc in range(1, T + 1):
    inputs = list(map(int, input().split()))
    N, stations = inputs[0], inputs[1:]

    ans = MAX_NUM
    dfs(0, -1)  # 1번 정류장에서 시작, 초기 교환 횟수 0

    print(f"#{tc} {ans}")