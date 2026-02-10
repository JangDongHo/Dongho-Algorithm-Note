# https://school.programmers.co.kr/learn/courses/30/lessons/77486#

def query(name, price):
    global money, tree
    
    price10 = int(price * 0.1)
    money[name] += price - price10
    
    if price10 == 0:
        return
        
    if name != '-':
        query(tree[name], price10)

def solution(enroll, referral, seller, amount):
    global money, tree
    
    money = dict()
    money['-'] = 0
    for name in enroll:
        money[name] = 0
        
    tree = dict()
    for child, parent in zip(enroll, referral):
        tree[child] = parent
        
    for name, num in zip(seller, amount):
        query(name, num * 100)
    
    ans = [money[name] for name in enroll]
    return ans