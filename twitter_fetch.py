# import required libraries
import tweepy
import time
import pandas as pd

pd.set_option('display.max_colwidth', 1000)

# api key
api_key = "xgLa6FF0AkRnOzgVT6dCX62ih"
# api secret key
api_secret_key = "ysvcziLpkBWe7MCF74mibtZFsLXDODJgswC5FYs0A9skJoaFm5"
# access token
access_token = "1021788589703786496-ZkueNth2E2FNAwybdNkJlHr8HdGzrJ"
# access token secret
access_token_secret = "gmEFCgDfBQlFrj5f60SAg4yDIuULS4FCLn9rELvNMa8i3"

# authorize the API Key
authentication = tweepy.OAuthHandler(api_key, api_secret_key)

# authorization to user's access token and access token secret
authentication.set_access_token(access_token, access_token_secret)

# call the api
api = tweepy.API(authentication, wait_on_rate_limit=True)


def get_related_tweets(text_query):
    # list to store tweets
    tweets_list = []
    # no of tweets
    count = 50
    try:
        # Pulling individual tweets from query
        for tweet in api.search(q=text_query, count=count):
            print(tweet.text)
            # Adding to list that contains all tweets
            tweets_list.append({'created_at': tweet.created_at,
                                'tweet_id': tweet.id,
                                'tweet_text': tweet.text})
        return pd.DataFrame.from_dict(tweets_list)

    except BaseException as e:
        print('failed on_status,', str(e))
        time.sleep(3)