class Solution:
    def reverse(self, x: int) -> int:
        # 判断符号
        sign = -1 if x < 0 else 1
        x_str = str(abs(x))
        reverse = x_str[::-1]
        x_int = int(reverse) * sign
        # 判断范围
        # 这里使用先命名 INT_MIN/INT_MAX的方法会更快更方便修改
        if x_int > 2 ** 31 - 1 or x_int < -2 ** 31:
            return 0
        return x_int


# 示例1
solution = Solution()
x = solution.reverse(-817623276)
print(x)


# 方法二：leecode官方题解，解决了过程中可能越界、python和其他语言底层代码不兼容的问题
class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
        rev = 0

        while x != 0:
            # 例：-123 // 10 = -13，python整数除法向负无穷取整，如果不 +1 则将导致 int_min 附近的区域多了几个数，无法正确判断是否溢出
            if rev < INT_MIN // 10 + 1 or rev > INT_MAX // 10:
                return 0
            digit = x % 10      # 余数
            # Python3 的取模运算在x为负数时也会返回 [0, 9) 以内的结果，因此这里需要进行特殊判断
            if x < 0 and digit > 0:
                digit -= 10

            # 同理，Python3的整数除法在x为负数时会向下（更小的负数）取整，因此不能写成 x //= 10
            x = (x - digit) // 10
            rev = rev * 10 + digit
        return rev
