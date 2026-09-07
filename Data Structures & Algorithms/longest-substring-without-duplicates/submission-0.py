class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # go thru all the chars one by one.
        # keep a set of items for the things you have seen
        # add to the set only if the new string is not in set
        # if it is set, we need to
        # [a,b,c,a,c]
        best = 0
        window = set()
        window_start = 0

        for i, char in enumerate(s):
            while char in window:
                # don't insert, but remove stuff from window there is no char
                window.remove(s[window_start])
                window_start += 1
            # if char not in window -> add to window
            window.add(char)
            # update best length
            best = max(best, i+1-window_start)

        return best
        