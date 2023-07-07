#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
 and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
    boxes is a list of lists
    :param boxes:
    :return: boolean
    """
    totalBoxes = len(boxes)
    checkBox = [False] * totalBoxes
    checkBox[0] = True
    stack = [0]

    while stack:
        currentBox = stack.pop()
        keys = boxes[currentBox]

        for key in keys:
            if key < totalBoxes and not checkBox[key]:
                checkBox[key] = True
                stack.append(key)
    return all(checkBox)
