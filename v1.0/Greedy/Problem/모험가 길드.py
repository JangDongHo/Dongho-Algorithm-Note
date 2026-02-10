'''
난이도: 1
목표 시간: 30분
시간 제한: 1초
메모리 제한: 128MB

성공 여부: 실패
'''

### 내가 푼 코드 (실패)
'''
반례
n=6이고 공포도가 4 3 3 3 3 2 인 경우
내림차순 정렬 4 3 3 3 / 3 2 -> result는 1인데
오름차순 정렬 2 3 / 3 3 3 / 4 -> result가 2여야 하므로 오류
'''

n = int(input())
people = list(map(int, input().split()))
people.sort(reverse=True)

index = 0
result = 0
while index < n:
  index += people[index]
  result += 1

print(result)
'''
접근 방법
- 최대 그룹수를 구하라고 했다. 그러려면, 최소한의 인원으로 그룹을 구성해야 한다.
- 공포도가 낮은 사람부터 최소한의 인원수로 그룹을 형성해 나가야 그룹수가 많아진다.
- 사람을 오름차순으로 정렬하고, 문제에서 그룹이 형성가능한 최소 조건대로 공포도가 인원수보다 작거나 같다면 그룹을 만든다.
'''

### 책 코드

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0  #총 그룹의 수
count = 0  #현재 그룹에 포함된 모험가의 수

for i in data:  #공포도를 낮은 것부터 하나씩 확인하며
  count += 1  #현재 그룹에 해당 모험가를 포함시키기
  if count >= i:  #현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
    result += 1  #총 그룹의 수 증가시키기
    count = 0  #현재 그룹에 포함된 모험가의 수 초기화

print(result)
