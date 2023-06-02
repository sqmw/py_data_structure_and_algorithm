"""
这里实现了KMP算法
next 数组表示的是 j 的下标
"""


def kmp_match(pattern_str, text_str) -> int:
    next_arr = get_next_arr(pattern_str)
    i = 0
    j = 0
    while True:
        if pattern_str[j] == text_str[i]:
            # 匹配成功
            if j + 1 == len(pattern_str):
                return i - j
            i += 1
            j += 1
        else:
            if i + 1 == len(text_str):
                return -1
            if j == 0:
                i += 1
            else:
                j = next_arr[j]


def get_max_common_pre_post_fix_len(s: str) -> int:
    for i in range(1, len(s)):
        # 从最长的开始到最短
        if s[:len(s)] == s[i:]:
            return len(s) - i
    return 0


# 用来计算移动的对应位置，我这里计算的是text里面的指针移动的长度，如果对应的 i 号 pattern 没有匹配上
# text文本的指针就下移 pattern[i] 个位置，指针此时继续指着text串的原先位置
# 因为未执行相对的原因，text的指针下移对应的就是 pattern 指针后移
def get_next_arr(pattern_str) -> tuple:
    next_arr = [-1, ]
    for i in range(1, len(pattern_str)):
        next_arr.append(get_max_common_pre_post_fix_len(pattern_str[:i]))
    return tuple(next_arr)


patterns_texts = [(("hello", "hello world"), ("world", "hello world")),
                  (("apple", "I love apples"), ("banana", "I really want a banana"),
                   ("pear", "I enjoyed eating pears yesterday")),
                  (("blue", "the sky is blue"), ("green", "the leaves on the trees are green"),
                   ("red", "I like to wear red clothes")),
                  (("cat", "I have a cat and a dog at home"), ("dog", "I love playing with my dog outside"),
                   ("hamster", "I used to have a pet hamster")),
                  (("football", "I'm going to play football tomorrow"),
                   ("basketball", "My favorite sport is basketball"),
                   ("baseball", "I don't know how to play baseball very well"))]

# 遍历所有的元组，获取模式串和主串
for patterns_text in patterns_texts:
    for pattern, text in patterns_text:
        print(kmp_match(pattern, text), text.find(pattern))
