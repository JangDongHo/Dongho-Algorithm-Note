def is_exist(left): # binary search
    global N, M, psum

    cur = left - 1
    step = N

    while step != 0:
        while (cur + step <= N) and (psum[cur + step] - psum[left - 1] <= M):
            cur += step
        step //= 2

    return (psum[cur] - psum[left - 1] == M)


# input
N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# solve
psum = [0] * (N + 1)

for i in range(1, N + 1):
    psum[i] = psum[i - 1] + arr[i]

print(psum)

ans = 0
for left in range(1, N + 1):
    ans += is_exist(left)

print(ans)