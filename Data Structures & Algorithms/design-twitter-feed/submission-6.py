class Twitter:

    def __init__(self):
        self.next_tweet_id = 1
        self.user_to_tweets = defaultdict(list)
        self.follower_to_creators = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.next_tweet_id += 1
        self.user_to_tweets[userId].append((self.next_tweet_id, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        self.follower_to_creators[userId].add(userId)
        res = []
        candidates = []
        for creator in self.follower_to_creators[userId]:
            if self.user_to_tweets[creator]:
                heapq.heappush_max(candidates, (self.user_to_tweets[creator][-1], creator, len(self.user_to_tweets[creator]) - 2))

        while len(res) < 10 and candidates:
            id, creator, index = heapq.heappop_max(candidates)
            heapq.heappush(res, id)
            if index >= 0:
                heapq.heappush_max(candidates, (self.user_to_tweets[creator][index], creator, index - 1))
        while len(res) > 10:
            heapq.heappop(res)
        final = [heapq.heappop(res)[1] for _ in range(len(res))]
        final.reverse()
        return final


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower_to_creators[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follower_to_creators[followerId].discard(followeeId)
