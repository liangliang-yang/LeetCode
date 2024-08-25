#
# @lc app=leetcode id=680 lang=python
#
# [680] Valid Palindrome II
#
# https://leetcode.com/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (40.87%)
# Likes:    8258
# Dislikes: 445
# Total Accepted:    782.3K
# Total Submissions: 1.9M
# Testcase Example:  '"aba"'
#
# Given a string s, return true if the s can be palindrome after deleting at
# most one character from it.
# 
# 
# Example 1:
# 
# 
# Input: s = "aba"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# 
# 
# Example 3:
# 
# 
# Input: s = "abc"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s consists of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution(object):
    def validPalindrome(self, s):
        i = 0
        j = len(s)-1
        while i < j:
            if s[i] != s[j]:
                delete_i = s[i+1:j+1]
                delete_j = s[i:j]
                return self._isPalindrome(delete_i) or self._isPalindrome(delete_j)
            i += 1
            j -= 1
        return True
    
    def _isPalindrome(self, s):
        return s == s[::-1]

# Time: O(n)
# Space: O(n)        

# @lc code=end

