"""백준 1992번. 쿼드트리"""

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(x: int, y: int, size: int, matrix: list[list[str]]) -> str:
    first = matrix[x][y]
    same = True

    for i in range(x, x + size):
        for j in range(y, y + size):
            if matrix[i][j] != first:
                same = False
                break
        if not same:
            break

    if same:
        return first

    half = size // 2

    return (
        "("
        + solve(x, y, half, matrix)               # 좌상
        + solve(x, y + half, half, matrix)        # 우상
        + solve(x + half, y, half, matrix)        # 좌하
        + solve(x + half, y + half, half, matrix)  # 우하
        + ")"
    )


def main() -> None:
    N = int(sys_input())
    matrix = [list(sys_input()) for _ in range(N)]

    answer = solve(0, 0, N, matrix)
    print(answer)


if __name__ == "__main__":
    main()
