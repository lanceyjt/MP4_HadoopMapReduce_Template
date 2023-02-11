#!/usr/bin/env python3
import sys
import math


#TODO
counts = []

for line in sys.stdin:
    # TODO
    line = line.strip()
    _, count = line.split('\t')
    counts.append(int(count))


sum_val = int(sum(counts))
mean_val = int(sum_val/len(counts))
min_val = int(min(counts))
max_val = int(max(counts))

temp_lst = [pow(x-mean_val, 2) for x in counts]
var_val = int(sum(temp_lst)/len(counts))

#TODO
# print('%s\t%s' % (  ,  )) print as final output

keys = ['Mean', 'Sum', 'Min', 'Max', 'Var']
vals = [mean_val, sum_val, min_val, max_val, var_val]

for i in range(5):
    print('%s\t%s' % (keys[i],vals[i]))