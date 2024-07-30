N, M = map(int, input().split())
arr = list(map(int, input().split()))

neg = []
pos = []
for x in arr:
    if x > 0:
        pos.append(x)
    else:
        neg.append(-x)

pos = sorted(pos)[::-1]
neg = sorted(neg)[::-1]

dists = []

for p in pos[::M]:
    dists.append(p)

for n in neg[::M]:
    dists.append(n)

ans = 2 * sum(dists) - max(dists)
print(ans)