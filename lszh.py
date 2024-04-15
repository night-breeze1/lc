#1. 两数之和v
"""给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出
和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        len = 0
        for i in nums:
            count = len+1
            for j in nums[count:]:
                if i + j == target:
                    return len,count
                else:
                    count += 1
            len += 1
if __name__=='__main__':
    q =Solution().twoSum(nums = [2,7,11,15], target=22)
    print(q)