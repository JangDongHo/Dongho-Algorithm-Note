'''
난이도: 1.5
목표 시간: 40분
시간 제한: 1초
메모리 제한: 128MB

성공 여부: 실패
'''
'''
접근 방법
- 크기가 20*20인 2차원 리스트에 있는 모든 원소에 접근할 때는 400번의 연산이 필요하다.
  - 따라서, 완전 탐색을 이용하여 문제를 해결할 수 있다.
1. 완전 탐색을 수월하게 하기 위해서 자물쇠의 크기를 기존의 3배로 변환한다.
2. 자물쇠의 크기가 3배인 새로운 리스트를 만들어 중앙 부분에 기존의 자물쇠를 넣는다.
3. 열쇠 배열을 왼쪽 위부터 시작해서 한 칸씩 이동하면서, 자물쇠에 열쇠를 끼워 넣는다.
  - 자물쇠에 열쇠를 끼워 넣을 때는 2차원 리스트의 값을 더하거나 빼는 것으로 처리한다.
  - 이때, 자물쇠의 중앙 부분이 모두 1인지 확인한다.
  - 만약 모두 1이라면 True를 반환한다.
4. 키를 90도 회전시킨 후, 3번부터 4번까지의 과정을 반복한다.
5. 만약 4방향 모두 실패했다면 False를 반환한다.
'''

### 책 코드

# 2차원 리스트 90도 회전하기
def rotate_a_matrix_by_90_degree(a):
    n = len(a) # 행 길이 계산
    m = len(a[0]) # 열 길이 계산
    result = [[0] * n for _ in range(m)] # 결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result

# 자물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 자물쇠의 크기를 기존의 3배로 변환
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    # 4가지 방향에 대해서 확인
    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key) # 열쇠 회전
        for x in range(n * 2):
            for y in range(n * 2):
                # 자물쇠에 열쇠를 끼워 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                # 새로운 자물쇠에 열쇠가 정확히 들어 맞는지 검사
                if check(new_lock) == True:
                    return True
                # 자물쇠에서 열쇠를 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False