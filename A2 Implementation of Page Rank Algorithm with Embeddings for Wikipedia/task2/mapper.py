#!/usr/bin/env python3
import sys
import math
import json 
with open(sys.argv[2]) as f:
    embeddings=json.load(f)
page_rank_dict= {}
v_file = open(sys.argv[1],"r")
for lines in v_file:
    lines= lines.strip()
    a = lines.split(",")
    node = a[0]
    if len(a)!=1:
        page_rank = float(a[1].strip('\n'))
        page_rank_dict[node] = page_rank
for line in sys.stdin:
    line=line.strip()
    try:
        a = line.split("#")
        source = a[0].strip()
        temp1 = a[1]
        temp2=temp1.strip('[')
        temp3=temp2.strip(']')
        dests = temp3.split(",")
        num_nodes = len(dests)
        for i in range(len(dests)): 
            destination=dests[i].strip(' ')
            #similarity = np.dot(embeddings[source], embeddings[destination])/(np.linalg.norm(embeddings[source])*np.linalg.norm(embeddings[destination]))
            similarity=sum(x*y for x, y in zip(embeddings[source], embeddings[destination]))/(math.sqrt(sum(x**2 for x in embeddings[source]))*math.sqrt(sum(x**2 for x in embeddings[destination])))
            #print(x*y for x, y in zip(embeddings[source], embeddings[destination]))
            node_contribution = float(page_rank_dict[source]*similarity)/float(num_nodes)
            print('%s#%s'%(destination,node_contribution))   
            print('%s#%s'%(source,0.00))                 
    except Exception as e:
        print(e)
v_file.close()