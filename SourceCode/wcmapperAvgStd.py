#!/usr/bin/env python
import sys
import string
import re

from dateutil.parser import parse

def is_date(string):
    try:
        parse(string)
        return True
    except ValueError:
        return False

flag = False
#count = 1
year = 1
yearFlag = False
#--- get all lines from stdin ---
for line in sys.stdin:
    #--- remove leading and trailing whitespace---
    """
    line = line.strip()
    if flag is False:
        if line.split(", ")[-1] == sys.argv[1]:
            flag = True
        continue
    if line.split(", ")[-1] == str(int(sys.argv[1]) + 4):
        break
    if line == "***":
        count += 1
        continue
    line = line.lower()
    line = re.sub(r'".+"', ' ', line)
    line = re.sub(r'[^a-zA-Z ]', ' ', line)
    #--- split the line into words ---
    words = line.split()

    for word in words:
        if word not in string.punctuation:
            print ('%s\t%s' % (word, str(1)+"_year"+str(count)))
    """
    line = line.strip()
    if flag is False:
        if line.split(", ")[-1] == sys.argv[1]:
            flag = True
        continue
    if yearFlag:
        if is_date(line):
            year += 1
            yearFlag = False

    if line.split(", ")[-1] == str(int(sys.argv[1]) + 4):
        break
    if line == "***":
        yearFlag = True
        continue
    line = line.lower()
    line = re.sub(r'".+"', ' ', line)
    line = re.sub(r'[^a-zA-Z ]', ' ', line)
    # --- split the line into words ---
    words = line.split()
    # count += 1
    for word in words:
        if word not in string.punctuation:
            print ('%s\t%s' % (word, str(1) + "_year" + str(year)))

