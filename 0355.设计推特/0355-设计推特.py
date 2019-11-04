# from https://leetcode-cn.com/problems/design-twitter/comments/14851
# awesome
import itertools
import collections
import heapq
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.twitts = collections.defaultdict(collections.deque)
        self.follows = collections.defaultdict(set)
        self.timestap = 2**31 # big enough

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.timestap -= 1
        self.twitts[userId].appendleft((self.timestap, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        tweets = heapq.merge(*(self.twitts[user] for user in (self.follows[userId] | {userId })))
        return [Id for _,Id in itertools.islice(tweets, 10)]
    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self.follows[followerId].discard(followeeId)                               
                                       
                                
                                       
                                       
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)