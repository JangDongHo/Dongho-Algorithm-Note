'''
난이도: 1
목표 시간: 20분
시간 제한: 1초
메모리 제한: 128MB

성공 여부: 일부 성공(숫자가 안 들어오는 경우를 고려하지 않았음)
풀이 시간: 8분
'''

### 내가 푼 코드

data = input()
alphabet_list = []
sum = 0

for char in data:
  if ord(char) >= 65:  # 대문자 A를 아스키코드로 변환할 시 65
    alphabet_list.append(char)
  else:
    sum += int(char)

alphabet_list.sort()

for char in alphabet_list:
  print(char, end="")
print(sum)

### 책 코드
data = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data:
  # 알파벳인 경우 결과 리스트에 삽입
  if x.isalpha():
    result.append(x)
  # 숫자는 따로 더하기
  else:
    value += int(x)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
  result.append(str(value))

# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))
