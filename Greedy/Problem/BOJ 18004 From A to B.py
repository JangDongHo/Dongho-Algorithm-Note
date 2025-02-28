# https://www.acmicpc.net/problem/18004

a, b = map(int, input().split())

cnt = 0
while (a > b):
    if a % 2 == 0:
        a //= 2
    else:
        a += 1
    cnt += 1

print(cnt + (b - a))