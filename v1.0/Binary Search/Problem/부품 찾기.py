'''
난이도: 1.5
목표 시간: 30분
시간 제한: 1초
메모리 제한: 128MB

성공 여부: 성공
풀이 시간: 17분
'''
'''
접근 방법
1. 매장 내 부품의 번호를 오름차순 정렬
  - N개의 부품을 정렬하는 시간: O(N * logN)
2. 이진 탐색을 이용하여 부품 찾기
  - 최악의 경우 시간 복잡도 O(M * logN)의 연산이 필요
  - 최대 100,000 * 20 번의 연산이 필요
- 결과적으로 이진 탐색을 사용하는 문제 풀이 방법의 경우 시간 복잡도는 O((M + N) * logN) 이다.
'''

### 이진 탐색을 이용한 풀이 방법 (내가 푼 코드)
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

# 이진 탐색을 위한 n_list 오름차순 정렬
n_list.sort()


# 이진 탐색 소스코드 구현(반복문)
def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    # 찾은 경우 index 반환
    if array[mid] == target:
      return mid
    # 찾을 값이 mid 값보다 작을 경우
    elif array[mid] > target:
      end = mid - 1
    # 찾을 값이 mid 값보다 클 경우
    else:
      start = mid + 1
  return None


for num in m_list:
  result = binary_search(n_list, num, 0, n - 1)
  if result == None:
    print("no", end=" ")
  else:
    print("yes", end=" ")

### 계수 정렬을 이용한 풀이 방법
'''
이 알고리즘의 시간 복잡도는 주어진 배열의 크기를 n, 주어진 숫자들의 개수를 m이라 할 때, 계수 정렬을 위한 배열 array를 초기화하고 업데이트하는데 O(n)의 시간이 소요되며, 이후에 각 주어진 숫자에 대해 array에서 해당 숫자를 확인하는데 O(m)의 시간이 소요됩니다. 따라서 총 시간 복잡도는 O(n + m)입니다.
'''
n = int(input())
array = [0] * 1000001

for i in input().split():
  array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
  if array[i] == 1:
    print('yes', end=' ')
  else:
    print('no', end=' ')

### 집합 자료형 이용
n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
  if i in array:
    print('yes', end=' ')
  else:
    print('no', end=' ')
