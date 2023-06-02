"""实现了插入排序"""
import random

"""插入排序就是每次取出一个插入到有序的序列中"""
"""都是升序排序"""


def insert_sort(arr):
    length = len(arr)
    # 依次取出 [1, n)
    for index_after in range(1, length):
        move_val = arr[index_after]
        # 找到现在需要插入的这个数字的位置
        set_pos = 0
        for index_before in range(0, index_after):
            # 表示取出来的数字比第一个数字还小
            if arr[index_after] < arr[0]:
                set_pos = 0
            # 表示找到了
            elif (arr[index_after] >= arr[index_before] and index_before + 1 >= index_after) or (
                    arr[index_before] <= arr[index_after] < arr[index_before + 1]):
                set_pos = index_before + 1
        for k in range(0, index_after - set_pos):
            arr[index_after - k] = arr[index_after - k - 1]
        arr[set_pos] = move_val


if __name__ == "__main__":
    a = [random.randint(1, 100000) for x in range(1, 100)]
    insert_sort(a)
    print(a)
