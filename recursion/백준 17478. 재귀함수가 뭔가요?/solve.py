# BOJ 17478 재귀함수가 뭔가요?

import sys


def sys_input() -> int:
    return int(sys.stdin.readline().strip())


INTRO = "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다."
QUESTION = '"재귀함수가 뭔가요?"'
ANSWER = '"재귀함수는 자기 자신을 호출하는 함수라네"'
CLOSING = "라고 답변하였지."
INDENT_UNIT = "____"

STORY = [
    '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.',
    "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.",
    "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"",
]


def solve(depth: int, max_depth: int) -> None:
    indent = INDENT_UNIT * depth

    print(indent + QUESTION)

    if depth == max_depth:
        print(indent + ANSWER)
        print(indent + CLOSING)
        return

    for line in STORY:
        print(indent + line)

    solve(depth + 1, max_depth)
    print(indent + CLOSING)


def main() -> None:
    n = sys_input()
    print(INTRO)
    solve(0, n)


if __name__ == "__main__":
    main()