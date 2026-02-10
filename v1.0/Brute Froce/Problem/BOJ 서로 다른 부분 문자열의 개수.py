# https://www.acmicpc.net/problem/11478

S = input()
seen = set()

for i in range(len(S)):
	for j in range(i, len(S)):
		seen.add(S[i:j + 1])

print(len(seen))