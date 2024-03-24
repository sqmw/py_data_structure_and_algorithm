"""@线性查找"""

"""
list 的第一个值为哨兵
"""


def line_search(s: list, d: float):
    if len(s)<1:
        return -1
    else:
        s[0] = d
        for i in range(len(s) - 1, 0, -1):
            if s[i] == d:
                return i



if __name__ == '__main__':
    print(line_search([-1, 1, 2, 3, 4, 5, 6, 67, 7, 8, 89], 89))
