#
# @lc app=leetcode id=1060 lang=python
#
# [1060] Missing Element in Sorted Array
#
# https://leetcode.com/problems/missing-element-in-sorted-array/description/
#
# algorithms
# Medium (56.99%)
# Likes:    1659
# Dislikes: 62
# Total Accepted:    140.3K
# Total Submissions: 244.7K
# Testcase Example:  '[4,7,9,10]\n1'
#
# Given an integer array nums which is sorted in ascending order and all of its
# elements are unique and given also an integer k, return the k^th missing
# number starting from the leftmost number of the array.
# 
# 
# Example 1:
# 
# 
# Input: nums = [4,7,9,10], k = 1
# Output: 5
# Explanation: The first missing number is 5.
# 
# 
# Example 2:
# 
# 
# Input: nums = [4,7,9,10], k = 3
# Output: 8
# Explanation: The missing numbers are [5,6,8,...], hence the third missing
# number is 8.
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,2,4], k = 3
# Output: 6
# Explanation: The missing numbers are [3,5,6,7,...], hence the third missing
# number is 6.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 5 * 10^4
# 1 <= nums[i] <= 10^7
# nums is sorted in ascending order, and all the elements are unique.
# 1 <= k <= 10^8
# 
# 
# 
# Follow up: Can you find a logarithmic time complexity (i.e., O(log(n)))
# solution?
#

# @lc code=start

class Solution(object):
    def missingElement(self, nums, k):
        # if not nums or k==0: 
        #     return 0
        # 第一个数字肯定不会 missing
        n = len(nums)
        
        # [4, 7, 9, 10], 4->10 应该有7个数字
        diff = nums[-1] - nums[0] + 1 # complete length

        # 现在只要四个数字， 说明缺三个
        n_missing_between = diff - n
        if k > n_missing_between: # 假如缺3个， 但是要找第四个missing的， 那么一定是加在nums之后的
            return nums[-1] + (k-n_missing_between)
        
        # 如果缺失的在 nums 中间， 用 BS - find last True 模板
        # 思路是 find max m, from [nums[0],..nums[m]], we have < K missing items
        # [4, 6, 7, 9, 10], k=2, 那么 到达6, or 7 ， 都可以
        # 实际上我们应该选择 7， 因为6，7连续， pick max True
        left, right = 0, n - 1
        
        while left < right:
            mid = right - (right - left) // 2 # Right-Biased Midpoint
            #  If mid were calculated in a standard way (mid = left + (right - left) // 2), 
            # there could be cases where left is not updated, leading to an infinite loop 
            # 计算在 [nums[0], nums[mid]] 之间 missing 的数字
            # begin_to_mid_complete_length = nums[mid]-nums[0]+1 #应该有这么多数字
            # begin_to_mid_actual_length = mid+1 # 实际上的数字
            n_missing_until_mid = nums[mid]-nums[0]-mid

            if n_missing_until_mid < k: # 可以试试右边包含mid [mid, right]
                left = mid
            else:
                right = mid-1

        # [4, 6, 7, 9, 10], k=2, 此时返回的 nums[left]=7, missing=8
        # 但是不能用 nums[left]+1, 因为假如 nums=[4, 7, 9, 10], k=2, nums[left]=4, 4+1=5 != 6
        # 可以肯定的是 [nums[0], answer]之间有 k 个missing, 同时有 left+1 个存在的
        # 所以： answer - nums[0] + 1 = k + left + 1
        # answer = nums[0] + k + left
        return nums[0] + k + left
    



# def findFirstTrue(self, nums):
#         left =0
#         right = len(nums)-1
#         while left < right:
#             mid = left + (right - left) // 2 # Left-Biased Midpoint
#             #  mid were calculated in a standard way

#             if nums[mid] is True: # nums[mid] still satisfies the condition
#                 # move to left side [left, mid], first True must inside 
#                 right = mid 
#             else:
#                 right = mid
#         return left


# def findLastTrue(self, nums):
#         left =0
#         right = len(nums)-1
#         while left < right:
#             mid = right - (right - left) // 2 # Right-Biased Midpoint
#             # If mid were calculated in a standard way (mid = left + (right - left) // 2), 
#             # there could be cases where left is not updated, leading to an infinite loop 

#             if nums[mid] is True: # nums[mid] still satisfies the condition
#                 # move to right side [mid, right], last True must inside
#                 left = mid 
#             else:
#                 right = mid -1
#         return left


        
# @lc code=end

