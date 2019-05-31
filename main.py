import time as t 
import credentials as c
import tweepy 
import tweet


credentials = c.get_credentials()
interval_int = 60 * 60 * 4  # 4 hours


# Twitter authentication set up goes here 
auth = tweepy.OAuthHandler(credentials["CONSUMER_KEY"], credentials["CONSUMER_SECRET"])
auth.set_access_token(credentials["ACCESS_KEY"], credentials["ACCESS_SECRET"])
api = tweepy.API(auth)


# loop to tweet ever 4 hours 
while True: 
    tweet_str = tweet.get_tweet() 
    
    api.update_status(tweet_str)
    
    t.sleep(interval_int) 
