#
# @lc app=leetcode id=355 lang=python
#
# [355] Design Twitter
#

# @lc code=start
# https://leetcode.com/problems/design-twitter/solutions/4711886/68-1-approach-1-o-n-log-k-python-c-step-by-step-explanation/

from collections import defaultdict
import heapq

class Twitter:
    def __init__(self):
        # Initialize a global counter to track tweet timestamps
        self.count = 0
        # Initialize tweetMap to store user tweets: userId -> list of [count, tweetIds]
        self.tweetMap = defaultdict(list)
        # Initialize followMap to store user relationships: userId -> set of followeeId
        self.followMap = defaultdict(set)

    def postTweet(self, userId, tweetId):
        # Append the tweet with its timestamp to the user's tweetMap
        self.tweetMap[userId].append([self.count, tweetId])
        # Decrement the count to simulate decreasing timestamps for newer tweets
        self.count -= 1

    def getNewsFeed(self, userId):
        # Initialize an empty list to store the result
        res = []
        # Initialize a min heap to store the most recent tweets from followed users
        minHeap = []

        # Ensure that the user follows themselves
        self.followMap[userId].add(userId)
        
        # Iterate over users followed by the given userId
        for followeeId in self.followMap[userId]:
            # Check if the followee has any tweets
            if followeeId in self.tweetMap:
                # Get the index of the most recent tweet from the followee
                index = len(self.tweetMap[followeeId]) - 1
                # Retrieve the count and tweetId of the tweet
                count, tweetId = self.tweetMap[followeeId][index]
                # Push the tweet onto the min heap along with additional information
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        # Retrieve the 10 most recent tweets from the min heap
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            # Append the tweetId to the result list
            res.append(tweetId)
            # If the followee has more tweets, push the next tweet onto the min heap
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        # Return the result list containing the 10 most recent tweets
        return res

    def follow(self, followerId, followeeId):
        # Add the followeeId to the set of users followed by the followerId
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        # Remove the followeeId from the set of users followed by the followerId
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

