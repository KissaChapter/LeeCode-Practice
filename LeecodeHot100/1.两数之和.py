from typing import List     # py3.8之前使用的是 导入+List 的方式，3.9后使用的是 不导入+list 的方式

# Ctrl+/一键注释

# 方法一：暴力，运行后有报错
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j] == target:
                    return [i,j]
        return []


# 方法二：计算补数+单切片
# 比方法一速度快一倍
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            j = target - i
            start_index = nums.index(i)
            next_index = start_index+1
            temp_nums = nums[next_index:]
            if j in temp_nums:
                return (nums.index(i),next_index + temp_nums.index(j))


# 方法三：哈希表
# 步骤如下：
# 1. 创建一个空的哈希表。
# 2. 遍历数组，对于每个元素：
#    a. 计算所需补数 = 目标值 - 当前值。
#    b. 检查补数是否已在哈希表中。
#    c. 如果在，返回 [哈希表中补数的索引, 当前索引]。
#    d. 如果不在，将当前值及其索引存入哈希表。
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement not in dic:
                dic[nums[i]] = i
            else:
                return [dic[target-nums[i]],i]


# 方法四：哈希表+枚举
#  leecode官方
class Solution:
    def twoSum(self, nums:List[int], target:int) -> List[int]:
        dic = {}
        for i,num in enumerate(nums):
            if target-nums[i] not in dic:
                dic[nums[i]] = i
            else:
                return [dic[target - nums[i]],i]