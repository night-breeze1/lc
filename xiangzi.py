#根据规则将箱子分类v
'''
给你四个整数 length ，width ，height 和 mass ，分别表示一个箱子的三个维度和质量，请你返回一个表示箱子 类别 的字符串。

如果满足以下条件，那么箱子是 "Bulky" 的：
箱子 至少有一个 维度大于等于 104 。
或者箱子的 体积 大于等于 109 。
如果箱子的质量大于等于 100 ，那么箱子是 "Heavy" 的。
如果箱子同时是 "Bulky" 和 "Heavy" ，那么返回类别为 "Both" 。
如果箱子既不是 "Bulky" ，也不是 "Heavy" ，那么返回类别为 "Neither" 。
如果箱子是 "Bulky" 但不是 "Heavy" ，那么返回类别为 "Bulky" 。
如果箱子是 "Heavy" 但不是 "Bulky" ，那么返回类别为 "Heavy" 。
'''
class Solution(object):
    def categorizeBox(self, length, width, height, mass):
        """
        :type length: int
        :type width: int
        :type height: int
        :type mass: int
        :rtype: str
        """
        a = "Bulky"
        b = "Heavy"
        c = "Both"
        d = "Neither"
        if length>=10**4 or width>=10**4 or height>=10**4 or length * width * height >=10**9:
            if mass>=100:
                return c
            else:
                return a
        elif mass>=100:
                return b
        else:
            return d
if __name__ == '__main__':
    a = Solution().categorizeBox(length = 1000,width = 35,height = 700,mass = 300)
    print(a)