import credentials, tweepy, tweet

c = credentials.get_credentials()

auth = tweepy.OAuthHandler(c["CONSUMER_KEY"], c["CONSUMER_SECRET"])
auth.set_access_token(c["ACCESS_KEY"], c["ACCESS_SECRET"])
api = tweepy.API(auth)

try: 
    tweet_str = tweet.get_tweet() 
    api.update_status(tweet_str)
    
    print(tweet_str) 
    print(len(tweet_str)) 
    print("Execution Complete")
except (Exception, tweepy.TweepError): 
    print("Just wait until tomorrow.")