
import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn

lemmatizer = WordNetLemmatizer()
inputword = "children"
wordlemma = lemmatizer.lemmatize(inputword)
print(inputword, " -> ", wordlemma)

forms = set() #We'll store the derivational forms in a set to eliminate duplicates
for happy_lemma in wn.lemmas(wordlemma): #for each "happy" lemma in WordNet
    forms.add(happy_lemma.name()) #add the lemma itself
    for related_lemma in happy_lemma.derivationally_related_forms(): #for each related lemma
        forms.add(related_lemma.name()) #add the related lemma


import inflect
engine = inflect.engine()
plural = engine.plural(wordlemma)
forms.add(plural)
print(inputword, ": ", forms)