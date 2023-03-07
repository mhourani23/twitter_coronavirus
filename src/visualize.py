#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
for k,v in items:
    print(k,':',v)


# first getting top 11
top_11 = sorted(items[:11], key=lambda x:x[1])

# new arrays for keys and values
k = []
v = []

for p, q in top_11:
    k.append(p)
    v.append(q)

# removing 'country_code'
if k[0] == "country_code":
    k = k[1:]
    v = v[1:]
else:
    k = k[:-1]
    v = v[:-1]

# test
for i in range(len(k)):
    print(k[i], v[i])

# importing needed libraries
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# plot if lang
if args.input_path == "reduced.lang":
    plt.bar([i for i in range(len(k))], v, width = 0.3, color = 'yellow')
    plt.ylabel("# tweets")
    plt.xlabel("lang")
    plt.xticks([i for i in range(len(k))], k)
    plt.title("languages with most tweets that have: " + str(args.key))
    if args.key == "#coronavirus":
        plt.savefig('eng_lang_plot1.png')
    else:
        plt.savefig('kor_lang_plot2.png')
else:
    plt.bar([i for i in range(len(k))], v, width = 0.3, color = 'red')
    plt.ylabel("# tweets")
    plt.xlabel("country")
    plt.xticks([i for i in range(len(k))], k)
    plt.title("countries with most tweets that have: " + str(args.key))
    if args.key == "#coronavirus":
        plt.savefig('eng_country_plot3.png')
    else:
        plt.savefig('kor_country_plot3.png')



