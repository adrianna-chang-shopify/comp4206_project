#! usr/bin/env python3

# COMP 4206 A Final Project
# File: fetch_top_post.py

# Purpose
#   fetch_top_post.py will fetch the top post off of Reddit's
#   front page, either by day or by week. It pulls important
#   information about that top post, as well as information about
#   the places the post has been cross-posted to. It puts all of this
#   in a CSV file, post_data.csv

# Acknowledgements
#   Crawler code adapted from https://www.storybench.org/how-to-scrape-reddit-with-python/
#   All other code original content by Adrianna Chang and Britta Evans-Fenton.

# Import necessary libraries
import praw
import pandas as pd
import datetime as dt


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

# Crawl from Reddit's main page
subreddit = reddit.subreddit('all')

# Specify number of top posts to grab
num_posts_to_grab = 10
# Specify whether to grab top posts for the day or for the week
time_band = 'week'

# Store all top posts for specified parameters in an array
top_posts = []
for post in subreddit.top(time_band, limit=num_posts_to_grab):
    top_posts.append(post)

# Grab one of those posts
# Typically we want the first one, but can manually adjust to find more data
top_post = top_posts[0]

# Set up dict with the data we want for each post
topics_dict = {"title": [],
               "id": [],
               "subreddit": [],
               "subreddit_subscribers": [],
               "subreddit_created_date": [],
               "score": [],
               "comms_num": [],
               "created": []
               }

# Get information about top post and append to topics_dict
topics_dict["title"].append(top_post.title)
topics_dict["id"].append(top_post.id)
topics_dict["subreddit"].append(top_post.subreddit)
topics_dict["subreddit_subscribers"].append(
    top_post.subreddit.subscribers)
topics_dict["subreddit_created_date"].append(
    top_post.subreddit.created_utc)
topics_dict["score"].append(top_post.score)
topics_dict["comms_num"].append(top_post.num_comments)
topics_dict["created"].append(top_post.created)

# Find duplicates (cross posts) for top post,
# Append information about all cross posts to topics_dict
for submission in top_post.duplicates():
    # Apparently users can cross post posts to their own feed
    # We'd like to filter these out
    if str(submission.subreddit).startswith('u_'):
        continue
    topics_dict["title"].append(submission.title)
    topics_dict["id"].append(submission.id)
    topics_dict["subreddit"].append(submission.subreddit)
    topics_dict["subreddit_subscribers"].append(
        submission.subreddit.subscribers)
    topics_dict["subreddit_created_date"].append(
        submission.subreddit.created_utc)
    topics_dict["score"].append(submission.score)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)

# Clean up the data in the dictionary and export to the specified CSV
topics_data = pd.DataFrame(topics_dict)
_post_timestamp = topics_data["created"].apply(get_date)
_subreddit_timestamp = topics_data["subreddit_created_date"].apply(get_date)
topics_data = topics_data.assign(post_timestamp=_post_timestamp)
topics_data = topics_data.assign(subreddit_timestamp=_subreddit_timestamp)
topics_data.to_csv('post_data.csv', index=False)
