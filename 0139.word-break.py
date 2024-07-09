#
# @lc app=leetcode id=139 lang=python
#
# [139] Word Break
#

# @lc code=start
# https://leetcode.com/problems/word-break/solutions/2722114/python-trie-solution-beats-80-simple-recursive/

# Complexity
# Time complexity: O(W * K) where W is length of words in dictionary and K is the length (average) of each word
# Space complexity: O(n) where n is the number of characters in the dictionary

class TrieNode:
    def __init__(self):
        self.children, self.end = {}, False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.memo = {}
    
    # Time O(K) - where K is the length of the word
    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.end = True
    
    # Time O(K) - where K is the length of the word
    def find(self, word):
        curr = self.root
        for i, char in enumerate(word):
            if char not in curr.children: return False
            
            if curr.children[char].end:
                remaining_word = word[i+1:]
                if remaining_word not in self.memo:
                    self.memo[remaining_word] = self.find(remaining_word)

                if self.memo[remaining_word]:
                    return True

            curr = curr.children[char]
        return curr.end

class Solution:
    def wordBreak(self, s, wordDict):
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        
        return trie.find(s)
        
# @lc code=end

