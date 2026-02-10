# https://school.programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    numbers = list(map(str, numbers))  # 숫자를 문자열로 변환
    numbers.sort(key=lambda x: x * 3, reverse=True)  # 숫자를 3자리 이상으로 반복 확장 후 정렬
    return str(int("".join(numbers)))  # "0000" 같은 경우 "0" 처리


