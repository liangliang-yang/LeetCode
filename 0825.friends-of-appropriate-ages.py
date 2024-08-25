#
# @lc app=leetcode id=825 lang=python
#
# [825] Friends Of Appropriate Ages
#
# https://leetcode.com/problems/friends-of-appropriate-ages/description/
#
# algorithms
# Medium (47.67%)
# Likes:    768
# Dislikes: 1216
# Total Accepted:    93.6K
# Total Submissions: 195.4K
# Testcase Example:  '[16,16]'
#
# There are n persons on a social media website. You are given an integer array
# ages where ages[i] is the age of the i^th person.
# 
# A Person x will not send a friend request to a person y (x != y) if any of
# the following conditions is true:
# 
# 
# age[y] <= 0.5 * age[x] + 7
# age[y] > age[x]
# age[y] > 100 && age[x] < 100
# 
# 
# Otherwise, x will send a friend request to y.
# 
# Note that if x sends a request to y, y will not necessarily send a request to
# x. Also, a person will not send a friend request to themself.
# 
# Return the total number of friend requests made.
# 
# 
# Example 1:
# 
# 
# Input: ages = [16,16]
# Output: 2
# Explanation: 2 people friend request each other.
# 
# 
# Example 2:
# 
# 
# Input: ages = [16,17,18]
# Output: 2
# Explanation: Friend requests are made 17 -> 16, 18 -> 17.
# 
# 
# Example 3:
# 
# 
# Input: ages = [20,30,100,110,120]
# Output: 3
# Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.
# 
# 
# 
# Constraints:
# 
# 
# n == ages.length
# 1 <= n <= 2 * 10^4
# 1 <= ages[i] <= 120
# 
# 
#

# @lc code=start


class Solution(object):
    def numFriendRequests(self, ages):
        count_in_ages = [0] * 121 # for each age n, how many people 
        prefix_sum = [0] * 121 # until age n, how many people in total
        unique_ages = set()
        
        for age in ages:
            count_in_ages[age] += 1
            unique_ages.add(age)

        for i in range(1, 121):
            # prefix_sum[0] = 0, keep update next
            prefix_sum[i] = prefix_sum[i - 1] + count_in_ages[i]

        total_requests = 0
        # if ageX * 0.5 + 7 >= ageY: continue
        # if ageX < ageY: continue
        # if ageX < 100 < ageY: continue 
        # 所以合理的是 ： ageX*0.5+7  < ageY <= ageX (但 Y 不能发给自己)
        # （ageX < 100 < ageY）  自动被上面的条件剔除

        # 所以对于所有年龄在 X 的， 我们可以对下面所有年龄段的发出request
        # ageY <= ageX -- upper bound , Y 要比 X年轻或者同龄， 比如 18 -> 17
        # ageY > ageX*0.5 + 7 -- lower bound
        for age in unique_ages: 
            
            #lb = age*0.5+7 -- 假如 age=21， 则为21*0.5+7 = 17.5， 需要 >=18, 剔除 17
            lb = age//2 + 7 # 21//2 + 7 = 17, 也为 integer
            hb = age # high bound
            # 需要的区间是 [lb+1,  hb], 但是不能包括 X->X, 所以 hb 里面需要去除自己

            if lb <= hb:
                # [0..., lb] 一共有 prefix_sum[lb] 
                # [0..., hb] 一共有 prefix_sum[hb] 
                # [lb+1 .... hb] 一共有 prefix_sum[hb] - prefix_sum[lb]， 这类还包括 X自己， 所以需要继续减一
                requests = count_in_ages[age] * (prefix_sum[hb] - prefix_sum[lb] - 1)
                total_requests += max(0, requests)

        return total_requests
        
# @lc code=end

