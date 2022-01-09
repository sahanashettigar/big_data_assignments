#!/usr/bin/env python3
import sys
import re

current_state = None
current_city=None
current_count_state = 0
current_count_city = 0
state = None
city=None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    #print(line)
    # parse the input we got from mapper.py
    state,city,count = line.split(' ')

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    #if current_state == state:
    if re.fullmatch(current_state,state):
        current_count_state += count
        if current_count_city==city:
            current_count_city += count
        else:
            if re.fullmatch(current_city,city):
                print(current_city,current_count_city)
            current_count_city = count
            current_city=city
    else:
        if current_state:
            # write result to STDOUT
            if current_count_city==city:
                current_count_city += count
            else:
                if current_city:
                    print(current_city,current_count_city)
                current_count_city = count
                current_city=city
            print(current_state,current_count_state)
        current_count_state = count
        current_state = state
        print(current_state)

# do not forget to output the last word if needed!
if re.fullmatch(current_city,city):
    print(current_city,current_count_city)
if re.fullmatch(current_state,state):
    print(current_state,current_count_state)