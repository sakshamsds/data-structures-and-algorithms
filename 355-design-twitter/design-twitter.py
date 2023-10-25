'''
    A follows B, c, D
    A -> set(B, C, D)

    A is followed in B, C
    A -> set(B, C)
'''


class Twitter:

    def __init__(self):
        self.follows = defaultdict(set) # userId - follows mapping
        # self.followedBy = defaultdict(set) # userId - followed_by mapping
        # self.tweets = defaultdict(list)  # userId - tweets
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        # self.tweets[userId].add(tweetId)
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        # iterate tweets in reverse order
        # if user id is self or in follows list then populate feed
        res = []
        for uid, tid in self.tweets[::-1]:
            if uid == userId or uid in self.follows[userId]:
                res.append(tid)
            if len(res) == 10:
                break
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        # self.followedBy[followeeId].add(followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # discard doesn't throw error if item not found
        self.follows[followerId].discard(followeeId)
        # self.followedBy[followeeId].discard(followerId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)