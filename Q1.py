# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         if nums.count(target/2)==2:
#             a=nums.index(target/2)
#             nums[a]=target/2+1
#             b=nums.index(target/2)
#             return [a,b]
#         for k, num in enumerate(nums):
#             if (target-num) in nums and num!=target/2:
#                 return [k, nums.index(target-num)]

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]



            
nums = [3,2,4]
target = 6          
A=Solution()
B=A.twoSum(nums, target)
print(B)