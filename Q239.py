
'''
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               ----- Heap                                      cur
[1  8  -1] -3  5  3  6  7       8   <1,0> <8,1>, <-1,2>                        2
 1 [8  -1  -3] 5  3  6  7       8   <1,0>, <8,1>, <-1,2>, <-3,3>               3
 1  8 [-1  -3  5] 3  6  7       5   <1,0>, <8,1>, <-1,2>, <-3,3>, <5,4>        4
 1  8  -1 [-3  5  3] 6  7       5   1,-1, -3, 5, 6 
 1  8  -1  -3 [5  3  6] 7       6   1, 3, -1, -3, 5, 3,
 1  8  -1  -3  5 [3  6  7]      7   1, 3, -1, -3, 5, 3, 6, 7
'''
# keep push one element into the heap, 
# every step if 

# create a new object ValIndex which has two attributes, value and index
# use a max heap to store this ValIndex
# have index to travelse the array
# first genreate the heap of size k and output the first max
# then when move to the right, we first add the new element
# then we peek the max in the heap, if its index outside  the range [index-k+1, index], we just pop it
# if the max in the heap is inside the range [index-k+1, index], we will add it into our final result
# Q is empty add to the right
# Q is not empty, new element > Q[-1], Q.pop(), keep pop until new element <=Q[-1].Val or Q is empty, add new elment to the right
# for index >=k-1:
# if Q[0].Index < index-k+1: Q.popleft()
# Result.append(Q[0].Val)

class ValIndex():
  def __init__(self, Val, Index):
    self.Val=Val
    self.Index=Index
  def __lt__(self, Other):
    return self.Val>Other.Val

from collections import deque
class Solution2():
  def WinMax(self, Array, k):
    Result=list()
    Q = deque()
    for index in range(len(Array)):
      Obj = ValIndex(Array[index], index)
      if len(Q)==0:
        Q.append(Obj)
      else:
        while len(Q)>0 and Obj.Val>Q[-1].Val:
          Q.pop()
        Q.append(Obj)
      if index>=k-1:
        if Q[0].Index<index-k+1:
          Q.popleft()
        Result.append(Q[0].Val)
    return Result
    
import heapq
class Solution():
  def WinMax(self, Array, k):
    Result=list()
    H = list()
    heapq.heapify(H)
    for index in range(len(Array)):
      Obj = ValIndex(Array[index], index)
      heapq.heappush(H, Obj)
      if index >=k-1:
        Tem = heapq.heappop(H)
        while Tem.Index < index-k+1:
          Tem = heapq.heappop(H)
        Result.append(Tem.Val)
        heapq.heappush(H,Tem)
     
    return Result  
  
nums = [1,3,-1,-3,5,3,6,7]
k = 3 
Sol=Solution2()
print(Sol.WinMax(nums, k))
  
          
          
          
        
    
  