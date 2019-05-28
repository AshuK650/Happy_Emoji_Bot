import time as t 
from tweet import get_tweet

#interval_int = 60 * 60 * 4  # 4 hours

interval_int = 60 * 15  # 15 minutes 

# Twitter authentication set up goes here 



# loop to tweet ever 4 hours 
while True: 
    tweet_str = get_tweet() 
    
    print(tweet_str)
    # .set_status() or whatever from twitter api 
    
    t.sleep(interval_int) 