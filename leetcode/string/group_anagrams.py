from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_maps = defaultdict(list)
        for text in strs:
            sorted_maps[''.join(sorted(text))].append(text)
        res = []
        for values in sorted_maps.values():
            res.append(values)
        return res