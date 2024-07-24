#
# @lc app=leetcode id=140 lang=python
#
# [140] Word Break II
#

# @lc code=start

# https://leetcode.com/problems/word-break-ii/solutions/4078366/share-my-trie-and-recursion-solutionre/

class Node:
    def __init__(self, ):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = Node()
        self.result = []

    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = Node()
            node = node.children[w]
        node.is_word = True

    def search(self, word, path):
        if not word:                                # this path is valid              
            self.result.append("".join(path).strip())
            return
        node = self.root
        for i, w in enumerate(word):
            path.append(w)
            if w not in node.children:
                return
            if node.children[w].is_word:
                self.search(word[i+1:], path+[" "]) # keep searching until all the is_word are consumed
            node = node.children[w]


class Solution:
    def wordBreak(self, s, wordDict):
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        
        trie.search(s, [])
        return trie.result
        

        
        
        
# @lc code=end

