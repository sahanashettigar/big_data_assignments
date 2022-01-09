#!/usr/bin/env python3
import sys
import re
current_state = ''
current_city=''
current_count_state = 0
current_count_city = 0
state = None
city=None
flag_state = 1

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    #print(line)
    # parse the input we got from mapper.py
    state,city,count = line.split('#', 2)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    
    if re.fullmatch(current_city, city):
            current_count_city += count
    else:
         if current_city:
              print(current_city,current_count_city)
         current_count_city = count
         current_city=city
    if re.fullmatch(current_state, state):
        current_count_state += count
    else:
        if current_state:
            print('%s %s' % (current_state, current_count_state))
        print(state)
        current_count_state = count
        current_state = state
            # write result to STDOUT
         

# do not forget to output the last word if needed!
if re.fullmatch(current_city, city):
    print(current_city,current_count_city)
if re.fullmatch(current_state,state):
    print(current_state,current_count_state)
