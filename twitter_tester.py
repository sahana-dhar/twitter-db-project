## testing the two separate functions


import os
from twitter_api import TwitterAPI
from twitter_objects import Tweet, Follows

def main():
    print('test')
    start_time = time.time()
    # Authenticate
    api = TwitterAPI()
    ex_user = api.getAllUsers()[0]

    # post new tweet
    api.postTweet(user_id=ex_user, tweet_text="hello tweet world")
    api.postTweet(user_id=ex_user, tweet_text="hello tweet world 2")

    # Get home timeline
    tweets_timeline = api.getHomeTimeline(ex_user)
    print('home timeline')
    print(f'time:{time.time() - start_time:.4f}s')
    for t in tweets_timeline:
        print(t)

    # post new tweet
    twee = Tweet(ex_user, "hello tweet world")
    api.postTweet(twee)


if __name__ == '__main__':
    main()