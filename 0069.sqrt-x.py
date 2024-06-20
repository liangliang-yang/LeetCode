#
# @lc app=leetcode id=69 lang=python
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 0, x + 1
        
        # search for minimal K satisfying condition k^2 > x
        while left < right:
            mid = left + (right - left) // 2
            if mid * mid > x:
                right = mid
            else:
                left = mid + 1
        
        # K-1 is the answer
        return left - 1  # `left` is the minimum k value, `k - 1` is the answer
    
    
        
# @lc code=end

