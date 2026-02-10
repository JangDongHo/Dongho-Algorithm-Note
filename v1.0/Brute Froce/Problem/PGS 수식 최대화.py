# https://school.programmers.co.kr/learn/courses/30/lessons/67257?language=python3

from re import split
from itertools import permutations

def solution(expression):
    # 브루트 포스로 해결합니다.
    values = []
    
    for priority in permutations(['*', '+', '-'], 3):
        # 연산자와 피연산자를 리스트에 저장합니다.
        operands = list(map(int, split('[*|+|-]', expression)))
        operators = [c for c in expression if c in ['*', '+', '-']]
        
        # 우선순위대로 연산을 수행합니다.
        for op in priority:
            while op in operators:
                i = operators.index(op)
                
                if op == "*":
                    v = operands[i] * operands[i + 1]
                elif op == "+":
                    v = operands[i] + operands[i + 1]
                else:
                    v = operands[i] - operands[i + 1]
                
                # 피연산자 리스트를 업데이트 합니다.
                operands[i] = v
                operands.pop(i + 1)
                
                # 연산자 리스트를 업데이트 합니다.
                operators.pop(i)
        values.append(abs(operands[0]))
    
    return max(values)