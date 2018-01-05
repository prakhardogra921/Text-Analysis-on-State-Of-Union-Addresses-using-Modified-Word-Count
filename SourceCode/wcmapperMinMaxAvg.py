#!/usr/bin/env python
import sys
import string
import re

count = 0
#--- get all lines from stdin ---
for line in sys.stdin:
    #--- remove leading and trailing whitespace---
    line = line.strip()
    if line == "***":
        count += 1
    line = line.lower()
    line = re.sub(r'".+"', ' ', line)
    line = re.sub(r'[^a-zA-Z ]', ' ', line)
    #--- split the line into words ---
    words = line.split()

    #count += 1
    #--- output tuples [word_year<number>, 1] in tab-delimited format---
    for word in words:
        if word not in string.punctuation:
            print ('%s\t%s' % (word+"_year"+str(count), "1"))