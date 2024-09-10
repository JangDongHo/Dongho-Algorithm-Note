# https://www.acmicpc.net/problem/2003

### 풀이1. 시작 지점을 고정하고 모든 끝점의 후보를 살펴보는 풀이
# input
N, M = map(int, input().split())
arr = list(map(int, input().split()))

# solve
ans = 0
for left in range(N):
    cur_sum = 0
    for right in range(left, N):
        cur_sum += arr[right]
        if cur_sum == M:
            ans += 1
            break

print(ans)

### 풀이2. 누적합 알고리즘을 사용하는 풀이
# input
N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# solve
psum = [0] * (N + 1)

for i in range(1, N + 1):
    psum[i] = psum[i - 1] + arr[i]

ans = 0
for left in range(1, N + 1):
    for right in range(left, N + 1):
        cur_sum = psum[right] - psum[left - 1]
        if cur_sum == M:
            ans += 1
            break
            
print(ans)

### 풀이3. 파라매트릭 서치
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

ans = 0
for left in range(1, N + 1):
    ans += is_exist(left)

print(ans)

### 풀이4. 투 포인터 알고리즘
# input
N, M = map(int, input().split())
arr = list(map(int, input().split()))

# solve (two pointer)
ans = 0

right = -1
cur_sum = 0
for left in range(N):
    while (right + 1 < N) and (cur_sum + arr[right + 1] <= M):
        right += 1
        cur_sum += arr[right]

    if cur_sum == M:
        ans += 1

    cur_sum -= arr[left]

print(ans)