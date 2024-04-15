# 706. 设计哈希映射v
'''
不使用任何内建的哈希表库设计一个哈希映射（HashMap）。
实现 MyHashMap 类：
MyHashMap() 用空映射初始化对象
void put(int key, int value) 向 HashMap 插入一个键值对 (key, value) 。如果 key 已经存在于映射中，则更新其对应的值 value 。
int get(int key) 返回特定的 key 所映射的 value ；如果映射中不包含 key 的映射，返回 -1 。
void remove(key) 如果映射中存在 key 的映射，则移除 key 和它所对应的 value 。
'''


class MyHashMap(object):

    def __init__(self):
        self.map = {}

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.map[key] = value

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.map:
            return -1
        return self.map.get(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key not in self.map:
            return self.map
        self.map.pop(key)


if __name__ == '__main__':
    myHashMap = MyHashMap()
    myHashMap.put(1, 1)  # myHashMap现在为[[1, 1]]
    print(myHashMap.map)
    myHashMap.put(2, 2)  # myHashMap现在为[[1, 1], [2, 2]]
    myHashMap.get(1)  # 返回1 ，myHashMap现在为[[1, 1], [2, 2]]
    myHashMap.get(3)  # 返回 - 1（未找到），myHashMap现在为[[1, 1], [2, 2]]
    myHashMap.put(2, 1)  # myHashMap现在为[[1, 1], [2, 1]]（更新已有的值）
    myHashMap.get(2)  # 返回1 ，myHashMap现在为[[1, 1], [2, 1]]
    print(myHashMap.map)
    myHashMap.remove(2)  # 删除键为2的数据，myHashMap现在为[[1, 1]]
    myHashMap.get(2)  # 返回 - 1（未找到），myHashMap现在为[[1, 1]]
    print(myHashMap.map)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
