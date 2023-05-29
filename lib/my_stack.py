# 通过基本的类型实现的list
class MyNode:
    def __init__(self, data, _next):
        self.__data = data
        self.__next = _next

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


class MyStack:
    def __init__(self):
        self.__cur = None
        self.__len = 0
        # 当 __list 非 None的时候，我们表示的就是首节点
        self.__list = None
        # 指向栈的顶部的前一个元素的指针，需要再栈的长度 > 1 的时候我们才能让这个值非None
        self.__top_pre = None

    def __len__(self):
        return self.__len

    def __iter__(self):
        print("这里实现了 __iter__ ")
        # 这段代码不需要
        # self.__cur = None
        return self

    # 实现了从栈底开始遍历到栈顶
    def __next__(self):
        print("这里是 __next__ ")
        if self.__len == 0:
            return
        else:
            if self.__cur is None:
                self.__cur = self.__list
                return self.__cur.data
            else:
                self.__cur = self.__cur.next
                if self.__cur is None:
                    raise StopIteration
                return self.__cur.data

    def push(self, val):
        if self.__len == 0:
            self.__list = MyNode(data=val, _next=None)
            self.__top_pre = self.__list
        elif self.__len == 1:
            self.__list.next = MyNode(data=val, _next=None)
            self.__top_pre = self.__list
        else:
            self.__top_pre.next.next = MyNode(data=val, _next=None)
            self.__top_pre = self.__top_pre.next
        self.__len += 1

    def pop(self):
        val = self.__top_pre.next.data
        self.__top_pre.next = None
        return val

    def seek(self):
        return self.__top_pre.next.data


if __name__ == "__main__":
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    for item in stack:
        print(item)

    # print(next(stack))
    # print(next(stack))
    # print(next(stack))
    # print(next(stack))
    print(iter(stack))
