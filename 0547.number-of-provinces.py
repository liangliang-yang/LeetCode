#
# @lc app=leetcode id=547 lang=python
#
# [547] Number of Provinces
#

# @lc code=start

# https://algo.itcharge.cn/07.Tree/05.Union-Find/01.Union-Find/#_6-2-%E7%9C%81%E4%BB%BD%E6%95%B0%E9%87%8F


class UnionFind:
    def __init__(self, n):                          # 初始化
        self.fa = {i:i for i in range(n)}           # 每个元素的集合编号初始化为数组 fa 的下标索引
    
    def find(self, x):                              # 查找元素根节点的集合编号内部实现方法
        if self.fa[x] != x:                         # 递归查找元素的父节点，直到根节点
            self.fa[x] = self.find(self.fa[x])      

        return self.fa[x]                                  

    def union(self, x, y):                          # 合并操作：令其中一个集合的树根节点指向另一个集合的树根节点
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:                        # x 和 y 的根节点集合编号相同，说明 x 和 y 已经同属于一个集合
            return False
        
        self.fa[root_x] = root_y                    # x 的根节点连接到 y 的根节点上，成为 y 的根节点的子节点
        return True

    def is_connected(self, x, y):                   # 查询操作：判断 x 和 y 是否同属于一个集合
        return self.find(x) == self.find(y)
    

class Solution(object):
    def findCircleNum(self, isConnected):
        size = len(isConnected)
        union_find = UnionFind(size)
        
        for i in range(size):
            for j in range(i + 1, size):
                if isConnected[i][j] == 1:
                    union_find.union(i, j)

        res = set()
        for i in range(size):
            res.add(union_find.find(i))
        return len(res)
        
# @lc code=end

