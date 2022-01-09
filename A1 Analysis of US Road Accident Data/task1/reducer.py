#!/usr/bin/env python3
import sys

dict_hours={}

# read the entire line from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	# slpiting the data on the basis of tab we have provided in mapper.py
	hour, count = line.split(' ', 1)
	try:
		count = int(count)
		hour=int(hour)
	except ValueError:
		continue

	if hour not in dict_hours.keys():
    		dict_hours[hour]=count
	else:
    		dict_hours[hour] += count
dict_hours = dict(sorted(dict_hours.items(),key=lambda x:x[0]))
for key in dict_hours.keys():
    print('%s %s' % (key, dict_hours[key]))
	# this IF-switch only works because Hadoop sorts map output
	# by key (here: hour) before it is passed to the reducer
	

