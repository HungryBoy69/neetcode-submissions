# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                # this means both are greater ( indicating we need to explore the right side of the tree)
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                # node is always greater for all the elements in the left sub truee
                cur = cur.left
            else:
                # elements are split ( p and q ) across the left and right side
                return cur