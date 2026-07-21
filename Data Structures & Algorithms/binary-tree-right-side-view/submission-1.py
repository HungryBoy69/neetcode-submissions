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
            for _ in range(qlen):
                print(qlen)
                node = queue.popleft()
                if node:
                    res.append(node.val)
                    print(node.val)
                    if node.left:
                        print(node.val == 4 , node.left.val)
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            ans.append(res[-1])
        return ans