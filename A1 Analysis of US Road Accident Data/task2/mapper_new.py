#!/usr/bin/env python3
import sys
import json
import requests
import time
def within_euclidean(x,y,given_latitude,given_longitude,d):
    #finding euclidean distance 
    #print(given_latitude,given_longitude)
    #print('hello')
    euclidean=float(float((x-float(given_latitude))**2+(y-float(given_longitude))**2)**0.5)
    #print(euclidean)
    if euclidean<=float(d):
        return True
    else:
        return False
def send_request(latitude,longitude):
    url='http://20.185.44.219:5000/'
    data={
                    "latitude": latitude,
                    "longitude": longitude
                    }
    x = requests.post(url, json = data)
    json_data=x.json()
    state=json_data['state']
    city=json_data['city']
    null=['','NaN']
    city.replace(' ','^')
    if(state not in null and city not in null):
        #print(state,city,1)
        print('%s#%s#%s' % (state,city,1))
start=time.time()
for line in sys.stdin:
    try:
        record = json.loads(line)
        #print(sys.argv[1],sys.argv[2],sys.argv[3])
        if(record['Start_Lat']!='NaN' and record['Start_Lng']!='NaN'):
            #print('here1')
            if(within_euclidean(record['Start_Lat'],record['Start_Lng'],sys.argv[1],sys.argv[2],sys.argv[3])):
                #print('here')
                send_request(record['Start_Lat'],record['Start_Lng'])
    except Exception as e:
        continue
    

