"""实现了选择排序"""
import random

"""插入排序就是每次取出一个插入到有序的序列中"""
"""都是升序排序"""


def select_sort(arr):
    # 需要进行交换位置的下标
    for i in range(0, len(arr) - 1):
        # 遍历寻找最小的下标
        min_index = i + 1
        for j in range(i + 2, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        t = arr[min_index]
        arr[min_index] = arr[i]
        arr[i] = t


if __name__ == "__main__":
    a = [random.randint(1, 100000) for x in range(1, 100)]
    select_sort(a)
    print(a)