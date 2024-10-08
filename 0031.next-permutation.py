#
# @lc app=leetcode id=31 lang=python
#
# [31] Next Permutation
#
# https://leetcode.com/problems/next-permutation/description/
#
# algorithms
# Medium (40.24%)
# Likes:    18666
# Dislikes: 4751
# Total Accepted:    1.5M
# Total Submissions: 3.6M
# Testcase Example:  '[1,2,3]'
#
# A permutation of an array of integers is an arrangement of its members into a
# sequence or linear order.
# 
# 
# For example, for arr = [1,2,3], the following are all the permutations of
# arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
# 
# 
# The next permutation of an array of integers is the next lexicographically
# greater permutation of its integer. More formally, if all the permutations of
# the array are sorted in one container according to their lexicographical
# order, then the next permutation of that array is the permutation that
# follows it in the sorted container. If such arrangement is not possible, the
# array must be rearranged as the lowest possible order (i.e., sorted in
# ascending order).
# 
# 
# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does
# not have a lexicographical larger rearrangement.
# 
# 
# Given an array of integers nums, find the next permutation of nums.
# 
# The replacement must be in place and use only constant extra memory.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3]
# Output: [1,3,2]
# 
# 
# Example 2:
# 
# 
# Input: nums = [3,2,1]
# Output: [1,2,3]
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,1,5]
# Output: [1,5,1]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100
# 
# 
#

# @lc code=start

        
class Solution(object):
    def nextPermutation(self, nums):
        # nums = [0, 1, 2, 5, 3, 3, 0]
        # find longest non-increasing suffix, 相当于找到 [5, 3, 3, 0]
        # 因为这一部分里面交换也不能得到更大的了， 必须和 5 之前的交换

        right = len(nums)-1
        while nums[right] <= nums[right-1] and right-1 >=0:
            right -= 1

        if right == 0: # 一直找到最左面， 说明整个nums由大到小
            return self.reverse(nums,0,len(nums)-1)
        
        
        swap_x = right-1 # right 左边的是需要交换的， [0, 1, 2, 5, 3, 3, 0] 就是 2

        # 那 swap_y 在哪里呢， 上面的 2 和 [5, 3, 3, 0] 里面的哪个交换呢？

        swap_y = 0
        # find rightmost number > swap_x, 找到最右边比 2 大的数字，上面就是最后一个 3
        for i in range(len(nums)-1, swap_x, -1):
            if nums[i] > nums[swap_x]:
                swap_y = i
                break # 找到了

        # swap pivot and 最右边比它大的， 得到 [0, 1, 3, 5, 3, 2, 0]
        nums[swap_x], nums[swap_y] = nums[swap_y], nums[swap_x]
        # reverse pivot 右边的， 就是 reverse [5, 3, 2, 0] -> [0, 2, 3, 5]
        self.reverse(nums, swap_x+1, len(nums)-1)
        
    def reverse(self,nums,l,r):
        while l < r:
            nums[l],nums[r] = nums[r],nums[l]
            l += 1
            r -= 1





# @lc code=end

