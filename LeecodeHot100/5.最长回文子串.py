# 方法一：双指针中心扩展法，时间复杂度为 O(n^2)
# 使用嵌套函数，兼具实用性与可维护性
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n<2:
            return s

        # 定义从中间向两边扩散的函数
        def expand(left:int, right:int) -> tuple:
            while(left >= 0 and right < n and s[left]==s[right]):
                left -= 1
                right +=1
            return (left+1, right-1)

        start, end = 0,0     # 对应expand函数的两个输入值left right
        for i in range(n):
            # 同一个中心位置可能同时产生奇数长度和偶数长度的回文，它们是完全不同的子串，所以需要同时处理两种可能得字符串
            # 奇数长度回文
            l1,r1 = expand(i,i)
            # 偶数长度回文
            l2,r2 = expand(i,i+1)
            # 更新最长回文
            if r1-l1>end-start:
                start, end = l1, r1
            if r2-l2>end-start:
                start, end = l2, r2

        return s[start: end+1]
# 还有动态规划法（DP），还没学