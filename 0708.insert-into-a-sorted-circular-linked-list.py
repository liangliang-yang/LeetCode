#
# @lc app=leetcode id=708 lang=python
#
# [708] Insert into a Sorted Circular Linked List
#
# https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/description/
#
# algorithms
# Medium (36.30%)
# Likes:    1224
# Dislikes: 778
# Total Accepted:    181.3K
# Total Submissions: 496.4K
# Testcase Example:  '[3,4,1]\n2'
#
# Given a Circular Linked List node, which is sorted in non-descending order,
# write a function to insert a value insertVal into the list such that it
# remains a sorted circular list. The given node can be a reference to any
# single node in the list and may not necessarily be the smallest value in the
# circular list.
# 
# If there are multiple suitable places for insertion, you may choose any place
# to insert the new value. After the insertion, the circular list should remain
# sorted.
# 
# If the list is empty (i.e., the given node is null), you should create a new
# single circular list and return the reference to that single node. Otherwise,
# you should return the originally given node.
# 
# 
# Example 1:
# 
# 
# 
# Input: head = [3,4,1], insertVal = 2
# Output: [3,4,1,2]
# Explanation: In the figure above, there is a sorted circular list of three
# elements. You are given a reference to the node with value 3, and we need to
# insert 2 into the list. The new node should be inserted between node 1 and
# node 3. After the insertion, the list should look like this, and we should
# still return node 3.
# 
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: head = [], insertVal = 1
# Output: [1]
# Explanation: The list is empty (given head is null). We create a new single
# circular list and return the reference to that single node.
# 
# 
# Example 3:
# 
# 
# Input: head = [1], insertVal = 0
# Output: [1,0]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [0, 5 * 10^4].
# -10^6 <= Node.val, insertVal <= 10^6
# 
# 
#

# @lc code=start

# Definition for a Node.

class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def insert(self, head, insertVal):
        # Scenario 1 : When head is None or empty list
        if head == None:
            newNode = Node(insertVal, None)
            newNode.next = newNode
            return newNode
 
        prev, curr = head, head.next # use two pointers

        # while prev != head: # can't use this since we init value for prev is head
        while True:
            
            if prev.val <= insertVal <= curr.val:
                # Scenario 2 : When insertion is between 2 values
                newNode = Node(insertVal, next=curr)
                prev.next = newNode
                return head
            
            elif prev.val > curr.val: # we are at 9 -> 1 转折点， prev=9, curr=1
                # Scenario 3 : When insertVal is smallest or largest
                # [3, 5, 7, 9, 1], insert 0 or 10
                if insertVal >= prev.val or insertVal <= curr.val:
                    newNode = Node(insertVal, next=curr)
                    prev.next = newNode
                    return head

           # keep moving
            prev, curr = curr, curr.next

            if prev == head: # if prev == head, we return to start position
                break

        # Scenario 4 : When insertion can be done anywhere, all node values are the same
        # [3, 3, 3, 3, 3], insert 10, just insert after head, 此事 prev=head, curr=head.next
        newNode = Node(insertVal, next=curr)
        prev.next = newNode
        return head
		
# @lc code=end

