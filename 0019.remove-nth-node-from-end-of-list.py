#
# @lc app=leetcode id=19 lang=python
#
# [19] Remove Nth Node From End of List
#
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (45.70%)
# Likes:    19006
# Dislikes: 818
# Total Accepted:    2.9M
# Total Submissions: 6.3M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given the head of a linked list, remove the n^th node from the end of the
# list and return its head.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# 
# 
# Example 2:
# 
# 
# Input: head = [1], n = 1
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: head = [1,2], n = 1
# Output: [1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
# 
# 
# 
# Follow up: Could you do this in one pass?
# 
#

# @lc code=start
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head

        fast = dummy
        slow = dummy
        # 不能用 fast = slow = dummy

        # [dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> null], n=2
        # fast 先移动 n+ step
        for i in range(n + 1):
            fast = fast.next # 此时 fast = 3

        # move fast & slow, until fast move to end
        while fast:
            fast = fast.next
            slow = slow.next
        
        # fast 需要继续移动三步到null, 此时 fast=null, slow=3
        slow.next = slow.next.next # 移除 3 后面的， 就是 4
        return dummy.next
    
        
# Time complexity : O(n)
# Space complexity : O(1)


# @lc code=end

