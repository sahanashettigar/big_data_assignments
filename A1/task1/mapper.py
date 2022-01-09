#!/usr/bin/env python3
import sys 
import json
import datetime

def records_per_hour(record):
    date=record['Start_Time']
    desc=["lane blocked", "shoulder blocked", "overturned vehicle"]
    weather_cond=["heavy snow", "thunderstorm", "heavy rain", "heavy rain showers","blowing dust"]
    description_present=False
    #for i in desc:
    record_check=record['Description'].lower()
    if desc[0] in  record_check or desc[1] in  record_check or desc[2] in  record_check: #or desc[3] in record['Description'].lower():
            description_present=True
    conditions=(description_present and (record['Severity']>=1 and record['Severity']<=4 ) and (record['Sunrise_Sunset']=='Night' or record['Sunrise_Sunset']=='night') and (record['Visibility(mi)']<=10.0) and (record['Precipitation(in)']>=0.2) and (record['Weather_Condition'].lower() in weather_cond))
    if(conditions):
        try:
            date_formatted = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
            print('%s %s' % (date_formatted.hour, 1))
        except ValueError:
            #print("Variable x is not defined")
            x=date.split(".")[0]
            #print(x)
            date_formatted = datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
            print('%s %s' % (date_formatted.hour, 1))
        
        


for line in sys.stdin:
    try:
        record = json.loads(line)
        records_per_hour(record)
    except Exception as e:
        print(e)  
