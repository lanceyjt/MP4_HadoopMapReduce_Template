#!/usr/bin/env python3
from operator import itemgetter
import sys

#TODO
current_word = None
current_count = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    # TODO
    line = line.strip()
    word, count = line.split('\t')
    try:
        count = int(count)
    except ValueError:
        continue
    
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # write result to STDOUT
            print('%s\t%s' % (current_word, current_count))
        current_count = count
        current_word = word


# TODO
# print('%s\t%s' % (  ,  )) print as final output
if current_word == word:
    print('%s\t%s' % (current_word, current_count))