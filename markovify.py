"""
preprocessing subreddit comment data
- combine data into txts (large chunks of data)
- clean the book
"""

import nltk
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
    """
    # Search for START and END tags to remove useless parts
    start_idx = get_index(rows,'*** START')
    end_idx = get_index(rows,'*** END')
    rows = rows[start_idx+1:end_idx]
    """
    # We need to create a string for markovify
    text = '\n'.join([r for r in rows if r!=''])
    return text

import markovify
corpus = clean_book('data-markovify/alice-adventures.txt')
text_model_a = markovify.Text(corpus)

for i in range(5):
    print("SENTENCE:")
    print(text_model_a.make_sentence())