## creates db
import sqlite3
import csv

def create_database():
    conn = sqlite3.connect('twitter.db')
    cursor = conn.cursor()
    
    cursor.execute("DROP TABLE IF EXISTS TWEET")
    cursor.execute("DROP TABLE IF EXISTS FOLLOWS")
    
    cursor.execute("""
        CREATE TABLE TWEET (
            tweet_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            tweet_ts DATETIME,
            tweet_text VARCHAR(140)) """)
    
    cursor.execute("""
        CREATE TABLE FOLLOWS (
            follower_id INTEGER,
            followee_id INTEGER,
            PRIMARY KEY (follower_id, followee_id))""")
    
    cursor.execute("CREATE INDEX idx_tweet_user_ts ON TWEET(user_id, tweet_ts DESC)")
    cursor.execute("CREATE INDEX idx_follows_follower ON FOLLOWS(follower_id)")
    
    conn.commit()
    conn.close()

def load_follows():
    conn = sqlite3.connect('twitter.db')
    cursor = conn.cursor()
    
    with open('follows.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        
        follows_data = [(int(row[0]), int(row[1])) for row in reader]
    
    cursor.executemany("INSERT INTO FOLLOWS VALUES (?, ?)", follows_data)
    conn.commit()
    conn.close()
    
    print(f"{len(follows_data)} follows inserted")

if __name__ == "__main__":
    create_database()
    load_follows()