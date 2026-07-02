# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    from typing import Optional

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def preorder(node):
            if not node:
                return "#,"

            return (
                "^" + str(node.val) + "," +
                preorder(node.left) +
                preorder(node.right)
            )

        root_str = preorder(root)
        sub_str = preorder(subRoot)

        return sub_str in root_str

                
