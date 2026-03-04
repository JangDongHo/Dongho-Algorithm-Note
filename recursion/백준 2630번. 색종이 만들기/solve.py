"""백준 2630번. 색종이 만들기"""

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(x: int, y: int, size: int, papers: list[list[int]]) -> list[int]:
    # 색종이가 모두 같은 색인지 확인
    first = papers[x][y]
    same = True

    for i in range(x, x + size):
        for j in range(y, y + size):
            if papers[i][j] != first:
                same = False
                break
        if not same:
            break

    # 모두 같은 색
    if same:
        result = [0, 0]
        result[first] += 1
        return result

    # 다른 색이면 4등분
    half = size // 2
    r1 = solve(x, y, half, papers)
    r2 = solve(x + half, y, half, papers)
    r3 = solve(x, y + half, half, papers)
    r4 = solve(x + half, y + half, half, papers)

    return [
        r1[0] + r2[0] + r3[0] + r4[0],
        r1[1] + r2[1] + r3[1] + r4[1]
    ]


def main() -> None:
    N = int(sys_input())
    papers = [list(map(int, sys_input().split())) for _ in range(N)]

    answer = solve(0, 0, N, papers)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
