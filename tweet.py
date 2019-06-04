import random as r 
from unicode_codes import EMOJI_LIST as emoji_list

def get_rand_emoji():
    
    rand_emoji = "   "
    
    while len(rand_emoji) != 1: 
        rand_int = r.randint(0, len(emoji_list))
        
        try: 
            rand_name = emoji_list[rand_int][0]
        except IndexError: 
            rand_name = "Name Not Found" 
        
        try: 
            rand_emoji = emoji_list[rand_int][1]
        except IndexError: 
            rand_emoji = "\U0001F3EB"
            rand_name = "School"
        
    
    return (rand_name, rand_emoji)

 
def get_tweet(): 
    emoji_tuples = [] 
    
    for i in range(2):  
        emoji_tuples.append(get_rand_emoji())
        
    name1_str = emoji_tuples[0][0].strip(":").replace("_", " ").title() 
    name2_str = emoji_tuples[1][0].strip(":").replace("_", " ").title() 
    
    emoji1_str = emoji_tuples[0][1].encode("utf-8", "ignore").decode("utf-8", "ignore")
    emoji2_str = emoji_tuples[1][1].encode("utf-8", "ignore").decode("utf-8", "ignore")
    
    emoji_str = "{} and {}".format(name1_str, name2_str)
    
    happy_face = """
        
            00        00 
            00        00
            00        00  
            00        00  
             
            
        11                11
          11            11
            11        11
                1111 
    """
    
 
             
    
    tweet_str = emoji_str + happy_face.replace("0", emoji1_str).replace("1", emoji2_str)
    
    while len(tweet_str.strip()) > 280: 
        tweet_str = get_tweet() 
    
    return tweet_str.strip() 
    

if __name__ == "__main__": 
    get_tweet()
