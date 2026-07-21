# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # practise the DFS and BFS traversal  DFS traversal
        res = []
        def traverse(node, level):
            if not node:
                return 
            
            if len(res) == level:
                res.append([]) # to create list within a list empty for each levels

            res[level].append(node.val)
            traverse(node.left, level+1)
            traverse(node.right, level+1)
        traverse(root, 0)
        return res
            