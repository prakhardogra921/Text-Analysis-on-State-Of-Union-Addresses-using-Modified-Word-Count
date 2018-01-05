#!/usr/bin/env python
import sys
import math

current_word = None
current_count = 0
word = None

word2count = {}
count_list = []

word2count_by_year = {}

def add_to_dict_by_year(current_word, current_count):
    if word2count_by_year.get(current_word) == None:
        word2count_by_year[current_word] = current_count
    else:
        count_val = word2count_by_year.get(current_word)
        word2count_by_year[current_word] = count_val + 1

def add_to_dict(current_word, current_count):
    if word2count.get(current_word) == None:
        word2count[current_word] = current_count
    else:
        count_val = word2count.get(current_word)
        word2count[current_word] = count_val + 1

def get_temp_dict(sourcedict, string):
    newdict = {}
    for key in sourcedict.keys():
        if key.startswith(string):
            newdict[key] = sourcedict[key]
    return newdict

def calculate_std_dev():
    average = 0
    for word in word2count:
        average = word2count.get(word) / 4.0
        partial_sq = 0
        sum = 0
        std_dev = 0
        temp_dict = get_temp_dict(word2count_by_year, word + "_")
        count = 0
        for tempkey in temp_dict:
            partial_sq = (int(temp_dict.get(tempkey)) - average) * (int(temp_dict.get(tempkey)) - average)
            sum += partial_sq
            count += 1
        while count < 4:                    		#takes care of the case when the word doesn't appear in the file
            sum += average*average
            count += 1
        std_dev = math.sqrt(sum / 4.0)
        print ('%s\t%s\t%s' % (word, average, std_dev))

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
 
    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)
    dict_word = ""
    dic_count = ""
    # convert count (currently a string) to int
    try:
        dict_word = word + "_" + count.split("_")[1]
        dic_count = count.split("_")[0]
        dic_count = int(dic_count)
    except ValueError:
        continue
    add_to_dict_by_year(dict_word, dic_count)
    add_to_dict(word, dic_count)

calculate_std_dev()