# https://school.programmers.co.kr/learn/courses/15008/lessons/121686

import heapq

def solution(program):
    answer = [0 for _ in range(10)]
    program.sort(key=lambda x: x[1])
    memory = []
    cur_time = 0 

    # 프로그램이 아직 남아 있거나 메모리에 실행 대기 중인 프로그램이 있으면 계속 반복
    while program or memory:
        # 현재 실행할 프로그램이 없을 때 시간을 건너뜀
        if not memory:
            cur_time = program[0][1]
        else:  
            # 메모리에서 우선순위가 가장 높은 프로그램을 꺼냄
            process = heapq.heappop(memory)
            # 프로그램이 대기했던 시간 = 현재 시간 - 호출된 시간
            answer[process[0] - 1] += cur_time - process[1] 
            # 실행 시간만큼 현재 시간을 업데이트
            cur_time += process[2]

        # 호출해야 할 프로그램을 메모리에 적재
        while program and program[0][1] <= cur_time:
            heapq.heappush(memory, program.pop(0))

    return [cur_time, *answer]