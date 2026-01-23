from typing import List     # py3.8之前使用的是 导入+List 的方式，3.9后使用的是 不导入+list 的方式

# Ctrl+/一键注释

# 先尝试暴力，运行后有报错
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         n = len(nums)
#         for i in range(n):
#             for j in range(i+1,n):
#                 if nums[i]+nums[j] == target:
#                     return [i,j]
#         return []


# 哈希表
# 看了哈希的讲解，对于它在数据结构上的应用有了进一步认识
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for 
