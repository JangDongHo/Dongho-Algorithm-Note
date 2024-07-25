from itertools import permutations

def calculate_ball_strike(num1, num2):
    ball = 0
    strike = 0

    for i in range(3):
        if num1[i] == num2[i]:
            strike += 1
        elif num1[i] in num2:
            ball += 1

    return strike, ball

N = int(input())
questions = [input().split() for _ in range(N)]
questions = [(question, int(strike), int(ball)) for question, strike, ball in questions]
result = 0

for candidate in permutations(range(1, 10), 3):
    candidate_str = ''.join(map(str, candidate))
    is_answer = True
    for question, strike, ball in questions:
        if calculate_ball_strike(question, candidate_str) != (strike, ball):
            is_answer = False
            break
    if is_answer:
        result += 1

print(result)