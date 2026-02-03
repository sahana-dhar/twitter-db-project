"""
filename: twitter_tester.py

description: A main tester function to test both:
    - How many tweets can we post per second?
    - How many timelines can we retrieve per second?

API call functions written by Anya
Rate logic written by Sahana
"""

import os
# from twitter_api import TwitterAPI
from twitter_api_redis import TwitterAPI
from twitter_objects import Tweet, Follows
import time
import random

def main():
    # API
    api = TwitterAPI()

    """
    Test 1: How many tweets can we post per second?
    """
    # use sample tweets file
    csv_file = 'tweets_sample.csv'
    # start count
    count_tweets = 0

    # open file and post all tweets
    with open(csv_file, 'r', encoding='utf-8') as f:
        # discard header
        next(f)
        # start timer for test 1
        start_time = time.time()

        for line in f:
            user_id, tweet_text = line.strip().split(',', 1)
            api.postTweet(int(user_id), tweet_text)
            count_tweets += 1

        end_time = time.time()
    duration = end_time - start_time

    print(f'tweets posted: {count_tweets}')
    print(f'duration: {duration:.4f} sec')
    print(f'rate: {count_tweets / duration:.2f} tweets/sec')

    """
    Test 2: How many timelines can we retrieve per second?
    """
    # list of all users to select from randomly
    all_users = api.getAllUsers()
    # start count
    count_timelines = 0
    # start timer for test 2
    start_time = time.time()

    # for one second, retrieve as many timelines as possible
    while time.time() - start_time <= 5:
        # select random user and retrieve timeline
        random_user = random.choice(all_users)
        tweets_timeline = api.getHomeTimeline(random_user)
        count_timelines += 1
    end_time = time.time()
    duration = end_time - start_time

    print(f'timelines retrieved: {count_timelines}')
    print(f'duration: {duration:.4f} sec')
    print(f'rate: {count_timelines / duration:.2f} timelines/sec')

if __name__ == '__main__':
    main()