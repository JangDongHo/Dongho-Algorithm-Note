'''
난이도: 2
풀이 시간: 30분
시간 제한: 1초
메모리 제한: 128MB

성공 여부: 실패
'''

### 내가 푼 코드

n = int(input())
n_list = list(map(int, input().split()))
max_list = [0] * (n + 1)

max_list[1] = n_list[0]
max_list[2] = max(n_list[1], n_list[0])
max_list[3] = n_list[2] + n_list[0]
for i in range(4, n + 1):
  max_list[i] = max(n_list[i - 1] + max_list[i - 2],
                    n_list[i - 1] + max_list[i - 3])

print(max_list[n])

### 책 코드
n = int(input())
array = list(map(int, input().split()))

d = [0] * 100

d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
  d[i] = max(d[i - 1], d[i - 2] + array[i])

print(d[n - 1])
'''
접근방법
1. 특정한 i번째 식량창고에 대해서 털지 안 털지의 여부를 결정할 때, 단 2가지 경우에 대해서만 확인하면 된다.
  a. (i-1)번째 식량창고를 털기로 결정한 경우 현재의 식량창고를 털 수 없다.
  b. (i-2)번째 식량창고를 털기로 결정한 경우 현재의 식량창고를 털 수 있다.
2. a와 b 중에서 더 많은 식량을 털 수 있는 경우를 생각하면 된다.
- 여기서 알아두어야 할 점은 i번째 식량창고에 대한 최적의 해를 구할 때 왼쪽부터 (i-3)번째 이하의 식량 창고에 대한 최적의 해에 대해서는 고려할 필요가 없다.
  - 예를 들어, d[i-3]은 d[i-1]과 d[i-2]을 구하는 과정에서 이미 계산되었기 때문에 d[i]의 값을 구할 때는 d[i-1]과 d[i-2]만 고려하면 된다.
'''
