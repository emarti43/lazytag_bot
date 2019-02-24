import requests
import time
import json

from clarifai import rest
from clarifai.rest import ClarifaiApp

import sys

app = ClarifaiApp(api_key='1f2c93de75074a088597cd7791491b5a')
model = app.public_models.general_model

def get_comments_from_pushshift(**kwargs):
    r = requests.get("https://api.pushshift.io/reddit/submission/search/",params=kwargs)
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

num_grab = 1
before = None
comment_data = ""
while num_grab > 0:
    comments = get_comments_from_pushshift(subreddit="pics", size=num_grab, before=before,sort='desc',sort_type='created_utc')
    if not comments: break

    # This will get the comment ids from Pushshift in batches of 100 -- Reddit's API only allows 100 at a time
    comment_bodies = ""
    for comment in comments:
        before = comment['created_utc'] # This will keep track of your position for the next call in the while loop
        #comment_bodies += comment['url'] + "\n"
        if (len(sys.argv) < 2):
            print(comment['url'])
            response = model.predict_by_url(comment['url'])
        else:
            break
        name_map = []
        for dict_item in response['outputs'][0]['data']['concepts']:
        	name_map.append([dict_item['name'], dict_item['value']])
        for item in name_map:
        	print(item)
    # This will then pass the ids collected from Pushshift and query Reddit's API for the most up to date information
    num_grab -= 1
    time.sleep(2)


#print(get_comments("pics", 100))
