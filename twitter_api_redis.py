# twitter_api_redis.py
import redis
import time
from twitter_objects import Tweet

class TwitterAPI:
    def __init__(self):
        self.r = redis.Redis(decode_responses=True)
        self.tweet_id = 0
    
    def postTweet(self, user_id, tweet_text):
        self.tweet_id += 1
        ts = time.time()
        
        # Store tweet data 
        self.r.hset(
            f"tweet:{self.tweet_id}",
            mapping={
                "user_id": user_id,
                "tweet_ts": ts,
                "tweet_text": tweet_text
            }
        )
        self.r.sadd("users", user_id)
        
        # Push tweet to all followers' timelines
        followers = self.r.smembers(f"followers:{user_id}")
        for follower in followers:
            self.r.lpush(f"timeline:{follower}", self.tweet_id)
            self.r.ltrim(f"timeline:{follower}", 0, 9) 
    
    def getHomeTimeline(self, user_id):
        # todo: Implement timeline retrieval
        pass
    
    def getAllUsers(self):
        return [int(u) for u in self.r.smembers("users")]