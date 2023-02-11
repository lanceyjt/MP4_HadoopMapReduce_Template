#!/usr/bin/env python3
import sys


# TODO
word_freq = []


for line in sys.stdin:

       #TODO
       word, count = line.split('\t')
       word_freq.append([word, count])

word_freq.sort(reverse=False, key=lambda x: (x[1], x[0]))


#TODO
# print('%s\t%s' % (  ,  )) pass this output to reducer
for x in word_freq[-10:]:
       print('%s\t%s' % (x[0],x[1]))
