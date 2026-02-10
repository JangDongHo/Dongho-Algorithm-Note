# https://school.programmers.co.kr/learn/courses/30/lessons/92335

from math import sqrt

def convert(num, k):
    ret = []
    
    while num != 0:
        ret.append(str(num % k))
        num //= k

    return ''.join(ret[::-1]) if ret else '0'

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    num_string = convert(n, k)
    nums = num_string.split("0")
    
    ans = 0
    for num in nums:
        if num != '':
            ans += is_prime(int(num))
    return ans
    