#
# @lc app=leetcode id=218 lang=python
#
# [218] The Skyline Problem
#

# @lc code=start

# Solution 1:  Brute Force II, Sweep Line
# https://leetcode.com/problems/the-skyline-problem/editorial/

class Solution1:
    def getSkyline(self, buildings):
        # Collect and sort the unique positions of all the edges.
        positions = sorted(list(set([x for building in buildings for x in building[:2]])))
        
        # 'answer' for skyline key points
        answer = []
        
        # For each position, draw an imaginary vertical line.
        for position in positions:
            # current max height.
            max_height = 0
            
            # Iterate over all the buildings:
            for left, right, height in buildings:
                # Update 'max_height' if necessary.
                if left <= position < right:
                    max_height = max(max_height, height)
            
            # If its the first key point or the height changes, 
            # we add [position, max_height] to 'answer'.
            if not answer or max_height != answer[-1][1]:
                answer.append([position, max_height])
                
        # Return 'answer' as the skyline.
        return answer
    
# Time complexity: O(n^2)
# Space complexity: O(n)


# Solution: Sweep Line + Priority Queue
# https://leetcode.com/problems/the-skyline-problem/editorial/
import heapq

class Solution:
    def getSkyline(self, buildings):
        # Iterate over all buildings, for each building i,
        # add (position, i) to edges.
        edges = []
        for i, build in enumerate(buildings):
            edges.append([build[0], i])
            edges.append([build[1], i])

        # Sort edges by non-decreasing order.
        edges.sort()
     
        # Initailize an empty Priority Queue 'live' to store all the 
        # newly added buildings, an empty list answer to store the skyline key points.
        live, answer = [], []
        idx = 0
        
        # Iterate over all the sorted edges.
        while idx < len(edges):
            
            # Since we might have multiple edges at same x,
            # Let the 'curr_x' be the current position.
            curr_x = edges[idx][0]
            
            # While we are handling the edges at 'curr_x':
            # 这里用 while 是因为可能有多条边同时以 curr_x 为节点
            while idx < len(edges) and edges[idx][0] == curr_x:
                # The index 'b' of this building in 'buildings'
                b = edges[idx][1]
                
                # If this is a left edge of building 'b', we
                # add (height, right) of building 'b' to 'live'.
                if buildings[b][0] == curr_x:
                    right = buildings[b][1]
                    height = buildings[b][2]
                    heapq.heappush(live, [-height, right])
                    
                # If the tallest live building has been passed,
                # we remove it from 'live'.
                while live and live[0][1] <= curr_x:
                    heapq.heappop(live)
                idx += 1
            
            # Get the maximum height from 'live'.
            max_height = -live[0][0] if live else 0
            
            # If the height changes at this curr_x, we add this
            # skyline key point [curr_x, max_height] to 'answer'.
            if not answer or max_height != answer[-1][1]:
                answer.append([curr_x, max_height])
        
        # Return 'answer' as the skyline.
        return answer
    
# Time complexity: O(N logN)
# Space complexity: O(n)
              
        
# @lc code=end

