#!/usr/bin/env python3
import sys

#TODO
current_page = None
current_count = 0
page = None

# input comes from STDIN
for line in sys.stdin:
    # TODO
    line = line.strip()
    page, count = line.split('\t')
    try:
        count = int(count)
    except ValueError:
        continue
    
    if current_page == page:
        current_count += count
    else:
        if current_page:
            print('%s\t%s' % (current_page, current_count))
        current_page = page
        current_count = count
# TODO
# print('%s\t%s' % (  ,  )) print as final output
if current_page == page:
    print('%s\t%s' % (current_page, current_count))