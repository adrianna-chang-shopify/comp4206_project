#! usr/bin/env python3

# COMP 4206 A Final Project
# File: generate_subreddit_network.py

#   generate_subreddit_network.py seeks to identify subreddit communities that often
#   post or cross post each other's content. Given a manual set of subreddits,
#   which are pulled from fetch_top_post.py, it looks at the top 100 posts in each
#   of those subreddits and then counts the number of cross posts *within* the fixed
#   set of subreddits we've specified.

# Acknowledgements
#   Code is original content by Adrianna Chang and Britta Evans-Fenton.

# Import necessary libraries
import praw
import pandas as pd
import datetime as dt

# def get_date(created)
# Transform timestamp into proper datetime object


def get_date(created):
    # Transform timestamp into proper datetime object
    return dt.datetime.fromtimestamp(created)


# Set up API Client Credentials
# Note: Reddit password has been redacted!
reddit = praw.Reddit(client_id='TZu3S6MMqOAs3g',
                     client_secret='9P143g-GRe9fyh98LbnerDawPnc',
                     user_agent='COMP4206',
                     username='adriannachang',
                     password='xxxxxxxxxxxxx')

# These need to be manually imported from fetch_top_post.py
# It is the list of all the subreddits the original top post
# was crossposted to, and serves as a starting point for identifying
# a larger community from a group of subreddits
subreddits = [
    'BlackPeopleTwitter',
    'electricians',
    'nursing',
    'walmart',
    'starbucks',
    'KitchenConfidential',
    'bartenders',
    'Snorkblot',
    'antiwork',
    'topofreddit',
    'mistyfront',
    'CinnamonToastKen',
]

# This data structure (all_counts) will store, for each subreddit, a dictionary;
# this dictionary will have all the subreddits as keys, and the number of cross-posts
# per each subreddit where the post was *originally* posted in the outer dictionary's
# subreddit.
# For example,
# all_counts = {
# 'memes': {
#     'pics': 1,
#     'awesome': 1,
# }
# }
# indicates that original content from the top 100 posts in r/memes was cross posted
# once in r/pics and once in r/awesome.
all_counts = {}


# We'll grab the top 100 posts for each subreddit
num_posts_to_fetch = 100

# For each subreddit in our set of related subreddits
for subreddit_str in subreddits:
    # dict_counters is the nested dictionary
    dict_counters = {subreddit: set() for subreddit in subreddits}
    # Grab the actual subreddit object from the subreddit string and print
    # which subreddit we're currently parsing
    subreddit = reddit.subreddit(subreddit_str)
    print('Subreddit: ' + subreddit_str)
    # Look at top 100 posts in the subreddit
    for post in subreddit.top('week', limit=num_posts_to_fetch):
        # Ensure that the post is the original
        # The PRAW API does not tell us whether a duplicate is the original or
        # not, so we have to look at timestamps and assume that the post
        # with the minimum timestamp is the original
        dup_post_timestamps = [d.created for d in post.duplicates()]
        if dup_post_timestamps:
            og_post_timestamp = min(dup_post_timestamps)
            if og_post_timestamp < post.created:
                continue
        else:
            continue
        # Look at cross posts for each top 100 post
        for duplicate in post.duplicates():
            # If duplicate post is in our fixed list of subreddits, increment counter for that subreddit
            # in dict_counters
            if duplicate.subreddit in subreddits:
                # We add the duplicate's id to the set to remove some weirdness that was
                # occurring with the same post being pulled twice by the crawler
                dict_counters[str(duplicate.subreddit)].add(duplicate.id)
                print('Original post, title: ' +
                      post.title + ', id: ' + post.id)
                print('\tDuplicate: subreddit: ' +
                      str(duplicate.subreddit) + ', title: ' + duplicate.title + ', id: ' + duplicate.id)
    # Set the key in all_counts equal to the dict we've built, dict_counters
    all_counts[subreddit_str] = dict_counters

# Print the data from all_counts in a readable format
for subreddit_key in all_counts:
    print(subreddit_key)
    dict_counters = all_counts[subreddit_key]
    for nested_subreddit in dict_counters:
        # Avoid printing if there were no cross posts for that subreddit
        if dict_counters[nested_subreddit]:
            print(
                '\t' + str(len(dict_counters[nested_subreddit])) + '\t' + nested_subreddit)
