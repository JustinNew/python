###################################################################################################
# Read in text file and tokenize it.

import nltk

file = open('2554-0.txt', 'r')
raw = file.read()

nltk.download('punkt')
tokens = nltk.word_tokenize(raw)

text = nltk.Text(tokens)
