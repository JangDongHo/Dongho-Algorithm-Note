'''
난이도: 1
목표 시간: 20분
시간 제한: 1초
메모리 제한: 256MB

성공 여부: 실패
'''
'''
접근 방식
- 이 문제의 핵심 아이디어는 정확히 중간값에 해당하는 위치의 집에 안테나를 설치했을 때, 안테나로부터 모든 집까지의 거리의 총합이 최소가 된다는 점이다.
'''

### 책 코드
N = int(input())
house_list = list(map(int, input().split()))
house_list.sort()
print(house_list[(N - 1) // 2])
