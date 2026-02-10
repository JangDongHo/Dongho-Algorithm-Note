# https://school.programmers.co.kr/learn/courses/30/lessons/150369

## 풀이 1. 그리디 - O(n)
def process_boxes(boxes, cap):
    """작업이 가능한 만큼 박스를 처리하는 함수"""
    while len(boxes):
        if cap < boxes[-1]: # 트럭의 적재 용량(cap)보다 처리해야 할 박스가 많은 경우
            boxes[-1] -= cap
            break
        else:
            cap -= boxes[-1]
            boxes.pop()
        

def solution(cap, n, deliveries, pickups):
    ans = 0
    
    while len(deliveries) or len(pickups): # 작업해야 할 물량이 남을 때 까지 반복
        # 작업이 필요 없는 집 삭제
        while len(deliveries) and deliveries[-1] == 0:
            deliveries.pop()
        while len(pickups) and pickups[-1] == 0:
            pickups.pop()
        
        ans += max(len(deliveries), len(pickups)) * 2 # 작업해야 할 물량이 있는 가장 먼 곳으로 이동
        process_boxes(deliveries, cap)
        process_boxes(pickups, cap)
    
    return ans

## 풀이 2. 그리디 - O(n)
def solution(cap, n, deliveries, pickups):
    # 가장 먼 곳부터 처리하기 위해 deliveries와 pickups 리스트를 reverse
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    
    answer = 0 # 이동한 총 거리의 합
    have_to_deli = 0 # 지금까지 배달해야 할 총 물품 수를 누적
    have_to_pick = 0 # 지금까지 수거해야 할 총 물품 수를 누적
		
		# 모든 집에 대해 배달 및 수거 작업을 처리
    for i in range(n):
        have_to_deli += deliveries[i]
        have_to_pick += pickups[i]
        
        # 배달할 물품이나 수거할 물품이 남아있으면 계속 작업
        while have_to_deli > 0 or have_to_pick > 0:
		        # 한 번에 트럭이 처리할 수 있는 물품 수만큼 배달/수거
            have_to_deli -= cap
            have_to_pick -= cap
            answer += (n - i) * 2

    return answer