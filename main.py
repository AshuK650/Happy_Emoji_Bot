import credentials as c 
import time as t 
import tweepy 
import tweet

credentials = c.get_credentials()
interval_int = 60 * 60 * 4 

auth = tweepy.OAuthHandler(credentials["CONSUMER_KEY"], credentials["CONSUMER_SECRET"])
auth.set_access_token(credentials["ACCESS_KEY"], credentials["ACCESS_SECRET"])
api = tweepy.API(auth)

while True: 
    
    try: 
        tweet_str = tweet.get_tweet() 
        api.update_status(tweet_str)
        
        # used for the bash console in pythonanywhere
        print(tweet_str)
        print(len(tweet_str))
        
    except: 
        api.update_status("Sorry! Check again later \U0001f600")
        print("Sorry! Check again later \U0001f600")
        
        
    t.sleep(interval_int) 