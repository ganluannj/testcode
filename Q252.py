# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 11:02:36 2021

@author: lsttl
"""
class Interval(object):
    def __init__(self, start, end):
        self.start=start
        self.end=end

class Solution():
    def canattendMeetins(self, Intervals):
        Intervals.sort(key=lambda x:x.start)
        for i, interval in enumerate(Intervals[1:]):
            if interval.start<Intervals[i].end:
                return False
        return True
    def canattendMeetins2(self, Intervals):
        if not len(Intervals): 
            return True
        from queue import PriorityQueue
        PQ=PriorityQueue()
        count=0
        for interval in Intervals:
            PQ.put((interval.start, count, interval))
            count=count+1
        cur=PQ.get()[2]
        while PQ.qsize():
            tem=PQ.get()[2]
            if tem.start<cur.end:
                return False
            else:
                cur=tem
        return True
            

#%%
S=Solution()
Intervals=[Interval(0,30), Interval(15,20), Interval(5,10)]
print(S.canattendMeetins(Intervals))
print(S.canattendMeetins2(Intervals))
#%%
S=Solution()
Intervals=[Interval(7,10), Interval(2,4), Interval(5,6)]
print(S.canattendMeetins(Intervals))
print(S.canattendMeetins2(Intervals))

#%%
for i in range(5):
    if i ==3:
        continue
    print(i)

#%%
Q=[1,2,3]
for _ in range(len(Q)):
    Q.append(1)
    print(Q)
    
#%%
from queue import PriorityQueue
PQ=PriorityQueue()
PQ.put((3,2,1))

#%%
import numpy as np
A=np.matrix(np.array([[1,0,2],[7,4,1],[1,9,3]]))
K=np.linalg.eig(A)[0]
Sum1=sum([1/k for k in K])
InvA=np.linalg.inv(A)
Sum2=sum([InvA[k,k] for k in range(len(A))])
print(Sum1-Sum2)
Sum3=sum([1/A[k,k] for k in range(len(A))])

#%%
for i in range(3,6):
    print (i)
#%%
for i in range(1,8,2):
    print(i)

#%%
for i in range(5):
    print (i)

#%%
L=[3,4,5,6]
for l in L:
    print (l)
#%%
L=[3,4,5,6]
for i, l in enumerate(L):
    print(i,l)

#%%
L=[3,4,5,6]
print(L[-1])
print(L[:-1])
print(L[1:])
#%%
a=3
b=2
if a>b:
    pass
