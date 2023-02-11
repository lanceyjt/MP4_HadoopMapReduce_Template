#!/usr/bin/env python3
import sys


# TODO
page_count = []


for line in sys.stdin:

       #TODO
       line = line.strip()
       page, count = line.split('\t')
       page_count.append([page, int(count)])

page_count.sort(reverse=False, key=lambda x: (x[1], x[0]))

#TODO
# print('%s\t%s' % (  ,  )) pass this output to reducer
for x in page_count[-10:]:
       print('%s\t%s' % (x[0],x[1]))
