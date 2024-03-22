# class Solution:
#     def minSubsequence(self, nums: List[int]) -> List[int]:
#         # get the sum of nums and then adding elements from the 
#         # largest to smallest to the final result until sum of the 
#         # result is greater than half of the original sum
#         Halfsum=sum(nums)/2
#         Ans=[]
#         while sum(Ans)<=Halfsum:
#             Max=max(nums)
#             Ans.append(Max)
#             nums.remove(Max)
#         return Ans
        

