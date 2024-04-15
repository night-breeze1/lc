#重复的DNA序列v
'''
DNA序列 由一系列核苷酸组成，缩写为 'A', 'C', 'G' 和 'T'.。
例如，"ACGAATTCCG" 是一个 DNA序列 。
在研究 DNA 时，识别 DNA 中的重复序列非常有用。
给定一个表示 DNA序列 的字符串 s ，返回所有在 DNA 分子中出现不止一次的 长度为 10 的序列(子字符串)。你可以按 任意顺序 返回答案。
'''

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        '''
        b = ''
        a = []
        c = []
        for i in range(len(s)):
            for j in s[i:i+10:1]:
                b += j
                if b in a and b not in c:
                    c.append(b)
            a.append(b)
            b = ''
        return c        
        '''
        #56ms
        a = ''
        b = {}
        c = []
        for i in range(len(s)):
            a = s[i:i+10]
            if len(a) == 10:
                b[a] = b.get(a, 0) + 1
        for i,j in b.items():
            if j > 1:
                c.append(i)
        return c





if __name__ == '__main__':
    q =Solution().findRepeatedDnaSequences(s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
    print(q)
'''
示例 1：
输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
输出：["AAAAACCCCC","CCCCCAAAAA"]
示例 2：
输入：s = "AAAAAAAAAAAAA"
输出：["AAAAAAAAAA"]
'''
'''#32ms
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        l=len(s)
        d={}
        chi=10
        ans=[]
        for i in range(l-chi+1):

            temp=s[i:i+chi]
            #print(d,temp)
            if d.get(temp,0)==0:
                d[temp]=1
            elif d.get(temp,0)==1:
                ans.append(temp)
                d[temp]+=1
        return ans
'''