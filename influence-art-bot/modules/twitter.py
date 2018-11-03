import tweepy
import json 

def sendTweet(sketchpath, caption):
    with open('twitterauth.json') as file:
        secrets = json.load(file)

    auth = tweepy.OAuthHandler(secrets['consumer_key'], secrets['consumer_secret'])
    auth.set_access_token(secrets['access_token'], secrets['access_token_secret'])

    twitter = tweepy.API(auth)

    twitter.update_with_media(sketchpath, caption)