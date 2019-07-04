### Gather Twitter Data

import sys
sys.path.append(r"C:\Users\terra\Anaconda3\envs\python37\cs591_project\GetOldTweets-python-master")
from got3.manager import TweetCriteria
from got3.manager import TweetManager

import pandas as pd
import datetime

import requests # Http for human
#from blk import cfg

def query_hist(query,start_date,end_date):
    tweet_criteria = TweetCriteria().setQuerySearch(query).setSince(start_date).setUntil(end_date)
    tweets = TweetManager.getTweets(tweet_criteria)
    
    columns = ['index','text','id','username','retweets','favorites', 'mentions',
             'hashtags','geo','permalink']
    data = []
    for i,tweet in enumerate(tweets):
        d = [tweet.date,tweets[i].text,tweets[i].id,
            tweet.username,tweets[i].retweets,tweets[i].favorites,tweets[i].mentions,
             tweet.hashtags, tweets[i].geo,tweets[i].permalink]
        data.append(d)
    tweets_DF = pd.DataFrame(data,columns = columns)
    return tweets_DF

query = 'art institute of Chicago'
start_date = '2018-04-07'
end_date = '2019-04-14'

tweets = query_hist(query,start_date,end_date)