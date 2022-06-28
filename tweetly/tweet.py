import tweepy
from config import get_settings

consumer_key = get_settings().consumer_key
consumer_secret = get_settings().consumer_secret
access_token = get_settings().access_token
access_token_secret = get_settings().access_token_secret


def create_tweet(tweet: str) -> None:
    """Create new tweet with post title and link"""
    client = tweepy.Client(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
    )

    response = client.create_tweet(text=tweet)

    print(f"https://twitter.com/user/status/{response.data['id']}")
