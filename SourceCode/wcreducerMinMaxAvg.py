#!/usr/bin/env python
import sys
 
# maps words to their counts
word2count = {}
current_word = None
current_count = 0
word = None

def add_to_dict(current_word, current_count):
    keyword = current_word.split("_")[0]
    if word2count.get(keyword) == None:
        count_list = []
        count_list.append(current_count)
        word2count[keyword] = count_list
    else:
        word2count.get(keyword).append(current_count)

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

    if current_word == word:
        current_count += count
    else:
        if current_word:
            add_to_dict(current_word, current_count)
        current_count = count
        current_word = word                                 #new word is stored as current_word

# do not forget to output the last word if needed!
if current_word == word:
    #print '%s\t%s' % (current_word, current_count)
    add_to_dict(current_word, current_count)

for word in word2count:
    minimum = min(word2count[word])
    maximum = max(word2count[word])
    average = sum(word2count[word])/231.0
    print ('%s\t%s\t%s\t%s' % (word, minimum, maximum, average))