#
# @lc app=leetcode id=516 lang=python
#
# [516] Longest Palindromic Subsequence
#
# https://leetcode.com/problems/longest-palindromic-subsequence/description/
#
# algorithms
# Medium (62.74%)
# Likes:    9566
# Dislikes: 330
# Total Accepted:    517.4K
# Total Submissions: 821.2K
# Testcase Example:  '"bbbab"'
#
# Given a string s, find the longest palindromic subsequence's length in s.
# 
# A subsequence is a sequence that can be derived from another sequence by
# deleting some or no elements without changing the order of the remaining
# elements.
# 
# 
# Example 1:
# 
# 
# Input: s = "bbbab"
# Output: 4
# Explanation: One possible longest palindromic subsequence is "bbbb".
# 
# 
# Example 2:
# 
# 
# Input: s = "cbbd"
# Output: 2
# Explanation: One possible longest palindromic subsequence is "bb".
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s consists only of lowercase English letters.
# 
# 
#

# @lc code=start
# class Solution:
#     def longestPalindromeSubseq(self, s):
#         if len(s) <= 1: 
#             return len(s) 
        
#         memo = {} 
#         # init memo, 所有的单个字母 longestPalindromeSubseq=1
#         for i in range(len(s)):
#             memo[(i, i)] = 1
        
#         return self.dfs(s, memo, 0, len(s) - 1)
    
#     # use dfs to find longestPalindromeSubseq between s[left:right] (include right) 
#     def dfs(self, s, memo, left, right): 
#         if left > right: 
#             return 0 
        
#         if (left, right) in memo: 
#             return memo[(left, right)] 

#         # if left == right: # 所有的单个字母 longestPalindromeSubseq=1， 这个也可以提前 init
#         #     memo[(left, right)] = 1 
#         #     return 1 
        
#         if s[left] == s[right]: 
#             cur_max = self.dfs(s, memo, left + 1, right - 1) + 2 
#         else: 
#             drop_left = self.dfs(s, memo, left + 1, right)
#             drop_right = self.dfs(s, memo, left, right-1)
#             cur_max = max(drop_left, drop_right)

#         # add cur_max to memo
#         memo[(left, right)] = cur_max
#         # print(memo) # see below for logs
        
#         return cur_max


class Solution:
    def longestPalindromeSubseq(self, s):
        if len(s) <= 1: 
            return len(s) 
        
        memo = {} 
        # init memo, 所有的单个字母 longestPalindromeSubseq=1
        for i in range(len(s)):
            memo[(i, i)] = 1
        
        return self.dfs(s, memo, 0, len(s) - 1)
    
    # use dfs to find longestPalindromeSubseq between s[left:right] (include right) 
    def dfs(self, s, memo, left, right): 
        if left > right: 
            return 0 
        
        if (left, right) in memo: 
            return memo[(left, right)] 
        
        
        if s[left] == s[right]: 
            cur_max = self.dfs(s, memo, left + 1, right - 1) + 2 
        else: 
            drop_left = self.dfs(s, memo, left + 1, right)
            drop_right = self.dfs(s, memo, left, right-1)
            cur_max = max(drop_left, drop_right)

        # add cur_max to memo
        memo[(left, right)] = cur_max
        # print(memo) # see below for logs
        
        return cur_max

# "bbbab"
# 4

# {(0, 0): 1, (3, 3): 1, (4, 4): 1, (2, 3): 1, (2, 2): 1, (1, 1): 1}

# {(1, 2): 2, (0, 0): 1, (3, 3): 1, (4, 4): 1, (2, 3): 1, (2, 2): 1, (1, 1): 1}

# {(1, 2): 2, (0, 0): 1, (3, 3): 1, (4, 4): 1, (1, 3): 2, (2, 3): 1, (2, 2): 1, (1, 1): 1}

# {(1, 2): 2, (0, 0): 1, (3, 3): 1, (4, 4): 1, (1, 3): 2, (2, 3): 1, (2, 2): 1, (0, 4): 4, (1, 1): 1}



# @lc code=end

