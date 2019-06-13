import time as t, random as r  
import credentials, tweepy, tweet 

c = credentials.get_credentials()

auth = tweepy.OAuthHandler(c["CONSUMER_KEY"], c["CONSUMER_SECRET"])
auth.set_access_token(c["ACCESS_KEY"], c["ACCESS_SECRET"])
api = tweepy.API(auth)

while True:
    rand_hour = r.randint(0,4) 
    rand_min = r.randint(0,60) 
    rand_sec = r.randint(0,60) 
    
    interval_int = (rand_hour * 3600)  + (rand_min * 60) + rand_sec
    
    try: 
        tweet_str = tweet.get_tweet() 
        api.update_status(tweet_str)
        
        print(tweet_str)
        print(str(len(tweet_str)) + "\n")
        print("Next tweet in: {} hours, {} minutes, and {} seconds".format(rand_hour, rand_min, rand_sec))       
                
    except (Exception, tweepy.TweepError): 
        print("Exception Occured. Just wait for the next tweet ")
        print("Next tweet in: {} hours, {} minutes, and {} seconds".format(rand_hour, rand_min, rand_sec))
    
    t.sleep(interval_int) 