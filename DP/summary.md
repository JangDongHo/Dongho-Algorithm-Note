## 중복되는 연산을 줄이자

- 컴퓨터를 활용해도 해결하기 어려운 문제는 무엇일까?
  - 최적의 해를 구하는데 시간이 매우 많이 필요하거나 메모리 공간이 많이 필요한 문제
- 그래서 우리는 연산 속도와 메모리 공간을 최대한으로 활용할 수 있는 효율적인 알고리즘을 고안해야 한다.
- 어떤 문제는 메모리 공간을 약간 더 사용하면 연산 속도를 비약적으로 증가시킬 수 있는 방법이 있다.
  - 이를 다이나믹 프로그래밍(Dynamic Programming)이라고 한다.
- 다이나믹 프로그래밍을 사용할 수 있는 조건
  - 큰 문제를 작은 문제로 나눌 수 있다.
  - 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.
- 다이나믹 프로그래밍이 필요한 예시: 피보나치 수열

  - 기존 방식대로 재귀 함수를 작성하면 지수 시간 복잡도를 가지게 된다.
  - 하지만 다이나믹 프로그래밍을 사용하면 시간 복잡도를 선형 시간으로 줄일 수 있다.

  ```python
  # 피보나치 함수(Fibonacci Function)을 재귀 함수로 구현
  def fibo(x):
      if x == 1 or x == 2:
          return 1
      return fibo(x - 1) + fibo(x - 2)
  ```

  ```python
  # 피보나치 수열(Fibonacci Sequence)을 메모제이션(Memoization)을 이용하여 구현
  d = [0] * 100

  # 피보나치 함수(Fibonacci Function)를 재귀 함수로 구현(Top-Down DP)
  def fibo(x):
      # 종료 조건(1 혹은 2일 때 1을 반환)
      if x == 1 or x == 2:
          return 1
      # 이미 계산한 적 있는 문제라면 그대로 반환
      if d[x] != 0:
          return d[x]
      # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
      d[x] = fibo(x - 1) + fibo(x - 2)
      return d[x]
  ```

- 정리하자면 다이나믹 프로그래밍이란 큰 문제를 작게 나누고, 같은 문제라면 한 번씩만 풀어 문제를 효율적으로 해결하는 알고리즘이다.
- 다이나믹 프로그래밍의 구현 방식은 크게 두 가지로 나뉜다.
  - Top-Down: 큰 문제를 해결하기 위해 작은 문제를 호출한다.
  - Bottom-Up: 작은 문제부터 차근차근 답을 도출한다.
- 다이나믹 프로그래밍의 전형적인 형태는 Bottom-Up 방식이다.

```python
# Bottom-Up 방식으로 구현
d = [0] * 100

# 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99

# 피보나치 함수(Fibonacci Function) 반복문으로 구현(Bottom-Up DP)
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])
```

## 다이나믹 프로그래밍 조언

- 메모제이션은 때에 따라서 다른 자료형, 예를 들어 사전(dict) 자료형을 이용할 수도 있다.
- 사전 자료형은 수열처럼 연속적이지 않은 경우에 유용하게 사용할 수 있다.
  - 예를 들어, 피보나치 수열처럼 이전의 두 항을 더하는 것이 아니라 임의의 항들을 더하는 경우에도 사용할 수 있다.
- 코딩 테스트에서의 다이나믹 프로그래밍 문제는 대체로 간단한 형태로 출제되므로, 기본 유형을 숙지하고 있으면 쉽게 풀 수 있다.
- 특정한 문제를 완전 탐색 알고리즘으로 접근했을 때 시간이 매우 오래 걸리면 다이나믹 프로그래밍을 적용할 수 있는지 해결하고자 하는 부분 문제들의 중복 여부를 확인해보자.
