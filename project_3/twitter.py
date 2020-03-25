from tweepy import Stream
from tweepy import OAuthHandler #For handling authentication
from tweepy.streaming import StreamListener #For streaming tweets
import json #For writing to a JSON file

# Credentials that are generated in the Twitter developer app
access_token = '837612670391988226-cOGK8kOF9xui3plGfaVtFdLgdEqoAK6'
access_token_secret = 'FQNFcWL4OfQ2BRp5KsIIXJD0CWJOY3aoGomtrmmMuYkmC'
consumer_token = 'xBeyAlAUemzXJZ1FDLgH4rZCp'
consumer_token_secret = 'oRElpAezmEwFctz0ASmuSDGUT8Tx06h1psFteeX7lqiF3rY1NP'

class Listen(StreamListener):
    def on_status (self, status):
        json_str = json.dumps(status._json)
        print(json_str) #printing the Json string that is being fetched...
        try:
            with open("coronatweets_11_53.json","a") as file: #appending the JSON
            #data to the file
                file.write(json_str+",\n")
        except:
            pass
        return True
    def on_error(self, status_code):
        print(status_code)
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False        
        
if __name__ == "__main__":
    print("I am here")
    listener = Listen() #listener object of Listener class
    print(OAuthHandler)
    authentication = OAuthHandler(consumer_token,consumer_token_secret)
    authentication.set_access_token(access_token, access_token_secret)
    stream = Stream(authentication, listener) #stream object with authentication
    stream.filter(follow = ['1242461488406843393']) #filtering the tweets with 
    listener.on_status()