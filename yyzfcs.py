#统计范围内的元音字符串数v
'''
给你一个下标从 0 开始的字符串数组 words 和两个整数：left 和 right 。
如果字符串以元音字母开头并以元音字母结尾，那么该字符串就是一个 元音字符串 ，其中元音字母是 'a'、'e'、'i'、'o'、'u' 。
返回 words[i] 是元音字符串的数目，其中 i 在闭区间 [left, right] 内。
'''
class Solution(object):
    def vowelStrings(self, words, left, right):
        """
        :type words: List[str]
        :type left: int
        :type right: int
        :rtype: int
        """
        count = 0
        yuan = ['a','e','i','o','u']
        for i in words[left:right+1]:
            le = i[0]
            l = len(i)
            ri = i[l-1]
            if le in yuan and ri in yuan:
                count += 1
        return count

if __name__ == '__main__':
    q = Solution().vowelStrings(words = ["are","amy","u"], left = 0, right = 2)
    print(q)
'''
示例 1：
输入：words = ["are","amy","u"], left = 0, right = 2
输出：2
解释：
- "are" 是一个元音字符串，因为它以 'a' 开头并以 'e' 结尾。
- "amy" 不是元音字符串，因为它没有以元音字母结尾。
- "u" 是一个元音字符串，因为它以 'u' 开头并以 'u' 结尾。
在上述范围中的元音字符串数目为 2 。
示例 2：
输入：words = ["hey","aeo","mu","ooo","artro"], left = 1, right = 4
输出：3
解释：
- "aeo" 是一个元音字符串，因为它以 'a' 开头并以 'o' 结尾。
- "mu" 不是元音字符串，因为它没有以元音字母开头。
- "ooo" 是一个元音字符串，因为它以 'o' 开头并以 'o' 结尾。
- "artro" 是一个元音字符串，因为它以 'a' 开头并以 'o' 结尾。
在上述范围中的元音字符串数目为 3 。
'''