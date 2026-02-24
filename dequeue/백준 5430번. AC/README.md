# 5430번. AC

## 문제

https://www.acmicpc.net/problem/5430

## TIL

- 파이썬 토글(Toggle) 방법

```python
reverse = False if reverse else True
```

```python
reverse = not reverse
```

- `deque.reverse()` 설명
  - deque 내부 원소들의 순서를 뒤집는 메서드
  - 리스트의 `list.reverse()`와 동일하게 제자리(in-place)에서 동작
  - O(n)의 시간 복잡도를 가짐

- `"".split(",")` 는 `[]`가 아닌 `[""]`이다.
  - 테스트케이스와 같이 빈 배열 문자열("[]")이 input으로 들어오는 경우를 신경써주어야 함