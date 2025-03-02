# https://www.acmicpc.net/problem/32627

from collections import Counter

N, M = map(int, input().split())
S = input()

count = Counter(S)
delete = {c: 0 for c in count}

# 삭제해야 할 문자 개수 계산
for c in sorted(count):
    if count[c] > M:
        delete[c] = M
        break
    else:
        delete[c] = count[c]
        M -= count[c]

# 출력
for s in S:
    if delete[s] > 0:
        delete[s] -= 1
    else:
        print(s, end="")