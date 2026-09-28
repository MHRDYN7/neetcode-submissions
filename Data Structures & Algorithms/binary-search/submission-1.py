class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        # while not found, keep going
        while left <= right:
            # check if the middle value matches or not
            mid = left + (right - left)//2
            val = nums[mid]
            if val == target:
                return mid
            elif val > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1