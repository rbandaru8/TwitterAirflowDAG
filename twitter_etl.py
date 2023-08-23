import pandas as pd
import tweepy
import json
from datetime import datetime
import s3fs

api_key = '7HY9FSG7YfImmWLyRXyHtn62U'
api_secret_key = 'Ew7i4jl4sANQERVGomnYDWXBw2ozK58Z0vicypPnCO4r1qDqOf'
access_token = '52071798-XNFbSW7wMHBBtTwqyykGzaMlnKH4dsKq1JR5ctXjN'
access_secret_token = 'PwCAUmILOjDBTgqdu6373jUam1TvGj1mILg4mYuYM4rXu'

 # Twitter authentication
auth = tweepy.OAuthHandler(api_key,api_secret_key)   
auth.set_access_token(access_token, access_secret_token) 

api = tweepy.API(auth)

user_objects = api.lookup_users(screen_names='elonmusk')
user_ids = [user.description for user in user_objects]
#tweets = api.user_timeline(screen_name='@elonmusk', count=200, include_rts = False,tweet_mode = 'extended')
list = []
for user in user_objects:
    refined_user = {"user": user.screen_name,
                        'text' : user.description,
                        'favorite_count' : user.followers_count,
                        'retweet_count' : user.friends_count,
                        'created_at' : user.created_at}
        
    list.append(refined_user)

    df = pd.DataFrame(list)
    df.to_csv('refined_userprofile.csv')