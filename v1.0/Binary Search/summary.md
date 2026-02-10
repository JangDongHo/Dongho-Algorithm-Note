# 1. 범위를 반씩 좁혀가는 탐색

## 순차 탐색

- 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법
- 데이터 정렬 여부와 상관없이 가장 앞에 있는 원소부터 하나씩 확인해야 한다.
- 따라서, 시간 복잡도는 O(N)

```python
# 순차 탐색 소스코드 구현
def sequential_search(n, target, array):
    # 각 원소를 하나씩 확인하며
    for i in range(n):
        # 현재의 원소가 찾고자 하는 원소와 동일한 경우
        if array[i] == target:
            return i + 1 # 현재의 위치 반환(인덱스는 0부터 시작하므로 1 더하기)

print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
input_data = input().split()
n = int(input_data[0]) # 원소의 개수
target = input_data[1] # 찾고자 하는 문자열

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()

# 순차 탐색 수행 결과 출력
print(sequential_search(n, target, array))
```

## 이진 탐색

- 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘
- 탐색 범위를 절반씩 좁혀가며 데이터를 탐색
- 이진 탐색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정한다.
  ![이진 탐색](https://t1.daumcdn.net/cfile/tistory/233C703B577E34840E)
- 이진 탐색은 한 번 확인할 때마다 확인하는 원소의 개수가 절반씩 줄어든다는 점에서 시간 복잡도는 O(logN)

### 구현 방법

1. 재귀 함수를 이용한 방법

```python
# 이진 탐색 소스코드 구현(재귀 함수)
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid + 1, end)

# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
```

2. 반복문을 이용한 방법

```python
# 이진 탐색 소스코드 구현(반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
```

### 코딩 테스트에서의 이진 탐색

- 이진 탐색은 코딩 테스트에서 단골로 등장하는 문젠이므로 가급적 외우는 것이 좋다.
- 처리해야 할 데이터의 개수나 값이 1,000만 단위 이상으로 넘어가면 이진 탐색과 같이 O(logN)의 속도를 내야하는 알고리즘을 떠올려야 문제를 풀 수 있는 경우가 많다.

## 트리 자료구조

![트리 자료구조](https://i.namu.wiki/i/8pViDtKiYxEmcz1zj2WHZEpLHeu4q4n1bAjOOTvA4rLde3d-miR4lbCeFRjhzuTV1SLW5vFdg81Q6vb6fm1I9Q.webp)

- 이진 탐색은 전제 조건이 데이터 정렬이다.
- 데이터베이스는 내부적으로 대용량 데이터 처리에 적합한 **트리 자료구조**를 이용하여 항상 데이터가 정렬되어 있다.
- 트리 구조는 노드와 노드의 연결로 표현하며, 이때 노드는 정보의 단위로서 어떠한 정보를 가지고 있는 개체(entity)이다.
  > - 트리는 부모 노드와 자식 노드의 관계로 표현된다.
  > - 트리의 최상단 노드를 루트 노드라고 한다.
  > - 트리의 최하단 노드를 단말(리프) 노드라고 한다.
  > - 트리에서 일부를 떼어내도 트리 구조이며 이를 서브 트리라고 한다.
  > - 트리는 파일 시스템과 같이 계층적이고 정렬된 데이터를 다루기에 적합하다.

## 이진 탐색 트리

![이진 탐색 트리](https://t1.daumcdn.net/cfile/tistory/2321CB4951A467AC0B)

- 트리 자료구조 중에서 가장 간단한 형태가 **이진 탐색 트리**이다.
- 이진 탐색 트리란 이진 탐색이 동작할 수 있도록 고안된 효율적인 탐색이 가능한 자료구조이다.
- 이진 탐색 트리의 특징
  > - 부모 노드보다 왼쪽 자식 노드가 작다.
  > - 부모 노드보다 오른쪽 자식 노드가 크다.
- 이진 탐색 트리에 데이터를 넣고 빼는 방법은 알고리즘보다는 자료구조에 가까우며, 이진 탐색 트리 자료구조를 구현하도록 요구하는 문제는 출제 빈도가 낮으므로, 이 책에서는 이진 탐색 트리를 구현하는 방법은 소개하지는 않는다.
- 따라서, 이진 탐색 트리가 미리 구현되어 있다고 가정하고 다음 그림과 같은 이진 탐색 트리에서 데이터를 조회하는 과정만 살펴보자.
- 다음은 찾는 원소가 37일 때 이진 탐색 트리에서의 탐색 과정이다.
  ![이진 탐색 트리 탐색 과정](https://velog.velcdn.com/images%2Fkirri1124%2Fpost%2F6a976a6e-c470-4d1c-9d3b-f50fa96b6bfb%2Fimage.png)
  1. 루트 노드부터 탐색을 시작한다.
  2. 탐색하고자 하는 값이 루트 노드의 값보다 크기 때문에 오른쪽 자식 노드로 이동한다.
  3. 오른쪽 자식 노드의 값이 찾고자 하는 값보다 작기 때문에 왼쪽 자식 노드로 이동한다.
  4. 왼쪽 자식 노드의 값이 찾고자 하는 값과 동일하므로 탐색을 마친다.

### 빠르게 입력받기

- 이진 탐색 문제는 입력 데이터가 많거나, 탐색 범위가 매우 넓은 편이다.
- 예를 들어, 데이터의 개수가 1,000만 개를 넘어가거나 탐색 범위의 크기가 1,000억 이상이라면 이진 탐색 알고리즘을 의심해보자.
- 그런데 이렇게 많은 데이터를 입력받을 때는 input() 함수를 사용하면 동작 속도가 느려서 시간 초과로 오답 판정을 받을 수 있다.
- 이 경우에는 sys 라이브러리의 readline() 함수를 이용하면 시간 초과를 피할 수 있다.

```python
import sys
# 하나의 문자열 데이터 입력받기
input_data = sys.stdin.readline().rstrip()

# 입력받은 문자열 그대로 출력하기
print(input_data)
```

- sys 라이브러리는 다음과 같은 방식으로 한 줄씩 입력받는다.
- sys 라이브러리를 사용할 때는 한 줄 입력받고 나서 rstrip() 함수를 꼭 호출해야 한다.
- readline()으로 입력하면 입력 후 엔터가 줄 바꿈 기호로 입력되는데, 이 공백 문자를 제거하려면 rstrip() 함수를 사용해야 한다.
- 코드가 짧으니, 관행적으로 외워서 사용하자.
