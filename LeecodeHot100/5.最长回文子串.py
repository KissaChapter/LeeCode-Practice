# 方法一：双指针中心扩展法，时间复杂度为 O(n^2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        def expand(left: int, right: int) -> tuple:
            """从中心向两边扩展，返回回文边界"""
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            # 循环结束时left和right已超出回文范围
            return left + 1, right - 1

        start, end = 0, 0

        for i in range(n):
            # 奇数长度回文（如"aba"）
            l1, r1 = expand(i, i)
            # 偶数长度回文（如"abba"）
            l2, r2 = expand(i, i + 1)

            # 更新最长回文
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]


# 还有动态规划法（DP），还没学