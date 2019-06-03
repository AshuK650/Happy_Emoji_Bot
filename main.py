import credentials as c 
import time as t 
import tweepy 
import tweet

credentials = c.get_credentials()
interval_int = 60 * 60 * 3 

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

    except tweepy.TweepError: 
        rand_emoji_tuple = tweet.get_rand_emoji() 
        rand_emoji = rand_emoji_tuple[1]
        
        tweet_str = "Sorry check again later {}".format(rand_emoji) 
        api.update_status(tweet_str) 
    
        
    t.sleep(interval_int) 
