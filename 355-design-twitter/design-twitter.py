class Twitter:

    def __init__(self):
        self.tweets = {}    # userId -> [(ts, tweetId)], user posted
        # self.newsFeed     # userId -> followers posted
        self.time = 0
        # userId -> following, follows itself
        self.following = collections.defaultdict(set)
        

    # O(1)      make this exp or make the next exp
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = collections.deque([])
        self.tweets[userId].append((self.time, tweetId))
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].popleft()
        self.time += 1

    # O(num_followers * 10)
    def getNewsFeed(self, userId: int) -> list[int]:
        self.recentTweets = []
        for f in list(self.following[userId]) + [userId]:
            for ts, tweet in self.tweets.get(f, []):        # add 10 tweets from all followers
                heapq.heappush(self.recentTweets, (ts, tweet))
                if len(self.recentTweets) > 10:
                    heapq.heappop(self.recentTweets)    # pop the old tweet

        mostRecent = []
        while self.recentTweets:
            mostRecent.append(heapq.heappop(self.recentTweets)[1])
        return mostRecent[::-1]
        
    # O(1)
    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    # O(1)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)      # doesn't return error like remove


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)