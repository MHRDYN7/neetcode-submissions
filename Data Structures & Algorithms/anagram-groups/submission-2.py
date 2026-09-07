
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         # preferably I would want to go through the strs list only once
#         data = {}
#         for word in strs:
            
#             sorted_word = tuple(sorted(word))
            
#             if sorted_word in data:
#                 data[sorted_word].append(word) 
#             else:
#                 data[sorted_word] = [word]
#         return list(data.values())


from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = defaultdict(list)

        for word in strs:
            data[tuple(sorted(word))].append(word)

        return list(data.values())


