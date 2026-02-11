""" solve.py for 1475번. 방 번호 """

import sys
import math


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(room_number: str) -> int:
    counts = [0] * 10

    for digit in room_number:
        counts[int(digit)] += 1

    six_nine_average = (counts[6] + counts[9]) / 2
    counts[6] = math.ceil(six_nine_average)
    counts[9] = math.floor(six_nine_average)

    return max(counts)


def main() -> None:
    room_number = sys_input()
    answer = solve(room_number)
    print(answer)


if __name__ == "__main__":
    main()