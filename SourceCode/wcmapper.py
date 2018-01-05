#!/usr/bin/env python
import sys
import string
import re

#--- get all lines from stdin ---
for line in sys.stdin:
    #--- remove leading and trailing whitespace---
    line = line.strip()
    line = line.lower()
    line = re.sub(r'".+"', ' ', line)
    line = re.sub(r'[^a-zA-Z ]', ' ', line)
    #--- split the line into words ---
    words = line.split()

    #--- output tuples [word, 1] in tab-delimited format---
    for word in words:
        if word not in string.punctuation:
            print ('%s\t%s' % (word, "1"))