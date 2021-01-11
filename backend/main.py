import praw
import config
import requests
import time
import json
from content import send
from server import configurations
##make call to subreddit using their information, store posts that are passed the threshold, 

# COMMAND CENTER ----------------------------------------------------------------------------------------------
# =============================================================================================================

target_subreddit = configurations['reddit_community']

sleep_interval = 60
dm_title = configurations['dm_title']
dm_message = configurations['dm_message']
is_running = configurations['is_running']
# FUNCTIONS ---------------------------------------------------------------------------------------------------
# =============================================================================================================

def bot_login():
  r = praw.Reddit(
        username = config.username,
        password = config.password,
        client_id = config.client_id,
        client_secret = config.client_secret,
        user_agent = "nwhacks messaging for r/ubc")
  return r

# returns list of submissions
def run_bot(r, post_retrieval_limit):
  submissions = r.subreddit(target_subreddit).new(limit=post_retrieval_limit)
  all_submissions = []
  for submission in submissions:
    #create submission object
    curr_sub = {}
    curr_sub["submission_id"] = submission.id
    curr_sub["wap_score"] = 10
    curr_sub["title"] = submission.title
    curr_sub["author"] = submission.author.name
    curr_sub["selftext"] = submission.selftext
    curr_sub["created_utc"] = submission.created_utc

    #add submission to all_submissions
    all_submissions.append(curr_sub)

  return all_submissions

def remove_old_subs(all_subs, prev_time):
  # Now you have all newest posts within all_subs
  # Remove the old posts from all_subs to get latest_subs
  latest_subs = []
  for sub in all_subs:
    if sub["created_utc"] > prev_time:
      latest_subs.append(sub)
  return latest_subs

# MAIN FUNCTON ------------------------------------------------------------------------------------------------
# =============================================================================================================
r = bot_login()

def run_script():
  prev_time = 1600246174
  post_retrieval_limit = 10

## runs every min
  while True:

    # WHILE LOOP --> continues until you have all the newest posts within all_subs (until you find the first non-new post)
    all_new_posts = True

#real time data 
    # while all_new_posts:
    #   # get post_retrieval_limit # of latest posts: 10
    #   all_subs = run_bot(r, post_retrieval_limit)
    #   print(all_subs)
    #   # check if there is a non-new post in the 10 latest. Do we need to retrieve more?
    #   for sub in all_subs:
    #     if sub["created_utc"] <= prev_time: # if a non-new post is found
    #       all_new_posts = False
    #       post_retrieval_limit = 10
    #       break
    #     elif sub["created_utc"] > prev_time:
    #       continue
      
    #   if all_new_posts: 
    #     post_retrieval_limit += 10
  
    #   # update retrieval time
    #   prev_time = all_subs[0]["created_utc"] ##WHYY??








    all_subs = run_bot(r, post_retrieval_limit)
    # print(all_subs)

    latest_subs = remove_old_subs(all_subs, prev_time)

    # print(latest_subs)
    prev_time = all_subs[0]["created_utc"]

  
    # send latest_subs to NLP & retrieve sus_post_ids from NLP --> list of submission_ids for submissions with 'wap_score > threshold'

    sus_post_ids, posts = send(latest_subs)
  
    # get sus_authors from the sus_post ids
    sus_authors_usernames = []
    for sub in all_subs:
      if sub["submission_id"] not in sus_post_ids:
        continue
      else:
        sus_authors_usernames.append(sub["author"])


    # send private message to each sus_author with (Title, Message)
    for sus_author in sus_authors_usernames:
      r.redditor(sus_author).message(dm_title, dm_message)
      print(sus_author)

run_script()
