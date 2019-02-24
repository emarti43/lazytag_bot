"""
preprocessing subreddit comment data
- combine data into txts (large chunks of data)
- clean the book
"""

import grab
import sys
import markovify

# Argument inputs
subreddit = 'foodporn'
num_comments = int(sys.argv[1])
corpus = grab.get_comments(subreddit, num_comments)

# Train Model
model = markovify.Text(corpus)

# Generate Sentences
for i in range(100):
    sentence = model.make_sentence()
    if (sentence != None):
        print("------------------------------")
        print(sentence)