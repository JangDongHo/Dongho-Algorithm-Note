"""백준 2469번. 사다리 타기"""

k = int(input())
n = int(input())
bottom = list(input().strip())
top = [chr(i) for i in range(65, 65 + k)]

lines = [input().strip() for _ in range(n)]
empty_idx = 0

for i in range(n):
    if lines[i][0] == '?':
        empty_idx = i
        break

for i in range(empty_idx):
    s = lines[i]
    for j in range(k - 1):
        if s[j] == '-':
            top[j], top[j + 1] = top[j + 1], top[j]

for i in range(n - 1, empty_idx, -1):
    s = lines[i]
    for j in range(k - 1):
        if s[j] == '-':
            bottom[j], bottom[j + 1] = bottom[j + 1], bottom[j]

answer = ['*'] * (k - 1)

for i in range(k - 1):
    if top[i] == bottom[i]:
        continue
    elif top[i] == bottom[i + 1] and top[i + 1] == bottom[i]:
        answer[i] = '-'
        top[i], top[i + 1] = top[i + 1], top[i]
    else:
        answer = ['x'] * (k - 1)
        break

print(''.join(answer))
