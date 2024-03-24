"""冒泡排序"""
import collections.abc

"""优化1 ：若是在某一次遍历的时候没有发生交换就说明已经排好顺序了"""
import random


def bubble_sort_init(arr: list):
    for i in range(0, len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                t = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = t


def bubble_sort1(arr: list):
    for i in range(0, len(arr)):
        changed = False
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                changed = True
                t = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = t
        if not changed:
            break


if __name__ == "__main__":
    arr = [random.randint(0, 1000) for i in range(0, 10000)]
    bubble_sort_init(arr)
    print(arr)
