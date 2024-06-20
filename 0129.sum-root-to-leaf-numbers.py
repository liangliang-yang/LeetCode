#
# @lc app=leetcode id=129 lang=python
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.


# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = []
        res = 0
        if root:
            stack.append(root)

        while stack: # 用 stack根本目的是为了loop tree 更新节点value
            # node = stack.pop() # DFS=pop(), BFS=pop(-1)
            node = stack.pop(0)# 这里用 BFS/DFS 都可以

            # 叶节点此时的value=整个path从上到下的value
            if not node.left and not node.right: #叶节点
                res += node.val

            # 如果当前节点有右面， 比如 1->3, 那么就把 3 的节点 value更新为 13
            # 如果是 1->3->5, 那么就先更新3为13， 然后更新5为 13x10+5=135
            # 最后添加叶节点的 value
            if node.right:
                node.right.val += node.val*10
                stack.append(node.right)

            if node.left: # left 类似
                node.left.val += node.val*10
                stack.append(node.left)
        return res



# @lc code=end

