import os
import argparse

from screenshots import API

parser = argparse.ArgumentParser()
parser.add_argument("tweet_id_str", help='id of the tweet to capture')
args = parser.parse_args()

bearer_token = os.environ.get("BEARER_TOKEN")

api = API(
    bearer_token
)
# big thread example: 1266954304793055238
# reply thread example: 1267083507295281155
api.take_tweet_screenshot(args.tweet_id_str, 'debug.png')
