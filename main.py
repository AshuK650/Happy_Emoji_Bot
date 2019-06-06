import time as t 
import random as r
import credentials 
import tweepy 
import tweet

c = credentials.get_credentials()

auth = tweepy.OAuthHandler(c["CONSUMER_KEY"], c["CONSUMER_SECRET"])
auth.set_access_token(c["ACCESS_KEY"], c["ACCESS_SECRET"])
api = tweepy.API(auth)

while True: 
    
    rand_hour = r.randint(1,4) 
    rand_min = r.randint(1,60) 
    rand_sec = r.randint(1,60) 
    
    interval_int = (rand_hour * 60 * 60)  + (rand_min * 60) + rand_sec
    
    try: 
        tweet_str = tweet.get_tweet() 
        api.update_status(tweet_str)
        
        print(tweet_str)
        print(len(tweet_str))
        print("Next tweet in: {} hours, {} minutes, and {} seconds.".format(rand_hour, rand_min, rand_sec))
                
    except (Exception, tweepy.TweepError): 
        print("Exception Occured. Just wait for the next tweet ")
        print("Next tweet in: {} hours, {} minutes, and {} seconds.".format(rand_hour, rand_min, rand_sec))
    
    t.sleep(interval_int) 
