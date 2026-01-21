## testing the two separate functions


import os
from twitter_api import TwitterAPI
from twitter_objects import Tweet, Follows

def main():

    # Authenticate
    api = TwitterAPI()

    ex_user = api.getAllUsers()[0]

    # Get home timeline
    tweets_timeline = api.getHomeTimeline(ex_user)
    for t in tweets_timeline:
        print(t)

    # post new tweet
    twee = Tweet(ex_user, "hello tweet world")
    api.postTweet(twee)


if __name__ == '__main__':
    main()