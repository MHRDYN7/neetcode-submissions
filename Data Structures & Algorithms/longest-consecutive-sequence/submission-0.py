class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s, best = set(nums), 0

        for val in s:
            if val-1 not in s:
                start = val
                while val in s:
                    val += 1

                best = max(best, val - start)
        return best
        