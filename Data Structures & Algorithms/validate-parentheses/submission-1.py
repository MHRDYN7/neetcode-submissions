class Solution:
    def isValid(self, s: str) -> bool:
        state = []
        rule = {"}":"{", ")":"(", "]":"["}

        for char in s:
            # if char in rule and state.pop() != rule[char]:
            #     return False
            # else:
            #     continue

            if char in rule:
                if not state or state.pop() != rule[char]:
                    return False
            else:
                state.append(char)

        # everything opened should be closed

        return not state



