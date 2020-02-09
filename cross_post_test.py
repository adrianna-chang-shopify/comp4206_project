#! usr/bin/env python3
import praw
import pandas as pd
import datetime as dt


def get_date(created):
    return dt.datetime.fromtimestamp(created)


def pretty(d, indent=0):
    for key, value in d.items():
        print('\t' * indent + str(key))
        if isinstance(value, dict):
            pretty(value, indent+1)
        else:
            print('\t' * (indent+1) + str(value))


reddit = praw.Reddit(client_id='TZu3S6MMqOAs3g',
                     client_secret='9P143g-GRe9fyh98LbnerDawPnc',
                     user_agent='COMP4206',
                     username='adriannachang',
                     password='tequilasunrise')

subreddits = [
    'Shitstatistssay',
    'AskReddit',
    'shitpost',
    'starbucks',
    'ABoringDystopia',
    'walmart',
    'antiwork',
    'GenZ',
    'chapotraphouse2',
    'topofreddit',
    'Anarcho_Capitalism',
    'popularpost'
]

all_counts = {}

for subreddit_str in subreddits:
    dict_counters = {
        'Shitstatistssay': 0,
        'AskReddit': 0,
        'shitpost': 0,
        'starbucks': 0,
        'ABoringDystopia': 0,
        'walmart': 0,
        'antiwork': 0,
        'GenZ': 0,
        'chapotraphouse2': 0,
        'topofreddit': 0,
        'Anarcho_Capitalism': 0,
        'popularpost': 0
    }
    subreddit = reddit.subreddit(subreddit_str)
    print(subreddit_str)
    for post in subreddit.top('week', limit=10):
        for duplicate in post.duplicates():
            if duplicate.subreddit in subreddits:
                dict_counters[str(duplicate.subreddit)] += 1
                print(duplicate.subreddit, duplicate.title)
    all_counts[subreddit_str] = dict_counters

print(pretty(all_counts))
