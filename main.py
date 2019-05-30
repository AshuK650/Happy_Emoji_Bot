import time as t 
import credentials
#import tweepy 
import tweet



#interval_int = 60 * 60 * 4  # 4 hours
interval_int = 60 * 15  # 15 minutes 

credentials = credentials.get_credentials() 


# Twitter authentication set up goes here 
#auth = tweetpy.OAuthHandler(credentials["CONSUMER_KEY"], credentials["CONSUMER_SECRET"])
#auth.set_access_token(credentials["ACCESS_KEY"], credentials["ACCESS_SECRET"])
#api = tweepy.API(auth)

# loop to tweet ever 4 hours 
while True: 
    tweet_str = tweet.get_tweet() 
    
    print(tweet_str)    
    
    t.sleep(interval_int) 

