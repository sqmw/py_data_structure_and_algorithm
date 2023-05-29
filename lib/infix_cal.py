"""
这个是用来直接计算中缀表达式的
下面仅仅实现了求没有括号的表达式求职
"""
from typing import Union

from lib.stack import Stack
from lib.cal_uitl import cal_by_char_num2

operator_chars = ('+', '-', '*', '/')

_expression = (19.1, "+", "3", "-", 2, "*", "3", "/", "5", "+", "1")


# 实现了一个计算没有括号的表达式求值，我们这里的expression是一个列表，这个是用来求中缀表达式的，其实我们还需要一个函数，将我们的字符串类型的表达式转化成我们需要的Union[list,tuple]
def cal_without_parentheses(expression: Union[list, tuple] = _expression) -> float:
    # 消除表达式里面的空格
    # 将表达式存在一个list里面，方便取出来
    expression_list = expression
    stack = Stack()
    # 先处理 * 和 /
    i = 0
    while i < len(expression_list):
        # 其实这里使用四个 if-else就可以了
        if expression_list[i] == '/' or expression_list[i] == '*':
            pre_val = stack.pop()
            stack.push(cal_by_char_num2(pre_val, expression_list[i + 1], expression_list[i]))
            i += 2
        else:
            stack.push(expression_list[i])
            i += 1

    # 处理 + -
    i = 0
    expression_list = stack.get_stack_copy_list()
    stack.clear()
    while i < len(expression_list):
        if expression_list[i] == '+' or expression_list[i] == '-':
            pre_val = stack.pop()
            stack.push(cal_by_char_num2(pre_val, expression_list[i + 1], expression_list[i]))
            i += 2
        else:
            stack.push(expression_list[i])
            i += 1
    return stack.pop()


print(cal_without_parentheses(expression=_expression))
