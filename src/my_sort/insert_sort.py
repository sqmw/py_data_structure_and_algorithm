"""实现了插入排序"""
import random

"""插入排序就是每次取出一个插入到有序的序列中"""
"""第一次实现的插入排序是先找到位置，再进行插入后面进行了修改，这里运用了查找的知识"""
"""第二次在查找位置的时候就进行修改，这里没有体现查找的思想"""
"""第三次通过二分查找找到位置，再进行插入，这个算是第一个算法的提高"""
"""都是升序排序"""


def insert_sort2(arr):
    length = len(arr)
    # 依次取出 [1, n)
    for index_after in range(1, length):
        j = index_after - 1
        # swap_index 一直指向的是 取出来的那个数字的下标
        swap_index = index_after
        while j >= 0:
            # 设置while的跳出条件，避免while一条路走到底
            if arr[j] <= arr[swap_index]:
                break
            # 表示的是需要插入的的那个数字要小一点，就交换位置
            if arr[j] > arr[swap_index]:
                t = arr[swap_index]
                arr[swap_index] = arr[j]
                arr[j] = t
                swap_index -= 1
            j -= 1


if __name__ == "__main__":
    a = [random.randint(0, 10000000) for x in range(1, 1000000)]
    insert_sort2(a)
    print(a)
