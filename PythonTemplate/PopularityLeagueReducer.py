#!/usr/bin/env python3
import sys
#TODO
page_count = []

# input comes from STDIN
for line in sys.stdin:
    # TODO
    line = line.strip()
    page, count = line.split('\t')
    page_count.append([int(page), int(count)])

#TODO
page_count.sort(reverse=False, key=lambda x: x[0])
# print('%s\t%s' % (  ,  )) print as final output
for p in page_count:
    print('%s\t%s' % (p[0],p[1]))