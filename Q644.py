# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 09:51:59 2021

@author: lsttl
"""
#%%
class Solution():
    def findMaxAvg(self,nums,k):
        # first find the perfixsum
        Max=float('-inf')
        for i in range(1, len(nums)):
            nums[i]=nums[i]+nums[i-1]
        for i in range(len(nums)-k+1):
            for c in range(i+k-1, len(nums)):
                if i==0:
                    Max=max(Max, (nums[c])/(c+1))
                else:
                    Max=max(Max, (nums[c]-nums[i-1])/(c-i+1))
        return Max
    
    def findMaxAvg2(self, nums, k):
        Min=min(nums)
        Max=max(nums)
        while Max-Min>0.000001:
            Mid=Min+(Max-Min)/2
            if self.valid(nums,k,Mid):
                Min=Mid
            else:
                Max=Mid
        return Min
    def valid(self, nums, k, target):
        Sum=0
        for i in range(k):
            Sum+=nums[i]-target
        if Sum>0: 
            return True
        prev=0
        for i in range(k, len(nums)):
            prev+=nums[i-k]-target
            Sum+=nums[i]-target
            if prev<0:
                Sum-=prev
                prev=0
            if Sum>0:
                return True
        return False
#%%
class Solution2:
    def findMaxAverage(self, nums, k: int) -> float:
        Max=float('-inf')
        Sum=0
        for i in range(k):
            Sum+=nums[i]
        Max=max(Max, Sum)
        for i in range(k, len(nums)):
            Sum+=nums[i]
            Sum-=nums[i-k]
            Max=max(Max, Sum)
        return Max/k
#%%
from random import choice
Total=[k for k in range(-20,3000)]
Nums=[choice(Total) for _ in range(10)]
Nums2=Nums[:]
Nums3=Nums[:]
S=Solution()
k=4
A=S.findMaxAvg(Nums,k)
print('A: ',A)
A3=S.findMaxAvg2(Nums3, k)
print('A3: ',A3)
A2=float('-inf')
S2=Solution2()
for i in range(k, len(Nums2)+1):
    A2=max(A2, S2.findMaxAverage(Nums2, i))
print('A2: ', A2)
    
