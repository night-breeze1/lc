#最长平衡子字符串v
'''
给你一个仅由 0 和 1 组成的二进制字符串 s 。
如果子字符串中 所有的 0 都在 1 之前 且其中 0 的数量等于 1 的数量，则认为 s 的这个子字符串是平衡子字符串。请注意，空子字符串也视作平衡子字符串。
返回  s 中最长的平衡子字符串长度。
子字符串是字符串中的一个连续字符序列。
'''
class Solution(object):
    def findTheLongestBalancedSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max = 0
        l = len(s)
        for i in range(l-1):
            if s[i] == '0' and s[i+1] == '1':
                count = 0
                left =i
                right = i+1
                while s[left] == '0' and s[right] == '1':
                    count += 2
                    if right >=l-1 or left-1<0:
                        break
                    else:
                        left -= 1
                        right += 1
                if count > max:
                    max = count
        return max
if __name__ == '__main__':
    q = Solution().findTheLongestBalancedSubstring(s = "001")
    print(q)

'''
示例 1：
输入：s = "01000111"
输出：6
解释：最长的平衡子字符串是 "000111" ，长度为 6 。
示例 2：
输入：s = "00111"
输出：4
解释：最长的平衡子字符串是 "0011" ，长度为  4 。
示例 3：
输入：s = "111"
输出：0
解释：除了空子字符串之外不存在其他平衡子字符串，所以答案为 0 。
'''