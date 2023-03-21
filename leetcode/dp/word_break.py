class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # split between 0 and last
        # if s[: split] is pre_computed, then only need to check s[split:] is in wordDict.

        length_s = len(s)
        dp = [False for _ in range(length_s + 1)]
        dp[0] = True

        words = set(wordDict)

        for end in range(1, length_s + 1):
            for split in range(0, end):
                if dp[split] and s[split: end] in words:
                    dp[end] = True
                    break

        return dp[-1]


class TTLSolution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        end = len(wordDict)

        def dfs(cur_word):
            # print(cur_word)
            if len(cur_word) > len(s):
                return False
            if cur_word == s:
                return True

            for next_start in range(0, end):
                next_word = f'{cur_word}{wordDict[next_start]}'
                if s.startswith(next_word) and dfs(next_word):
                    return True
            return False

        return dfs("")