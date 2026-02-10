'''
난이도: 1
목표 시간: 20분
시간 제한: 1초
메모리 제한: 128MB

성공 여부: 실패
'''
'''
접근 방식
- 스테이지 번호 (i)를 1부터 N까지 증가시키며, 해당 단계에 머물러 있는 플레이어들의 수(count)를 계산한다.
- 그러한 플레이어들의 수(count) 정보를 이용하여 모든 스테이지에 따른 실패율을 계산한 뒤에 저장하면 된다.
- 최종적으로 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호를 출력하라고 요구하고 있으므로, 실패율을 기준으로 내림차순 정렬을 수행해야 한다.
- 전체 스테이지의 개수는 200,000 이하이기 때문에 기본적인 정렬 라이브러리를 이용해서 O(NlogN)의 시간으로 내림차순으로 정렬을 수행하면 충분하다.
'''
### 책 코드
def solution(N, stages):
  answer = []
  length = len(stages)

  # 스테이지 번호를 1부터 N까지 증가시키며
  for i in range(1, N + 1):
      # 해당 스테이지에 머물러 있는 사람의 수 계산
      count = stages.count(i)

      # 실패율 계산
      if length == 0:
          fail = 0
      else:
          fail = count / length

      # 리스트에 (스테이지 번호, 실패율) 원소 삽입
      answer.append((i, fail))
      length -= count

  # 실패율을 기준으로 각 스테이지를 내림차순 정렬
  answer = sorted(answer, key=lambda t: t[1], reverse=True)

  # 정렬된 스테이지 번호 반환
  answer = [i[0] for i in answer]
  return answer