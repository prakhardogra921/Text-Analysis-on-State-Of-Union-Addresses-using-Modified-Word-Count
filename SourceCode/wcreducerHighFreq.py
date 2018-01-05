#!/usr/bin/env python
import sys
 
# maps words to their counts
word2count = {}
word_high_freq = {}

f = open(sys.argv[1], "r")
for line in f.readlines():
    word = line.split("\t")[0]
    avg = float(line.split("\t")[1])
    std_dev = float(line.split("\t")[2])
    word_high_freq[word] = avg + 2.0*std_dev
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
 
    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        continue

    try:
        word2count[word] = word2count[word]+count
    except:
        word2count[word] = count
for word in word2count:
    if word in word_high_freq.keys() and word2count[word] > word_high_freq[word]:
        print ('%s\t%s\t%s' % (word, word2count[word], word_high_freq[word]))
# write the tuples to stdout
# Note: they are unsorted
