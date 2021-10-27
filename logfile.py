#!/bin/env python
"""
This log file has 2520 entries
 Make      Color    Plate    YYYY MM DD hr min sec
 Nissan    Black    BDKK-863 2021  2 24  9  0  0
 Subaru    Green    ANEJ-773 2021  2 24  9  0 20
"""

import sys, re, datetime
s=sys.stdin.readline().rstrip()
cols=sys.stdin.readline().rstrip()
#print(cols)
ml=re.findall(r"\b\w+",cols)
if ml:
    ids=[]
    for m in ml:
        ids.append(cols.index(m))
ids[-1]-=1
#print(ids)
colnames=[cols[f:t].strip() for f,t in zip(ids,ids[1:])]
colnames.append(cols[ids[-1]:].strip())
#print(colnames)
data=list()
for s in sys.stdin:
    tmp=dict()
    for k in range(3):
        tmp[colnames[k]]=s[ids[k]:ids[k+1]].strip()
    tmp["dt"]=datetime.datetime(
     int(s[ids[3]:ids[4]]), 
     int(s[ids[4]:ids[5]]), 
     int(s[ids[5]:ids[6]]), 
     int(s[ids[6]:ids[7]]), 
     int(s[ids[7]:ids[8]]), 
     int(s[ids[8]:]))
    data.append(tmp)
#print(len(data))
t0=datetime.datetime(
    2021, 
    2, 
    24, 
    14, 
    15, 
    )
io=list()
for tmp in data:
    if tmp["Make"] != "Nissan":
        continue
    if tmp["Color"] != "White":
        continue
    if tmp["dt"] > t0:
        continue
    io.append(tmp)
#print(len(io))
"""
The below-listed license plate(s) should be contacted:
Plate hr min
Note: In your output file, between the plate numbers and hour should be 
five spaces and between hour and minute should be two spaces.
"""
print("The below-listed license plate(s) should be contacted:")
print("Plate"+" "*5+"hr"+" "*2+"min")
for tmp in io:
    dt=tmp["dt"].timetuple()
    s=tmp["Plate"] + " "*5 + str(dt[3]) + " "*2 + str(dt[4])
    print(s)
