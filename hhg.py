#环和杆v
'''
总计有 n 个环，环的颜色可以是红、绿、蓝中的一种。这些环分别穿在 10 根编号为 0 到 9 的杆上。
给你一个长度为 2n 的字符串 rings ，表示这 n 个环在杆上的分布。rings 中每两个字符形成一个 颜色位置对 ，用于描述每个环：
第 i 对中的 第一个 字符表示第 i 个环的 颜色（'R'、'G'、'B'）。
第 i 对中的 第二个 字符表示第 i 个环的 位置，也就是位于哪根杆上（'0' 到 '9'）。
例如，"R3G2B1" 表示：共有 n == 3 个环，红色的环在编号为 3 的杆上，绿色的环在编号为 2 的杆上，蓝色的环在编号为 1 的杆上。
找出所有集齐 全部三种颜色 环的杆，并返回这种杆的数量。
'''
class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        num = {}
        count = 0
        ring = zip(rings[0::2],rings[1::2])
        for i,j in ring:
            num.setdefault(j, []).append(i)
        for i,j in num.items():
            a = list(set(j))#去重
            if a ==['B','G','R'] or a ==['B','R','G'] or a==['R','G','B'] or a==['G','B','R'] or a==['G','R','B'] or a==['R','B','G']:
                count += 1
        return count
if __name__ == '__main__':
    q = Solution().countPoints("G7G9R4B0G6R1R9R5B8R4G4B4R6B4B1G2B9G5B6G5")
    print(q)

'''
示例 1：
输入：rings = "B0B6G0R6R0R6G9"
输出：1
解释：
- 编号 0 的杆上有 3 个环，集齐全部颜色：红、绿、蓝。
- 编号 6 的杆上有 3 个环，但只有红、蓝两种颜色。
- 编号 9 的杆上只有 1 个绿色环。
因此，集齐全部三种颜色环的杆的数目为 1 。
示例 2：
输入：rings = "B0R0G0R9R0B0G0"
输出：1
解释：
- 编号 0 的杆上有 6 个环，集齐全部颜色：红、绿、蓝。
- 编号 9 的杆上只有 1 个红色环。
因此，集齐全部三种颜色环的杆的数目为 1 。
示例 3：
输入：rings = "G4"
输出：0
解释：
只给了一个环，因此，不存在集齐全部三种颜色环的杆。
'''