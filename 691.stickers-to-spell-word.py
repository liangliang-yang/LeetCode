#
# @lc app=leetcode id=691 lang=python
#
# [691] Stickers to Spell Word
#

# @lc code=start
class Solution(object):
    def minStickers(self, stickers, target):
        result = self.dfs(stickers, target, 0, {})
        return result if result != float("inf") else -1
    
    def dfs(self, stickers, target, idx, memo):
        # if target is empty then we don't need to take any sticker
        if target == "":
            return 0
        # if we've searched through all stickers and haven't completed the target
        # then there is no solution
        if idx == len(stickers):
            return float("inf")

        # lookup the answer in the cache
        key = (idx, target)
        if key in memo:
            print("find key in memo")
            # print(memo)
            return memo[key]
        
        # choice 1 don't take the current sticker
        result = self.dfs(stickers, target, idx+1, memo)

        # choice 2 try to take the current sticker
        currentSticker = stickers[idx]
        newTarget = target
        somethingRemoved = False
        for c in currentSticker: # try every char, 这里用 for loop 移除尽量多的 char
            idxToRemove = newTarget.find(c) # see if currentSticker has char
            if idxToRemove != -1:
                newTarget = newTarget[:idxToRemove] + newTarget[idxToRemove+1:]
                somethingRemoved = True
        
        # for loop 结束之后我们希望 newTarget 已经比原来 target 少了一些 char (至少移除一个 char)

        
        # only try this sticker again if we were able to remove something from
        # the target string, 如果不存在可以移除的 char, 那么就不要 choice 2
        if somethingRemoved:
            result = min(result, 1 + self.dfs(stickers, newTarget, idx, memo))

        # cache the result, 这里是记录什么呢？
        # print(memo)
        memo[key] = result
        return result
    

# stickers = ["with","example","science"]
# target = "thehat"

# s = Solution()
# print(s.minStickers(stickers, target))



    # def minStickers(self, stickers, target):
    #     result = self.dfs(stickers, target, 0)
    #     return result if result != float("inf") else -1
    
    # def dfs(self, stickers, target, idx):
    #     # if target is empty then we don't need to take any sticker
    #     if target == "":
    #         return 0
    #     # if we've searched through all stickers and haven't completed the target
    #     # then there is no solution
    #     if idx == len(stickers):
    #         return float("inf")

    #     # lookup the answer in the cache
    #     key = (idx, target)
    #     # if key in memo:
    #     #     # print("find key in memo")
    #     #     return memo[key]
        
    #     # choice 1 don't take the current sticker
    #     result = self.dfs(stickers, target, idx+1)

    #     # choice 2 try to take the current sticker
    #     currentSticker = stickers[idx]
    #     newTarget = target
    #     somethingRemoved = False
    #     for c in currentSticker: # try every char, 这里用 for loop 移除尽量多的 char
    #         idxToRemove = newTarget.find(c) # see if currentSticker has char
    #         if idxToRemove != -1:
    #             newTarget = newTarget[:idxToRemove] + newTarget[idxToRemove+1:]
    #             somethingRemoved = True
        
    #     # for loop 结束之后我们希望 newTarget 已经比原来 target 少了一些 char (至少移除一个 char)

        
    #     # only try this sticker again if we were able to remove something from
    #     # the target string, 如果不存在可以移除的 char, 那么就不要 choice 2
    #     if somethingRemoved:
    #         result = min(result, 1 + self.dfs(stickers, newTarget, idx))

    #     # cache the result, 这里是记录什么呢？
    #     # print(memo)
    #     # memo[key] = result
    #     return result
    
# stickers = ["with","example","science"]
# target = "thehat"
# memo = 
# {}
# {(2, 'thhat'): inf}
# {(2, 'thhat'): inf, (2, 'thehat'): inf}
# {(2, 'thhat'): inf, (2, 'thehat'): inf, (2, 'thht'): inf}
# {(2, 'thhat'): inf, (2, 'thehat'): inf, (2, 'thht'): inf, (1, 'thht'): inf}
# {(2, 'thhat'): inf, (2, 'thehat'): inf, (2, 'thht'): inf, (1, 'thht'): inf, (1, 'thehat'): inf}
# {(2, 'thhat'): inf, (2, 'thehat'): inf, (2, 'thht'): inf, (1, 'thht'): inf, (1, 'thehat'): inf, (2, 'hat'): inf}
# {(2, 'thhat'): inf, (2, 'thehat'): inf, (2, 'thht'): inf, (1, 'thht'): inf, (1, 'thehat'): inf, (2, 'hat'): inf, (2, 'ehat'): inf}
# {(2, 'thhat'): inf, (2, 'thehat'): inf, (2, 'thht'): inf, (1, 'thht'): inf, (1, 'thehat'): inf, (2, 'hat'): inf, (2, 'ehat'): inf, (2, 'ht'): inf}
# {(2, 'thhat'): inf, (2, 'thehat'): inf, (2, 'thht'): inf, (1, 'thht'): inf, (1, 'thehat'): inf, (2, 'hat'): inf, (2, 'ehat'): inf, (2, 'ht'): inf, (1, 'ht'): inf}
# {(2, 'thhat'): inf, (2, 'thehat'): inf, (2, 'thht'): inf, (1, 'thht'): inf, (1, 'thehat'): inf, (2, 'hat'): inf, (2, 'ehat'): inf, (2, 'ht'): inf, (1, 'ht'): inf, (1, 'ehat'): inf}
# {(2, 'thhat'): inf, (2, 'thehat'): inf, (2, 'thht'): inf, (1, 'thht'): inf, (1, 'thehat'): inf, (2, 'hat'): inf, (2, 'ehat'): inf, (2, 'ht'): inf, (1, 'ht'): inf, (1, 'ehat'): inf, (2, 'a'): inf}
# {(2, 'thhat'): inf, (2, 'thehat'): inf, (2, 'thht'): inf, (1, 'thht'): inf, (1, 'thehat'): inf, (2, 'hat'): inf, (2, 'ehat'): inf, (2, 'ht'): inf, (1, 'ht'): inf, (1, 'ehat'): inf, (2, 'a'): inf, (2, 'ea'): inf}
# {(2, 'thhat'): inf, (2, 'thehat'): inf, (2, 'thht'): inf, (1, 'thht'): inf, (1, 'thehat'): inf, (2, 'hat'): inf, (2, 'ehat'): inf, (2, 'ht'): inf, (1, 'ht'): inf, (1, 'ehat'): inf, (2, 'a'): inf, (2, 'ea'): inf, (1, 'ea'): 1}
# {(2, 'thhat'): inf, (2, 'thehat'): inf, (2, 'thht'): inf, (1, 'thht'): inf, (1, 'thehat'): inf, (2, 'hat'): inf, (2, 'ehat'): inf, (2, 'ht'): inf, (1, 'ht'): inf, (1, 'ehat'): inf, (2, 'a'): inf, (2, 'ea'): inf, (1, 'ea'): 1, (0, 'ea'): 1}
# {(2, 'thhat'): inf, (2, 'thehat'): inf, (2, 'thht'): inf, (1, 'thht'): inf, (1, 'thehat'): inf, (2, 'hat'): inf, (2, 'ehat'): inf, (2, 'ht'): inf, (1, 'ht'): inf, (1, 'ehat'): inf, (2, 'a'): inf, (2, 'ea'): inf, (1, 'ea'): 1, (0, 'ea'): 1, (0, 'ehat'): 2}
# @lc code=end

