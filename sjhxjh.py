# 705. 设计哈希集合v
'''
不使用任何内建的哈希表库设计一个哈希集合（HashSet）。
实现 MyHashSet 类：
void add(key) 向哈希集合中插入值 key 。
bool contains(key) 返回哈希集合中是否存在这个值 key 。
void remove(key) 将给定值 key 从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。
'''


class MyHashSet(object):

    def __init__(self):
        self.set = set()

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.set.add(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key not in self.set:
            return
        self.set.remove(key)

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        if key in self.set:
            return True
        else:
            return False


if __name__ == '__main__':
    myHashSet = MyHashSet()

    myHashSet.add(1)  # set = [1]

    myHashSet.add(2)  # set = [1, 2]

    c = myHashSet.contains(1)  # 返回True
    print(c)

    myHashSet.contains(3)  # 返回False ，（未找到）

    myHashSet.add(2)  # set = [1, 2]

    myHashSet.contains(2)  # 返回True

    myHashSet.remove(2)  # set = [1]

    myHashSet.contains(2)  # 返回False ，（已移除）
    print(myHashSet.set)

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
