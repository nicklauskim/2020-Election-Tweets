#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 18:18:39 2020

@author: nicklauskim
"""



# Import libraries
import os
import csv
from datetime import datetime
import tweepy as tw



# Declare API credentials: Keys and Access Tokens
access_token = '1320809215011639296-0t1shiTHchun8EIjvcGinjyfysJ3pS'
access_secret = '73gonPzTrfFKKzYNjtpSUvbZzkvdukKYHgPzIMttpjrbj'
consumer_key = 'nAYZQZf9CN5acPI6mVesqapH1'
consumer_secret = 'qGyuafUqLkvQWIabmrAyjJb57MskmDJ1QDdhOVdijlTDuzR2jt'



# Access the Twitter API via Tweepy
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tw.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify= True, compression = False)



# Run a quick test to make sure everything's working by posting a tweet
#api.update_status("Hello, world! This is my first tweet, posted through the #TwitterAPI using #Python!")
#print("Tweet posted!\n")



# TO DO: Create a class to make API call + scrape data - better design



# Set search parameters
search_terms = "#Election2020 -filter:retweets"
start_date = '2020-10-22'
num_tweets = 10000



# Search for tweets
tweets = tw.Cursor(api.search, q = search_terms, tweet_mode = 'extended', lang = 'en', since = start_date)
#tweets_json = [tweet._json for tweet in tweets]


# Add "countdown" for when the rate limit is reached and need to sleep?


# Create data from tweet search results
data = []
for tweet in tweets:
    attributes = {
        'tweet_id': tweet.id,
        'created_at': tweet.created_at,
        'text': tweet.full_text,
        'hashtags': [tag['text'] for tag in tweet.entities['hashtags']],
        'retweets_count': tweet.retweet_count,
        'favorites_count': tweet.favorite_count,
        'user_id': tweet.user.id,
        'user_name': tweet.user.name,
        'user_screen_name': tweet.user.screen_name,
        'user_desc': tweet.user.description,
        'user_location': tweet.user.location,
        'user_join_date': tweet.user.created_at,
        'user_followers_count': tweet.user.followers_count,
        'user_statuses_count': tweet.user.statuses_count,
        'source': tweet.source,
        'time_collected': datetime.now()
    }
    
    data.append(attributes)
    
    
    
# Write compiled data to csv file
keys = data[0].keys()
with open('./data/raw/election_day_tweets.csv', 'wt', newline='')  as f:
    dict_writer = csv.DictWriter(f, keys)
    dict_writer.writeheader()
    dict_writer.writerows(data)    

    
    
    
    