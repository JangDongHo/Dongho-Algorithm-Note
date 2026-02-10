'''
난이도: 1.5
목표 시간: 50분
시간 제한: 5초
메모리 제한: 128MB

성공 여부: 실패
'''

### 내가 푼 코드 (실패)

# 기둥 상태 체크
def check_pillar_defect(simulator_map, x, y):
    # 다른 기둥 위
    if y > 0 and simulator_map[y-1][x] == 0:
        return True
    # 보의 한쪽 끝 부분
    if x > 0 and simulator_map[y][x-1] == 1:
        return True
    # 바닥 위
    if y == 0:
        return True
    return False

# 보 상태 체크
def check_wall_defect(simulator_map, x, y):
    # 바닥 위가 아닌지
    if y > 0:
        # 보가 설치될 수 있는 범위인지
        if x < (len(simulator_map)):
            # 한쪽 끝 부분이 기둥 위
            if simulator_map[y-1][x] == 0 or simulator_map[y-1][x+1] == 0:
                return True
            # 양쪽 끝 부분이 다른 보와 동시에
            if x > 0 and simulator_map[y][x-1] == 1 and simulator_map[y][x+1] == 1:
                return True
    return False
    

def solution(n, build_frame):
    simulator_map = [[-1] * (n+1) for _ in range(n+1)]
    for command in build_frame:
        [x, y, a, b] = command
        # 삭제
        if b == 0:
            # 구조물이 존재하는지 확인
            if simulator_map[y][x] != -1:
                # 구조물 제거
                simulator_map[y][x] = -1
                # 기둥 하자 체크
                if a == 0 and not check_pillar_defect(simulator_map, x, y+1):
                    simulator_map[y][x] = 0
                # 보 하자 체크
                if a == 1 and not check_wall_defect(simulator_map, x+1, y):
                    simulator_map[y][x] = 1
        # 설치
        if b == 1:
            # 빈 공간인지 확인
            if simulator_map[y][x] == -1:
                # 기둥 설치
                if a == 0 and check_pillar_defect(simulator_map, x, y):
                    simulator_map[y][x] = 0
                # 보 설치
                if a == 1 and check_wall_defect(simulator_map, x, y):
                    simulator_map[y][x] = 1
    # 출력
    result = []
    for i in range(n+1):
        for j in range(n+1):
            if simulator_map[j][i] != -1:
                result.append([i, j, simulator_map[j][i]])
    return result

### 책 코드
'''
접근 방식
- 전체 명령의 개수는 최대 1000개이다.
- 전체 명령의 개수를 M이라고 할 때, 시간 복잡도 O(M^2)으로 해결하는 것이 이상적이다.
- 하지만 본 문제의 시간 제한은 5초로 넉넉한 편이므로 O(M^3)의 알고리즘으로 문제를 해결할 수 있다.

- 따라서, 설치 및 삭제 연산을 수행할 때마다 '현재 구조물들이 정상인지 확인'하는 과정을 거친다.
'''
# 현재 설치된 구조물이 '가능한' 구조물인지 확인하는 함수
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0: # 설치된 것이 '기둥'인 경우
            # '바닥 위' 혹은 '보의 한쪽 끝 부분 위' 혹은 '다른 기둥 위'라면 정상
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False # 아니라면 거짓(False) 반환
        elif stuff == 1: # 설치된 것이 '보'인 경우
            # '한쪽 끝부분이 기둥 위' 혹은 '양쪽 끝부분이 다른 보와 동시에 연결'이라면 정상
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False # 아니라면 거짓(False) 반환
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame: # 작업(frame)의 개수는 최대 1,000개
        x, y, stuff, operate = frame
        if operate == 0: # 삭제하는 경우
            answer.remove([x, y, stuff]) # 일단 삭제를 해본 뒤에
            if not possible(answer): # 가능한 구조물인지 확인
                answer.append([x, y, stuff]) # 가능한 구조물이 아니라면 다시 설치
        if operate == 1: # 설치하는 경우
            answer.append([x, y, stuff]) # 일단 설치를 해본 뒤에
            if not possible(answer): # 가능한 구조물인지 확인
                answer.remove([x, y, stuff]) # 가능한 구조물이 아니라면 다시 제거
    return sorted(answer) # 정렬된 결과를 반환