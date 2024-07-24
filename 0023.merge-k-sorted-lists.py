#
# @lc app=leetcode id=23 lang=python
#
# [23] Merge k Sorted Lists
#

# @lc code=start


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        h = [] # heap size is N of lists
        dummy = ListNode(0) # dummy is same as node
        
        for node in lists: # every node is head node of each list
            if node: # 把所有list 的第一个元素加入到 heap 里
                heapq.heappush(h, (node.val, node)) # min heap
        
        cur = dummy # 先指向 dummy，用来更新 merged list
        while h:
            min_val, min_node = heapq.heappop(h)
            cur.next = min_node
            cur = cur.next
            
            if min_node.next: # add the next node to current heap
                heapq.heappush(h, (min_node.next.val, min_node.next))

        return dummy.next
    
    
    
        
# @lc code=end

