# https://school.programmers.co.kr/learn/courses/30/lessons/150368

def calculate_result(discounts):
    global users, emoticons
    """ 조합된 할인율로 결과를 시뮬레이션 하는 함수 """
    result = [0, 0]  # (가입자 수, 매출액)
    
    for user_discount, user_limit in users:
        money = 0
        for emoticon_price, discount in zip(emoticons, discounts):
            if discount >= user_discount:
                money += emoticon_price * (100 - discount) // 100
        if money >= user_limit:
            result[0] += 1
        else:
            result[1] += money
    return result

def dfs(discounts, depth):
    """ 모든 경우의 할인율 조합을 구하는 함수 """
    global answer
    
    # Base Case
    if depth == len(discounts):
        answer = max(answer, calculate_result(discounts))
        return
    
    # Recursive Case
    for p in [10, 20, 30, 40]:
        discounts[depth] += p
        dfs(discounts, depth + 1)
        discounts[depth] -= p

def solution(_users, _emoticons):
    global users, emoticons, answer
    users = _users
    emoticons = _emoticons
    
    discounts = [0] * len(emoticons) # 상품 별 할인율
    answer = [0, 0] # (가입자 수, 매출액)
    dfs(discounts, 0)
    return answer