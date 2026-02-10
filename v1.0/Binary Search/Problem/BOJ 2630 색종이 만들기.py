# https://www.acmicpc.net/problem/2630

def divide(x, y, n):
    global white_cnt, blue_cnt

    # Base Case: 주어진 영역이 단색인지 확인
    color = matrix[y][x]
    is_single_color = True
    for ny in range(y, y + n):
        for nx in range(x, x + n):
            if matrix[ny][nx] != color:
                is_single_color = False
                break
        if not is_single_color:
            break

    # Base Case: 모두 같은 색이라면 해당 색의 카운트를 증가시키고 종료
    if is_single_color:
        if color == 0:
            white_cnt += 1
        else:
            blue_cnt += 1
        return

    # Recursive Case: 색이 섞여 있으면 4개로 분할
    half = n // 2
    divide(x, y, half)
    divide(x, y + half, half)
    divide(x + half, y, half)
    divide(x + half, y + half, half)
    

# 입력 값 받기
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 분할 정복
white_cnt, blue_cnt = 0, 0

divide(0, 0, N)

print(white_cnt)
print(blue_cnt)