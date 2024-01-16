'''
난이도: 1
목표 시간: 20분
시간 제한: 2초
메모리 제한: 128MB

성공 여부: 성공
풀이 시간: 13분
'''

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
  if a[i] >= b[i]:
    break
  a[i], b[i] = b[i], a[i]

print(sum(a))
