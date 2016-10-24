from twitter import *
import re

token                   = '13375022-eYpiRxwkpRMOidbeekvhILtTtjR0d6BpYHVhOIn2F'
token_secret            = 'moU80PqslYUm3e2ioKe5VpWorzFHECC85kSSqsdVSticW'
consumer_key            = '4GYytG4LCji5EYgEh49lgPZU6'
consumer_secret_key     = 'hLNdWgJiQImdKFy0zv0msA0C9eVeRJu1X2i4jRTIfWN6Ecgy6p'

tweet = Twitter(auth=OAuth(token, token_secret, consumer_key, consumer_secret_key))
tweets = tweet.search.tweets(q='#thevoiceth', lang='th', count=1)

pattern = '^RT'
prog = re.compile(pattern)

tweet_collection = []

for t in tweets['statuses']:
