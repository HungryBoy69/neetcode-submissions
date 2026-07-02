# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(node):
            if not node:
                return None
            root = TreeNode(node.val)
            root.left = traverse(node.right)
            root.right = traverse(node.left)
            return root
        return traverse(root)