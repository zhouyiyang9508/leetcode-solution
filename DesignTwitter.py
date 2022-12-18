import collections
from typing import List
from heapq import *

class Twitter:

    def __init__(self):
        self.following = collections.defaultdict(set)
        self.user_tweets = collections.defaultdict(collections.deque)
        self.timer = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timer += 1
        tweets = self.user_tweets[userId]
        tweets.append((self.timer, tweetId))
        if len(tweets) > 10:
            tweets.popleft()

    def getNewsFeed(self, userId: int) -> List[int]:
        h = []
        # get user's own tweets
        u = self.user_tweets[userId]
        h.extend(u)
        heapify(h)

        for user in self.following[userId]:
            other_user_tweets = self.user_tweets[user]
            for x in range(len(other_user_tweets)):
                if len(h) < 10:
                    heappush(h, other_user_tweets[x])
                else:
                    if h[0][0] < other_user_tweets[x][0]:
                        heappushpop(h, other_user_tweets[x])

        return [heappop(h)[1] for x in range(len(h))][::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.following[followerId].remove(followeeId)


if __name__ == '__main__':
    twitter = Twitter()
    twitter.postTweet(1, 5)
    print(twitter.getNewsFeed(1) == [5])
    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    print(twitter.getNewsFeed(1) == [6, 5])
    twitter.unfollow(1, 2)
    print(twitter.getNewsFeed(1) == [5])

