#import credentials as c 
import time as t 
import tweepy 
import tweet
from os import environ

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

#credentials = c.get_credentials()
interval_int = 60 * 60 * 3 

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True: 
    
    try: 
        tweet_str = tweet.get_tweet() 
        api.update_status(tweet_str)
        
        # used for the bash console
        print(tweet_str)
        print(len(tweet_str))

    except tweepy.TweepError: 
        rand_emoji_tuple = tweet.get_rand_emoji() 
        rand_emoji = rand_emoji_tuple[1]
        
        tweet_str = "Sorry check again later {}".format(rand_emoji.encode("utf-8", "ignore").decode("utf-8", "ignore"))
        api.update_status(tweet_str) 
        
        # used for the bash console 
        print(tweet_str)
        
        
    t.sleep(interval_int) 