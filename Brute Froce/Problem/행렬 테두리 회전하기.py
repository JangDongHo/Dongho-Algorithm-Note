# https://school.programmers.co.kr/learn/courses/30/lessons/77485

def rotate_side_number(y1, x1, y2, x2):
    global matrix
    
    # 테두리 영역 좌표 값 수집
    pos = []
    for x in range(x1, x2 + 1):
        pos.append((y1, x))
    for y in range(y1 + 1, y2 + 1):
        pos.append((y, x2))
    for x in range(x2 - 1, x1 - 1, -1):
        pos.append((y2, x))
    for y in range(y2 - 1, y1, -1):
        pos.append((y, x1))
    N = len(pos)
    
    # 회전
    for i in range(N - 1, 0, -1):
        ny, nx = pos[i][0], pos[i][1]
        y, x = pos[i - 1][0], pos[i - 1][1]
        matrix[ny][nx], matrix[y][x] = matrix[y][x], matrix[ny][nx]
        
    return min(matrix[y][x] for y, x in pos)

def solution(rows, columns, queries):
    global matrix
    
    # Init
    matrix = [[0 for _ in range(columns + 1)] for _ in range(rows + 1)] # 1-Index
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            matrix[i][j] = (i-1) * columns + j
    
    # Solve
    answer = []
    for query in queries:
        y1, x1, y2, x2 = query
        min_num = rotate_side_number(y1, x1, y2, x2)
        answer.append(min_num)
    
    return answer