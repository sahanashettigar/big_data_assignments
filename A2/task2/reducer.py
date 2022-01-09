#!/usr/bin/env python3
import sys
p_required=-1
total_contrib=0.00
for line in sys.stdin:
    try:
        line=line.strip()
        p,contrib=line.split('#',2)
        p=int(p)
        contrib=float(contrib)
        if p_required==-1:
            p_required=p
            total_contrib+=contrib
        elif p!=p_required:
            rank=0.15+0.85*total_contrib
            rank = float("{0:.2f}".format(rank))
            print('%s,%s'%(p_required,rank))
            total_contrib=0.00
            p_required=p
            total_contrib+=contrib
        else:
            total_contrib+=contrib
    except Exception as e:
        print(e)  
rank=0.15+0.85*total_contrib
rank = "{:.2f}".format(rank)
print('%s,%s'%(p_required,rank))