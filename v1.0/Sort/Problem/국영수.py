'''
난이도: 1
목표 시간: 20분
시간 제한: 1초
메모리 제한: 256MB

성공 여부: 실패
'''
'''
새롭게 알게된 점
- 파이썬에서는 튜플을 원소로 하는 리스트가 있을 때, 그 리스트를 정렬하면 기본적으로 각 튜플을 구성하는 원소의 순서에 맞게 정렬된다는 특징이 있다.
- 리스트의 원소를 정렬할 때는 sort() 함수의 key 속성에 값을 대입하여 내가 원하는 '조건'에 맞게 튜플을 정렬시킬 수 있다는 점을 기억하자.
  - ex) students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
  - '-'를 붙이면 내림차순
'''

### 내가 푼 코드

import sys

input = sys.stdin.readline()

n = int(input)

students = []
for _ in range(n):
  data = list(sys.stdin.readline().split())
  [name, kor, eng, math] = data[0], int(data[1]), int(data[2]), int(data[3])
  students.append((name, kor, eng, math))

sorted_students = sorted(students, key=lambda x: (-x[1], x[2], -x[3], x[0]))
for student in sorted_students:
  print(student[0])

### 책 코드
n = int(input())
students = []  # 학생 정보를 담을 리스트

# 모든 학생 정보를 입력 받기
for _ in range(n):
  students.append(input().split())
'''
[ 정렬 기준 ]
1) 두 번째 원소를 기준으로 내림차순 정렬
2) 두 번째 원소가 같은 경우, 세 번째 원소를 기준으로 오름차순 정렬
3) 세 번째 원소가 같은 경우, 네 번째 원소를 기준으로 내림차순 정렬
4) 네 번째 원소가 같은 경우, 첫 번째 원소를 기준으로 오름차순 정렬
'''
students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

# 정렬된 학생 정보에서 이름만 출력
for student in students:
  print(student[0])
