import time as t 
import credentials as c
#import tweepy 
import tweet


credentials = c.get_credentials()

#interval_int = 60 * 60 * 4  # 4 hours
interval_int = 60 * 15  # 15 minutes  

# Twitter authentication set up goes here 

#auth = tweetpy.OAuthHandler(credentials["CONSUMER_KEY"], credentials["CONSUMER_SECRET"])
#auth.set_access_token(credentials["ACCESS_KEY"], credentials["ACCESS_SECRET"])
#api = tweepy.API(auth)

# loop to tweet ever 4 hours 
while True: 
    tweet_str = tweet.get_tweet() 
    
    print(tweet_str) # replace this line with tweepy's update status function    
    
    t.sleep(interval_int) 

