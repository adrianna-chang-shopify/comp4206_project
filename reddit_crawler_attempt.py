#! usr/bin/env python3
import praw
import pandas as pd
import datetime as dt


def get_date(created):
    return dt.datetime.fromtimestamp(created)


reddit = praw.Reddit(client_id='TZu3S6MMqOAs3g',
                     client_secret='9P143g-GRe9fyh98LbnerDawPnc',
                     user_agent='COMP4206',
                     username='adriannachang',
                     password='tequilasunrise')

subreddit = reddit.subreddit('all')

# Get id for top post
top_posts = []

for post in subreddit.top('week', limit=1):
    top_posts.append(post)

top_post = top_posts[0]

topics_dict = {"title": [],
               "id": [],
               "subreddit": [],
               "subreddit_subscribers": [],
               "subreddit_created_date": [],
               "score": [],
               "comms_num": [],
               "created": []
               }

# Get info about top post
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

# Find duplicates
for submission in top_post.duplicates():
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

topics_data = pd.DataFrame(topics_dict)
_post_timestamp = topics_data["created"].apply(get_date)
_subreddit_timestamp = topics_data["subreddit_created_date"].apply(get_date)
topics_data = topics_data.assign(post_timestamp=_post_timestamp)
topics_data = topics_data.assign(subreddit_timestamp=_subreddit_timestamp)
topics_data.to_csv('test.csv', index=False)

# -------------------------------

# top_subreddit = subreddit.top(limit=5)
# for submission in top_subreddit:
#     topics_dict["title"].append(submission.title)
#     topics_dict["score"].append(submission.score)
#     topics_dict["id"].append(submission.id)
#     topics_dict["url"].append(submission.url)
#     topics_dict["comms_num"].append(submission.num_comments)
#     topics_dict["created"].append(submission.created)
#     topics_dict["body"].append(submission.selftext)

# topics_data = pd.DataFrame(topics_dict)
# _timestamp = topics_data["created"].apply(get_date)
# topics_data = topics_data.assign(timestamp=_timestamp)
# topics_data.to_csv('test.csv', index=False)
