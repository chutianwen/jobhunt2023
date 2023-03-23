class Solution:
    def longestValidParentheses(self, s: str) -> int:

        cnt_left = cnt_right = max_len = 0
        for letter in s:
            if letter == "(":
                cnt_left += 1
            if letter == ")":
                cnt_right += 1

            if cnt_left == cnt_right:
                max_len = max(max_len, cnt_left + cnt_right)
            elif cnt_right > cnt_left:
                cnt_left = cnt_right = 0

        cnt_left = cnt_right = 0
        for letter in s[::-1]:
            if letter == "(":
                cnt_left += 1
            if letter == ")":
                cnt_right += 1

            if cnt_left == cnt_right:
                max_len = max(max_len, cnt_left + cnt_right)
            elif cnt_right < cnt_left:
                cnt_left = cnt_right = 0

        return max_len