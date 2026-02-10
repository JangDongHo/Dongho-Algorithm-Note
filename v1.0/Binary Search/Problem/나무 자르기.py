# https://www.acmicpc.net/problem/2805

# 풀이. 파라매트릭 서치
def is_possible(h):
    global trees, M

    store = 0
    for tree in trees:
        if h < tree:
            store += tree - h

    return (store >= M)


def parametric_search():
    cur = -1
    step = int(1e9) + 1

    while step != 0:
        while (cur + step <= int(1e9)) and is_possible(cur + step):
            cur += step
        step //= 2

    return cur


N, M = map(int, input().split())
trees = list(map(int, input().split()))
h = parametric_search()
print(h)