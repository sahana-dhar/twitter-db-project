"""
filename: create_db_redis.py

description: Setup script for REDIS Twitter database. Creates FOLLOWS table.

Written by Sahana
"""

import redis
import csv

r = redis.Redis(decode_responses=True)
r.flushdb() # clear existing data 

# load follows data from csv
with open("follows_sample.csv") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    
    count = 0
    for follower_id, followee_id in reader:
        
        # create a followers set for each followee_id in Redis
        r.sadd(f"followers:{followee_id}", follower_id)
        
        ## remove? - r.sadd(f"following:{follower_id}", followee_id)  - not used in api, only follower is

        # add follower_id/followee_id to a users set, Redis automatically removes duplicates
        r.sadd("users", follower_id)
        r.sadd("users", followee_id)
        count += 1
    
    print(f"Loaded {count} follow relationships into Redis")
    print(f"Total users: {r.scard('users')}")