# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def traverse(node):
            if not node:
                return 0
            left_val = traverse(node.left)
            right_val = traverse(node.right)
            return max(left_val, right_val)+1
        return traverse(root)
        