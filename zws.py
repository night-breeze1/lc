#寻找两个正序数组的中位数v
'''
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
算法的时间复杂度应该为 O(log (m+n)) 。
'''

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        num = nums1+nums2
        num.sort()
        s = m+n
        a = (s-1)//2
        if len(num) % 2 == 0:
            return (num[s//2]+num[(s//2)-1])/2.0
        else:
            return num[a]

if __name__ == '__main__':
    q = Solution().findMedianSortedArrays(nums1 = [1,2], nums2 = [3])
    print(q)
'''
示例 1：
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：
输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
'''