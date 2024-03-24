import random


def merge(arr1, arr2) -> list:
    arr = []
    i, j = 0, 0
    while len(arr) < len(arr1) + len(arr2):
        if arr1[i] <= arr2[j] and i < len(arr1):
            arr.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j] and j < len(arr2):
            arr.append(arr2[j])
            j += 1
        while i < len(arr1):
            arr.append(arr1[i])
            i += 1
        while j < len(arr2):
            arr.append(arr2[j])
            j += 1
    return arr


def merge_sort(arr):
    print(1)


if __name__ == '__main__':
    arr = random.sample(range(10), 10)  # 生成一个随机数组
    print("原始数组:", arr)
