"""백준 1780번. 종이의 개수"""

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(x: int, y: int, size: int, papers: list[list[int]]) -> list[int]:
    first = papers[x][y]
    same = True

    # 현재 영역이 같은 값인지 검사
    for i in range(x, x + size):
        for j in range(y, y + size):
            if papers[i][j] != first:
                same = False
                break
        if not same:
            break

    # 모두 같으면 해당 값 1개 리턴
    if same:
        result = [0, 0, 0]
        result[first + 1] = 1
        return result

    # 아니면 9등분 후 결과 합치기
    step = size // 3
    result = [0, 0, 0]

    for dx in (0, step, 2 * step):
        for dy in (0, step, 2 * step):
            sub = solve(x + dx, y + dy, step, papers)
            for k in range(3):
                result[k] += sub[k]

    return result


def main() -> None:
    N = int(sys_input())
    papers = [list(map(int, sys_input().split())) for _ in range(N)]

    answer = solve(0, 0, N, papers)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
