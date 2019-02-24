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
"""
if (num_comments < 1):
    num_comments = 1
elif (num_comments > 100):
    num_comments = 100
"""
#num_comments = '100'
corpus = grab.get_comments(subreddit, num_comments)

# Preprocess data

# Generate
model = markovify.Text(corpus)

for i in range(100):
    sentence = model.make_sentence()
    if (sentence != None):
        print("------------------------------")
        print(sentence)