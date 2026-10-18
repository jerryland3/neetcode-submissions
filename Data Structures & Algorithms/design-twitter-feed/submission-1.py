from collections import defaultdict
import heapq
class Twitter:
    def __init__(self):
        self.time: int = 0
        self.users = defaultdict(list)
        self.usersFollow = defaultdict(set)
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        tweetTup = (-self.time, tweetId)
        heapq.heappush(self.users[userId], tweetTup)

    def getNewsFeed(self, userId: int) -> List[int]:
        tempDict = defaultdict(list)
        allUsers = [userId]
        for followeeId in self.usersFollow[userId]:
            allUsers.append(followeeId)
        
        output = []
        while len(output) < 10 and not self.allHeapEmpty(allUsers):
            mostRecentTime = 0
            mostRecentUser = None
            for userId in allUsers:
                if len(self.users[userId]) > 0 and self.users[userId][0][0] < mostRecentTime:
                    mostRecentUser = userId
                    mostRecentTime = self.users[userId][0][0]
            
            tweetTup = heapq.heappop(self.users[mostRecentUser])
            output.append(tweetTup[1])
            tempDict[mostRecentUser].append(tweetTup)
        
        for userId, tweetTups in tempDict.items():
            for tweetTup in tweetTups:
                heapq.heappush(self.users[userId], tweetTup)
            
        return output
    
    def allHeapEmpty(self, allUsers: list) -> bool:
        for userId in allUsers:
            if len(self.users[userId]) != 0:
                return False
        return True

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.usersFollow[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.usersFollow[followerId].discard(followeeId)
        
"""
allFeedHeap = [heap1, heap2, ...] (time, tweetId)


users dict keep track of each users tweet. 
    - key is user ID
    - value is (time, tweetId) tuple in a maxHeap
    - Post Tweet is O(log(m)) operation, where m is the size of individual heap

the users that a user follow is stored in usersFollow dict
    - a set is used to keep track of the userId that the current user is following
    - follow is O(1) opertion
    - unfollow is also O(1) operation

get news feed:
    - need to retrieve the user's feed
    - need to also retrieve all the followeeId
    - find the 10 most recent tweets from the user and the followee's
        - get the current userId and all of its followeeId
        - loop through all the ID and find which have most recent tweet
        - pop that tweet from his/her heap and append tweet id to output
        - put that (time, tweetId) tuple in a temp dictionary
        - keep doing this unti either all their heap are empty or output is length 10
        - put all tweet in temporary dictionary back into the heap
        - time complexity should be O(20log(m)), where m is the size of the heap 
                      
user heap [(10, tw1) (7, tw2) (5, tw3)]
followee1 [(6, tw5) (8, tw4)]  
followee2 [(9, tw7) (11, tw6)]

[userId, followee1Id, followee2Id]

tempDict = {
    user: []
    followee1: []
    followee2: []
}
"""