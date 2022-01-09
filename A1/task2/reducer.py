#!/usr/bin/env python3
import sys

dict_state={}

# read the entire line from STDIN
for line in sys.stdin:
    city_found=0
	# remove leading and trailing whitespace
    line = line.strip()
	# slpiting the data on the basis of tab we have provided in mapper.py
    state, city = line.split(' ', 1)
    try:
        if state not in dict_state.keys():
            dict_state[state]={}
        for key, value in dict_state[state].items():
            if city==key:
                dict_state[state][key]=value+1
                city_found=1
                break
        if(city_found==0):
            dict_state[state][city]=1
        #if city not in dict_state[state].keys():
         #   dict_state[state][city]=1
        #else:
          #  dict_state[state][city]+=1
    except ValueError:
        continue
dict_state = dict(sorted(dict_state.items(),key=lambda x:x[0]))
for state in dict_state.keys():
    print(state)
    dict_state[state] = dict(sorted(dict_state[state].items(),key=lambda x:x[0]))
    #print(dict_state[state])
    for key in dict_state[state].keys():
        print(key, dict_state[state][key])
    state_total = dict_state[state].values()
    total = sum(state_total) 
    print('%s %s' % (state, total))
	# this IF-switch only works because Hadoop sorts map output
	# by key (here: hour) before it is passed to the reducer
	

