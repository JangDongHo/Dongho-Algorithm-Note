'''
난이도: 1
목표 시간: 20분
시간 제한: 1초
메모리 제한: 128MB

1회독 성공 여부: 실패
2회독 성공 여부: 성공
풀이 시간: 40분
'''
'''
접근 방법
- 재귀 함수를 이용하여 구현하는 문제
- 특정 문자열에서 "균형 잡힌 문자열" 의 인덱스를 반환하는 함수
- "균형잡힌 괄호 문자열"이 "올바른 괄호 문자열"인지 확인하는 함수
'''

### 내가 푼 코드
def algorithm(w):
  # 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
  if w == '':
      return ''
  # 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다
  is_balance = True
  index = 0
  count = 0
  for c in w:
      if c == '(':
          count += 1
      elif c == ')':
          count -= 1
      index += 1
      if count < 0:
          is_balance = False
      if count == 0:
          u = w[0:index]
          v = w[index:len(w)]
          break
  if is_balance:
      return u + algorithm(v)
  else:
      tmp = '('
      tmp += algorithm(v)
      tmp += ')'
      u = list(u[1:len(u)-1])
      for i in range(len(u)):
          if u[i] == '(':
              u[i] = ')'
          elif u[i] == ')':
              u[i] = '('
      tmp += "".join(u)
      return tmp

def solution(p):
  answer = algorithm(p)
  print(answer)
  return answer

### 책 코드
# "균형잡힌 괄호 문자열"의 인덱스 반환
def balanced_index(p):
    count = 0 # 왼쪽 괄호의 개수
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i

# "올바른 괄호 문자열"인지 판단
def check_proper(p):
    count = 0 # 왼쪽 괄호의 개수
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0: # 쌍이 맞지 않는 경우에 False 반환
                return False
            count -= 1
    return True # 쌍이 맞는 경우에 True 반환

def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1:]
    # "올바른 괄호 문자열"이면, v에 대해 함수를 수행한 결과를 붙여 반환
    if check_proper(u):
        answer = u + solution(v)
    # "올바른 괄호 문자열"이 아니라면 아래의 과정을 수행
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1]) # 첫 번째와 마지막 문자를 제거
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer