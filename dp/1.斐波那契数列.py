# 方法一：数组，空间复杂度高
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


# 方法二：leecode，空间复杂度为O(1)，滚轮数组法
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        p, q, sum = 0, 0, 1
        for i in range(2, n + 1):
            p, q = q, sum
            sum = p + q
        return sum


# 测试用例
solution = Solution()
a = solution.fib(12)
print(a)