class Stack:
    def __init__(self):
        self.__container = []

    def pop(self):
        return self.__container.pop()

    def push(self, val):
        self.__container.append(val)

    def seek(self):
        return self.__container[len(self.__container)]

    def is_empty(self) -> bool:
        return len(self.__container) == 0

    def get_stack_copy_list(self):
        return self.__container.copy()

    def clear(self) -> bool:
        try:
            self.__container.clear()
        except Exception as e:
            return False
        return True

    def __len__(self):
        return len(self.__container)
