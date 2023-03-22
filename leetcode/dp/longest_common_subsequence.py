class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0

        num_rows = len(text1)
        num_cols = len(text2)
        dp = [[0 for _ in range(num_cols)] for _ in range(num_rows)]

        dp[0][0] = 1 if text1[0] == text2[0] else 0

        for col in range(1, num_cols):
            dp[0][col] = max(dp[0][col - 1], 1 if text1[0] == text2[col] else 0)

        for row in range(1, num_rows):
            dp[row][0] = max(dp[row - 1][0], 1 if text1[row] == text2[0] else 0)

        for row in range(1, num_rows):
            for col in range(1, num_cols):
                candidate_grow = dp[row - 1][col - 1] + (1 if text1[row] == text2[col] else 0)
                dp[row][col] = max(candidate_grow, dp[row - 1][col], dp[row][col - 1])

        # table = ''
        # for row in range(num_rows):
        #     row_msg = []
        #     for col in range(num_cols):
        #         row_msg.append(str(dp[row][col]))
        #     row_msg = ','.join(row_msg)
        #     table = f'{table}\n{row_msg}'
        # print(table)
        return dp[num_rows - 1][num_cols - 1]
