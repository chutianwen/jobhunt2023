from collections import defaultdict

from collections import Counter

from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s or len(s) < k:
            return 0

        counter = Counter(s)
        break_points = []
        for idx, letter in enumerate(s):
            if counter[letter] < k:
                break_points.append(idx)

        if len(break_points) == 0:
            return len(s)
        else:
            # handle the last piece
            break_points.append(len(s))
            largest_value = self.longestSubstring(s[:break_points[0]], k)
            pre_break_point = break_points[0]

            for break_point in break_points[1:]:
                cur_value = self.longestSubstring(s[pre_break_point + 1: break_point], k)
                pre_break_point = break_point
                largest_value = max(largest_value, cur_value)

            return largest_value



class Solution1:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s or len(s) < k:
            return 0

        counter = Counter(s)
        cut_off_idx = None
        for idx, letter in enumerate(s):
            if counter[letter] < k:
                cut_off_idx = idx

        if cut_off_idx is None:
            return len(s)
        else:
            first_half = self.longestSubstring(s[:cut_off_idx], k)
            second_half = self.longestSubstring(s[cut_off_idx + 1:], k)
            return max(first_half, second_half)


class Solution2:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s or len(s) < k:
            return 0

        s_len = len(s)
        longest_candidate, longest_candidate_len = None, None

        # counter: key -> remaining need to pass, num: how many char need to pass
        dp = [[(defaultdict(int), 0) for _ in range(s_len)] for _ in range(s_len)]
        for row in range(s_len):
            for col in range(row, s_len):
                # print(row, col)
                cur_dict, num_char_to_remove = dp[row][col][0], dp[row][col][1]
                if row == col:
                    # update dict
                    cur_dict[s[row]] = k - 1
                    dp[row][col] = (cur_dict, 0 if k == 1 else 1)
                else:
                    left_dict, left_num_char_to_remove = dp[row][col - 1][0], dp[row][col - 1][1]
                    if s[col] in left_dict:
                        left_dict[s[col]] -= 1
                        if left_dict[s[col]] == 0:
                            left_num_char_to_remove -= 1

                        dp[row][col] = (left_dict, left_num_char_to_remove)
                    else:
                        left_dict[s[col]] = k - 1
                        if k > 1:
                            left_num_char_to_remove += 1
                        dp[row][col] = (left_dict, left_num_char_to_remove)

                        # valid
                if dp[row][col][1] == 0:
                    cur_len = col - row + 1
                    if longest_candidate_len is None or longest_candidate_len < cur_len:
                        longest_candidate_len = cur_len

        return longest_candidate_len if longest_candidate_len is not None else 0

from collections import Counter

c = Counter('123')
c.most_common()