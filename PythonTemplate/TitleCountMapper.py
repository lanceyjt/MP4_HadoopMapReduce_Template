#!/usr/bin/env python3

import sys
import string



stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]


# TODO
with open(stopWordsPath) as f:
    # TODO
    stop_words = [line.strip() for line in f]

#TODO 
with open(delimitersPath) as f:
    # TODO
    delimiters = f.read()
    delimiters = [c for c in delimiters]

default_delimiter = delimiters[0]
for line in sys.stdin:
  
    # TODO
    line = line.strip()
    for d in delimiters[1:]:
        line = line.replace(d, default_delimiter)
    word_lst = line.lower().split(default_delimiter)
    word_lst = [w for w in word_lst if w not in stop_words]
    for w in word_lst:
        print('%s\t%s' % (w , 1)) # pass this output to reducer


