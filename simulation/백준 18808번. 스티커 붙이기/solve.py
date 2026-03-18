"""백준 18808번. 스티커 붙이기"""

import sys

input = sys.stdin.readline


def rotate_sticker(sticker, R, C):
    new_sticker = [[0] * R for _ in range(C)]

    for r in range(R):
        for c in range(C):
            new_sticker[c][R - 1 - r] = sticker[r][c]

    return new_sticker, C, R


def can_attach(x, y, sticker, R, C):
    for r in range(R):
        for c in range(C):
            if sticker[r][c] == 1 and laptop[x + r][y + c] == 1:
                return False
    return True


def attach_sticker(x, y, sticker, R, C):
    for r in range(R):
        for c in range(C):
            if sticker[r][c] == 1:
                laptop[x + r][y + c] = 1


def find_space(sticker, R, C):
    for _ in range(4):
        for i in range(N - R + 1):
            for j in range(M - C + 1):
                if can_attach(i, j, sticker, R, C):
                    attach_sticker(i, j, sticker, R, C)
                    return

        sticker, R, C = rotate_sticker(sticker, R, C)


N, M, K = map(int, input().split())
laptop = [[0] * M for _ in range(N)]

for _ in range(K):
    R, C = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(R)]
    find_space(sticker, R, C)

answer = sum(sum(row) for row in laptop)
print(answer)