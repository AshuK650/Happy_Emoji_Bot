import credentials, tweepy, tweet


c = credentials.get_credentials()

auth = tweepy.OAuthHandler(c["CONSUMER_KEY"], c["CONSUMER_SECRET"])
auth.set_access_token(c["ACCESS_KEY"], c["ACCESS_SECRET"])
api = tweepy.API(auth)

try: 
    tweet_str = tweet.get_tweet() 
    api.update_status(tweet_str)
    
    print(tweet_str)
    print(str(len(tweet_str)) + "\n")
            
except (Exception, tweepy.TweepError): 
    print("Exception Occured. Just wait for the next tweet ")

