#
# @lc app=leetcode id=261 lang=python
#
# [261] Graph Valid Tree
#

# @lc code=start

# https://leetcode.com/problems/graph-valid-tree/editorial/
# https://leetcode.com/problems/graph-valid-tree/solutions/1791850/simple-python3-solution-with-union-by-rank-path-compression/

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
    def validTree(self, n, edges):
        # After union, if there is only one connected component and num_edges = num_vertices - 1, then
        # this is a valid tree and we return true, otherwise false

        count = n

        # Condition 1: The graph must contain n - 1 edges.
        if len(edges) != n - 1: return False
        
        # Condition 2: The graph must contain a single connected component.      
        unionFind = UnionFind(n) # Create a new UnionFind object with n nodes. 
        
        for A, B in edges: # Add each edge, if connected, count = count -1
            if not unionFind.union(A, B):
                return False
            else:
                count = count -1
        
        return count == 1
        
# @lc code=end

