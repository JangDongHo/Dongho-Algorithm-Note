# https://www.acmicpc.net/problem/1987

### 풀이1. set를 사용한 백트레킹

# 이동 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# Input
R, C = map(int, input().split()) # 세로, 가로
board = [list(input()) for _ in range(R)]

# Solve
answer = 1

st = set()
st.add((0, 0, board[0][0]))

while st:
    x, y, used = st.pop()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < C and 0 <= ny < R and board[ny][nx] not in used:
            st.add((nx, ny, used + board[ny][nx]))
            answer = max(answer, len(used)+1)

print(answer)

### 풀이2. list를 사용한 백트레킹
def search(y, x):
    global dy, dx, R, C, board, check, cur_len, ans

    # base case
    if y < 0 or x < 0 or y >= R or x >= C:
        return
    if check[ord(board[y][x]) - ord('A')]:
        return
    check[ord(board[y][x]) - ord('A')] = True
    cur_len += 1

    ans = max(ans, cur_len)

    # recursive case
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        search(ny, nx)

    cur_len -= 1
    check[ord(board[y][x]) - ord('A')] = False


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

R, C = map(int, input().split())
board = [input() for _ in range(R)]

check = [False] * 26
cur_len = 0
ans = 0

search(0, 0)

print(ans)