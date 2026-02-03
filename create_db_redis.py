import redis
import csv

r = redis.Redis(decode_responses=True)
# clear existing data 
r.flushdb()

with open("follows_sample.csv") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    
    count = 0
    for follower_id, followee_id in reader:
        r.sadd(f"followers:{followee_id}", follower_id)
        r.sadd(f"following:{follower_id}", followee_id)  
        r.sadd("users", follower_id)
        r.sadd("users", followee_id)
        count += 1
    
    print(f"Loaded {count} follow relationships into Redis")
    print(f"Total users: {r.scard('users')}")