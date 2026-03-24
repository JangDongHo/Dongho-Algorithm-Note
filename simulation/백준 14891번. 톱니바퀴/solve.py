"""백준 14891번. 톱니바퀴"""

from collections import deque

RIGHT_SIDE_INDEX = 2
LEFT_SIDE_INDEX = 6

wheels = [None]
for _ in range(4):
    wheel = deque(list(map(int, input())))
    wheels.append(wheel)

K = int(input())

# 톱니바퀴 회전
for _ in range(K):
    wheel_num, rotate_dir = map(int, input().split())

    dirs = [0] * 5
    dirs[wheel_num] = rotate_dir

    # 왼쪽 전파
    for i in range(wheel_num, 1, -1):
        if wheels[i][LEFT_SIDE_INDEX] != wheels[i - 1][RIGHT_SIDE_INDEX]:
            dirs[i - 1] = -dirs[i]
        else:
            break

    # 오른쪽 전파
    for i in range(wheel_num, 4):
        if wheels[i][RIGHT_SIDE_INDEX] != wheels[i + 1][LEFT_SIDE_INDEX]:
            dirs[i + 1] = -dirs[i]
        else:
            break

    # 한꺼번에 회전
    for i in range(1, 5):
        if dirs != 0:
            wheels[i].rotate(dirs[i])

# 톱니바퀴 점수의 합 계산
score = 0
for i in range(1, 5):
    score += wheels[i][0] * (2 ** (i - 1))

print(score)
