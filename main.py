import credentials, tweepy, tweet

c = credentials.get_credentials()

auth = tweepy.OAuthHandler(c["CONSUMER_KEY"], c["CONSUMER_SECRET"])
auth.set_access_token(c["ACCESS_KEY"], c["ACCESS_SECRET"])
api = tweepy.API(auth)

count = 0 

while True: 
    try: 
        tweet_str = tweet.get_tweet() 
        api.update_status(tweet_str)
        
        print(tweet_str) 
        print(len(tweet_str))
        
        count += 1 
        break
        
    except (Exception, tweepy.TweepError): 
        print("An Error was found.")
        count += 1 

if count == 1: 
    print("Execution Complete: {} attempt were made.".format(count))
else: 
    print("Execution Complete: {} attempts were made.".format(count))