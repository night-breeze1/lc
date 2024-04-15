#无重复字符的最长子串v
'''
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        a = []
        b = []
        for i in range(len(s)):
            a.append(s[i])
            for j in s[i+1::]:
                if j not in a:
                    #print(j)
                    a.append(j)
                else:
                    break
            b.append(len(a))
            a = []
            return max(b)
        '''
        i = 0
        m = 0
        left = 0
        a = []
        while i<len(s):
            if s[i] not in a:
                a.append(s[i])
                m = max(m,i-left+1)
                i += 1
            else:
                a.remove(s[left])
                left +=1
        return m
if __name__ == '__main__':
    q =Solution().lengthOfLongestSubstring(s = "pwwkew")
    print(q)

'''
示例 1:
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''
'''
滑动窗口
Python
思路：
这道题主要用到思路是：滑动窗口
什么是滑动窗口？
其实就是一个队列,比如例题中的 abcabcbb，进入这个队列（窗口）为 abc 满足题目要求，当再进入 a，队列变成了 abca，这时候不满足要求。所以，我们要移动这个队列！
如何移动？
我们只要把队列的左边的元素移出就行了，直到满足题目要求！
一直维持这样的队列，找出队列出现最长的长度时候，求出解！
时间复杂度：O(n)O(n)O(n)
代码：
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:max_len = cur_len
            lookup.add(s[i])
        return max_len
下面介绍关于滑动窗口的万能模板,可以解决相关问题,相信一定可以对滑动窗口有一定了解!
模板虽好,还是少套为好!多思考!更重要!
还有类似题目有:
3. 无重复字符的最长子串
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict
        lookup = defaultdict(int)
        start = 0
        end = 0
        max_len = 0
        counter = 0
        while end < len(s):
            if lookup[s[end]] > 0:
                counter += 1
            lookup[s[end]] += 1
            end += 1
            while counter > 0:
                if lookup[s[start]] > 1:
                    counter -= 1
                lookup[s[start]] -= 1
                start += 1
            max_len = max(max_len, end - start)
        return max_len
'''