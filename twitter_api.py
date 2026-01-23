"""
filename: twitter_api.py

description: Twitter API implementation using SQLite database.
Provides methods for 
    - posting tweets
    - retrieving timelines
    - retrieving all users

Written by Sahana
"""
from twitter_utils import DBUtils
from twitter_objects import Tweet, Follows

class TwitterAPI:
    def __init__(self, database="twitter.db"):
        self.dbu = DBUtils(database)
    
    def postTweet(self, user_id, tweet_text):
        sql = "INSERT INTO TWEET (user_id, tweet_text) VALUES (?, ?)"
        val = (user_id, tweet_text)
        self.dbu.insert_one(sql, val)
    
    def getHomeTimeline(self, user_id):
        sql = """
            SELECT t.tweet_id, t.user_id, t.tweet_ts, t.tweet_text
            FROM TWEET t
            JOIN FOLLOWS f ON t.user_id = f.followee_id
            WHERE f.follower_id = """ + str(user_id) + """
            ORDER BY t.tweet_ts DESC
            LIMIT 10
        """
        df = self.dbu.execute(sql)
        # extract tweets
        tweets = [Tweet(*df.iloc[i]) for i in range(len(df))]
        return tweets
    
    def getAllUsers(self):
        sql = "SELECT DISTINCT follower_id FROM FOLLOWS"
        df = self.dbu.execute(sql)
        return df['follower_id'].tolist()