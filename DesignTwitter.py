import collections
import itertools
from typing import List

# class Twitter:
#
#     def __init__(self):
#
#
#     def postTweet(self, userId: int, tweetId: int) -> None:
#
#
#     def getNewsFeed(self, userId: int) -> List[int]:
#
#     def follow(self, followerId: int, followeeId: int) -> None:
#
#     def unfollow(self, followerId: int, followeeId: int) -> None:

if __name__ == '__main__':
    user_tweets = collections.defaultdict(collections.deque)
    tweets = user_tweets[1]
    tweets.append(((1), 123))
    print(type(tweets))
