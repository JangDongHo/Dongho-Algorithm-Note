import sys
input = lambda: sys.stdin.readline().rstrip()

# input
N, H = map(int, input().split())

tops = [0] * (H + 1)
bots = [0] * (H + 1)

for i in range(N):
	num = int(input())
	if i % 2 == 0:
		bots[num] += 1
	else:
		tops[H - num + 1] += 1

# solve
mn = int(1e12)
mn_num = 0

cnt = N // 2
for h in range(1, H + 1):
    cnt -= bots[h - 1]
    cnt += tops[h]
	
    if mn == cnt:
        mn_num += 1

    if mn > cnt:
        mn = cnt
        mn_num = 1

print(mn, mn_num)
