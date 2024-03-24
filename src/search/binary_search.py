"""
折半查找，针对的是有序的列表
"""
import math


def binary_search(s: list, d: float):
    start = 0
    stop = len(s) - 1
    mid = math.floor((start + stop) / 2)
    while start <= stop:
        if s[mid] == d:
            return mid
        elif d < s[mid]:
            stop = mid - 1
        else:
            start = mid + 1
        mid = math.floor((start + stop) / 2)
    return -1



if __name__ == "__main__":
    print(binary_search(list(range(100)), -2))
