#
# @lc app=leetcode id=23 lang=python
#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (53.16%)
# Likes:    19394
# Dislikes: 718
# Total Accepted:    2.1M
# Total Submissions: 3.8M
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# You are given an array of k linked-lists lists, each linked-list is sorted in
# ascending order.
# 
# Merge all the linked-lists into one sorted linked-list and return it.
# 
# 
# Example 1:
# 
# 
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
# ⁠ 1->4->5,
# ⁠ 1->3->4,
# ⁠ 2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# 
# 
# Example 2:
# 
# 
# Input: lists = []
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: lists = [[]]
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 10^4.
# 
# 
#

# @lc code=start

# Definition for singly-linked list.

import heapq

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):

        h = [] # heap size is N of lists
        dummy = ListNode(0) # dummy is same as node
        
        for node in lists: # every node is head node of each list
            if node: # 把所有list 的第一个元素加入到 heap 里
                # min heap, sort based on node.val
                heapq.heappush(h, (node.val, node)) 
        
        cur = dummy # 先指向 dummy，用来更新 merged list
        while h:
            min_val, min_node = heapq.heappop(h)
            cur.next = min_node
            cur = cur.next
            
            if min_node.next: # add the next node to current heap
                heapq.heappush(h, (min_node.next.val, min_node.next))

        return dummy.next
        
# @lc code=end

