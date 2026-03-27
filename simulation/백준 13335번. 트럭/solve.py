"""백준 13335번. 트럭"""

from collections import deque

n, w, L = map(int, input().split())
trucks = deque(map(int, input().split()))

bridge = deque([0] * w)
bridge_weight = 0
time = 0

while trucks or bridge_weight > 0:
    # 한 칸 이동
    leaving_truck = bridge.popleft()
    bridge_weight -= leaving_truck

    # 다음 트럭 진입 가능하면 올리기
    if trucks and bridge_weight + trucks[0] <= L:
        entering_truck = trucks.popleft()
        bridge.append(entering_truck)
        bridge_weight += entering_truck
    else:
        bridge.append(0)

    time += 1

print(time)
