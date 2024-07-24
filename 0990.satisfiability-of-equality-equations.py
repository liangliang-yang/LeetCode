#
# @lc app=leetcode id=990 lang=python
#
# [990] Satisfiability of Equality Equations
#

# @lc code=start

# https://leetcode.com/problems/satisfiability-of-equality-equations/editorial/
# https://algo.itcharge.cn/07.Tree/05.Union-Find/01.Union-Find/#_6-1-%E7%AD%89%E5%BC%8F%E6%96%B9%E7%A8%8B%E7%9A%84%E5%8F%AF%E6%BB%A1%E8%B6%B3%E6%80%A7


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
    def equationsPossible(self, equations):

        union_find = UnionFind(26) # 只有 26个字母
        # "a==b", 只有 4 chars, 都是小写字母
        for eqn in equations:
            if eqn[1] == "=":
                index1 = ord(eqn[0]) - ord('a')
                index2 = ord(eqn[3]) - ord('a')
                union_find.union(index1, index2)

        for eqn in equations:
            if eqn[1] == "!":
                index1 = ord(eqn[0]) - ord('a')
                index2 = ord(eqn[3]) - ord('a')
                if union_find.is_connected(index1, index2):
                    return False
        return True
        
# @lc code=end

