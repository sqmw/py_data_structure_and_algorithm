class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def resole(arr):
    if not arr:
        return None

    # 创建根节点
    root = Node(arr[0])

    # 遍历数组中的每个元素，从第二个元素开始逐个插入二叉排序树
    for i in range(1, len(arr)):
        insert_node(root, arr[i])

    return root


def insert_node(root, value):
    # 插入节点到二叉排序树的递归函数
    if value < root.value:
        if root.left is None:
            root.left = Node(value)
        else:
            insert_node(root.left, value)
    elif value > root.value:
        if root.right is None:
            root.right = Node(value)
        else:
            insert_node(root.right, value)


if __name__ == '__main__':
    a = [10, 2, 3, 23, 2, 3, 4, 23, 4, 3, 43, 4]
    root = resole(a)
    print(sorted(a))

