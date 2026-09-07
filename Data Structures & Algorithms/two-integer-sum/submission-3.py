class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # strategy: as you see new numbers, save them with index as keys in the dict
        data = {}
        for i, num in enumerate(nums):
            # check if the partner is in data already
            partner = target - num
            if partner in data:
                return [data[partner], i]
            # save the seen number in data
            data[num] = i
