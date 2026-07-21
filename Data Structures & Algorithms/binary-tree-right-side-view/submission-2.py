# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        queue  = deque([root])
        while queue:
            qlen = len(queue)
            res = []
            lastelem = None
            for _ in range(qlen):
                node = queue.popleft()
                if node:
                    lastelem = node.val
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            ans.append(lastelem)
        return ans