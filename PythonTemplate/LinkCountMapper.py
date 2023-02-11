#!/usr/bin/env python3
import sys


for line in sys.stdin:
  #TODO
  line = line.strip()
  _, dest = line.split(":")
  dests = [x.strip() for x in dest.split(' ') if x.strip()!='']
  for d in dests:
      print('%s\t%s' % (d,1))
  # print('%s\t%s' % (  ,  )) pass this output to reducer
