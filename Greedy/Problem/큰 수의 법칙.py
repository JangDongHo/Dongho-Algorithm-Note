"""
난이도: 1
목표 시간: 30분
시간 제한: 1초
메모리 제한: 128MB
기출: 2019 국가 교육기관 코딩 테스트

1회독 성공 여부: 실패
2회독 성공 여부: 성공
풀이 시간: 7분
"""

### 내가 푼 코드
N, M, K = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort(reverse=True)

tmp = 0
sum = 0
for i in range(M):
  if tmp == K:
    sum += num_list[1]
    tmp = 0
  else:
    sum += num_list[0]
    tmp += 1

print(sum)

### 책 코드
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()  # 입력 받은 수 정렬
first = data[n - 1]  # 가장 큰 수
second = data[n - 2]  # 두 번째로 큰 수
result = 0  # 결과 값 저장

while True:
  for i in range(k):
    if m == 0:
      break
    result += first
    m -= 1
  if m == 0:
    break
  result += second
  m -= 1

print(result)
"""
새롭게 배운 점
1. input() 함수
  - 한 줄의 문자열을 입력하는 함수
2. sort() 메소드
  - 파이썬의 sort() 메소드는 Time Sort 알고리즘을 기반으로 하고 있다.
  - Time Sort 알고리즘은 삽입 정렬과 합병 정렬을 합친 정렬 알고리즘이다.
  - Time Sort 알고리즘의 시간 복잡도는 최선의 경우 O(n), 최악의 경우 O(nlogn)의 시간 복잡도를 가진다.
3. sort() vs sorted()
  - sort 함수는 리스트명.sort( ) 형식으로 "리스트형의 메소드"이며 리스트 원본값을 직접 수정
    - 즉, 이 함수는 입력값으로 리스트밖에 받지 못함
  - sorted 함수는 sorted(리스트명) 형식으로 "내장 함수"이며 리스트 원본 값은 그대로이고 정렬 값을 반환
    - sort 함수와는 다르게 어떤 입력값이든 받을 수 있음
"""
