#!/bin/env python

#Start: ./logfile.py <logfile.txt

""" Task:
A witness reported that a vehicle has hit
another vehicle when it was getting out of a
parking spot in a mega shopping mall. The
witness could only identify the make and the
color of the guilty car but not its license plate.
The mega shopping mall only monitors the
entering vehicles from the single entrance of its
parking lot by recording the make, color, and
license plate number of the entering vehicles. We have given the log file (logfile.txt) of all
vehicles on the date of the accident. Assuming that the guilty car is a white Nissan, and the
accident took place around 2:15pm, write a Fortran program to identify those plate numbers
entered before the accident time. Your code should create an output text file named
output_plates.txt and lists the license plate(s), and hour & minute of entry(ies) following
the below sentence & header.
The below-listed license plate(s) should be contacted:
Plate
hr min
Note: In your output file, between the plate numbers and hour should be five spaces and between hour
and minute should be two spaces.
"""

""" The begining of the logfile.txt:
This log file has 2520 entries
 Make      Color    Plate    YYYY MM DD hr min sec
 Nissan    Black    BDKK-863 2021  2 24  9  0  0
 Subaru    Green    ANEJ-773 2021  2 24  9  0 20
...
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
