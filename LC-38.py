# https://leetcode-cn.com/problems/count-and-say/
"""
给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。

注意：整数序列中的每一项将表示为一个字符串。

「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
第一项是数字 1

描述前一项，这个数是 1 即 “一个 1 ”，记作 11

描述前一项，这个数是 11 即 “两个 1 ” ，记作 21

描述前一项，这个数是 21 即 “一个 2 一个 1 ” ，记作 1211

描述前一项，这个数是 1211 即 “一个 1 一个 2 两个 1 ” ，记作 111221
"""
n = int(input()) # 第n个
next_item = "1" # 下一个元素

for i in range(n-1):
    # print(next_item)
    item = next_item # 当前需要分析的数
    next_item = '' # 下一个元素
    count = 1 # 计数
    j = 0 # 索引
    L = len(item) # 长度
    while j < L: # 遍历字符串
        while j < L - 1 and item[j] == item[j+1]:
            count += 1
            j = j + 1
        j = j + 1
        next_item += str(count) + str(item[j-1])
        count = 1

print(next_item)   