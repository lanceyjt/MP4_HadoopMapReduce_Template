#!/usr/bin/env python3
import sys


for line in sys.stdin:
  # TODO
  line = line.strip()
  source, dest = line.split(":")
  source = source.strip()
  dests = [x.strip() for x in dest.split(' ')]
  for d in dests:
      print('%s\t%s' % (source,d))
  # print('%s\t%s' % (  ,  )) pass this output to reducer

