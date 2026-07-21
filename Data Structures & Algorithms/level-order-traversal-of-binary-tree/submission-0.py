# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # practise the DFS and BFS traversal
        queue = deque()
        queue.append(root)
        ans = []
        while queue:
            qlen = len(queue)
            level = []
            for _ in range(qlen):
                cur = queue.popleft()
                if cur:
                    level.append(cur.val)
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
            if level:
                ans.append(level)
        return ans
            
            