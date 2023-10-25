class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list)   # userId - list of (count, tweetIds)
        self.follows = defaultdict(set)     # userId - followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time += 1    

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap = []
        res = []

        self.follows[userId].add(userId)        # user follows himself
        for followeeId in self.follows[userId]:  
            if followeeId in self.tweetMap:  # this guy has some tweets
                idx = len(self.tweetMap[followeeId]) - 1
                time, tweetId = self.tweetMap[followeeId][-1] # take last tweet
                heapq.heappush(min_heap, (-time, tweetId, followeeId, idx))

        while min_heap and len(res) < 10:
            _, tweetId, followeeId, idx = heapq.heappop(min_heap)
            res.append(tweetId)
            if idx > 0:  # more tweet available under the followeeId
                new_idx = idx - 1
                time, tweetId = self.tweetMap[followeeId][new_idx]
                heapq.heappush(min_heap, (-time, tweetId, followeeId, new_idx))
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)