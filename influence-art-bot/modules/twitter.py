import tweepy
import json 

class TwitterInteractions:
    """
    TwitterInteraction is responsible for interaction with Twitter.
    Includes Auth, Tweeting and stat collection
    """

    def __init__(self):
        with open('twitterauth.json') as file:
            self._secrets = json.load(file)

        self._auth = tweepy.OAuthHandler(self._secrets['consumer_key'], self._secrets['consumer_secret'])
        self._auth.set_access_token(self._secrets['access_token'], self._secrets['access_token_secret'])
        self._twitter = tweepy.API(self._auth)
        self._handle = ""

    def sendTweetWithPhoto(self, sketchpath, caption):
        """
        Sends a Tweet containing a photo
        """
        status = self._twitter.update_with_media(sketchpath, caption)
        print(status._json['id'])

    def collectUpdateTweets(self):
        """
        Pulls the Tweet history of the TweetInteraction user.
        """
        for tweet in tweepy.Cursor(self._twitter.api.user_timeline, screen_name=self._handle).items():
            self.processTweets(tweet)

    def processTweets(self, tweet):
        """
        Process the tweet statistics to data store.
        Will add or update the store depending on if its a new tweet or not.
        """
        print(tweet._json['favorite_count'])
        print(tweet._json['retweet_count'])
        print(tweet._json['id'])
