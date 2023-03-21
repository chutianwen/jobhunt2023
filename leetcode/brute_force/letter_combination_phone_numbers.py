class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        digit_letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        combinations = []
        end = len(digits)

        def dfs(cur_idx, cur_string):

            if cur_idx == end:
                if end != 0:
                    combinations.append(cur_string)
                return

            if digits[cur_idx] in digit_letter_map:
                for letter in digit_letter_map[digits[cur_idx]]:
                    dfs(cur_idx + 1, cur_string + letter)
            else:
                dfs(cur_idx + 1, cur_string)

        dfs(0, '')
        return combinations


class BackTrackSolution:
    def letterCombinations(self, digits: str) -> List[str]:

        digit_letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def dfs(cur_idx):
            if cur_idx < 0:
                return []

            res = []
            combinations = dfs(cur_idx - 1)
            if digits[cur_idx] in digit_letter_map:
                for letter in digit_letter_map[digits[cur_idx]]:
                    if combinations:
                        for combination in combinations:
                            res.append(f'{combination}{letter}')
                    else:
                        res.append(f'{letter}')

            return res

        return dfs(len(digits) - 1)