import credentials as c 
import time as t 
import datetime as dt 
import tweepy 
import tweet

credentials = c.get_credentials()
interval_int = 60 * 60 * 4 

auth = tweepy.OAuthHandler(credentials["CONSUMER_KEY"], credentials["CONSUMER_SECRET"])
auth.set_access_token(credentials["ACCESS_KEY"], credentials["ACCESS_SECRET"])
api = tweepy.API(auth)

while True: 
    
    now_obj = dt.datetime.now() 
    
    hour_int = now_obj.hour + 4
    min_int = now_obj.minute
    sec_int = now_obj.second
    
    try: 
        tweet_str = tweet.get_tweet() 
        api.update_status(tweet_str)
        
        # used for the bash console in pythonanywhere
        print(tweet_str)
        print(len(tweet_str))
        
        if hour_int >= 12: 
            print("Next tweet at: {}:{}:{} PM".format(hour_int - 12, min_int, sec_int))
        else: 
            print("Next tweet at: {}:{}:{} PM".format(hour_int, min_int, sec_int))
    except: 
        api.update_status("Sorry! Check again later \U0001f600")
        print("Sorry! Check again later \U0001f600")
        
        if hour_int >= 12: 
            print("Next tweet at: {}:{}:{} PM".format(hour_int - 12, min_int, sec_int))
        else: 
            print("Next tweet at: {}:{}:{} PM".format(hour_int, min_int, sec_int))
        
    t.sleep(interval_int) 