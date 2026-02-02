# 方法一：数学映射法。来自破站up
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n = 2 * numRows - 2  # 一个周期的元素个数
        res = [""] * numRows  # 每一行的输出元素列表
        for i, element in enumerate(s):
            x = i % n
            res[min(x, n - x)] = res[min(x, n - x)] + element
            # 注意不能写成 res[min(x, n - x)] = element + res[min(x, n - x)]！字符串会反向拼接
        return "".join(res)
# crtl + alt + L一键规范字符


# 方法二：矩阵模拟法。来自leecode官方，比方法一慢很多，因为创建了一个较大的矩阵
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n, r = len(s), numRows
        if r == 1 or r >= n:
            return s
        t = r * 2 - 2       # 和上面的方法原理一样，都是计算一个周期的元素个数
        c = (n + t - 1) // t * (r - 1)      # 总列数 = 周期数 × 每周期列数 = ceil(n / t) × (r-1)
        '''每个周期占据 (r-1) 列
        向下走：占1列（垂直列）
        向上走：占(r-2)列（斜线）
        总计：1 + (r-2) = r-1 列
        周期数 = ceil(n / t) = (n + t - 1) // t
        总列数 = 周期数 × 每周期列数 = ceil(n / t) × (r-1)
        '''
        # 这里内层函数生成的是一个 c列的列表，外层函数将其组合成 r行矩阵
        mat = [[''] * c for _ in range(r)]
        '''_是虚拟变量，作用同i用于循环。
        第1次循环: _=0  →  生成 ['', '', '', '']   (第0行，4个元素)
        第2次循环: _=1  →  生成 ['', '', '', '']   (第1行，4个元素)  
        第3次循环: _=2  →  生成 ['', '', '', '']   (第2行，4个元素)
        最终 mat = [
            ['', '', '', ''],  # 第0行，长度4 (c列)
            ['', '', '', ''],  # 第1行，长度4 (c列)
            ['', '', '', '']   # 第2行，长度4 (c列)
        ]'''
        x, y = 0, 0
        for i, ch in enumerate(s):
            mat[x][y] = ch
            if i % t < r - 1:
                x += 1  # 向下移动
            else:
                x -= 1
                y += 1  # 向右上移动
        return ''.join(ch for row in mat for ch in row if ch)