# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 22:44:52 2018

@author: Mansimran Anand
"""

import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

class listener(StreamListener):
    
    def on_data(self, data):
        print(data)
        return True
    
    def on_error(self, status):
        print(status)


auth = tweepy.OAuthHandler('7zypktGrYXfIE48x6W9PSbkan','V4L6WdPFovhGsgrGGUe7Og3FUpwcDH3VO0diGzKnqsSia0o18v')
auth.set_access_token('904823005838114817-3qVEGlAS7ZqbcinP4QOlWkyjmdYShlE','jV8HzhqSqrq3nyHCbcQHz7xjhkfkdlqWcW8ZSDgAEuqi6')
# here after verifying the authorization keys all the tweets that contain th eword car are getting printed in real time 

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["asia"])

api = tweepy.API(auth)

public_tweets = api.home_timeline()

# here all the MY recent tweets are getting printed 
for tweet in public_tweets:
    print(tweet.text)