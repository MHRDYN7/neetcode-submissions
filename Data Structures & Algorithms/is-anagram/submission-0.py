class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def processor(string):
            data = {}
            for character in string:
                if character not in data:
                    data[f"{character}"] = 1
                else:
                    data[f"{character}"] += 1
            return data

        return processor(s) == processor(t)  