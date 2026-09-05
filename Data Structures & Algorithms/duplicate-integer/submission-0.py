class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # print(nums)
        nums.sort()
        # print(nums)
        for i in range(len(nums)):
            if i < len(nums)-1:
                if nums[i+1] == nums[i]:
                    return True

        return False

        