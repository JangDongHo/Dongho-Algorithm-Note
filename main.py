N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 누적합 배열 초기화
psum = [[0] * (N + 1) for _ in range(N + 1)]

# 2차원 누적합 계산
for i in range(1, N + 1):
    for j in range(1, N + 1):
        psum[i][j] = psum[i - 1][j] + psum[i][j - 1] - psum[i - 1][j - 1] + grid[i - 1][j - 1]

# 최대 따뜻한 직원 수 구하기
max_count = 0
for i in range(K, N + 1):
    for j in range(K, N + 1):
        total = psum[i][j] - (psum[i - K][j] + psum[i][j - K] - psum[i - K][j - K])
        max_count = max(max_count, total)

print(max_count)
