#!/usr/bin/env python3
import sys


#TODO
is_orphan_page = {}
dests = []

for line in sys.stdin:
  # TODO
  line = line.strip()
  source, dest = line.split('\t')
  is_orphan_page[source] = True
  dests.append(dest)

for dest in dests:
  is_orphan_page[dest] = all([is_orphan_page.get(dest, False), False])

for (k,v) in is_orphan_page.items():
  if v:
    print(k)

#TODO
# print(xx) print as final output