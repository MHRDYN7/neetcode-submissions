class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # has duplicate if the set len and list len are not same (set is smaller)
        return len(set(nums)) != len(nums)


        