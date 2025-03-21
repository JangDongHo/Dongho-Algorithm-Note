# https://www.acmicpc.net/problem/1024

N, L = map(int, input().split())

for i in range(L, 101):
    x = N / i - (i + 1) / 2
    if int(x) == x: # x는 정수여야 한다.
        x = int(x)
        if x + 1 >= 0: # 첫항(x+1)은 0보다 크거나 같아야한다.
            for j in range(x + 1, x + i + 1):
                print(j, end=" ")
            break
else:
    print(-1)