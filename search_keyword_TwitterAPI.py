# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 09:45:41 2019

@author: Xing Lu
"""

from twython import Twython  
import json
import pandas as pd

# Load credentials from json file
with open("twitter_credentials.json", "r") as file:  
    creds = json.load(file)

# Instantiate an object
python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])

# Create our query
query = {'q': 'Metropolitan Museum Art',  
        'result_type': 'recent',
        'count': 100,
        'lang': 'en',
        }

# Search tweets
dict_ = {'user': [], 'date': [], 'text': []}  
for status in python_tweets.search(**query)['statuses']:  
    dict_['user'].append(status['user']['screen_name'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['text'])

# Structure data in a pandas DataFrame for easier manipulation
df = pd.DataFrame(dict_)  
df.sort_values(by='date', inplace=True, ascending=False)  
df.head(5) 