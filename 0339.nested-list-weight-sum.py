#
# @lc app=leetcode id=339 lang=python
#
# [339] Nested List Weight Sum
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

# https://leetcode.com/problems/nested-list-weight-sum/editorial/

class Solution(object):
    def depthSum(self, nestedList):
        
        q = [] # 存 [item, depth]
        res = 0

        for item in nestedList:
            q.append([item, 1]) # 开始的所有都是 depth=1

        while q:
            [x, depth] = q.pop(0) # pop(0) 为 BFS， 表示 pop最开始添加的
 
            if x.isInteger(): # x is NestedInteger object as integer
                res += depth * x.getInteger()
            else: # x is a nestedList
                for xi in x.getList():
                    q.append([xi, depth+1])
        
        return res
    

    
# @lc code=end

