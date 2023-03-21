class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        num_row = len(matrix)
        num_col = len(matrix[0])

        max_area = 0
        dp = [[int(matrix[row][col]) for col in range(num_col)] for row in range(num_row)]

        for row in range(0, num_row):
            for col in range(0, num_col):
                if row > 0 and col > 0:
                    cur_width = min(dp[row-1][col], dp[row][col-1], dp[row-1][col-1]) + 1 if matrix[row][col] == '1' else 0
                    max_area = max(cur_width * cur_width, max_area)
                    dp[row][col] = cur_width
                else:
                    if dp[row][col] == 1:
                        max_area = max(max_area, 1)
        return max_area