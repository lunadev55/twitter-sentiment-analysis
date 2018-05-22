import tweepy
from textblob import TextBlob

consumer_key = 'DuVPg5fJf2CPfQBSSvCX5OzDp'
consumer_secret = 'EQ7vS8BK5HLDABRrK0d9exPOKcctZCmf4MjnNsRG3Me6aNEQ7I' 

access_token = '998742627066482688-OZjxdvWmR9veGMVKDEAritYRrybEn3v'
access_token_secret = 'NAsadfAIBpMP2NglaZQPrYX1wBsbU6Kje6Gfc9PxScMgJ' 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)