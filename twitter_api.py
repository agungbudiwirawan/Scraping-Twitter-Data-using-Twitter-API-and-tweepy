# library
import tweepy as tw
import pandas as pd
import configparser as cp

# read config
cnfg = cp.ConfigParser()
cnfg.read('config.ini')

api_key = cnfg['twitter']['api_key']
api_key_secret = cnfg['twitter']['api_key_secret']
access_token = cnfg['twitter']['access_token']
access_token_secret = cnfg['twitter']['access_token_secret']

# authentication
auth = tw.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access_token,access_token_secret)
api = tw.API(auth)

#keyword for scraping
search_word = 'python'

#input keyword and amount of data
tweets = tw.Cursor(api.search_tweets, q=search_word, result_type='popular',tweet_mode='extended').items(500) 

# create a data list containing tweet, source, like, retweet, created at
output = []
for tweet in tweets:
    text = tweet._json["full_text"]
    favourite_count = tweet.favorite_count
    retweet_count = tweet.retweet_count
    created_at = tweet.created_at
    source_tweet = tweet.source
        
    line = {'created_at' : created_at, 'source':source_tweet,'like_count' : favourite_count, 'retweet_count' : retweet_count, 'tweet' : text}
    output.append(line)

# create dataframe from list
df = pd.DataFrame(output)

# print dataframe
print(df)