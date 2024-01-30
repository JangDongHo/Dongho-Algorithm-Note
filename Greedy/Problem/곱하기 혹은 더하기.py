'''
난이도: 1
목표 시간: 30분
시간 제한: 1초
메모리 제한: 128MB

성공 여부: 성공
풀이 시간: 11분
'''

### 내가 푼 코드 (브루트포스)
'''
접근 방법
- 대부분은 '+'보다는 'x'가 더 값을 크게 만든다.
- 하지만 특정한 수에서는 '+'가 'x'보다 더 큰 수를 만들 수 있을 것이라 생각했다.
- 그래서, 브루트포스를 이용해서 두 가지 경우의 수를 모두 계산했다.
'''
input = input()
n = len(input)
count = int(input[0])

for i in range(1, n):
  num = int(input[i])
  if count + num > count * num:
    count += num
  else:
    count *= num

print(count)

### 책 코드 (그리디)
'''
접근 방법
- 대부분은 '+'보다는 'x'가 더 값을 크게 만든다.
- 하지만 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기를 수행하는 것이 효율적이다.
- 두 수에 대하여 연산을 수행할 때, 두 수 중에서 하나라도 1 이하인 경우에는 더하며, 두 수가 모두 2 이상인 경우에는 곱하면 된다.
'''
data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
  # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
  num = int(data[i])
  if num <= 1 or result <= 1:
    result += num
  else:
    result *= num

print(result)
