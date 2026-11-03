# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        seen = 0
        answer = None
        def dfs(cur):
            nonlocal seen, answer
            if not cur:
                return
            dfs(cur.left)
            seen += 1
            if seen == k:
                answer = cur.val
                return 
            dfs(cur.right)
        dfs(root)
        return answer
