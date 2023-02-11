#!/usr/bin/env python3
import sys

page_count = []


# input comes from STDIN
for line in sys.stdin:
    # TODO
    line = line.strip()
    page, count = line.split('\t')
    page_count.append([page, int(count)])
    # print('%s\t%s' % (  ,  )) print as final output

page_count.sort(reverse=False, key=lambda x: (x[1], x[0]))

for x in page_count[-10:]:
       print('%s\t%s' % (x[0],x[1]))
