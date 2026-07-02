# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        sum_val = float('-inf')
        def traverse(node):
            nonlocal sum_val
            if not node:
                return 0
            left_val = traverse(node.left)
            right_val = traverse(node.right)
            sum_val = max(sum_val, (left_val + right_val ))
            max_depth = max(left_val, right_val)+ 1
            return max_depth
        traverse(root)
        return 0 if sum_val == float('-inf') else sum_val