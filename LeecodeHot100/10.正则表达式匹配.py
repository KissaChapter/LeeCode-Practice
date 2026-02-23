import re

# 方法一：直接调用正则表达式re库
# fullmatch方法返回值：匹配失败时，返回 None；匹配成功时，返回一个Match对象
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return re.fullmatch(p,s)


# 方法二：不用 re 库，用 DP
# 需要建立一个二维数组
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        # dp[i][j] 表示 s 的前 i 个字符和 p 的前 j 个字符是否匹配，初始值均为 false
        dp = [[False] * (n + 1) for _ in range(m + 1)]  # 从长度为 0 开始，所以需要加 1 到最大长度
        dp[0][0] = True     # 都是空字符串所以匹配成功

        # 处理 s 中的空字符串匹配 p 中的 a* 的情况，从 2 到 n
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]     # 这个赋值会传播 True 值

        # 填充DP表格
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 最后一个字符是 * 的情况：
                if p[j - 1] == '*':
                    # '*' 匹配0次
                    dp[i][j] = dp[i][j - 2]
                    # '*' 匹配1次或多次
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                else:
                    # 当前字符匹配
                    if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                        dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]