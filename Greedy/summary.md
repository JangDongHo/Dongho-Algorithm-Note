# 1. 당장 좋은 것만 선택하는 그리디

- 그리디 알고리즘은 현재 상황에서 지금 당장 좋은 것만 고르는 방법을 의미한다.
- 단순하지만 강력한 문제 해결 방법

## 그리디 알고리즘의 특징

- 사전에 외우고 있지 않아도 풀 수 있을 가능성이 높은 문제 유형
- 문제의 유형이 매우 다양하기에 암기한다고 해서 풀 수 있는 문제가 아니다.

## 왜 출제하는가?

- 창의력, 즉 문제를 풀기 위한 최소한의 아이디어를 떠올릴 수 있는 능력을 요구하기 때문
  - 특정한 문제를 만났을 때 단순히 현재 상황에서 가장 좋아 보이는 것만을 선택해도 문제를 풀 수 있는지 검토할 수 있어야 한다.
- 그리디 알고리즘은 기준에 따라 좋은 것을 선택하는 알고리즘이므로 문제에서 **가장 큰 순서대로, 가장 작은 순서대로**와 같은 기준을 알게 모르게 제시해준다.

  - ex) 대표적인 문제: 거스름돈 문제

    ```
    n = 1260
    count = 0

    coin_types = [500, 100, 50, 10]

    for coin in coin_types:
      count += n // coin
      n %= coin

    print(count)
    ```

## 주의할 점

- 그리디 알고리즘을 모든 알고리즘 문제에 적용할 수 있는 것은 아니다.
- 거스름돈 문제를 그리디 알고리즘으로 해결할 수 있는 이유는 **큰 단위가 작은 단위의 배수이므로 작은 단위의 동전들을 종합해 다른 해가 나올 수 없기 때문**이다.
- 대부분의 그리디 알고리즘 문제에서는 문제 풀이를 위한 최소한의 아이디어를 떠올리고 이것이 정당한지 검토할 수 있어야 답을 도출할 수 있다.
