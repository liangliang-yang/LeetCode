#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (34.94%)
# Likes:    40209
# Dislikes: 1927
# Total Accepted:    6.3M
# Total Submissions: 17.8M
# Testcase Example:  '"abcabcbb"'
#
# Given a string s, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# 
# 
# Example 2:
# 
# 
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# Example 3:
# 
# 
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a
# substring.
# 
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
# 
# 
#

# @lc code=start

import collections

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        N = len(s)
        max_len = 0

        counts = collections.defaultdict(int) # {char: count}

        # window: [left....right], include right
        for right in range(N):
            counts[s[right]] += 1 # update, default 0 due to defaultdict(int)

            # if s[right] 有重复了， 那么需要移动左边直到没有重复
            while counts[s[right]] > 1:
                counts[s[left]] -= 1
                # if counts[s[left]] == 0: # 这里可以不需要这一步
                    # del counts[s[left]]
                left += 1
            
            # after remove repeating chars, now calculate the new window length
            cur_len = right-left+1
            max_len = max(max_len, cur_len)

        return max_len


        
# @lc code=end

