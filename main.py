import time as t 
from credentials import get_credentials
#import tweepy 
from tweet import get_tweet


#interval_int = 60 * 60 * 4  # 4 hours

interval_int = 60 * 15  # 15 minutes 

# Twitter authentication set up goes here 

#auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
#auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
#api = tweepy.API(auth)


# loop to tweet ever 4 hours 
while True: 
    tweet_str = get_tweet() 
    
    print(tweet_str)
    # .set_status() or whatever from twitter api 
    
    t.sleep(interval_int) 