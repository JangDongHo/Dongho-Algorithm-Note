N = 11

current_num = N
use4 = current_num // 4
current_num %= 4
use2 = current_num // 2
current_num %= 2
use1 = current_num // 1
current_num %= 1

print(f"1을 사용한 횟수: {use1}")
print(f"2을 사용한 횟수: {use2}")
print(f"4을 사용한 횟수: {use4}")
print(f"사용한 동전의 총 개수: {use1 + use2 + use4}")