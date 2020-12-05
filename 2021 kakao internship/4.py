import sys
import re
import itertools

dic = {}
attri = []
n = int(input())
per = float(input())
members = int(input())
arrs = [sys.stdin.readline() for i in range(members)]

for arr in arrs:
    temp = re.split(',', arr)
    for i in temp:
        if i not in dic:
            dic[i] = 1
            attri.append(i)
        else:
            dic[i] += 1

combi = list(itertools.combinations(attri,n))