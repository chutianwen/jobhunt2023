# Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) :
        # (root, size) -> tree
        self.visited = {}
        self.helper(1, n)
        return self.helper(1, n)

    def helper(self, start, end):
        if start > end:
            return [[]]
        if (start, end) in self.visited:
            return self.visited[(start, end)]
        if end - start == 0:
            return [[start]]

        res = []
        for cut in range(start, end + 1):
            lefts = self.helper(start, cut - 1)
            rights = self.helper(cut + 1, end)
            for left in lefts:
                for right in rights:
                    tmp = [cut]
                    depth = 1
                    while left or right:
                        size_branch = 2 ** (depth - 1)
                        if left:
                            tmp.extend(left[:size_branch])
                            left = left[size_branch:]
                        else:
                            tmp.extend([None] * size_branch)
                        if right:
                            tmp.extend(right[:size_branch])
                            right = right[size_branch:]
                        else:
                            tmp.extend([None] * size_branch)
                        depth += 1
                    res.append(tmp)

        self.visited[(start, end)] = res
        return res

solution = Solution()
print(solution.generateTrees(3))

class Solution2:
    def generateTrees(self, n: int):
        # (root, size) -> tree
        self.visited = {}
        self.helper(1, n)
        return self.helper(1, n)

    def helper(self, start, end):
        if start > end:
            return [None]
        if (start, end) in self.visited:
            return self.visited[(start, end)]
        if end == start:
            root = TreeNode(start)
            return [root]

        res = []
        for cut in range(start, end + 1):
            lefts = self.helper(start, cut - 1)
            rights = self.helper(cut + 1, end)
            for left in lefts:
                for right in rights:
                    root = TreeNode(cut)
                    root.left = left
                    root.right = right
                    res.append(root)

        self.visited[(start, end)] = res
        return res