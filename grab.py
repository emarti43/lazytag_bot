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
### IMPORTANT ######################
# Set this variable to your username
# author = "stuck_in_the_matrix"
####################################

def get_comments(sr_name, comment_no):
    comments_left = comment_no
    before = None
    comment_data = ""
    while comments_left > 0:
        num_grab = comments_left if comments_left < 100 else 100
        comments = get_comments_from_pushshift(subreddit=sr_name, size=num_grab, before=before,sort='desc',sort_type='created_utc')
        if not comments: break

        # This will get the comment ids from Pushshift in batches of 100 -- Reddit's API only allows 100 at a time
        comment_bodies = ""
        for comment in comments:
            before = comment['created_utc'] # This will keep track of your position for the next call in the while loop
            comment_bodies += comment['body'] + "\n"
        # This will then pass the ids collected from Pushshift and query Reddit's API for the most up to date information
        comment_data += comment_bodies
        comments_left -= 100 
        time.sleep(2)
    return comment_data

print(get_comments("foodporn", 100))
