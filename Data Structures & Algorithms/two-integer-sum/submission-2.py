class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for I, num in enumerate(nums):
            candidate = target - num
            for J, option in enumerate(nums[I+1:]):
                if option == candidate:
                    return [I, J+I+1]
    