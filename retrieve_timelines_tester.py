# test retrieving timelines from random user

import os
from twitter_api import TwitterAPI
from twitter_objects import Tweet, Follows
import time
import random

def main():
    print('test')
    start_time = time.time()
    # Authenticate
    api = TwitterAPI()
    all_users = api.getAllUsers()

    count = 0

    # for one minute, continue as many times as possible
    while time.time() - start_time <= 5:
        random_user = random.choice(all_users)
        tweets_timeline = api.getHomeTimeline(random_user)
        count+=1

    print(count)

if __name__ == '__main__':
    main()