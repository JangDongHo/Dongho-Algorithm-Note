"""백준 9663번. N-Queen (시간 초과)"""

import sys

def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def can_place(r: int, c: int, boards: list[list[int]], n: int) -> bool:
    # 같은 column 검사
    for i in range(r):
        if boards[i][c] == 1:
            return False

    # 좌상 대각선 검사
    i, j = r - 1, c - 1
    while i >= 0 and j >= 0:
        if boards[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # 우상 대각선 검사
    i, j = r - 1, c + 1
    while i >= 0 and j < n:
        if boards[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve(row: int, boards: list[list[int]], n: int) -> int:
    if row == n:
        return 1

    answer = 0

    for col in range(n):
        if can_place(row, col, boards, n):
            boards[row][col] = 1
            answer += solve(row + 1, boards, n)
            boards[row][col] = 0

    return answer


def main() -> None:
    N = int(sys_input())
    boards = [[0] * N for _ in range(N)]

    answer = solve(0, boards, N)
    print(answer)


if __name__ == "__main__":
    main()