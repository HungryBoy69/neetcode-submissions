# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def traverse(node):
            if not node:
                return 0
            print(node.left.val if node.left else None)
            left_val = traverse(node.left)
            if left_val is False:
                return False
            print(node.right.val if node.right else None)
            right_val = traverse(node.right)
            if right_val is False:
                return False
            max_depth = max(left_val, right_val)+ 1
            if abs(left_val - right_val) > 1:
                return False
            return max_depth
        return traverse(root) is not False