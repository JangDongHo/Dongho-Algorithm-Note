## 문제

https://www.acmicpc.net/problem/2577

---

## 핵심 키워드

- 수학
- 구현
- 사칙연산
- 빈도수 배열

---

## 회고

### Learned (새롭게 알게 된 점)

- Python 3는 `int`가 메모리가 허용하는 한 거의 무한대까지 커질 수 있다는 것을 알게 됐다.
- `collections`의 `Counter`를 사용해서 문제를 해결할 수도 있다는 사실을 알게 됐다.

```ts
from collections import Counter

def solve(a: int, b: int, c: int) -> str:
    num = str(a * b * c)
    counter = Counter(num)
    return "\n".join(str(counter.get(str(d), 0)) for d in range(10))
```

### Lacked (부족했던 점)

- 최악의 경우 `A*B*C`의 값이 int의 범위를 벗어나는지 체크하지 않았다.
- 문제가 쉬워서 너무 생각하지 않고 바로 코드로 옮기는 것 같다.

### Longed for (시도할 점)

- 아무리 쉬운 문제라도 내가 구현해야할 것들을 주석으로 간단히 남기고 코드로 옮기자.

### Liked (좋았던 점)

- 다른 사람의 풀이에서 새롭게 알게된 점들을 기록하는 것
