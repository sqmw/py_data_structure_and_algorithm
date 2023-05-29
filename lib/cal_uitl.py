from typing import Union


def cal_by_char_num2(a: Union[int, float, str], b: Union[int, float, str], operator: str):
    if operator == '+':
        return float(a) + float(b)
    elif operator == '-':
        return float(a) - float(b)
    elif operator == '*':
        return float(a) * float(b)
    elif operator == '/':
        if float(b) == 0:
            raise ZeroDivisionError
        return float(a) / float(b)
