def solution(dartResult):
    n = len(dartResult)
    
    scores = []
    i = 0
    
    while i < n:
        # 1. 점수 파싱 (10 예외 처리)
        if dartResult[i] == '1' and i + 1 < n and dartResult[i + 1] == '0':
            num = 10
            i += 2
        else:
            num = int(dartResult[i])
            i += 1
        
        # 2. 보너스 적용
        bonus = dartResult[i]
        if bonus == 'S':
            num **= 1
        elif bonus == 'D':
            num **= 2
        else:
            num **= 3
        i += 1
        
        scores.append(num)
        
        # 3. 옵션 적용
        if i < n:
            if dartResult[i] == '*':
                scores[-1] *= 2
                if len(scores) > 1:
                    scores[-2] *= 2
                i += 1
            elif dartResult[i] == '#':
                scores[-1] *= -1
                i += 1
    
    return sum(scores)