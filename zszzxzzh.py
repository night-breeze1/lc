#907. 子数组的最小值之和v
'''
给定一个整数数组 arr，找到 min(b) 的总和，其中 b 的范围为 arr 的每个（连续）子数组。
由于答案可能很大，因此 返回答案模 10^9 + 7 。
'''
class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        #超时
        MOD = 10**9+7
        sum = 0
        for i in range(len(arr)):
            a = []
            for j in arr:
                a.append(j)
                if len(a) == i+1:
                    sum += min(a)
                    del a[0]
        return sum%MOD




if __name__ == '__main__':
    q = Solution().sumSubarrayMins(arr = [3,1,2,4])
    print(q)

'''
示例 1：
输入：arr = [3,1,2,4]
输出：17
解释：
子数组为 [3]，[1]，[2]，[4]，[3,1]，[1,2]，[2,4]，[3,1,2]，[1,2,4]，[3,1,2,4]。 
最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。
示例 2：
输入：arr = [11,81,94,43,3]
输出：444
'''
'''
这个问题可以使用单调栈来解决。单调栈是一种特殊的栈，它的特点是栈中的元素是单调递增或递减的。
在这个问题中，我们可以使用一个单调递减的栈来存储数组中的元素的索引。这样，当遇到一个新的元素时，
如果它小于栈顶元素对应的值，那么就可以确定栈顶元素是一个子数组的最小值，然后将其弹出栈，直到栈为空或者栈顶元素对应的值大于新元素。
然后将新元素的索引压入栈中。最后，栈中剩下的元素对应的值就是所有子数组的最小值。
def sumSubarrayMins(arr):
    MOD = 10**9 + 7  # 定义模数为10^9+7
    N = len(arr)  # 获取数组长度

    stack = []  # 初始化栈
    prev = [0]*N  # 初始化前驱数组，用于存储每个元素左边第一个比它小的元素的索引
    for i in range(N):  # 遍历数组
        while stack and arr[i] <= arr[stack[-1]]:  # 如果栈不为空且当前元素小于等于栈顶元素
            stack.pop()  # 弹出栈顶元素
        prev[i] = stack[-1] if stack else -1  # 更新前驱数组
        stack.append(i)  # 将当前元素的索引入栈

    stack = []  # 重新初始化栈
    next_ = [0]*N  # 初始化后继数组，用于存储每个元素右边第一个比它小的元素的索引
    for k in range(N-1, -1, -1):  # 从数组末尾开始遍历
        while stack and arr[k] < arr[stack[-1]]:  # 如果栈不为空且当前元素小于栈顶元素
            stack.pop()  # 弹出栈顶元素
        next_[k] = stack[-1] if stack else N  # 更新后继数组
        stack.append(k)  # 将当前元素的索引入栈

    return sum((i - prev[i]) * (next_[i] - i) * arr[i] for i in range(N)) % MOD  # 计算子数组最小值之和并取模


在这段代码中，prev数组用于存储每个元素左边第一个比它小的元素的索引，next_数组用于存储每个元素右边第一个比它小的元素的索引。
然后，对于每个元素，计算以它为最小值的子数组的数量，并将其乘以该元素的值，最后将所有的结果相加，得到最终的答案。
'''
'''
class Solution:
    def sumSubarrayMins(self, arr):
        MOD = 10**9 + 7
        N = len(arr)
        left, right = [0] * N, [0] * N
        stack = []
        for i in range(N):
            while stack and arr[i] <= arr[stack[-1]]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        stack = []
        for i in range(N - 1, -1, -1):
            while stack and arr[i] < arr[stack[-1]]:
                stack.pop()
            right[i] = stack[-1] if stack else N
            stack.append(i)
        return sum((i - left[i]) * (right[i] - i) * arr[i] for i in range(N)) % MOD

'''