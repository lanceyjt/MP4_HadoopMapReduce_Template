#!/usr/bin/env python3
import sys
#TODO
page_count = []

# input comes from STDIN
for line in sys.stdin:
    # TODO
    line = line.strip()
    try:
        page, count = line.split('\t')
        page_count.append([int(page), int(count)])
    except:
        continue

#TODO
page_count.sort(reverse=False, key=lambda x: x[1])
diff = [page_count[i][1] - page_count[i-1][1] for i in range(1, len(page_count))]
ranks = [0]
for i in range(len(diff)):
    current_rank = ranks[-1]
    if diff[i] > 0:
        ranks.append(len(ranks))
    else:
        ranks.append(current_rank)

# page_rank = [[page_count[0][0], 0]]
# current_rank = num = 0
# for i in range(1, len(page_count)):
#     if page_count[i][1] > page_count[i-1][1]:
#         current_rank += 1
#     num += 1
#     page_rank.append([page_count[i][0], current_rank])

pages = [x[0] for x in page_count]
page_rank = list(zip(pages, ranks))
page_rank.sort(reverse=True, key=lambda x: x[0])
# print('%s\t%s' % (  ,  )) print as final output
for p in page_rank:
    print('%s\t%s' % (p[0],p[1]))