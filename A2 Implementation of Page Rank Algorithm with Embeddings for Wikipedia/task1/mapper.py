#!/usr/bin/env python3
import sys
for line in sys.stdin:
    try:
        source,dest=line.split()
        print('%s/%s' %(source,dest))
    except Exception as e:
        print(e)  