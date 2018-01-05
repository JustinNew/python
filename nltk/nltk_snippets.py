###################################################################################################
# Read in text file and tokenize it.

import nltk

file = open('2554-0.txt', 'r')
raw = file.read()

nltk.download('punkt')
tokens = nltk.word_tokenize(raw)

text = nltk.Text(tokens)

###################################################################################################
# Get the frequency distribution.
wsj = sorted(set(nltk.corpus.treebank.words()))
fd = nltk.FreqDist(vs for word in wsj for vs in re.findall(r'[aeiou]{2,}', word))

###################################################################################################
# Greedy version of regular expression .*
re.findall(r'^(.*)(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processes')
# [('processe', 's')]

# Non-greedy version of regular expression .*, .*?
re.findall(r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processes')
# [('process', 'es')]
