# 方法一：数学映射法。来自破站up
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n = 2 * numRows - 2  # 一个周期的元素个数
        res = [""] * numRows  # 每一行的输出元素列表
        for i, element in enumerate(s):
            x = i % n
            res[min(x, n - x)] = element + res[min(x, n - x)]
        return "".join(res)
# crtl + alt + L一键规范字符


# 方法二：矩阵模拟法。来自leecode官方，比方法一慢很多，因为创建了一个较大的矩阵
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n, r = len(s), numRows
        if r == 1 or r >= n:
            return s
        t = r * 2 - 2
        c = (n + t - 1) // t * (r - 1)
        mat = [[''] * c for _ in range(r)]
        x, y = 0, 0
        for i, ch in enumerate(s):
            mat[x][y] = ch
            if i % t < r - 1:
                x += 1  # 向下移动
            else:
                x -= 1
                y += 1  # 向右上移动
        return ''.join(ch for row in mat for ch in row if ch)