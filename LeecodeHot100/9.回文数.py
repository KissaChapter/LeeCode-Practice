# -2 ** 31 <= x <= 2 ** 31 - 1
# 给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false
# 进阶：你能不将整数转为字符串来解决这个问题吗？

# 方法一：
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        if x_str[::-1] == x_str:
            return True
        else:
            return False


# 方法二：还可以更简洁
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) ==  str(x)[::-1]