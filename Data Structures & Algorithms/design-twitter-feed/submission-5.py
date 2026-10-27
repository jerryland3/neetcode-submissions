from collections import defaultdict
import heapq
class Twitter:
    def __init__(self):
        self.userTweet = defaultdict(list)
        self.userFollow = defaultdict(set)
        self.time = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweet[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        for followeeId in self.userFollow[userId]:
            index = len(self.userTweet[followeeId]) - 1
            if index > -1:
                time, tweetId = self.userTweet[followeeId][index]
                minHeap.append((-time, tweetId, followeeId, index - 1))
        
        index = len(self.userTweet[userId]) - 1
        if index > -1:
            time, tweetId = self.userTweet[userId][index]
            minHeap.append((-time, tweetId, userId, index - 1))
        
        heapq.heapify(minHeap)
        output = []
        while len(output) < 10 and minHeap:
            _, tweetId, userId, index = heapq.heappop(minHeap)
            output.append(tweetId)
            if index > -1:
                time, tweet = self.userTweet[userId][index]
                heapq.heappush(minHeap, (-time, tweet, userId, index - 1))
        
        return output

        
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.userFollow[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.userFollow[followerId].discard(followeeId)
   
"""
[u1 u2 u3]
[p1 p2 p3]

1 5 8
2 6
4 7

                  (8, tweet7, u1, 2)
    (6, tweet4, u2, 1)            (7, tweet6, u3, 1)


Twitter() - initalize twitter object

PostTweet(userId, tweetId) - publish a new tweet for user ID with tweet ID, each tweetId is unique
    - need to store tweets associated with user, dictionary is good for fast access
      {
      user1: [(1, tweet1) (5, tweet2) (8, tweet7)]
      user2: [(2, tweet3) (6, tweet4)]
      user3: [(4, tweet5) (7, tweet6)]
      }
    - O(1) time


getNewsFeed(userId) - fetch 10 most recent tweet ID in the user news feed (including user itself and the followings). order from most recent to least
    - indicate we need to also be able to fetch the users followings, can use a dictionary as well
      {
      user1: [user2 user3]
      user2: [...]
      }
    
    - use max heap to store the tweets from the user list, heap size is the size of the user + followings
    
    - outer while loop (tweetList < 10 and sum(UserIndex) > 0)
    

follow(followerId, followeeID) - user with ID FollowerId follows followeeId
    - add to the dictionary value list follow[followerId].append(followeeId)
    - O(1) time

unfollow(followerId, followeeID) - user followerId unfollows followeeID
    - remove from follow dictionary, follow[followerId].discard(followeeId)
    - O(1) time

Space complexity is O(n + m), where n is the number of users and m is the number of tweets for the two dictionary.
"""