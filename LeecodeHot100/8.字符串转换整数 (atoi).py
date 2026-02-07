# 方法一：来自b站
class Solution:
    def myAtoi(self, s: str) -> int:
        # 读入字符串并丢弃无用的前导空格（" "）
        n = len(s)
        i = 0

        while i < n and s[i] == ' ':
            i += 1
        if i == n:
            return 0
        # 检查下一个字符（假设还未到字符末尾）为 '-' 还是 '+'。如果两者都不存在，则假定结果为正
        flag = 1
        if s[i] == '-':
            flag = -1
        if s[i] == '-' or s[i] == '+':
            i += 1
        # 通过跳过前置零来读取该整数，直到遇到非数字字符或到达字符串的结尾。如果没有读取数字，则结果为 0。
        ans = 0
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 -1
        while i < n and '0' <= s[i] <= '9':
            ans = int(s[i]) + ans * 10
            i += 1
            # 如果整数数超过 32 位有符号整数范围 [−2**31,  2**31 − 1] ，需要截断这个整数，使其保持在这个范围内。
            # 具体来说，小于 −2**31 的整数应该被舍入为 −2**31 ，大于 2**31 − 1 的整数应该被舍入为 2**31 − 1
            if ans > INT_MAX:
                break

        ans = ans * flag
        if ans < INT_MIN:
            return INT_MIN
        elif ans > INT_MAX:
            return  INT_MAX
        else:
            return ans


# 方法二：deepseek优化版本
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  # 更简洁的去空格方式
        if not s:   # 检查字符串是否为空
            return 0

        flag = 1
        if s[0] in ('-', '+'):
            flag = -1 if s[0] == '-' else 1
            s = s[1:]   # 如果字符串是 "123"（没有符号），s[0] 是 '1'，不在 ('-', '+') 中，则不会执行 s = s[1:]

        ans = 0
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
        limit = INT_MAX if flag == 1 else -INT_MIN

        for ch in s:
            if not ch.isdigit():    # 检查字符是否是数字（0-9），返回 true或者false
                break
            #可以换成：if not ('0' <= ch <= '9'):
                # break
            digit = int(ch)
            # 事前预防（反转整数的逻辑），在运算过程中就判断是否溢出 并溢出截断，而不是最后返回时才判断是否截断
            if ans > (limit - digit) // 10:
                return INT_MAX if flag == 1 else INT_MIN
            ans = ans * 10 + digit

        return min(max(ans * flag, INT_MIN), INT_MAX)

'''    isdigit()的用法：
'5'.isdigit()   # True
'a'.isdigit()   # False
' '.isdigit()   # False
'+'.isdigit()   # False
'Ⅳ'.isdigit()   # True（罗马数字4，但在Python中也被认为是数字）
'''