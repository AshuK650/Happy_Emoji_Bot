import credentials as c
import datetime as dt 
import time as t 
import tweepy 
import tweet


credentials = c.get_credentials()


# Twitter authentication set up goes here 
auth = tweepy.OAuthHandler(credentials["CONSUMER_KEY"], credentials["CONSUMER_SECRET"])
auth.set_access_token(credentials["ACCESS_KEY"], credentials["ACCESS_SECRET"])
api = tweepy.API(auth)


# loop to tweet ever 4 hours 
while True: 
    
    now_obj = dt.datetime.now() 
    
    if now_obj.hour % 4 == 0 and now_obj.minute == 0:  # tweet ever 4 hours 
        
        try: 
            tweet_str = tweet.get_tweet() 
            api.update_status(tweet_str)
            print(tweet_str)
            print(len(tweet_str))
            t.sleep(60)
            
        except TweepError: 
            api.update_status("Check Again Next Time \U0001f600")
            t.sleep(60)
            
            pass
        