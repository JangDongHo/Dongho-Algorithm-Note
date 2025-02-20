import sys
input = lambda: sys.stdin.readline()

def count_binary_sequences(N):
    if N == 1:
        return 1
    if N == 2:
        return 2

    prev1, prev2 = 1, 2

    for _ in range(3, N + 1):
        cur = (prev1 + prev2) % 15746
        prev1, prev2 = prev2, cur

    return prev2


# 입력 값 받기
N = int(input())
print(count_binary_sequences(N))