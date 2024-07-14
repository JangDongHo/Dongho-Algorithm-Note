### 풀이1. 직접 구현
def permutation(level):
    global N, choose, check

    # base case
    if level == N:
        print(' '.join(map(str, choose)))
        return

    # recursive case
    for i in range(1, N + 1):
        if check[i] == True:
            continue

        choose.append(i)
        check[i] = True

        permutation(level + 1)

        check[i] = False
        choose.pop()


N = int(input())
choose = []
check = [False] * (N + 1)

permutation(0)


### 풀이2. 라이브러리 이용
from itertools import permutations


N = int(input())

for permutation in permutations(range(1, N + 1)):
    print(' '.join(map(str, permutation)))