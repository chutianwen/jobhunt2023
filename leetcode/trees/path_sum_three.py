# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
#
# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).
# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.counter = 0
        self.helper(root, [], targetSum)
        return self.counter

    def helper(self, root, pre_sums, targetSum):
        if not root:
            return

        cur_sums = []
        for pre_sum in pre_sums:
            if pre_sum + root.val == targetSum:
                self.counter += 1
            cur_sums.append(pre_sum + root.val)

        if root.val == targetSum:
            self.counter += 1
        cur_sums.append(root.val)
        self.helper(root.left, cur_sums, targetSum)
        self.helper(root.right, cur_sums, targetSum)


class Solution2(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.res = 0

        cache =collections.defaultdict(int)
        # full path used, only one combination.
        cache[0] = 1

        def dfs(root, sum, current_sum, cache):

            if not root: return

            current_sum += root.val
            old_sum = current_sum - sum

            self.res += cache.get(old_sum, 0)
            cache[current_sum] += 1

            dfs(root.left, sum, current_sum, cache)
            dfs(root.right, sum, current_sum, cache)

            cache[current_sum] -= 1

        dfs(root, sum, 0, cache)
        return self.res