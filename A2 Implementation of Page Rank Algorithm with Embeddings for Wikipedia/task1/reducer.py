#!/usr/bin/env python3
import sys
source_required=-1
source_adjlist=[]
v_file= open(sys.argv[1],'w')
ch1=0;
for line in sys.stdin:
    try:
        line = line.strip()
        source,dest=line.split('/',2)
        source=int(source)
        dest=int(dest)
        if source_required==-1:
            source_required=source
            source_adjlist.append(int(dest))
        elif source!=source_required:
            print('%s#%s'%(source_required,source_adjlist))
            v_file.write(str(source_required)+',1\n')
            source_adjlist=[]
            source_required=source
            source_adjlist.append(int(dest))
        else:
            source_adjlist.append(int(dest))
    except Exception as e:
        print(e)  
print('%s#%s'%(source_required,source_adjlist))
v_file.write(str(source_required)+',1')
v_file.close()