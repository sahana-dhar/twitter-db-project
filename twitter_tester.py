## testing the two separate functions


import os
from twitter_api import TwitterAPI
from twitter_objects import Tweet, Follows


def main():

    # Authenticate
    api = TwitterAPI()

    ex_user = api.getAllUsers()[0]

    # post new tweet
    api.postTweet(user_id=ex_user, tweet_text="hello tweet world")
    api.postTweet(user_id=ex_user, tweet_text="hello tweet world 2")

    # Get home timeline
    tweets_timeline = api.getHomeTimeline(ex_user)
    for t in tweets_timeline:
        print(t)

if __name__ == '__main__':
    main()