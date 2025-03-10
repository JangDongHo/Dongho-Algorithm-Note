# https://school.programmers.co.kr/learn/courses/30/lessons/49191

from collections import defaultdict


def solution(n, results):
    win, lose = defaultdict(set), defaultdict(set)

    for p1, p2 in results:
        win[p1].add(p2)
        lose[p2].add(p1)

    for p in range(1, n + 1):
        for winner in lose[p]:  # p가 이긴 모든 상대를 winner도 이길 수 있음
            win[winner].update(win[p])
        for loser in win[p]:  # loser는 p에게 졌으므로, p에게 이긴 선수들에게도 질 것
            lose[loser].update(lose[p])

    answer = 0
    for p in range(1, n + 1):
        if len(win[p]) + len(lose[p]) == n - 1:
            answer += 1

    return answer
