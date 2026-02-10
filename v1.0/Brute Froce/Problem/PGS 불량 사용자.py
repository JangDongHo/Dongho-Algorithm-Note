# https://school.programmers.co.kr/learn/courses/30/lessons/64064#

from itertools import product


def solution(user_id, banned_id):
    banned_candidate = []

    for b_id in banned_id:
        temp = []
        for u_id in user_id:
            if len(u_id) == len(b_id):
                is_possible = True
                for c1, c2 in zip(b_id, u_id):
                    if c1 != c2 and c1 != '*':
                        is_possible = False
                        break
                if is_possible:
                    temp.append(u_id)
        if temp:
            banned_candidate.append(temp)

    result = set()
    for p in product(*banned_candidate):
        set_p = set(p)
        if len(set_p) == len(banned_id):
            result.add(tuple(sorted(set_p)))

    return len(result)
