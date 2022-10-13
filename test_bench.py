import tweepy as twp
import time
import random

#Open and read keys by line
key_in_line = open('keys.txt', 'r').read().split() 

api_key = key_in_line[0]

api_secret_key = key_in_line[1]

access_tok = key_in_line[2]

access_sec_tok = key_in_line[3] 

#Twitter API Authenticator

authenticator = twp.OAuthHandler(api_key, api_secret_key)
authenticator.set_access_token(access_tok, access_sec_tok)

api = twp.API(authenticator, wait_on_rate_limit=True)
##api = twp.API(authenticator)

##FILE to keep track of previously read Tweet IDs
FILE_NAME = 'last_seen.txt'

#Function: read_last_seen() Parameters: FILE
#purpose: Read the last seen tweet id and return it

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

#Function store_last_seen() Parameters: FILE, last_seen_ID
#purpose: Store previously seen tweet ID to keep track of already replied tweets of the bot. Avoid duplicate replies
def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

#Iterate through the tweets that mention the bot and store in array


def reply_back():

    tweets = api.mentions_timeline(since_id = read_last_seen(FILE_NAME), tweet_mode='extended')

    for tweet in reversed(tweets):

        #print(str(tweet.id) + ' - ' + tweet.full_text)

        if '#vicebots' in tweet.full_text.lower(): #Conditional keyword statement to trigger a bot reply, subject to change or mutate

            print(str(tweet.id) + ' - ' + tweet.full_text)
            print("General Condition")
            general_reply = open('tweets.txt', 'r').read().splitlines()
            num_rand = random.randint(0,10)


            api.update_status(status = "@" +  tweet.user.screen_name  + general_reply[num_rand] , in_reply_to_status_id= tweet.id) #Reply to mention if keyword is found in tweet
            # api.create_favorite(id=tweet.id)
            # api.retweet(id=tweet.id)
            store_last_seen(FILE_NAME, tweet.id) #Store last responded tweet ID in file

        elif '#vicebot_advice' in tweet.full_text.lower():
            print(str(tweet.id) + ' - ' + tweet.full_text)
            print("advice condition")
            advice_reply = open('advice.txt', 'r').read().splitlines()
            num_rand2 = random.randint(0, 10)
            api.update_status(status = "@" +  tweet.user.screen_name  + advice_reply[num_rand2] , in_reply_to_status_id= tweet.id) #Reply to mention if keyword is found in tweet
            store_last_seen(FILE_NAME, tweet.id)

            
while True:
    reply_back()
    time.sleep(10)

