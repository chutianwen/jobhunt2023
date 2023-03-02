# Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

# Definition for a binary trees node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def numTrees(self, n: int) -> int:
        #n:   0, 1, 2
        dp = [1, 1, 2]
        for root in range(3, n+1):
            res = 0
            for cur in range(1, root + 1):
                left_size = cur - 1
                right_size = root - cur
                res += dp[left_size] * dp[right_size]
            dp.append(res)
        return dp[n]