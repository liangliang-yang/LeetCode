#
# @lc app=leetcode id=691 lang=python
#
# [691] Stickers to Spell Word
#

# # @lc code=start

# class Solution(object):
#     def minStickers(self, stickers, target):
#         memo = {}
#         result = self.dfs(stickers, target, 0, memo)
#         return result if result != float("inf") else -1
    
#     # dfs to find how min number of stickers to create target (given memo) 
#     def dfs(self, stickers, target, idx, memo): 
#         # if target is empty then we don't need to take any sticker
#         if target == "":
#             return 0
#         # if we've searched through all stickers and haven't completed the target
#         # then there is no solution
#         if idx == len(stickers):
#             return float("inf")

#         # lookup the answer in the cache
#         key = (idx, target)
#         if key in memo:
#             print("find key in memo")
#             # print(memo)
#             return memo[key]
        
#         # choice 1 don't take the current sticker
#         result = self.dfs(stickers, target, idx+1, memo)

#         # choice 2 try to take the current sticker
#         currentSticker = stickers[idx]
#         newTarget = target
#         somethingRemoved = False
#         for c in currentSticker: # try every char, 这里用 for loop 移除尽量多的 char
#             idxToRemove = newTarget.find(c) # see if currentSticker has char
#             if idxToRemove != -1:
#                 newTarget = newTarget[:idxToRemove] + newTarget[idxToRemove+1:]
#                 somethingRemoved = True
        
#         # for loop 结束之后我们希望 newTarget 已经比原来 target 少了一些 char (至少移除一个 char)

        
#         # only try this sticker again if we were able to remove something from
#         # the target string, 如果不存在可以移除的 char, 那么就不要 choice 2
#         if somethingRemoved:
#             result = min(result, 1 + self.dfs(stickers, newTarget, idx, memo))

#         # cache the result, 这里是记录什么呢？
#         # print(memo)
#         memo[key] = result
#         return result
  

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



  
import collections
class Solution(object):
    def minStickers(self, stickers, target):
        memo = {}
        target_count = collections.Counter(target)
        stickers_count=[collections.Counter(sticker) for sticker in stickers]

        result = self.dfs(stickers_count, target, memo)
        return result if result != float("inf") else -1
    
    # dfs to find how min number of stickers to create s (given memo) 
    def dfs(self, stickers_count, s, memo):
        # print(s, memo)
        if s == "": # empty s
            return 0
        if s in memo:
            return memo[s]
        
        minStickers = float("inf") # init as inf
        s_count = collections.Counter(s) # get char count of s
        # print(s_count)
        for sticker_count in stickers_count: # try each sticker, here we use Counter(sticker)
            if s[0] in sticker_count: # why not s[1], s[2 ?]
            # if set(s_count.keys()) & set(sticker_count.keys()) is not None:
                new_s = "" # 记录用完 current sticker 之后的 new_s
                
                for char in s_count: # try every char in s, see if we have the same char in sticker
                    if s_count[char] > sticker_count[char]: 
                        # can't remove all char from s, need more stickers 
                        remaining_char_count = s_count[char] - sticker_count[char]
                        new_s += char * remaining_char_count 
                        # print(new_s)
                    # if s_count[char] <= sticker_count[char]: char will be fully removed
                
                # after we use the current sticker, s -> new_s
                if new_s != s:
                    use_current_sticker = self.dfs(stickers_count, new_s, memo)
                    # choose between use or not use
                    minStickers = min(minStickers, use_current_sticker+1)

        # update memo
        memo[s] = minStickers
        print(s, memo, minStickers)
        return minStickers


# stickers = ["with","example","science"]
# target = "thehat"

# if use  -> if set(s_count.keys()) & set(sticker_count.keys()) is not None:
# (u'a', {u'a': 1}, 1)
# (u'ae', {u'a': 1, u'ae': 1}, 1)
# (u'ht', {u'a': 1, u'ae': 1, u'ht': 1}, 1)
# (u'aht', {u'a': 1, u'ae': 1, u'aht': 2, u'ht': 1}, 2)
# (u'ahet', {u'a': 1, u'ahet': 2, u'ae': 1, u'aht': 2, u'ht': 1}, 2)
# (u'hhtt', {u'a': 1, u'ae': 1, u'hhtt': 2, u'ht': 1, u'aht': 2, u'ahet': 2}, 2)
# (u'ahhtt', {u'a': 1, u'ae': 1, u'hhtt': 2, u'ht': 1, u'aht': 2, u'ahhtt': 3, u'ahet': 2}, 3)
# (u'thehat', {u'a': 1, u'ae': 1, u'hhtt': 2, u'thehat': 3, u'ht': 1, u'aht': 2, u'ahhtt': 3, u'ahet': 2}, 3)

# if use -> if s[0] in sticker_count:
# (u'ht', {u'ht': 1}, 1)
# (u'ahet', {u'ahet': 2, u'ht': 1}, 2)
# (u'thehat', {u'thehat': 3, u'ahet': 2, u'ht': 1}, 3)

# @lc code=end

