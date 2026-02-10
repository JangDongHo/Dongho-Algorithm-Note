# https://school.programmers.co.kr/learn/courses/30/lessons/147354

def solution(data, col, row_begin, row_end):
    # 1. 데이터 정렬
    # col-1로 정렬 (0-index), 같은 값일 경우 첫 번째 컬럼(기본키) 기준 내림차순
    data.sort(key=lambda x: (x[col - 1], -x[0]))

    # 2. S_i 계산 및 XOR 누적
    hash_value = 0
    for i in range(row_begin, row_end + 1):
        # i번째 행의 나머지 합 계산
        s_i = sum(value % i for value in data[i - 1])  # i-1로 0-index 보정
        # XOR 누적
        hash_value ^= s_i

    return hash_value