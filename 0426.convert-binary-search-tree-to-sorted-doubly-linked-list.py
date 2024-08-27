#
# @lc app=leetcode id=426 lang=python
#
# [426] Convert Binary Search Tree to Sorted Doubly Linked List
#
# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/description/
#
# algorithms
# Medium (64.84%)
# Likes:    2615
# Dislikes: 215
# Total Accepted:    300.1K
# Total Submissions: 462.4K
# Testcase Example:  '[4,2,5,1,3]'
#
# Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in
# place.
# 
# You can think of the left and right pointers as synonymous to the predecessor
# and successor pointers in a doubly-linked list. For a circular doubly linked
# list, the predecessor of the first element is the last element, and the
# successor of the last element is the first element.
# 
# We want to do the transformation in place. After the transformation, the left
# pointer of the tree node should point to its predecessor, and the right
# pointer should point to its successor. You should return the pointer to the
# smallest element of the linked list.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: root = [4,2,5,1,3]
# 
# 
# Output: [1,2,3,4,5]
# 
# Explanation: The figure below shows the transformed BST. The solid line
# indicates the successor relationship, while the dashed line means the
# predecessor relationship.
# 
# 
# 
# Example 2:
# 
# 
# Input: root = [2,1,3]
# Output: [1,2,3]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000
# All the values of the tree are unique.
# 
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS in-order traversal solution
class Solution_DFS(object):
    def treeToDoublyList(self, root):
        if not root:
            return
        
        res = [] # List to save in-order nodes from DFS traversal
        self.dfs(root, res)

        # at this moment, res=[1, 2, 3, 4, 5], need to create double-linked
        for i in range(len(res) - 1):
            res[i].right = res[i + 1] # add right link
            res[i + 1].left = res[i] # add left link
        
        res[-1].right = res[0] # add right for the last element
        res[0].left = res[-1] # add left for the first element

        # return head
        return res[0]
    
    def dfs(self, root, res): # in-order traversal
        if root:
            self.dfs(root.left, res)
            res.append(root) # not root.val
            self.dfs(root.right, res)
        # else:
        #     return


# DFS stack solution 
class Solution(object):
    def treeToDoublyList(self, root):
        if not root:
            return
        
        res = [] # List to save in-order nodes from BFS traversal
        q = [(root, False)]

        while q:
            node, visited = q.pop() # pop() = pop(-1)
            if node:
                if visited:
                    res.append(node)
                else: # in-order: left -> root -> right
                    q.append((node.right, False))
                    q.append((node, True))
                    q.append((node.left, False))

        # at this moment, res=[1, 2, 3, 4, 5], need to create double-linked
        for i in range(len(res) - 1):
            res[i].right = res[i + 1] # add right link
            res[i + 1].left = res[i] # add left link
        
        res[-1].right = res[0] # add right for the last element
        res[0].left = res[-1] # add left for the first element

        # return head
        return res[0]
        
# @lc code=end

