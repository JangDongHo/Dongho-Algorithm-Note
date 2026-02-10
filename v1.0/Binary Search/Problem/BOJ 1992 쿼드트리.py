# https://www.acmicpc.net/problem/1992

def quad_tree(x, y, n):
    for ny in range(y, y + n):
        for nx in range(x, x + n):
            if matrix[y][x] != matrix[ny][nx]:
                half_n = n // 2
                result = "("
                result += quad_tree(x, y, half_n)
                result += quad_tree(x + half_n, y, half_n)
                result += quad_tree(x, y + half_n, half_n)
                result += quad_tree(x + half_n, y + half_n, half_n)
                result += ")"
                return result
    return matrix[y][x]

# 입력 값 받기
N = int(input())
matrix = [input() for _ in range(N)]

print(quad_tree(0, 0, N))