#
# @lc app=leetcode id=140 lang=python
#
# [140] Word Break II
#
# https://leetcode.com/problems/word-break-ii/description/
#
# algorithms
# Hard (51.03%)
# Likes:    7172
# Dislikes: 538
# Total Accepted:    665K
# Total Submissions: 1.3M
# Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
#
# Given a string s and a dictionary of strings wordDict, add spaces in s to
# construct a sentence where each word is a valid dictionary word. Return all
# such possible sentences in any order.
# 
# Note that the same word in the dictionary may be reused multiple times in the
# segmentation.
# 
# 
# Example 1:
# 
# 
# Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
# Output: ["cats and dog","cat sand dog"]
# 
# 
# Example 2:
# 
# 
# Input: s = "pineapplepenapple", wordDict =
# ["apple","pen","applepen","pine","pineapple"]
# Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
# Explanation: Note that you are allowed to reuse a dictionary word.
# 
# 
# Example 3:
# 
# 
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 20
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 10
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.
# Input is generated in a way that the length of the answer doesn't exceed
# 10^5.
# 
# 
#

# @lc code=start

# https://leetcode.com/problems/word-break-ii/solutions/44311/Python-easy-to-understand-solution/

# 1.Every time, we check whether s starts with a word. If so, we check whether the substring s[len(word):] starts with a word, etc.
# 2.resultOfTheRest keeps calling until we hit the last word. If the last word is in the dict, we append it to res.
# The last word is 'dog ==> 'res = [ "dog"]

# This time, we skip "else," since we fulfill the condition " if len(word) == len(s)." We store it in memo: {'dog': ['dog']}
# 4.Then we return to "resultOfTheRest = self.helper(s[len(word):], wordDict, memo)"
# s = "sanddog" because we start with "cat" (cat is the first word in the dict) and "cat" leads to "sand".
# resultOfTheRest = ["dog"]
# word = "sand"
# item = "sand dog"
# res = ["sand dog"]
# memo ={'dog': ['dog'], "sanddog":["sand dog"] }

# Why do we need memo?
# We always recurse to the last word in the string and backtrack, so storing all possible combinations of the substring in the memo saves time for the next iteration of the whole string. For example, "catsanddog," if we don't store "dog," then we have to iterate through the dictionary. This is very DP.

# My print statement "s" is a line below "for word in wordDict:"

# s catsanddog
# s sanddog
# s sanddog
# s sanddog
# s sanddog
# s dog
# s dog
# s dog
# s dog
# s dog
# {'dog': ['dog']}
# res ['sand dog']
# s sanddog
# {'dog': ['dog'], 'sanddog': ['sand dog']}
# res ['cat sand dog']
# s catsanddog
# s anddog
# s anddog
# s anddog
# res ['and dog']
# s anddog
# s anddog
# {'dog': ['dog'], 'sanddog': ['sand dog'], 'anddog': ['and dog']}
# res ['cat sand dog', 'cats and dog']
# s catsanddog
# s catsanddog
# s catsanddog
# {'dog': ['dog'], 'sanddog': ['sand dog'], 'anddog': ['and dog'], 'catsanddog': ['cat sand dog', 'cats and dog']}

class Solution(object):
    def wordBreak(self, s, wordDict):
        word_set = set(wordDict) # set to remove duplicates
        memo = {} # store {s: wordBreakResults}， 例如 "sanddog": [["sand", "dog"]]
        res = self.dfs(s, word_set, memo)
        # res is 2D list [["cats", "and", "dog"], ["cat", "sand", "dog"]]
        ans = []
        for possible_break in res:
            ans.append(" ".join(possible_break))
        return ans
    
    # Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
    # Output: ["cats and dog","cat sand dog"]
    def dfs(self, s, word_set, memo):

        if s in memo: 
            return memo[s]
        if not s: 
            return []
        
        res = [] # store all possible wordBreakResults for s
        # 2D list [["cats", "and", "dog"], ["cat", "sand", "dog"]]

        # 这里考虑 s 必须由 word_set 里面的单词拼凑起来， 例如 "sanddog": ["sand", "dog"]
        # 所有必须有一个单词 和 s的开头一样， s[:k] == word
        for word in word_set:
            if not s.startswith(word): # 找开头的单词
                continue

            k=len(word)
            
            # 如果正好长度一样， 就可以直接用 word
            if k == len(s):
                s_possible_break = [word] # 1D list, possible break
                res.append(s_possible_break) # 直接到 return 了 [[word]]

            # 如果 s[:k] == word, 那么还需要找之后的 s[k:]的 wordBreakResults
            else:
                remaining_str_possible_break = self.dfs(s[k:], word_set, memo) 
                # remaining_str_possible_break is a 2D list
                for break_method in remaining_str_possible_break: 
                    s_possible_break = [word] + break_method 
                    res.append(s_possible_break)

        memo[s] = res
        return res
        

# {'dog': ['dog'], 'sanddog': ['sand dog'], 'anddog': ['and dog'], 'catsanddog': ['cat sand dog', 'cats and dog']}
# @lc code=end

