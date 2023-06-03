"""冒泡排序"""
import random


def bubble_sort_init(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                t = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = t


if __name__ == "__main__":
    arr = [random.randint(0, 1000) for i in range(0, 1000)]
    bubble_sort_init(arr)
    print(arr)
