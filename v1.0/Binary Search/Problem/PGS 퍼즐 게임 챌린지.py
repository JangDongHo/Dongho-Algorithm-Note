# https://school.programmers.co.kr/learn/courses/30/lessons/340212#

MAX = int(1e15)

def is_can_solve(level) -> bool:
    global diffs, times, limit
    n = len(diffs)
    
    cur_time = times[0]
    if cur_time > limit:
            return False
    
    for i in range(1, n):
        if diffs[i] > level:
            cur_time += (diffs[i] - level) * (times[i] + times[i - 1]) + times[i]
        else:
            cur_time += times[i]
            
        if cur_time > limit:
            return False
    return True

def parametric_search():
    cur = 0
    steps = MAX
    
    while (steps != 0):
        while (cur + steps <= MAX) and not is_can_solve(cur + steps):
            cur += steps
        steps //= 2
    return cur

def solution(_diffs, _times, _limit):
    global diffs, times, limit
    diffs = _diffs
    times = _times
    limit = _limit
    
    level = parametric_search()
    return level + 1