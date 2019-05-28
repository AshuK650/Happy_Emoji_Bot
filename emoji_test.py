from unicode_codes import EMOJI_ALIAS_UNICODE 
import random 


#print(e.EMOJI_ALIAS_UNICODE)
emoji_dict = EMOJI_ALIAS_UNICODE 


emoji_list = [(k,v) for (k,v) in emoji_dict.items()]

for i in range(10): 
    rand_int = random.randint(0, len(emoji_list))
    
    rand_emoji = emoji_list[rand_int][1]
    
    output_str = rand_emoji.encode("unicode-escape").decode("ASCII")
    
    rand_name = emoji_list[rand_int][0].strip(":").replace("_", " ")
    
    # output_str is the emoji unicode to use 
    print(rand_name, output_str) 
