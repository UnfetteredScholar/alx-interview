#!/usr/bin/python3

"""Defines the canUnlockAll function"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened

    Args:
        boxes (List[List[int]]): list of boxes

    Returns:
        True if all boxes can be opened, else return False
    """
    if len(boxes) == 0:
        return True
    keys = []
    box_indexes = {0}
    keys.extend(boxes[0])

    while len(keys) > 0 and len(box_indexes) < len(boxes):
        key = keys.pop()
        if key in box_indexes:
            continue
        box_indexes.add(key)
        keys.extend(boxes[key])

    return len(box_indexes) == len(boxes)
