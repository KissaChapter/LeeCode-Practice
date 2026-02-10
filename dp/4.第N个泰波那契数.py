# 方法一：滚轮数组法
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        p, q, r, sum = 0, 1, 1, 2
        for i in range(4, n + 1):
            p, q, r = q, r, sum
            sum = p + q + r
        return sum

#测试用例
solution = Solution()
a = solution.tribonacci(4)
print(a)