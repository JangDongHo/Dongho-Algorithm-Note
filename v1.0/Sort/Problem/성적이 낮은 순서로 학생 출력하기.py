'''
난이도: 1
목표 시간: 20분
시간 제한: 1초
메모리 제한: 128MB

성공 여부: 성공
풀이 시간: 13분
'''

### 내가 푼 코드
n = int(input())
object = {}
for _ in range(n):
  name, grade = input().split()
  grade = int(grade)
  object[name] = grade

sorted_object = sorted(object.items(), key=lambda object: object[1])

for object in sorted_object:
  name, grade = object
  print(name, end=" ")

### 책 코드
n = int(input())

array = []
for _ in range(n):
  input_data = input().split()
  array.append((input_data[0], int(input_data[1])))

array = sorted(array, key=lambda student: student[1])

for student in array:
  print(student[0], end=" ")
