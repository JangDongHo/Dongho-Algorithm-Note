### 풀이1. 모든 순열에 대해 살펴본 후에, 중복된 결과를 수학적으로 처리해주는 방법 (브루트 포스)

from itertools import permutations

def fact(x):
    if x == 0:
        return 1
    return fact(x - 1) * x

S = input()
ans = 0

for perm in permutations(S):
    ok = True
    for i in range(0, len(S) - 1):
        if perm[i] == perm[i + 1]:
            ok = False
            break
    ans += ok

for i in range(ord('a'), ord('z') + 1):
    ans //= fact(S.count(chr(i)))

print(ans)

### 풀이2. 문자의 종류를 기준으로 각 자리를 완성하는 방법 (백 트레킹)
def func(lev):
    global S, chars, cnt, choose, ans

    # base case
    if lev == len(S):
        ans += 1
        return

    # recursive case
    for c in chars:
        if cnt[c] == 0:
            continue

        if (not choose) or (choose[-1] != c):
            cnt[c] -= 1
            choose.append(c)
            func(lev + 1)
            cnt[c] += 1
            choose.pop()

S = input()
chars = set()
cnt = dict()

for c in S:
    chars.add(c)
    if c not in cnt:
        cnt[c] = 0
    cnt[c] += 1

choose = []
ans = 0

func(0)

print(ans)