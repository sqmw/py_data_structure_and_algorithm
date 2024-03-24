"""
快排
1. 是基于比较和交换的排序算法
2. 是双指针的一种应用
3. 通过递归实现
4. 原则上，确定了位置之后就不等你动它
"""
import random
import time
from typing import List


def _swap(index_i, index_j, arr: List[int]):
    arr[index_i], arr[index_j] = arr[index_j], arr[index_i]


def quick_sort(arr: List[int], left: int, right: int):
    """
    这里实现的升序排序
    每次都把第一个数字 arr[left] 作为标准
    [left, right)
    """
    if right - left < 2:
        return
    i = left + 1
    j = right - 1
    while i < j:
        while i < j and arr[i] < arr[left]:
            i += 1
        while i < j and arr[j] > arr[left]:
            j -= 1
        if i < j and arr[i] >= arr[left] >= arr[j]:
            _swap(i, j, arr)
    while arr[i] > arr[left]:
        i -= 1
    _swap(i, left, arr)

    quick_sort(arr, left, i)
    quick_sort(arr, i + 1, right)


if __name__ == '__main__':
    t0 = time.time()
    length = 5
    nums = [random.randint(0, 100) for i in range(0, length)]
    # nums = [81, 75, 7, 47, 51]
    print(nums)
    quick_sort(nums, 0, len(nums))
    print(nums)
