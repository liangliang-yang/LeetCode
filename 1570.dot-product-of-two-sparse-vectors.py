#
# @lc app=leetcode id=1570 lang=python
#
# [1570] Dot Product of Two Sparse Vectors
#
# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/description/
#
# algorithms
# Medium (89.83%)
# Likes:    1210
# Dislikes: 146
# Total Accepted:    270.4K
# Total Submissions: 301K
# Testcase Example:  '[1,0,0,2,3]\n[0,3,0,4,0]'
#
# Given two sparse vectors, compute their dot product.
# 
# Implement class SparseVector:
# 
# 
# SparseVector(nums) Initializes the object with the vector nums
# dotProduct(vec) Compute the dot product between the instance of SparseVector
# and vec
# 
# 
# A sparse vector is a vector that has mostly zero values, you should store the
# sparse vector efficiently and compute the dot product between two
# SparseVector.
# 
# Follow up: What if only one of the vectors is sparse?
# 
# 
# Example 1:
# 
# 
# Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
# Output: 8
# Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
# v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8
# 
# 
# Example 2:
# 
# 
# Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
# Output: 0
# Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
# v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0
# 
# 
# Example 3:
# 
# 
# Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
# Output: 6
# 
# 
# 
# Constraints:
# 
# 
# n == nums1.length == nums2.length
# 1 <= n <= 10^5
# 0 <= nums1[i], nums2[i] <= 100
# 
# 
#

# @lc code=start


class SparseVector:
    def __init__(self, nums):
        self.dic = {}

        for i, val in enumerate(nums): # store non-zero {index: value}
            if val != 0:
                self.dic[i] = val

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        res = 0

        # # v1.dotProduct(v2), we want v1 has less non-zero digits
        if len(self.dic) <= len(vec.dic):
            A, B = self.dic, vec.dic
        else:
            A, B = vec.dic, self.dic

        for key, value in A.items():
            product = value * B.get(key, 0)
            res += product

        return res
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)



# @lc code=end

