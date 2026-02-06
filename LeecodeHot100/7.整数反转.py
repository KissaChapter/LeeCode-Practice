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


# 方法二：leecode官方题解。没有使用 abs函数，模拟的是底层原理，对语言没有依赖性
class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
        rev = 0
        while x != 0:
            # 检查是否会溢出
            if rev > INT_MAX // 10:
                return 0
            if rev < INT_MIN // 10:
                return 0

            # 处理Python的负数取余问题：
            # 处理Python与其他语言（如C++/Java）在负数取余和除法运算上的差异
            digit = x % 10
            if x < 0 and digit > 0:
                digit -= 10
            # 更新x和rev
            x = (x - digit) // 10  # 这样处理可以正确处理负数
            rev = rev * 10 + digit
        return rev