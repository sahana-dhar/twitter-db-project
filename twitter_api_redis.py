"""
filename: twitter_api_redis.py

description: Twitter API implementation using Redis.
Provides methods for 
    - posting tweets
    - retrieving timelines
    - retrieving all users - used in tests

Written by Sahana (postTweet) and Anya (getHomeTimeline)
"""

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
        
        # store tweet data as hash  
        self.r.hset(
            f"tweet:{self.tweet_id}",
            mapping={
                "user_id": user_id,
                "tweet_ts": ts,
                "tweet_text": tweet_text
            }
        )
        ## remove? - self.r.sadd("users", user_id)
        
        # push tweet to all followers' timelines
        followers = self.r.smembers(f"followers:{user_id}")
        for follower in followers:
            self.r.lpush(f"timeline:{follower}", self.tweet_id)

            # keep only 10 tweets for faster timeline pulling
            self.r.ltrim(f"timeline:{follower}", 0, 9)
    
    def getHomeTimeline(self, user_id):
        # get tweet_ids for this user's timeline
        tweet_ids = self.r.lrange(f"timeline:{user_id}", 0, 9)

        # get tweet hashes from all tweet ids to return timeline
        return [self.r.hgetall(f"tweet:{tweet_id}") for tweet_id in tweet_ids]

    def getAllUsers(self):
        return list(self.r.smembers("users")) # return Redis set of users as list