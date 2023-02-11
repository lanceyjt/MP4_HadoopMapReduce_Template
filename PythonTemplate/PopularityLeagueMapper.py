#!/usr/bin/env python3
import sys


leaguePath = sys.argv[1]
#TODO


with open(leaguePath) as f:
       #TODO
       pages = [line.strip() for line in f]

for line in sys.stdin:

       #TODO
       line = line.strip()
       page, count = line.split('\t')
       if page in pages:
               print('%s\t%s' % (page,count))
       # print('%s\t%s' % (  ,  )) pass this output to reducer
