import requests
import time
import json

def get_comments_from_pushshift(**kwargs):
    r = requests.get("https://api.pushshift.io/reddit/comment/search/",params=kwargs)
    data = r.json()
    return data['data']

'''
def get_comments_from_reddit_api(comment_ids,author):
    headers = {'User-agent':'Comment Collector for /u/{}'.format(author)}
    params = {}
    params['id'] = ','.join(["t1_" + id for id in comment_ids])
    r = requests.get("https://api.reddit.com/api/info",params=params,headers=headers)
    data = r.json()
    return data['data']['children']
'''
before = None

### IMPORTANT ######################
# Set this variable to your username
author = "stuck_in_the_matrix"
####################################
comment_data = ""
i = 0
while i < 3:
    comments = get_comments_from_pushshift(subreddit="foodporn", size=100,before=before,sort='desc',sort_type='created_utc')
    if not comments: break

    # This will get the comment ids from Pushshift in batches of 100 -- Reddit's API only allows 100 at a time
    comment_bodies = ""
    for comment in comments:
        before = comment['created_utc'] # This will keep track of your position for the next call in the while loop
        comment_bodies += comment['body'] + "\n"

    # This will then pass the ids collected from Pushshift and query Reddit's API for the most up to date information
    comment_data += comment_bodies
    i+= 1
    time.sleep(2)
