#切割后面积最大的蛋糕v
'''
矩形蛋糕的高度为 h 且宽度为 w，给你两个整数数组 horizontalCuts 和 verticalCuts，其中：
 horizontalCuts[i] 是从矩形蛋糕顶部到第  i 个水平切口的距离
verticalCuts[j] 是从矩形蛋糕的左侧到第 j 个竖直切口的距离
请你按数组 horizontalCuts 和 verticalCuts 中提供的水平和竖直位置切割后，请你找出 面积最大 的那
份蛋糕，并返回其 面积 。由于答案可能是一个很大的数字，因此需要将结果 对 109 + 7 取余 后返回。
'''

class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        horizontalCuts.append(h)
        verticalCuts.append(w)
        horizontalCuts.sort()
        verticalCuts.sort()
        b = 0
        c = 0
        for i in range(len(horizontalCuts)):
            b = max(horizontalCuts[i]-horizontalCuts[i-1],b,horizontalCuts[0])
        for j in range(len(verticalCuts)):
            c = max(verticalCuts[j]-verticalCuts[j-1],verticalCuts[0],c)
        return b*c%(10**9+7)
if __name__ == '__main__':
    a = Solution().maxArea(h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3])
    print(a)




'''

示例 1：
输入：h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
输出：4 
解释：上图所示的矩阵蛋糕中，红色线表示水平和竖直方向上的切口。切割蛋糕后，绿色的那份蛋糕面积最大。
示例 2：
输入：h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
输出：6
解释：上图所示的矩阵蛋糕中，红色线表示水平和竖直方向上的切口。切割蛋糕后，绿色和黄色的两份蛋糕面积最大。
示例 3：
输入：h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
输出：9
'''