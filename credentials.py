def get_credentials(): 
    
    file_obj = open("credentials.txt") 
    
    credentials_dict = {} 
    
    for line in file_obj: 
        line = line.split(":") 
        
        credentials_dict[line[0].strip()] = line[1].strip() 
    
    return credentials_dict
    

if __name__ == "__main__": 
    get_credentials() 
