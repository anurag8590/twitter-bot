import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
BEARER_KEY = os.getenv("BEARER_KEY")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")


# print(API_KEY)
# print(API_SECRET)
# print(BEARER_KEY)
# print(ACCESS_TOKEN)
# print(ACCESS_TOKEN_SECRET)


client = tweepy.Client(BEARER_KEY, API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# # Creating a tweet to test the bot
# client.create_tweet(text="Hello World")