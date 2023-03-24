class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''

        length_str = len(s)
        dp = [[False] * length_str for _ in range(length_str)]
        res = s[0]
        for row in range(length_str, -1, -1):
            for col in range(row, length_str):
                if row == col:
                    dp[row][col] = True
                    continue
                if s[row] == s[col] and (dp[row+1][col -1] or col - row == 1):
                    if len(res) < len(s[row: col + 1]):
                        res = s[row:col + 1]
                    dp[row][col] = True
        return res
