# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         res = []
#         for i, num in enumerate(nums):
#             new_list = nums[:i] + nums[i+1:]
#             val = 1
#             for j in new_list:
#                 val *= j
#             res.append(val)
#         return res

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        left = [1]*n
        right = [1]*n

        temp1 = 1
        for i, num in enumerate(nums):
            left[i] *= temp1
            temp1 *= num
        
        temp2 = 1
        for j in range(n-1, -1, -1):
            right[j] *= temp2
            temp2 *= nums[j]

        return [l*r for l,r in zip(left, right)]



            
