class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        # single for loop checks if two consecutive nums are same
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
        