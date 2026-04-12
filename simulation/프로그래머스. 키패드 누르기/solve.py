"""프로그래머스. 키패드 누르기"""


def solution(numbers, hand):
    pos = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }

    left = pos['*']
    right = pos['#']
    answer = []

    def dist(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    for n in numbers:
        target = pos[n]

        if n in [1, 4, 7]:
            left = target
            answer.append('L')
        elif n in [3, 6, 9]:
            right = target
            answer.append('R')
        else:
            l_dist = dist(left, target)
            r_dist = dist(right, target)

            if l_dist > r_dist:
                right = target
                answer.append('R')
            elif l_dist < r_dist:
                left = target
                answer.append('L')
            else:
                if hand == "left":
                    left = target
                    answer.append('L')
                else:
                    right = target
                    answer.append('R')

    return "".join(answer)
