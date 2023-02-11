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

orphan_pages = []
for (k,v) in is_orphan_page.items():
  if v:
    orphan_pages.append(int(k))

orphan_pages.sort()
for p in orphan_pages:
  print(p)

#TODO
# print(xx) print as final output