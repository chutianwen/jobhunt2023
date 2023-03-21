'''
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
'''
from collections import defaultdict


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        length_s = len(s)
        explored = defaultdict(list)
        words = set(wordDict)

        for end in range(1, length_s + 1):
            candidates = []
            for split in range(0, end):
                right_part_s = s[split: end]
                if right_part_s in words:
                    if split == 0:
                        candidates.append(right_part_s)
                    if split in explored:
                        for pre_candidate in explored[split]:
                            candidates.append(f'{pre_candidate} {right_part_s}')
                    explored[end] = candidates

        return explored.get(length_s, [])

