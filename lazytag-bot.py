import requests
import time
import json
import sys
import grab

from clarifai import rest
from clarifai.rest import ClarifaiApp

import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn

import inflect
import markovify

app = ClarifaiApp(api_key='1f2c93de75074a088597cd7791491b5a')
model = app.public_models.general_model

## Lazytag Bot ##
# 1. Generate list of keywords from Clarifai model
# 2. Filter the keywords
# 3. Recieve most search words from each sub-reddit from the worddit api
# 4. Compare the keywords with most search word
# 5. Find the subreddit that has the highest probability of producing an acurate comment
# 6. Generate comment with comments produced from the subreddit

## Inputs ##
# an image url
sample_img = "https://images-na.ssl-images-amazon.com/images/I/41By-%2BguaYL.jpg"

# list of banned words
banned_words = {"nude"}

# list of subreddits for training data
subreddits = ["aww", "pics", "funny", "gaming", "AskReddit", "science", "worldnews",
"todayilearned", "videos", "movies", "Music", "IAmA", "gifs", "news", "EarthPorn",
"blog", "askscience", "Showerthoughts", "foodporn", "sports", "explainlikeimfive",
"books", "Jokes", "mildlyinteresting", "LifeProTips", "television", "DIY", "food",
"space", "gadgets", "nottheonion", "Art", "photoshopbattles", "UpliftingNews", "listentothis",
"GetMotivated", "Documentaries", "tifu", "history", "Futurology", "OldSchoolCool", "philosophy",
"personalfinance", "dataisbeautiful", "WritingPrompts", "nosleep", "creepy", "TwoXChromosomes",
"technology", "Fitness",  "AdviceAnimals", "interestingasfuck", "wholesomememes", "politics"]

# declare a function to get word index
def get_index(in_list,in_string):
    for num,row in enumerate(in_list):
        if in_string in row:
            return num
# We convert the script from the NLTK Stopwords tutorial into a def
def clean_book(path):
    # Let's open the book we downloaded
    book = open(path,'r').read()
    # Divide text by rows
    rows = book.split('\n')
    # Search for START and END tags to remove useless parts
    start_idx = get_index(rows,'*** START')
    end_idx = get_index(rows,'*** END')
    rows = rows[start_idx+1:end_idx]
    # We need to create a string for markovify
    text = '\n'.join([r for r in rows if r!=''])
    return text


'''
Clean the keyword list.
input: clarifai_keywords, banned_words
output: list of keywords, their lemmas, synonyms, and pluralized lemmas
*no duplicates
'''
def filter_keywords(clarifai_keywords, banned_words):
    lemmatizer = WordNetLemmatizer()
    keywords = set()
    for word in clarifai_keywords:
        # set of forms to check for duplicates
        forms = set()
        forms.add(word)

        # find lemma of input word
        lemma = lemmatizer.lemmatize(word)
        forms.add(lemma)

        # find derivational forms
        for lemma_type in wn.lemmas(lemma): # loop though the different definitions of the lemma
            for lemma_form in lemma_type.derivationally_related_forms():
                if lemma_form.name() not in forms:
                    forms.add(lemma_form.name())

        # add pluralized forms
        engine = inflect.engine()
        plural = engine.plural(lemma)
        forms.add(plural)

        # sanity check
        print(word, ": ", forms)

        # add if the form is not a banned word
        for word_form in forms:
            if word_form not in banned_words:
                keywords.add(word_form)

    # sanity check
    print ("final keywords:", keywords)

    return keywords

'''
input: keywords that have been filtered
output: corpus of the most probable subreddit that will output the best comments for image
uses the keyworrddit api, which is the most probable words used from each subreddit
'''
def generate_corpus(input_keywords, subreddits):
    # a part for getting from keyworddit api
    # a part for matching keywords
    # a part for using reddit api

    # store dict of [sr name, description(array)]
    keywords = {}
    for sr in subreddits:
        r = requests.get("http://www.keyworddit.com/api/retrieve/" + sr)
        data = r.json()

        # split discription of sr into array
        sr_keywords = []
        for key in data:
            for word in key.split():
                sr_keywords.append(word)
        keywords[sr] = sr_keywords

    # count frequency of keywords in each description
    # thinking of differing weights by accuracy in clarifai returns
    weights = {}
    for key in keywords:
        weights[key] = 0
    for label in input_keywords:
        for sr in keywords:
            for word in keywords[sr]:
                if word == label: weights[sr] += 1

    # sanity check
    print(weights)

    subreddit_max = max(weights, key=weights.get)
    print(subreddit_max)
    num_comments = 100
    corpus = grab.get_comments(subreddit_max, num_comments)
    return corpus

'''
Generates a set of sentences from a corpus
input: corpus of reddit comments
output: set of non-empty sentences.
'''
def generate_comment(model):
    # Train Model
    model = markovify.Text(corpus)

    # Normalize English
    normalizer = clean_book('data-markovify/english-grammar.txt')
    model_b = markovify.Text(normalizer)

    combined_models = markovify.combine([model, model_b])

    # Generate Sentences
    for i in range(20):
        sentence = combined_models.make_sentence()
        if (sentence != None):
            print("------------------------------")
            print(sentence)


# 1. Generate keywords from Clarifai model
# input: image url, sample_img
# output: keywords list, clarifai_keywords
print("##### Step 1. GENERATE KEYWORDS ######")
response = model.predict_by_url(sample_img)
clarifai_keywords = []
for dict_item in response['outputs'][0]['data']['concepts']:
    clarifai_keywords.append(dict_item['name'])

# Sanity check: print keywords generated by Clarifai
for item in clarifai_keywords:
    print(item)

# 2. Filter the keywords:
#   remove inappropriate words
#   lemmatize keywords and add the morphological versions
print("##### Step 2. CLEAN KEYWORDS ######")
keywords = filter_keywords(clarifai_keywords, banned_words)


# 3. Generate the training data for Markov Model.
print("##### Step 3. GENERATE TRAINING CORPUS ######")
corpus = generate_corpus(keywords, subreddits)

# 4. Generate the comment.
#   Train Markov model specific to the image
#   Create a bunch of sentences
print("##### Step 4. MARKOV MODEL ######")
generate_comment(model)


'''
def get_comments_from_reddit_api(comment_ids,author):
    headers = {'User-agent':'Comment Collector for /u/{}'.format(author)}
    params = {}
    params['id'] = ','.join(["t1_" + id for id in comment_ids])
    r = requests.get("https://api.reddit.com/api/info",params=params,headers=headers)
    data = r.json()
    return data['data']['children']
'''
