# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        end = len(preorder)
        root = TreeNode(preorder[0])
        stack = [root]
        p1 = 1
        p2 = 0

        while p1 < end:
            node = TreeNode(preorder[p1])
            if stack[-1].val != inorder[p2]:
                stack[-1].left = node
            else:
                last_node = None
                while stack and stack[-1].val == inorder[p2]:
                    last_node = stack.pop()
                    p2 += 1
                if last_node:
                    last_node.right = node

            p1 += 1
            stack.append(node)

        return root


class Solution2:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            root = TreeNode(preorder.pop(0))
            root_inorder_idx = inorder.index(root.val)

            root.left = self.buildTree(preorder, inorder[: root_inorder_idx])
            root.right = self.buildTree(preorder, inorder[root_inorder_idx + 1:])

            return root


class SolutionPostOrder:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            root = TreeNode(postorder.pop())
            idx = inorder.index(root.val)
            root.right = self.buildTree(inorder[idx + 1:], postorder)
            root.left = self.buildTree(inorder[: idx], postorder)

            return root


class SolutionPostOrder2:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None

        root = TreeNode(postorder[-1])
        end = len(postorder)
        stack = [root]
        p1 = end - 2
        p2 = end - 1

        while p1 >= 0:
            node = TreeNode(postorder[p1])
            if stack[-1].val != inorder[p2]:
                stack[-1].right = node
            else:
                last_node = None
                while stack and stack[-1].val == inorder[p2]:
                    last_node = stack.pop()
                    p2 -= 1
                if last_node:
                    last_node.left = node

            p1 -= 1
            stack.append(node)

        return root