import requests
import time
import json
import sys
import grab
import markovify

from clarifai import rest
from clarifai.rest import ClarifaiApp

import sys

app = ClarifaiApp(api_key='1f2c93de75074a088597cd7791491b5a')
model = app.public_models.general_model

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
def lazy_comment(clarifai_keywords, subreddits):
    keywords = {}
    for sr in subreddits:
        r = requests.get("http://www.keyworddit.com/api/retrieve/" + sr)
        data = r.json()
        sr_keywords = []
        for key in data:
            for word in key.split():
                sr_keywords.append(word)
        keywords[sr] = sr_keywords
    weights = {}
    for key in keywords:
        weights[key] = 0
    for label in clarifai_keywords:
        for sr in keywords:
            for word in keywords[sr]:
                if word == label: weights[sr] += 1
    print(weights)
    subreddit_max = max(weights, key=weights.get)
    num_comments = 100
    corpus = grab.get_comments(subreddit_max, num_comments)
    # Train Model
    model = markovify.Text(corpus)

    # Generate Sentences
    for i in range(20):
        sentence = model.make_sentence()
        if (sentence != None):
            print("------------------------------")
            print(sentence)


sample_img = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_UtMjzw6-oCeHqiaiWyHVJMcv5a3Gz1UQ9DKR4t49PDKN6aQy"
response = model.predict_by_url(sample_img)
clarifai_keywords = []
for dict_item in response['outputs'][0]['data']['concepts']:
    clarifai_keywords.append(dict_item['name'])
for item in clarifai_keywords:
    print(item)
subreddits = ["aww", "pics", "funny", "gaming", "AskReddit", "science", "worldnews", "todayilearned", "videos", "movies", "Music", "IAmA", "gifs", "news", "EarthPorn", "blog", "askscience", "Showerthoughts", "foodporn", "sports"]
lazy_comment(clarifai_keywords, subreddits)




#print(get_comments("pics", 100))
