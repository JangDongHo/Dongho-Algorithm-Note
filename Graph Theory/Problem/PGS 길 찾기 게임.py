# https://school.programmers.co.kr/learn/courses/30/lessons/42892

import sys
sys.setrecursionlimit(10**6)


class Node:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.left = None
        self.right = None

    def __lt__(self, other):
        if (self.y == other.y):
            return self.x < other.x
        return self.y > other.y


def addNode(parent, child):
    if child.x < parent.x:
        if parent.left is None:
            parent.left = child
        else:
            addNode(parent.left, child)
    else:
        if parent.right is None:
            parent.right = child
        else:
            addNode(parent.right, child)


def preorder(ans, node):
    # Base Case
    if node is None:
        return

    # Recursive Case
    ans.append(node.id)
    preorder(ans, node.left)
    preorder(ans, node.right)
    return ans


def postorder(ans, node):
    # Base Case
    if node is None:
        return

    # Recursive Case
    postorder(ans, node.left)
    postorder(ans, node.right)
    ans.append(node.id)
    return ans


def solution(nodeinfo):
    N = len(nodeinfo)

    # 1. 트리 생성
    node_list = []
    for i in range(N):
        node_list.append(Node(i + 1, nodeinfo[i][0], nodeinfo[i][1]))

    node_list.sort()
    root = node_list[0]
    for i in range(1, N):
        addNode(root, node_list[i])

    # 2. 순회
    answer = [[], []]
    preorder(answer[0], root)
    postorder(answer[1], root)

    return answer
