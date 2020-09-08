# https://leetcode-cn.com/problems/factorial-trailing-zeroes/
"""
给定一个整数 n，返回 n! 结果尾数中零的数量。

示例 1:

输入: 3
输出: 0
解释: 3! = 6, 尾数中没有零。
示例 2:

输入: 5
输出: 1
解释: 5! = 120, 尾数中有 1 个零.
说明: 你算法的时间复杂度应为 O(log n) 
"""
class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        while n > 0: # n = 25, 5
            n //= 5 # 5, 1
            res += n # +5, +1
        return res

def fact(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

s = Solution()
for i in range(1, 31):
    print(i, "! =", fact(i), s.trailingZeroes(i))        