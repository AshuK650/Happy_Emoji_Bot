import credentials as c 
import tweepy 
import tweet


credentials = c.get_credentials()

auth = tweepy.OAuthHandler(credentials["CONSUMER_KEY"], credentials["CONSUMER_SECRET"])
auth.set_access_token(credentials["ACCESS_KEY"], credentials["ACCESS_SECRET"])
api = tweepy.API(auth)
      
try: 
    tweet_str = tweet.get_tweet() 
    api.update_status(tweet_str)
    
except TweepError: 
    api.update_status("Sorry! Check again tomorrow \U0001f600")
    