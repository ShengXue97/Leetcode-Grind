class Twitter:

    def __init__(self):
        # Map of userId -> (time, tweetId)
        self.tweets = defaultdict(list)
        # Map of follower userId -> followee userId
        self.follows = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.follows[userId].add(userId)
        for followeeId in self.follows[userId]:
            if len(self.tweets[followeeId]) > 0:
                tweets = self.tweets[followeeId]
                index = len(tweets) - 1
                time, tweetId = tweets[index]
                minHeap.append((time, tweetId, followeeId, index - 1))
        
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            time, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                newTime, newTweetId = self.tweets[followeeId][index]
                heapq.heappush(minHeap, (newTime, newTweetId, followeeId, index - 1))
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)