import credentials, tweepy, tweet

c = credentials.get_credentials()

auth = tweepy.OAuthHandler(c["CONSUMER_KEY"], c["CONSUMER_SECRET"])
auth.set_access_token(c["ACCESS_KEY"], c["ACCESS_SECRET"])
api = tweepy.API(auth)

try: 
    tweet_str = tweet.get_tweet() 
    api.update_status(tweet_str)
    
    print("Execution Complete: No Errors")
except (Exception, tweepy.TweepError) as e: 
    print("Here's the problem: {}".format(e))