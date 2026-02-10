'''
난이도: 1
목표 시간: 15분
시간 제한: 1초
메모리 제한: 128MB

성공 여부: 성공
풀이 시간: 6분
'''

n = int(input())
num_list = []
for _ in range(n):
  num_list.append(int(input()))
num_list.sort(reverse=True)
for num in num_list:
  print(num, end=" ")
'''
새롭게 알게된 점
- sort와 sorted 함수 내림차순 매개변수 'reverse'
'''
