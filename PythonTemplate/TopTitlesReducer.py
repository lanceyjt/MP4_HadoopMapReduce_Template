#!/usr/bin/env python3
import sys


word_freq = []

# input comes from STDIN
for line in sys.stdin:
    # TODO
    line = line.strip()
    word, count = line.split('\t')
    word_freq.append([word, int(count)])

    # print('%s\t%s' % (  ,  )) print as final output
word_freq.sort(reverse=False, key=lambda x: (x[1], x[0]))
for x in word_freq[-10:]:
       print('%s\t%s' % (x[0],x[1]))
