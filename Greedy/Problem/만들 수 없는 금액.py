'''
난이도: 1
목표 시간: 30분
시간 제한: 1초
메모리 제한: 128MB

성공 여부: 실패
'''
'''
접근 방법
- 동전을 화폐 단위 기준으로 정렬한 뒤에, 화폐 단위가 작은 동전부터 하나씩 확인하면서 target 변수를 업데이트하는 방법으로 최적의 해를 계산할 수 있다.
![만들 수 없는 금액](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcRTvtg%2FbtrBuy1i3Sr%2FcZMexJEORqKmvyY7zUTryk%2Fimg.png)
'''

n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
  # 만들 수 없는 금액을 찾았을 때 반복 종료
  if target < x:
    break
  target += x

# 만들 수 없는 금액 출력
print(target)
