"""
filename: twitter_tester.py

description: A main tester function to test both:
    - How many tweets can we post per second?
    - How many timelines can we retrieve per second?
"""

import os
from twitter_api import TwitterAPI
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
    count_tweets = 0 # starting count

    # open file and post as many tweets as possible
    with open(csv_file, 'r', encoding='utf-8') as f:
        next(f)
        # start timer for test 1
        start_time = time.time()
        # for one second, post as many tweets as possible
        for line in f:
            if time.time() - start_time <= 1:
                user_id, tweet_text = line.strip().split(',', 1)
                api.postTweet(int(user_id), tweet_text)
                count_tweets += 1
            else:
                break

    print(f'tweets posted: {count_tweets}')
    print(f'rate: {count_tweets} tweets/sec')

    """
    Test 2: How many timelines can we retrieve per second?
    """
    # list of all users to select from randomly
    all_users = api.getAllUsers()
    count_timelines = 0 # start count
    # start timer for test 2
    start_time = time.time()

    # for one second, retrieve as many timelines as possible
    while time.time() - start_time <= 1:
        random_user = random.choice(all_users)  # select random user
        tweets_timeline = api.getHomeTimeline(random_user)
        count_timelines+= 1

    print(f'timelines retrieved: {count_timelines}')
    print(f'rate: {count_timelines} timelines/sec')

if __name__ == '__main__':
    main()