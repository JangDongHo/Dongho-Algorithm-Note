R, C, N = map(int, input().split())

grid = [list(input()) for _ in range(R)]
booms = [[-1] * C for _ in range(R)]

for r in range(R):
    for c in range(C):
        if grid[r][c] == 'O':
            booms[r][c] = 3

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for t in range(1, N + 1):

    # 1. 시간 감소
    for r in range(R):
        for c in range(C):
            if booms[r][c] != -1:
                booms[r][c] -= 1

    # 2. 짝수 초 → 설치
    if t % 2 == 0:
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '.':
                    grid[r][c] = 'O'
                    booms[r][c] = 3

    # 3. 홀수 초 → 폭발
    else:
        explode = []
        for r in range(R):
            for c in range(C):
                if booms[r][c] == 0:
                    explode.append((r, c))

        for r, c in explode:
            booms[r][c] = -1
            grid[r][c] = '.'

            for d in range(4):
                nr = r + dx[d]
                nc = c + dy[d]

                if 0 <= nr < R and 0 <= nc < C:
                    booms[nr][nc] = -1
                    grid[nr][nc] = '.'

for r in range(R):
    print("".join(grid[r]))