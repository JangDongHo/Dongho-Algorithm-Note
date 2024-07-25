from itertools import permutations

N = int(input())
infos = [input().split() for _ in range(N)]
ans = 0

for cur in permutations(range(1, 10), 3):
    ok = True

    for num, st, bl in infos:
        cur_st = cur_bl = 0

        for i in range(3):
            if str(cur[i]) == num[i]:
                cur_st += 1
            elif str(cur[i]) in num:
                cur_bl += 1

        if cur_st != int(st) or cur_bl != int(bl):
            ok = False
            break

    if ok:
        ans += 1

print(ans)