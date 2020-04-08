from tweepy import Stream
from tweepy import OAuthHandler #For handling authentication
from tweepy.streaming import StreamListener #For streaming tweets
import json #For writing to a JSON file

# Credentials that are generated in the Twitter developer app,
# you will need to change this in the future
access_token = '4499120554-xlLcrpreHvGvBgs99IKYGwme7w7tfmwPWbEYM5X'
access_token_secret = 'UfoVVeJBD6klcPOkYOBnC0uiQM4hV7YWX7OfoEYfRihtZ'
consumer_token = 'cHBdb7LKMSPTQyfGJ2GjxuysX'
consumer_token_secret = 'n23SRANIVjqBG7ol3NHPvfWYEFLpIK9dA39FXcSTziEZNehfot'

class Listen(StreamListener):
    def on_status (self, status):
        json_str = json.dumps(status._json)
        print(json_str) #printing the Json string that is being fetched...
        #appending the JSON response to the end of a file 
        try:
            with open("bitcointweets_test.json","a") as file: 
            #data to the file
                file.write(json_str+",")
        except:
            pass
        return True
    def on_error(self, status_code):
        print("Exception has occurred, here is the access code: ", status_code)
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
    #use follow in order to track an ID
    list_of_search_terms = ['bitcoin', 'cryptocurrencies', 'Ethereum']
    
    stream.filter(track = list_of_search_terms)