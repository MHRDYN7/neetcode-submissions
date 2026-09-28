class Solution:
    def isPalindrome(self, s: str) -> bool:
        # gotta have pointer on two ends
        left, right = 0, len(s)-1

        # shift the the pointers closer to the center in each iteration in a while loop

        while left < right:
            # check the left and right chars if they are alphanumeric
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1

            else:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
        return True

        